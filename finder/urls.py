from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('404/', views.error, name='error'),
	path('register/', views.register, name='register'),
	path('tables/', views.tables, name='tables'),
	path('forgot-password/', views.forgot_password, name='forgot_password'),
	path('main/', views.main, name='main'),
	path('chats/', views.chats, name='chats'),
	path('blank/', views.blank, name='blank'),
	path('login/', views.login, name='login'),

	# doctors dashboard
	path('doctor/', views.index1, name='index1'),
	path('doctor/about/', views.about1, name='about1'),
	path('doctor/contact/', views.contact1, name='contact1'),
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



]