from django.urls import path
from .views import RenterSignupView, OwnerSignupView, CustomAuthToken, LogoutView, OwnerOnlyView, RenterOnlyView
urlpatterns = [
    path('signup/renter/', RenterSignupView.as_view(), name = 'renter-login'),
    path('signup/owner/', OwnerSignupView.as_view(), name = 'owner-login'),
    path('login/',CustomAuthToken.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name='login'),
    path('renter/dashboard/', RenterOnlyView.as_view(), name = 'renter-only-view'),
    path('owner/dashboard/', OwnerOnlyView.as_view(), name = 'owner-only-view'),
    
]