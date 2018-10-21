from django.shortcuts import render
import random
import re
from home.models import Builder,Buyers,Develop,HomeBuyers,Land,Landlords,Project

# Create your views here.

def error_check(data,class_type):
	errors=[]
	if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", data['email_id'])) == False:
		errors.append("Invalid Email")
	if data['password']!=data['password2']:
		errors.append('Passwords dont match')
	if len(data['contact_number'])!=10 or data['contact_number'].isupper() or data['contact_number'].islower():
		errors.append('Contact number invalid')
	email_exists=class_type.objects.filter(email_id=data['email_id']).exists()
	phone_exists=class_type.objects.filter(contact_number=data['contact_number']).exists()

	if email_exists:
		errors.append('Email already registered')
	if phone_exists:
		errors.append('Phone number already registered')
	return errors



def home_buyer(request):

	#"INSERT INTO home_buyers (email_id,password,first_name,middle_name,last_name,contact_number,address,buyer_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
	context={}
	if request.POST:
		context={'errors':'','success':'','email_id':request.POST['email_id'],'password':request.POST['password'],'password2':request.POST['password2'],'first_name':request.POST['first_name'],'middle_name':request.POST['middle_name'],'last_name':request.POST['last_name'],'contact_number':request.POST['contact_number'],'address':request.POST['address'],'buyer_id':random.getrandbits(32)}
		errors=error_check(context,HomeBuyers)
		if not errors:
			obj=HomeBuyers(email_id=context['email_id'],password=context['password'],first_name=context['first_name'],middle_name=context['middle_name'],last_name=context['last_name'],contact_number=context['contact_number'],address=context['address'],buyer_id=context['buyer_id'])
			obj.save()
			context['success']='success'
		context['errors']=errors
	return render(request,'signup/home_buyer.html',context)

def landlord(request):

	context={}
	if request.POST:
		context={'errors':'','success':'','email_id':request.POST['email_id'],'password':request.POST['password'],'password2':request.POST['password2'],'first_name':request.POST['first_name'],'middle_name':request.POST['middle_name'],'last_name':request.POST['last_name'],'contact_number':request.POST['contact_number'],'address':request.POST['address'],'landlord_id':random.getrandbits(32)}
		errors=error_check(context,Landlords)
		if not errors:
			obj=Landlords(email_id=context['email_id'],password=context['password'],first_name=context['first_name'],middle_name=context['middle_name'],last_name=context['last_name'],contact_number=context['contact_number'],address=context['address'],landlord_id=context['landlord_id'])
			obj.save()
			context['success']='success'
		context['errors']=errors
	return render(request,'signup/landlord.html',context)

def builder(request):
	context={}
	if request.POST:
		context={'errors':'','success':'','email_id':request.POST['email_id'],'password':request.POST['password'],'password2':request.POST['password2'],'name':request.POST['name'],'contact_number':request.POST['contact_number'],'office_address':request.POST['office_address'],'builder_id':random.getrandbits(32)}
		errors=error_check(context,Builder)
		if not errors:
			obj=Builder(email_id=context['email_id'],password=context['password'],name=context['name'],contact_number=context['contact_number'],office_address=context['office_address'],builder_id=context['builder_id'])
			obj.save()
			context['success']='success'
		context['errors']=errors
	return render(request,'signup/builder.html',context)
