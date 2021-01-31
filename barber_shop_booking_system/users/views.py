from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, CustomerRegisterForm, CustomerUpdateForm
from django.contrib.auth.decorators import login_required


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
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        customer_form = CustomerUpdateForm(request.POST, instance=request.customerinfo)

        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        customer_form = CustomerUpdateForm()
        context = {
            "user_form": user_form,
            "customer_form": customer_form
        }

        return render(request, 'customer/profile.html', context=context)
