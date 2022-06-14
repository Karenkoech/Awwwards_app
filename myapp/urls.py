
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_view, name='home_view'),
    path('upload_project/',views.Upload_Project,name="upload_project"),
    path('rating/(?P<pk>\d+)$',views.RateProject,name="rate_project"),
    path('myprofile/',views.User_Profile,name="my_profile"),
    
]

