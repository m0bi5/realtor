from django.shortcuts import render
from django.http import Http404
from home.models import Builder,Buyers,Develop,HomeBuyers,Land,Landlords,Project

# Create your views here.

def detail(request, object_id):
	path=request.get_full_path()
	context={'object_details':'','home_buyer':'','builder':'','landlord':''}
	obj=None

	if 'home_buyer' in path:
		obj=HomeBuyers.objects.get(buyer_id=object_id)
		context['home_buyer']='set'
	elif 'landlord' in path:
		obj=Landlords.objects.get(landlord_id=object_id)
		context['landlord']='set'
	elif 'land' in path:
		obj=Land.objects.get(land_id=object_id)
	elif 'project' in path:
		obj=Project.objects.get(project_id=object_id)
	elif 'builder' in path:
		obj=Builder.objects.get(builder_id=object_id)
		context['builder']='set'

	context['object_details']=obj.get_details()

	return render(request,'details/details.html',context)