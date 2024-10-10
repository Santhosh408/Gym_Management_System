from django.urls import path
from authapp import views
urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handlelogout,name="handlelogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="attendance"),
    path('about',views.about,name="about"),
    path('services',views.service,name="service"),
    path('trainers',views.trainer,name="trainer"),
    path('biceps',views.biceps,name="biceps"),
    path('back',views.back,name="back"),
    path('shoulder',views.shoulder,name="shoulder"),
    path('chest',views.chest,name="chest"),
    path('legs',views.legs,name="legs"),
    path('triceps',views.triceps,name="triceps"),
]