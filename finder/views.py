from django.shortcuts import render

# Create your views here.

def map (request):
	return render (request,'finder/maps.html')

def diseases (request):
	return render (request,'finder/diseases/diseases.html')

def home (request):
	return render (request,'finder/doctor/home.html')

def index (request):
	return render (request,'finder/patient/index.html')

def about (request):
	return render (request,'finder/patient/about.html')

def contact (request):
	return render (request,'finder/patient/contact.html')


def chats(request):
	return render (request,'finder/patient/chats.html')
 
def tables (request):
	return render (request,'finder/patient/tables.html')

def register (request):
	return render (request,'finder/patient/register.html')

def error (request):
	return render (request,'finder/patient/404.html')


def main (request):
	return render (request,'finder/patient/main.html')


def blank (request):
	return render (request,'finder/patient/blank.html')


def forgot_password (request):
	return render (request,'finder/patient/forgot-password.html')

def login (request):
	return render (request,'finder/patient/login.html')

# doctor dashboard

def index1 (request):
	return render (request,'finder/doctor/index.html')

def about1 (request):
	return render (request,'finder/doctor/about.html')

def contact1 (request):
	return render (request,'finder/doctor/contact.html')


def chats1(request):
	return render (request,'finder/doctor/chats.html')
 
def tables1 (request):
	return render (request,'finder/doctor/tables.html')

def register1 (request):
	return render (request,'finder/doctor/register.html')

def error1 (request):
	return render (request,'finder/doctor/404.html')


def main1 (request):
	return render (request,'finder/doctor/main.html')


def blank1 (request):
	return render (request,'finder/doctor/blank.html')


def forgot_password1 (request):
	return render (request,'finder/doctor/forgot-password.html')

def login1 (request):
	return render (request,'finder/doctor/login.html')

# hospital dashboard
def registration(request):
	return render (request,'finder/hospital/registration.html')

