import mysql.connector
import names
from faker import Faker
import random
connection=mysql.connector.connect(host='localhost',password='mohit123',user='dbms',auth_plugin='mysql_native_password')
cursor=connection.cursor(buffered=True)
queries=['use dbms_project']
cursor.execute(queries[0])

fake=Faker()

def get_n_numbers(n):
	return f'{random.randrange(1, 10**n):n}'

def pick_city():
	cities=['Bangalore, Karnataka, '+'56'+get_n_numbers(4),'Hyderabad, Telangana, '+'50'+get_n_numbers(4),'Chennai, Tamil Nadu, 600'+get_n_numbers(3)]
	cities2=['Mumbai, Maharashtra, 400'+get_n_numbers(3),'Kochi, Kerala, 68'+get_n_numbers(4),'Delhi, 11'+get_n_numbers(4)]
	cities3=['Bhopal, Madhya Pradesh, 462'+get_n_numbers(3),'Allahabad, Uttar Pradesh, 21'+get_n_numbers(4)]
	city_tier=random.choice([cities3,cities2,cities])
	city=random.choice(city_tier)
	return city

def pick_appartment():
	suffix=['Towers','Woods','Homes','Casa','Gems','Castle','Lake Front','Shoreline','Heights','Acres','Meadows','Orchards']
	return random.choice(suffix)

def pick_mail(name):
	providers=['@gmail.com','@yahoo.com','@mailtor.com']
	mail=random.choice(providers)
	return name+mail

def pick_phone():
	return random.choice(['9','8','7'])+get_n_numbers(9) 

def pick_company():
	return random.choice([' and Sons',' Inc.',' Corporation'])

def pick_address():
	return fake.address().split('\n')[0]+', '+pick_city()

def pick_project_price():
	a=[x*5 for x in range(100,2000)]
	return random.choice(a)


def pick_land_price():
	a=[x*5 for x in range(10,200)]
	return random.choice(a)

def pick_size():
	a=[x*5 for x in range(200,1800)]
	return random.choice(a)

def populate_home_buyers():
	query = "INSERT INTO home_buyers (email_id,password,first_name,middle_name,last_name,contact_number,address,buyer_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
	for i in range(30):
		first_name=names.get_first_name()
		email_id=pick_mail(first_name)
		password=first_name+'123'
		middle_name=random.choice([names.get_first_name(),""])
		last_name=names.get_last_name()
		contact_number=pick_phone()
		address=pick_address()
		buyer_id=random.getrandbits(32)
		val=(email_id,password,first_name,middle_name,last_name,contact_number,address,buyer_id)
		cursor.execute(query,val)
		
def populate_builder():
	query = "INSERT INTO builder (email_id,password,name,contact_number,office_address,builder_id) VALUES (%s, %s,%s, %s,%s, %s)"
	for i in range(30):
		first_name=names.get_first_name()
		name=fake.company()
		email_id=pick_mail(first_name)
		password=first_name+'123'
		contact_number=pick_phone()
		office_address=pick_address()
		builder_id=random.getrandbits(32)
		val=(email_id,password,name,contact_number,office_address,builder_id)
		cursor.execute(query,val)

def populate_landlords():
	query = "INSERT INTO landlords(email_id,password,first_name,middle_name,last_name,contact_number,address,landlord_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
	for i in range(30):
		first_name=names.get_first_name()
		email_id=pick_mail(first_name)
		password=first_name+'123'
		middle_name=random.choice([names.get_first_name(),""])
		contact_number=pick_phone()
		address=pick_address()
		landlord_id=random.getrandbits(32)
		val=(email_id,password,first_name,middle_name,last_name,contact_number,address,landlord_id)
		cursor.execute(query,val)	

def populate_land():
	cursor.execute('select landlord_id from landlords')
	landlord_ids=[]
	for x in cursor.fetchall():
		landlord_ids.append(x[0])

	query = "INSERT INTO land(price,size,address,landlord_id,land_id) VALUES (%s, %s,%s, %s,%s)"
	for i in range(30):
		no_of_lands=random.choice([0,1,2])
		if no_of_lands:
			for j in range(no_of_lands):
				price=pick_land_price()
				size=pick_size()
				address=pick_address()
				land_id=random.getrandbits(32)
				landlord_id=landlord_ids[i]
				val=(price,size,address,landlord_id,land_id)
				cursor.execute(query,val)

def populate_project():
	cursor.execute('select builder_id from builder')
	builder_ids=[]
	for x in cursor.fetchall():
		builder_ids.append(x[0])

	query = "INSERT INTO project(description,name,number_of_bedrooms,project_id,size,price,address,builder_id) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
	for i in range(30):
		no_of_projects=random.choice([2,3,4,5])
		if no_of_projects:
			for j in range(no_of_projects):
				description=fake.text(max_nb_chars=200, ext_word_list=None)
				name=names.get_first_name()+' '+pick_appartment()
				price=pick_project_price()
				size=pick_size()
				address=pick_address()
				number_of_bedrooms=random.choice([1,2,3,4,5])
				project_id=random.getrandbits(32)
				builder_id=builder_ids[i]
				val=(description,name,number_of_bedrooms,project_id,size,price,address,builder_id)
				cursor.execute(query,val)

def populate_develop():
	cursor.execute('select builder_id,project_id from project')
	builder_ids=[]
	project_ids=[]
	for x in cursor.fetchall():
		builder_ids.append(x[0])
		project_ids.append(x[1])

	query = "INSERT INTO develop(completion_date,builder_id,project_id) VALUES (%s, %s,%s)"
	for i in range(len(builder_ids)):
		completion_date=fake.date(pattern="%Y-%m-%d", end_datetime=None)
		val=(completion_date,builder_ids[i],project_ids[i])
		cursor.execute(query,val)

def populate_buyers():
	cursor.execute('select project_id from project')
	home_buyer_ids=[]
	project_ids=[]
	for x in cursor.fetchall():
		project_ids.append(x[0])

	cursor.execute('select buyer_id from home_buyers')
	for x in cursor.fetchall():
		home_buyer_ids.append(x[0])

	query = "INSERT INTO buyers(buyer_id,project_id) VALUES (%s, %s)"
	for i in range(10):
		x=random.choice([y for y in range(0,30)])
		buyer_id=home_buyer_ids[x]
		project_id=random.choice(project_ids)
		val=(buyer_id,project_id)
		cursor.execute(query,val)



connection.commit()
connection.close()

