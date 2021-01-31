from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('my_bookings/<int:pk>', views.UserBookingListView.as_view(), name='my_bookings'),
    path('booking/new/', views.BookingCreateView.as_view(), name='new_booking'),
    path('booking/<int:pk>/update/', views.BookingUpdateView.as_view(), name='update_booking'),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail')
]
