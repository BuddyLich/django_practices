from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, CustomerRegisterForm, CustomerUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        # user_form = UserRegisterForm(request.POST, instance=request.user)
        user_form = UserRegisterForm(request.POST)
        print('check 2')
        customer_form = CustomerRegisterForm(request.POST)
        print('check 3')

        if user_form.is_valid() and customer_form.is_valid():
            print('valid')
            user = user_form.save(commit=False)
            user.is_customer = True
            user.save()
            customer_form.save()
            return redirect('login')

        else:
            print(f'user_form is {user_form.is_valid()}')
            print(f'customer_form is {customer_form.is_valid()}')
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
            return redirect('customer_profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        customer_form = CustomerUpdateForm()
        context = {
            "user_form": user_form,
            "customer_form": customer_form
        }

        return render(request, 'customer/profile.html', context=context)
