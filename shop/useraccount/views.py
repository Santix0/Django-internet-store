from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView, UpdateView

from .models import User
from .forms import *


# function, that will return information about user
@login_required()
def user_data(request, user_id):
    user_information = User.objects.get(id=user_id)

    context = {
        'user_information': user_information
    }

    return render(request, 'useraccount/user_data.html', context)


# form class that change user account information
class ChangeUserAccount(UpdateView):
    form_class = UserUpdateForm
    template_name = 'useraccount/user_change_account.html'

    def get_object(self, **kwargs):
        return self.request.user


# from class that change user password
class PasswordChange(UpdateView):
    form_class = PasswordChange
    template_name = 'useraccount/change_password.html'

    def get_object(self, **kwargs):
        return self.request.user


def sign_in(request) -> dict:
    if request.method == 'POST':
        # taking the username and password from form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate user by username and password
        user = authenticate(request, username=username, password=password)
        form = UserSignInForm(request.POST)

        if user is not None:
            # if user exits, we login user
            login(request, user)
            return redirect('main_page')
        else:
            ...
            # messages.info(request, 'Username or password is incorrect.')
    else:
        form = UserSignInForm()

    context = {'form': form}

    return render(request, 'useraccount/sign_in.html', context)


def sign_up(request) -> dict:
    # checking the method of request
    if request.method == 'POST':
        # creating form for sign up to user
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = UserSignUpForm()

    # creating context
    context = {
        'form': form,
    }
    # form = UserSignUpForm()
    return render(request, 'useraccount/sign_up.html', context)


def logout_user(reqeust) -> dict:
    logout(reqeust)
    return redirect('main_page')
