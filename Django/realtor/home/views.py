from django.shortcuts import render

def index(request):
	context={'builder':'','landlord':'','home_buyer':''}
	return render(request,'home/home.html',context)