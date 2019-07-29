from django.db import models

# Create your models here.

#models for the teenagers.
class Student(models.Model):

	STATE_CHOICE = (('FCT' , 'Abuja'),('AB' , 'Abia'),('AD' , 'Adamawa'),('AK' , 'Akwa Ibom'),
	('AN' , 'Anambra'),('BA' , 'Bauchi'),('BY' , 'Bayelsa'),('BE' , 'Benue'),('BO' , 'Borno'),
	('CR' , 'Cross River'),('DE' , 'Delta'),('EB' , 'Ebonyi'),('ED' , 'Edo'),('EK' , 'Ekiti'),
	('EN' , 'Enugu'),('GO' , 'Gombe'),('IM' , 'Imo'),('JI' , 'Jigawa'),('KD' , 'Kaduna'),
	('KN' , 'Kano'),('KT' , 'Katsina'),('KE' , 'Kebbi'),('KO' , 'Kogi'),('KW' , 'Kwara'),
	('LA' , 'Lagos'),('NA' , 'Nassarawa'),('NI' , 'Niger'),('OG' , 'Ogun'),('ON' , 'Ondo'),
	('OS' , 'Osun'),('OY' , 'Oyo'),('PL' , 'Plateau'),('RI' , 'Rivers'),('SO' , 'Sokoto'),
	('TA' , 'Taraba'),('YO' , 'Yobe'),('ZA' , 'Zamfara'),)
	CLASS = (('JSS-1','JSS-1'),('JSS-2','JSS-2'),('JSS-3','JSS-3'),('SS-1','SS-1'),('SS-2','SS-2'),('SS-3','SS-3'),('100L','100L'),
		('200L','200L'),('300L','300L'),('400L','400L'),('500L','500L'),
		('ND1','ND1'),('ND-2','ND-2'),('HND-1','HND-2'))
	first_name = models.CharField(max_length=225)
	last_name = models.CharField(max_length =225)
	middle_name = models.CharField(max_length=225, null=True)
	date_of_birth = models.DateField(max_length=225)
	state_of_origin = models.CharField(max_length=20, choices = STATE_CHOICE, default='Abuja')
	name_of_school = models.CharField(max_length = 225)
	email_address = models.EmailField(unique = True)
	active = models.BooleanField(default= True)
	phone_number = models.CharField(max_length = 11)



	def __str__(self):
		return self.first_name


	#def get_absolute_url(self):
    #   return reverse('personel_detail', kwargs={'pk': self.pk})

