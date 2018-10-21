from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Builder,Buyers,Develop,HomeBuyers,Land,Landlords,Project
from itertools import chain


def dashboard(request):
	context={'home_buyer':'','user_id':'','properties':[],'landlord':'','builder':'','built':[],'user_details':''}
	try:
		context['user_id']=request.session['user_id']
		if request.session['type']=='HomeBuyer':
			context['home_buyer']='Yes'
			context['user_details']=HomeBuyers.objects.filter(buyer_id=context['user_id'])[0].get_details()
		if request.session['type']=='Landlord':
			context['landlord']='Yes'
			context['user_details']=Landlord.objects.filter(landlord_id=context['user_id'])[0].get_details()
		if request.session['type']=='Builder':
			context['builder']='Yes'
			context['user_details']=Builder.objects.filter(builder_id=context['user_id'])[0].get_details()

	except:
		return HttpResponseRedirect('/')
	if context['home_buyer']:
		land=Land.objects.filter(bought_by=context['user_id'])
		homes=Buyers.objects.filter(buyer_id=context['user_id'])
		properties=[]
		for i in land:
			properties.append(i.get_details())
		for j in homes:
			pid=j.get_details()['project_id']
			pid=pid.get_details()['project_id']
			proj=Project.objects.filter(project_id=pid)[0]
			properties.append(proj.get_details())
		context['properties'] = properties
	if context['landlord']:
		land=Land.objects.filter(landlord_id=context['user_id'])
		lands=[]
		for i in land:
			lands.append(i.get_details())
		context['properties']=lands
	if context['builder']:
		land=Land.objects.filter(bought_by=context['user_id'])
		homes=Project.objects.filter(builder_id=context['user_id'])
		purchased=[]
		for i in land:
			purchased.append(i.get_details())
		built=[]
		for i in homes:
			built.append(i.get_details())
		context['built']=built
		context['properties']=purchased

	return render(request,'dashboard/dashboard.html',context)

def edit(request):
	obj=None
	errors=[]
	context={'home_buyer':'','user_id':'','landlord':'','builder':'','built':[],'email_id':'','contact_number':'','password':'','address':'','errors':[]}
	try:
		context['user_id']=request.session['user_id']
		if request.session['type']=='HomeBuyer':
			context['home_buyer']='Yes'
			obj=HomeBuyers.objects.filter(buyer_id=context['user_id'])[0]

		if request.session['type']=='Landlord':
			context['landlord']='Yes'
			obj=Landlord.objects.filter(landlord_id=context['user_id'])[0]
		if request.session['type']=='Builder':
			context['builder']='Yes'
			obj=Builder.objects.filter(builder_id=context['user_id'])[0]
	except:
		return HttpResponseRedirect('/')

	context['email_id']=obj.get_details()['email_id']
	context['contact_number']=obj.get_details()['contact_number']
	context['password']=obj.password
	try:
		context['address']=obj.get_details()['address']
	except:
		context['address']=obj.get_details()['office_address']

	if request.POST:
		obj.email_id=request.POST['email_id']
		obj.contact_number=request.POST['contact_number']
		if request.POST['password']==request.POST['password2']:
			obj.password=request.POST['password']
		else:
			errors.append('Passwords do not match')
		if len(request.POST['contact_number'])!=10 or request.POST['contact_number'].isupper() or request.POST['contact_number'].islower():
			errors.append("Contact number invalid")
		if context['builder']:
			obj.office_address=request.POST['office_address']
		else:
			obj.address=request.POST['address']
		if not errors:
			obj.save()
			return HttpResponseRedirect('/dashboard')
	return render(request,'dashboard/edit.html',context)
