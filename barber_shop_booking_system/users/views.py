from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, CustomerRegisterForm, CustomerUpdateForm
from django.contrib.auth.decorators import login_required
from .models import User, CustomerInfo


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        customer_form = CustomerRegisterForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.is_customer = True
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()

            messages.success(request, 'Account Created!')
            return redirect('login')
        else:
            messages.error(request, 'Account Created Failed!')
            return redirect('register')

    else:
        user_form = UserRegisterForm()
        customer_form = CustomerRegisterForm()
        context = {
            "user_form": user_form,
            "customer_form": customer_form
        }

        return render(request, 'customer/register.html', context=context)


@login_required
def profile(request, pk):
    profile_customer = get_object_or_404(CustomerInfo, pk=pk)

    if not request.user.is_staff and request.user != profile_customer.user:
        return redirect('home')

    profile_user = profile_customer.user

    context = {
        'phone': profile_customer.mobile_number,
        'email': profile_user.email,
        'username': profile_user.username
    }

    return render(request, 'customer/profile.html', context=context)


@login_required
def profile_update(request, pk):
    profile_customer = get_object_or_404(CustomerInfo, pk=pk)
    profile_user = profile_customer.user

    if request.user != profile_customer.user:
        return redirect('home')

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=profile_user)
        customer_form = CustomerUpdateForm(request.POST, instance=profile_customer)

        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            return redirect('profile', pk=pk)

    else:
        user_form = UserUpdateForm(instance=profile_user)
        customer_form = CustomerUpdateForm(instance=profile_customer)
        context = {
            "user_form": user_form,
            "customer_form": customer_form
        }

        return render(request, 'customer/profile_update.html', context=context)
