from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Booking
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import CustomerInfo, User
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, 'booking/home.html')


class UserBookingListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Booking
    template_name = 'booking/my_bookings.html'
    context_object_name = 'bookings'
    ordering = ['-booking_date', '-booking_time']
    paginate_by = 5

    def get_queryset(self):
        query_customer = get_object_or_404(CustomerInfo, pk=self.kwargs.get('pk'))

        url_query_status = self.request.GET.get('status')
        if not url_query_status:
            return Booking.objects.filter(customer=query_customer).order_by('-pk')
        else:
            return Booking.objects.filter(customer=query_customer, status=url_query_status).order_by('-pk')

    def test_func(self):
        query_user = get_object_or_404(CustomerInfo, pk=self.kwargs.get('pk')).user

        return self.request.user == query_user or self.request.user.is_barber or self.request.user.is_staff
        # Only customer himself, or barber or admin can check user's booking


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.customer = user.customer_id
        form.instance.customer_name = user.username
        form.instance.customer_mobile_number = user.customer_id.mobile_number
        form.instance.email = user.email

        return super().form_valid(form)


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    form_class = BookingForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.customer = user.customer_id
        form.instance.customer_name = user.username
        form.instance.customer_mobile_number = user.customer_id.mobile_number
        form.instance.email = user.email

        return super().form_valid(form)

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.customer.user


class BookingDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Booking

    def test_func(self):
        query_customer = get_object_or_404(Booking, pk=self.kwargs.get('pk')).customer.user

        return self.request.user == query_customer or self.request.user.is_barber or self.request.user.is_staff
        # Only customer himself, or barber or admin can check user's booking


@login_required
def cancel_booking(request, pk):
    booking = Booking.objects.filter(pk=pk).first()
    if request.user != booking.customer.user:
        return redirect('home')

    booking.set_status('cancelled')

    messages.info(request, 'Booking cancelled')
    return redirect('my_bookings', pk=request.user.pk)


@login_required
def confirm_booking(request, pk):
    booking = Booking.objects.filter(pk=pk).first()
    if not (request.user.is_staff or request.user.is_barber):
        return redirect('home')

    booking.set_status('confirmed')

    # send_confirm_email()
    messages.info(request, 'Booking confirmed')
    return redirect('back_stage_bookings')


class BackStageBookingListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Booking
    template_name = 'booking/back_stage_bookings.html'
    context_object_name = 'bookings'
    ordering = ['-booking_date', '-booking_time']
    paginate_by = 5

    def get_queryset(self):
        url_query_status = self.request.GET.get('status')
        if not url_query_status:
            return Booking.objects.filter().order_by('-pk')
        else:
            return Booking.objects.filter(status=url_query_status).order_by('-pk')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_barber
        # Only customer himself, or barber or admin can check user's booking
