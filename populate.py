import mysql.connector
import names
from faker import Faker
import random
connection=mysql.connector.connect(host='localhost',password='mohit123',user='dbms',auth_plugin='mysql_native_password')
cursor=connection.cursor()
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
		name=first_name+pick_company()
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

populate_landlords()

connection.commit()
connection.close()

