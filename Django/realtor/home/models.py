from django.db import models

class Builder(models.Model):
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    office_address = models.CharField(max_length=100)
    builder_id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'builder'

    def get_details(self):
        details={'email_id':self.email_id,'name':self.name,'contact_number':self.contact_number,'office_address':self.office_address,'builder_id':self.builder_id}
        return details


class Buyers(models.Model):
    buyer_id = models.CharField(max_length=100,primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'buyers'

    def get_details(self):
        details={'buyer_id':self.buyer_id,'project_id':self.project}
        return details


class Develop(models.Model):
    completion_date = models.DateField()
    builder = models.ForeignKey(Builder, models.DO_NOTHING,primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'develop'

    def get_details(self):
        details={'builder_id':self.builder,'completion_date':self.completion_date,'project_id':self.project}
        return details


class HomeBuyers(models.Model):
    email_id = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    buyer_id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'home_buyers'

    def get_details(self):
        details={'email_id':self.email_id,'first_name':self.first_name,'middle_name':self.middle_name,'last_name':self.last_name,'contact_number':self.contact_number,'address':self.address,'buyer_id':self.buyer_id}
        return details


class Land(models.Model):
    price = models.FloatField()
    size = models.FloatField()
    address = models.CharField(max_length=100)
    bought_by = models.CharField(max_length=100)
    landlord = models.ForeignKey('Landlords', models.DO_NOTHING)
    land_id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'land'

    def get_details(self):
        details={'price':self.price,'size':self.size,'address':self.address,'landlord_id':self.landlord,'land_id':self.land_id,'bought_by':self.bought_by}
        return details


class Landlords(models.Model):
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100)
    landlord_id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'landlords'


    def get_details(self):
        details={'email_id':self.email_id,'first_name':self.first_name,'middle_name':self.middle_name,'last_name':self.last_name,'contact_number':self.contact_number,'address':self.address,'landlord_id':self.landlord_id}
        return details


class Project(models.Model):
    description = models.CharField(max_length=10000, blank=True, null=True)
    name = models.CharField(max_length=100)
    number_of_bedrooms = models.IntegerField()
    project_id = models.CharField(primary_key=True, max_length=100)
    price = models.FloatField()
    address = models.CharField(max_length=100)
    builder = models.ForeignKey(Builder, models.DO_NOTHING)
    size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'

    def get_details(self):
        details={'description':self.description,'name':self.name,'number_of_bedrooms':self.number_of_bedrooms,'project_id':self.project_id,'price':self.price,'address':self.address,'builder_id':self.builder,'size':self.size}
        return details
