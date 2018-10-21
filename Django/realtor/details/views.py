from django.shortcuts import render
from django.http import Http404
from home.models import Builder,Buyers,Develop,HomeBuyers,Land,Landlords,Project

# Create your views here.

def detail(request, object_id):
	path=request.get_full_path()
	try:
		if 'home_buyer' in path:
			obj=HomeBuyers.objects.get(pk=object_id)
		if 'landlord' in path:
			obj=Landlords.objects.get(pk=object_id)
		if 'land' in path:
			obj=Land.objects.get(pk=object_id)
		if 'project' in path:
			obj=Project.objects.get(pk=object_id)
		if 'builder' in path:
			obj=Builder.objects.get(pk=object_id)
		context={'object_details':obj.get_details()}
	except:
		raise Http404("Invalid Object ID")
	
	
	return render(request,'details/details.html',context)