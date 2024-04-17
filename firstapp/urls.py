from django.contrib import admin
from django.urls import path , include
from firstapp import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('' , views.index , name="firstapp/index"),
    path('' , views.index , name="index"),
    path('home' , views.index , name="index"),
    path('about' , views.about , name="about"),
    path('contact' , views.contact , name="contact"),
    path('memories' , views.memoreis , name="memories"),
    path('registration' , views.registration, name="register"),
    path('students' , views.student_profile , name="students"),
    path('studdetails/<int:id>' , views.studdetails , name="studdetails"),
    path('login', views.login_page, name='login'),
    path('login_require', views.login_req, name='login_require'),
    path('logout', views.logout_user, name='logout'),
    path('submit-email/', views.submit_email, name='submit_email'),
    path('working', views.working, name='working'),
    path('success', views.login_success_view, name='success'),
    path('csuccess/<str:first_name>/', views.contact_success_view, name='csuccess'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
