from django.shortcuts import render
from django.http import Http404
from home.models import Builder,Buyers,Develop,HomeBuyers,Land,Landlords,Project
from itertools import chain

# Create your views here.

def filter_price(items,price):
	final=[]
	for i in items:
		if price >= i.get_details()['price']:
			final.append(i)
	return final

def filter_size(items,size):
	final=[]
	for i in items:
		if size >= i.get_details()['size']:
			final.append(i)
	return final

def filter_city(items,city):
	final=[]
	for i in items:
		if city in i.get_details()['address']:
			final.append(i)
	return final

def search(request):
	property_type=''
	price=''
	size=''
	city=''
	All=''
	Appartments=''
	Land=''
	context={}
	if request.POST:
		property_type=request.POST['type']
		if property_type=='All':
			All='All'
		if property_type=='Appartments':
			Appartments='Appartments'
		if property_type=='Land':
			Land='Land'
		price=request.POST['price']
		size=request.POST['size']
		city=request.POST['city']
		context={'All':All,'Appartments':Appartments,'Land':Land,'price':price,'city':city,'size':size}
		print(context)
		result=get_objects(context)
		result=[x.get_details() for x in result]
		context['result']=result
		return render(request,'search/search.html',context)
	else:
		return render(request,'search/search.html',context)


def get_objects(query):
	res=None
	if query['All']:
		project=Project.objects.all()
		land=Land.objects.all()
		
		res = list(chain(project,land))

		if query['city']:
			res=filter_city(res,query['city'])
		if query['price'] :
			res=filter_price(res,float(query['price']))
		if query['size']:
			res=filter_size(res,float(query['size']))


	if query['Appartments']:
		res=Project.objects.all()
	if query['Land']:
		res=Land.objects.all()

	if  not query['All']:
		if query['price']:
			res=res.filter(price__lte=float(query['price']))
		if query['size']:
			res=res.filter(size__lte=float(query['size']))
		if query['city']:
			res=res.filter(address__icontains=query['city'])
	return res
