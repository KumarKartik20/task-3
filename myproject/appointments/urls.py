
from django.urls import path
from .views import doctor_list, book_appointment, appointment_details, SignUpView

urlpatterns = [
    path('list/', doctor_list, name='doctor_list'),
    path('book/', book_appointment, name='book_appointment'),
    path('details/', appointment_details, name='appointment_details'),
    path('signup/', SignUpView.as_view(), name='signup'),  # Add this line
]
