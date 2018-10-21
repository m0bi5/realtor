from django.shortcuts import render
import random
import re
from home.models import Builder,Buyers,Develop,HomeBuyers,Land,Landlords,Project

# Create your views here.

from django.contrib.auth.decorators import login_required

def login_home_buyer(request):
	context={'error':''}
	if request.method != 'POST':
		raise Http404('Only POSTs are allowed')
	try:
		obj = HomeBuyers.objects.get(email_id=request.POST['email_id'])
		if obj.get_details()['password'] == request.POST['password']:
			request.session['id'] = obj.get_details()['buyer_id']
			request.session['type']='HomeBuyer'
			return render(request,'dashboard/dashboard.html',context)
		else:
			context['error']="Password incorrect"
			return render(request,'login/login.html',context)
	except HomeBuyers.DoesNotExist:
		context['error']="Invalid Email ID"
		return render(request,'login/login.html',context)


def login_landlord(request):

	#"INSERT INTO home_buyers (email_id,password,first_name,middle_name,last_name,contact_number,address,buyer_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
	context={}
	return render(request,'login/login.html',context)

def login_builder(request):

	#"INSERT INTO home_buyers (email_id,password,first_name,middle_name,last_name,contact_number,address,buyer_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
	context={}
	return render(request,'login/login.html',context)
