from django.urls import path
from . import views

urlpatterns = [

	path('', views.map, name='map'),
# patient dashboard
	path('patient/', views.index, name='index'),
	path('patient/about/', views.about, name='about'),
	path('patient/contact/', views.contact, name='contact'),
	path('patient/404/', views.error, name='error'),
	path('patient/register/', views.register, name='register'),
	path('patient/tables/', views.tables, name='tables'),
	path('patient/forgot-password/', views.forgot_password, name='forgot_password'),
	path('patient/main/', views.main, name='main'),
	path('patient/chats/', views.chats, name='chats'),
	path('patient/blank/', views.blank, name='blank'),
	path('patient/login/', views.login, name='login'),

	# doctors dashboard
	path('doctor/', views.index1, name='index1'),
	path('doctor/about/', views.about1, name='about1'),
	path('doctor/contact/', views.contact1, name='contact1'),
	path('doctor/home/', views.home, name='home'),
	path('doctor/404/', views.error1, name='error1'),
	path('doctor/register/', views.register1, name='register1'),
	path('doctor/tables/', views.tables1, name='tables1'),
	path('doctor/forgot-password/', views.forgot_password1, name='forgot_password1'),
	path('doctor/main/', views.main1, name='main1'),
	path('doctor/chats/', views.chats1, name='chats1'),
	path('doctor/blank/', views.blank1, name='blank1'),
	path('doctor/login/', views.login1, name='login1'),


	#hospital dashboard
		path('hospital/', views.registration, name='registration'),
		
	#diseases dashboard
		path('diseases/', views.diseases, name='diseases'),



]