from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
import datetime

CHOICES = (
    (0, 'Zero'),
    (1, 'One'),
    (2, 'Two'),
)
BRIDE_JOB = (
    ('Need', 'Need'),
    ('Need not go for job', 'Need not go for job'),
)
MSTATUS = (
    ('Never Married', 'Never Married'),
    ('Divorcee', 'Divorcee'),
    ('Widow/Widower', 'Widow/Widower'),
)
HSTATUS = (
    ('Match is must', 'Match is must'),
    ('Mutual acceptance will also hold good', 'Mutual acceptance will also hold good'),
)
RSTATUS = (
    ('MESHAM', 'MESHAM'),
    ('MITHUNAM', 'MITHUNAM'),
    ('KANNI', 'KANNI'),
    ('KUMBAM', 'KUMBAM'),
    ('MEENAM', 'MEENAM'),
    ('SIMMAM', 'SIMMAM'),
    ('TULAM', 'TULAM'),
    ('VIRUCHIGAM', 'VIRUCHIGAM'),
    ('THANUSU', 'THANUSU'),
    ('MAKARAM', 'MAKARAM'),
    ('RISHABAM', 'RISHABAM'),
    ('KADAGAM', 'KADAGAM'),
)
NSTATUS = (
    ('Aswini', 'Aswini'),
    ('Bharani', 'Bharani'),
    ('Karthigai', 'Karthigai'),
    ('Rohini', 'Rohini'),
    ('Mrigasheersham', 'Mrigasheersham'),
    ('Thiruvaathirai', 'Thiruvaathirai'),
    ('Punarpoosam', 'Punarpoosam'),
    ('Poosam', 'Poosam'),
    ('Aayilyam', 'Aayilyam'),
    ('Makam', 'Makam'),
    ('Pooram', 'Pooram'),
    ('Uthiram', 'Uthiram'),
    ('Hastham', 'Hastham'),
    ('Chithirai', 'Chithirai'),
    ('Swaathi', 'Swaathi'),
    ('Visaakam', 'Visaakam'),
    ('Anusham', 'Anusham'),
    ('Kettai', 'Kettai'),
    ('Moolam', 'Moolam'),
    ('Pooraadam', 'Pooraadam'),
    ('Uthiraadam', 'Uthiraadam'),
    ('Thiruvonam', 'Thiruvonam'),
    ('Avittam', 'Avittam'),
    ('Chathayam/Sadayam', 'Chathayam/Sadayam'),
    ('Poorattathi', 'Poorattathi'),
    ('Uthirattathi', 'Uthirattathi'),
    ('Revathi', 'Revathi'),
)
PASTATUS = (
    ('0', '1'),
    ('1', '2'),
    ('2', '3'),
    ('3', '4'),
)
     
     
     
     
     

ESTATUS = (
    ('Central Govt', 'Central Govt'),
    ('Central Govt. Undertaking', 'Central Govt. Undertaking'),
    ('State Govt.', 'State Govt.'),
    ('State Govt. Undertaking', 'State Govt. Undertaking'),
    ('Private', 'Private'),
    ('Self Employee', 'Self Employee'),
    ('(MNC(India))', '(MNC(India))'),
    ('(MNC(Abroad))', '(MNC(Abroad))'),
)
NEESTATUS = (
    ('Never Married', 'Never Married'),
    ('Divorcee', 'Divorcee'),
    ('Widow/widower', 'Widow/widower'),
)
HOUSTATUS = (
    ('Own House', 'Own House'),
    ('Rented House', 'Rented House'),
)






# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=200)
    #picture = models.ImageField()
    date_of_birth = models.DateField(default=datetime.date.today)
    time = models.CharField(max_length=120)
    place = models.CharField(max_length=120)
    origin = models.CharField(max_length=120)
    gothram = models.CharField(max_length=120)
    family_name = models.CharField(max_length=120)
    natchathram = models.CharField(max_length=20,choices=NSTATUS)
    #padam = models.CharField(max_length=2,choices=PASTATUS)
    padam = models.IntegerField()
    rasi = models.CharField(max_length=20,choices=RSTATUS)
    height = models.CharField(max_length=120)
    colour = models.CharField(max_length=120)
    blood_group = models.CharField(max_length=120)
    mother_f_name = models.CharField(max_length=120)
    education = models.CharField(max_length=120)
    employment_details =  models.CharField(max_length=20,choices=ESTATUS)
    #employment_details =  models.CharF(max_length=2,choices=CHOICES, widget=models.RadioSelect())
    office_address = models.TextField()
    email_address = models.CharField(max_length=120)
    salary = models.CharField(max_length=120)
    father_name=models.CharField(max_length=120)
    mother_name=models.CharField(max_length=120)
    applicant_is = models.CharField(max_length=120)
    brief_information = models.TextField()
    contact_address =  models.TextField()
    phone = models.CharField(max_length=120)
    mobile =  models.CharField(max_length=120)
    having_house = models.CharField(max_length=20,choices=HOUSTATUS)
    languages_known =  models.CharField(max_length=120)
    marital_status = models.CharField(max_length=20,choices=MSTATUS)
    education_bride =  models.CharField(max_length=120)
    origin_place = models.CharField(max_length=120)
    living_in =  models.CharField(max_length=120)
    working_in =  models.CharField(max_length=120)
    doing_business = models.CharField(max_length=120)
    height_shld_be = models.CharField(max_length=120)
    bride_for_job  = models.CharField(max_length=50,choices=BRIDE_JOB)
    bride_forced   = models.CharField(max_length=120)
    horoscope = models.CharField(max_length=50,choices=HSTATUS)
    need = models.CharField(max_length=20,choices=NEESTATUS)
        
    
    
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('application_edit', kwargs={'pk': self.pk})
