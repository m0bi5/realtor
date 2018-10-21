from django.shortcuts import render
import random
from django.http import HttpResponseRedirect
import re
from home.models import Builder,Buyers,Develop,HomeBuyers,Land,Landlords,Project

# Create your views here.

from django.contrib.auth.decorators import login_required
def logout(request):
	del request.session['type']
	del request.session['user_id']
	return HttpResponseRedirect('/')
def login(request):
	print(request.POST)
	context={'error':''}
	if request.method != 'POST':
		return render(request,'login/login.html',context)
	hb_obj=None
	b_obj=None
	ll_obj=None
	try:
		hb_obj = HomeBuyers.objects.get(email_id=request.POST['email_id'])
	except:
		a=0
	try:
		b_obj = Builder.objects.get(email_id=request.POST['email_id'])
	except:
		a=0
	try:
		ll_obj = Landlords.objects.get(email_id=request.POST['email_id'])
	except:
		a=0
	if hb_obj:
		obj = hb_obj
		if obj.password == request.POST['password']:
			request.session['type']='HomeBuyer'
			request.session['user_id']=obj.get_details()['buyer_id']
			return HttpResponseRedirect('/dashboard')
		else:
			context['error']="Password incorrect"
			return render(request,'login/login.html',context)

	if b_obj:
		obj = b_obj
		if obj.password == request.POST['password']:
			request.session['type']='Builder'
			request.session['user_id']=obj.get_details()['builder_id']

			return HttpResponseRedirect('/dashboard')
		else:
			context['error']="Password incorrect"
			return render(request,'login/login.html',context)


	if ll_obj:
		obj = ll_obj
		if obj.password == request.POST['password']:
			request.session['type']='Landlord'
			request.session['user_id']=obj.get_details()['landlord_id']

			return HttpResponseRedirect('/dashboard')
		else:
			context['error']="Password incorrect"
			return render(request,'login/login.html',context)
	


