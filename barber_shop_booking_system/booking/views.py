from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Booking
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import CustomerInfo, User


def home(request):
    return render(request, 'booking/home.html')


class UserBookingListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Booking
    template_name = 'booking/my_bookings.html'
    context_object_name = 'bookings'
    ordering = '-booking_dt'
    # paginate_by = 10
    # deal with pagination later

    def get_queryset(self):
        query_customer = get_object_or_404(CustomerInfo, pk=self.kwargs.get('pk'))
        return Booking.objects.filter(customer=query_customer).order_by('-booking_dt')

    def test_func(self):
        query_user = get_object_or_404(CustomerInfo, pk=self.kwargs.get('pk')).user

        return self.request.user == query_user or self.request.user.is_barber or self.request.user.is_staff
        # Only customer himself, or barber or admin can check user's booking


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['booking_dt', 'type', 'additional_massages']

    def form_valid(self, form):
        customer = self.request.user.customer_id
        form.instance.customer = customer
        form.instance.customer_name = customer.user.username
        form.instance.customer_mobile_number = customer.mobile_number
        form.instance.email = customer.email

        return super().form_valid(form)


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    fields = ['booking_dt', 'type', 'additional_massages']

    def form_valid(self, form):
        user = self.request.user
        form.instance.customer = user
        form.instance.customer_name = user.username
        form.instance.customer_mobile_number = user.mobile
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
