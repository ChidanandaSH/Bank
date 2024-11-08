from django.contrib import admin
from django.urls import path
from .views import home,login_view,transaction_history,transfer_view,bill_payment_view,bill_payment_history,logout_view,about,contact,signup,services
urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('transaction_history/', transaction_history, name='transaction_history'),
    path('transfer/', transfer_view, name='transfer'),
    path('bill_payment/',bill_payment_view, name='bill_payment'),  # URL for bill payment
    path('bill_payment_history/', bill_payment_history, name='bill_payment_history'),  # URL for bill payment history
    path('logout/', logout_view, name='logout'),  # URL for logout
    path('about/', about, name='about'),  # URL pattern for the About Us page
    path('contact/', contact, name='contact'),  # URL pattern for the Contact Us page
    path('services/', services, name='services'),
    
]
