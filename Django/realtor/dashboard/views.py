from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Builder,Buyers,Develop,HomeBuyers,Land,Landlords,Project
from itertools import chain
import random
from django.contrib import messages

def dashboard(request):
	context={'home_buyer':'','user_id':'','properties':[],'landlord':'','builder':'','built':[],'user_details':''}
	try:
		context['user_id']=request.session['user_id']
		if request.session['type']=='HomeBuyer':
			context['home_buyer']='Yes'
			context['user_details']=HomeBuyers.objects.filter(buyer_id=context['user_id'])[0].get_details()
		if request.session['type']=='Landlord':
			context['landlord']='Yes'
			context['user_details']=Landlords.objects.filter(landlord_id=context['user_id'])[0].get_details()
		if request.session['type']=='Builder':
			context['builder']='Yes'
			context['user_details']=Builder.objects.filter(builder_id=context['user_id'])[0].get_details()

	except Exception as e:
		print(e)
		return HttpResponseRedirect('/')
	if context['home_buyer']:
		land=Land.objects.filter(bought_by=context['user_id'])
		homes=Buyers.objects.filter(buyer_id=context['user_id'])
		properties=[]
		projects=[]
		for i in land:
			obj=i.get_display_details()
			properties.append(obj)
		for j in homes:
			pid=j.get_details()['project_id']
			pid=pid.get_details()['project_id']
			proj=Project.objects.filter(project_id=pid)[0]
			p=proj
			proj=proj.get_display_details() 
			temp={'Builder':''}
			for i in proj:
				temp[i]=''
			for i in proj:
				temp[i]=proj[i]
			temp['Builder']={'name':Builder.objects.filter(builder_id=p.builder_id)[0].name,'link':p.builder_id}
			projects.append(proj)
		context['properties'] = properties
		context['projects'] = projects

	if context['landlord']:
		land=Land.objects.filter(landlord_id=context['user_id'])
		lands=[]
		for i in land:

			obj=i.get_display_details()
			b=HomeBuyers.objects.filter(buyer_id=i.bought_by)
			c=Builder.objects.filter(builder_id=i.bought_by)
			if len(b):
				obj['Bought by']={'name':b[0].first_name+" "+b[0].last_name,'link':b[0].buyer_id,'type':'home_buyer'}
			elif len(c):
				obj['Bought by']={'name':c[0].name,'link':c[0].builder_id,'type':'builder'}
			else:
				obj['land_id']=i.land_id
			lands.append(obj)
		context['properties']=lands


	if context['builder']:
		land=Land.objects.filter(bought_by=context['user_id'])
		homes=Project.objects.filter(builder_id=context['user_id'])
		purchased=[]
		for i in land:
			purchased.append(i.get_display_details())
		projects=[]
		for i in homes:
			obj=i.get_display_details()
			try:
				b=Buyers.objects.filter(project_id=i.project_id)[0]
				b=HomeBuyers.objects.filter(buyer_id=b.buyer_id)[0]
				obj['Bought by']={'name':b.first_name+" "+b.last_name,'link':b.buyer_id}
				projects.append(obj)
			except Exception as e:
				obj['project_id']=i.project_id
				projects.append(obj)

		context['projects']=projects
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
			obj=Landlords.objects.filter(landlord_id=context['user_id'])[0]
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

		if len(Builder.objects.filter(contact_number=request.POST['contact_number'])) + len(Landlords.objects.filter(contact_number=request.POST['contact_number'])) + len(HomeBuyers.objects.filter(contact_number=request.POST['contact_number'])) > 1:
			errors.append("Contact number registered by another user")
		if len(Builder.objects.filter(email_id=request.POST['email_id'])) +  len(Landlords.objects.filter(email_id=request.POST['email_id'])) + len(HomeBuyers.objects.filter(email_id=request.POST['email_id'])) > 1:
			errors.append("Email ID registered by another user")

		if context['builder']:
			obj.office_address=request.POST['office_address']
		else:
			obj.address=request.POST['address']
		if not errors:
			obj.save()
			return HttpResponseRedirect('/dashboard')
		else:
			context['errors']=errors
			return render(request,'dashboard/edit.html',context)
	return render(request,'dashboard/edit.html',context)

def addListing(request):
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
			obj=Landlords.objects.filter(landlord_id=context['user_id'])[0]
		if request.session['type']=='Builder':
			context['builder']='Yes'
			obj=Builder.objects.filter(builder_id=context['user_id'])[0]
	except:
		return HttpResponseRedirect('/')



	if request.POST:
		if context['landlord']:
			obj=Land(price=request.POST['price'],size=request.POST['size'],landlord_id=context['user_id'],land_id=random.getrandbits(32),address=request.POST['address'])
			obj.save()
			messages.success(request, "Your listing has been saved!")
			return HttpResponseRedirect('/dashboard')

		if context['builder']:
			obj=Project(number_of_bedrooms=request.POST['number_of_bedrooms'],price=request.POST['price'],name=request.POST['name'],description=request.POST['description'],size=request.POST['size'],builder_id=context['user_id'],project_id=random.getrandbits(32),address=request.POST['address'])
			dev=Develop(completion_date=request.POST['completion_date'],builder_id=context['user_id'],project_id=obj.project_id)
			obj.save()
			dev.save()
			messages.success(request, "Your listing has been saved!")
			return HttpResponseRedirect('/dashboard')

	return render(request,'dashboard/add.html',context)

def sell(request):
	obj=None
	buyer=None
	errors=[]
	context={'home_buyer':'','user_id':'','landlord':'','builder':'','built':[],'email_id':'','contact_number':'','password':'','address':'','errors':[]}
	try:
		context['user_id']=request.session['user_id']
		if request.session['type']=='HomeBuyer':
			context['home_buyer']='Yes'
			obj=HomeBuyers.objects.filter(buyer_id=context['user_id'])[0]
		if request.session['type']=='Landlord':
			context['landlord']='Yes'
			obj=Landlords.objects.filter(landlord_id=context['user_id'])[0]
		if request.session['type']=='Builder':
			context['builder']='Yes'
			obj=Builder.objects.filter(builder_id=context['user_id'])[0]
	except:
		return HttpResponseRedirect('/')

	if request.POST:
		a=1
		if context['landlord']:
			try:
				buyer=HomeBuyers.objects.filter(contact_number=request.POST['buyer'])[0]
				obj=Land.objects.filter(land_id=request.POST['land_id'])[0]
				obj.bought_by=buyer.buyer_id
				obj.save()
				messages.success(request, "Your listing has been marked sold!")
			except:
				messages.success(request,'Buyer is not registered to our database')
				a=0
			try:
				buyer=Builder.objects.filter(contact_number=request.POST['buyer'])[0]
				obj=Land.objects.filter(land_id=request.POST['land_id'])[0]
				obj.bought_by=buyer.builder_id
				obj.save()
				messages.success(request, "Your listing has been marked sold!")
			except:
				if a!=0:
					messages.success(request,'Buyer is not registered to our database')

		if context['builder']:
			try:
				buyer=HomeBuyers.objects.filter(contact_number=request.POST['buyer'])[0]
				obj=Buyers(project_id=request.POST['project_id'],buyer_id=buyer.buyer_id)
				obj.save()
				messages.success(request, "Your listing has been marked sold!")
			except:
				messages.success(request,'Home buyer is not registered to our database')

		return HttpResponseRedirect('/dashboard')
