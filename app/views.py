from django.shortcuts import render
from app.forms import RegisterForm, VaccinationSlotForm, VaccinationCenterForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from app.models import VaccinationCenter, VaccinationSlot, DosageDetail
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
import datetime
from django.contrib.auth.decorators import permission_required



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            role = request.POST['roles']
            group = Group.objects.get(name=role)
            user = form.instance
            user.groups.add(group)
            messages.success(request, "Registration Successful")
            return redirect(reverse('login'))
    else:
        form = RegisterForm()
    return render(request, 'app/register.html', {'form':form})

def loginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return redirect(reverse('home'))
        else:
            form = AuthenticationForm()
        return render(request, 'app/login.html', {'form':form})
    else:
        return redirect(reverse('home'))

def logoutView(request):
    logout(request)
    return redirect(reverse('login'))


@never_cache
@login_required
def home(request):
    a = VaccinationCenter.objects.all()
    return render(request, 'app/home.html', {'vacc': a})

#  Booking Slot
def vaccineSlot(request, pk):
    if request.method == 'POST':
        center = VaccinationCenter.objects.get(id=pk)
        form = VaccinationSlotForm(request.POST)
        if form.is_valid():
            slot_count = VaccinationSlot.objects.filter(date=datetime.date.today(), center=pk).count()
            print(slot_count)
            if slot_count >= 10:
              messages.error(request, 'No available slots for today at this center.')
            else:
              slot = VaccinationSlot(
                center=center,
                name=form.cleaned_data['name'],
                phone_number=form.cleaned_data['phone_number'],
                date=form.cleaned_data['date']
              )
              slot.save()
              messages.success(request, 'Vaccination Slot Booked')
              return redirect(reverse('home'))
    else:
        form = VaccinationSlotForm()
    return render(request, 'app/bookSlot.html', {'form': form, 'pk':pk})       


@login_required
@permission_required('app.delete_vaccinecenter', raise_exception=True)
def delete(request, pk):
    center = VaccinationCenter.objects.get(id=pk)
    center.delete()
    messages.success(request, "Vaccine Center Deleted Successfully")
    return redirect(reverse('home')) 


@login_required
@permission_required('app.add_vaccinecenter', raise_exception=True)
@never_cache
def add(request):
    if request.method == 'POST':
        form = VaccinationCenterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vaccine Center Added Successfully")
            return redirect(reverse('home'))
    else:
        form = VaccinationCenterForm()
    return render(request, 'app/add.html', {'form':form})
