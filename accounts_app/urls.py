from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', login_required(views.Logout.as_view()), name='logout'),
    path('dashboard/', login_required(views.Dashboard.as_view()), name='dashboard'),
    path('', login_required(views.Dashboard.as_view()), name='dashboard'),

    # for makeing account activate of users
    path('activate/<uidb64>/<token>/', views.Activate.as_view(), name='activate'),


    path('forgotPassword/', views.ForgotPassword.as_view(), name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.Resetpassword_validate.as_view(), name='resetpassword_validate'),

    path('resetPassword/', views.ResetPassword.as_view(), name='resetPassword'),
]              