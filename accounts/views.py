from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages
from . decorators import *
from . filters import *
# Create your views here.


def index(request):
    context = {}
    return render(request, 'accounts/index.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='flair_user')
                user.groups.add(group)
                FlairUser.objects.create(
                    user=user,
                    username=user.username,
                    email=user.email
                )
                messages.success(request, 'Account was created for ' + username)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['flair_user'])
def health_form(request):
    form = HealthFormCreation()
    if request.method == 'POST':
        form = HealthFormCreation(request.POST, request.FILES)
        if form.is_valid():
            form.instance.health_form_submitted_by = request.user.flairuser
            form.save()
            messages.success(request, 'Form successfully submitted!')
            return redirect('healthform')

    context = {'form': form}
    return render(request, 'accounts/health_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_redirect(request):
    context = {}
    return render(request, 'accounts/admin_redirect.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_user_logs(request):
    flair_users = FlairUser.objects.all() # query user database
    total_flair_users = flair_users.count()
    context = {'flair_users': flair_users, 'total_flair_users': total_flair_users}
    return render(request, 'accounts/admin_user_logs.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_update_user(request, pk):
    update_user = FlairUser.objects.get(id=pk)
    form = UpdateUserForm(instance=update_user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=update_user)
        if form.is_valid():
            form.save()
            return redirect('adminuserlogs')
    context = {'form': form, 'update_user': update_user}
    return render(request, 'accounts/update_user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_health_form_logs(request):
    health_forms = HealthForm.objects.all()
    total_health_form = health_forms.count()
    health_form_filter = HealthFormFilter(request.GET, queryset=health_forms)
    health_forms = health_form_filter.qs
    context = {'health_forms': health_forms, 'total_health_form': total_health_form, 'health_form_filter':health_form_filter}
    return render(request, 'accounts/admin_healthform_logs.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_update_health_form(request, pk):
    update_health_form = HealthForm.objects.get(id=pk)
    form = HealthFormCreation(instance=update_health_form)
    if request.method == 'POST':
        form = HealthFormCreation(request.POST, instance=update_health_form)
        if form.is_valid():
            form.save()
            return redirect('adminhealthformlogs')
    context = {'form': form}
    return render(request, 'accounts/update_health_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_delete_health_form(request, pk):
    delete_health_form = HealthForm.objects.get(id=pk)
    if request.method == 'POST':
        delete_health_form.delete()
        return redirect('adminhealthformlogs')
    context = {'delete_health_form': delete_health_form}
    return render(request, 'accounts/delete_health_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_delete_user(request, pk):
    delete_user = FlairUser.objects.get(id=pk)
    if request.method == 'POST':
        delete_user.delete()
        return redirect('adminuserlogs')
    context = {'delete_user': delete_user}
    return render(request, 'accounts/delete_user.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def features(request):
    context = {}
    return render(request, 'accounts/features.html', context)


def about_us(request):
    context = {}
    return render(request, 'accounts/about_us.html', context)


def contact_us(request):
    context = {}
    return render(request, 'accounts/contact_us.html', context)