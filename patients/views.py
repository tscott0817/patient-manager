from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import PatientDemo
# from .models import PatientContact
from .forms import PatientForm, CreateUserForm


# Create your views here
def registerPage(request):
    # form = UserCreationForm()
    form = CreateUserForm()

    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def home(request):
    queryset = PatientDemo.objects.all().order_by('name_last')
    context = {
        'queryset': queryset
    }
    return render(request, 'app/base.html', context)


def create(request):
    form = PatientForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        "form": form
    }
    return render(request, 'app/createform.html', context)