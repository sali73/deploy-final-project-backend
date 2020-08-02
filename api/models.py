from django.db import models
from datetime import date
from phone_field import PhoneField

class Students(models.Model):
    student_id = models.CharField(max_length=30)
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.CharField(max_length=400 ,blank=True)
    email = models.EmailField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    fax_no = models.CharField(max_length=200 , blank=True)
    gender_choose= (
        (1, 'Male'),
        (2, 'Female')
    )
    gender = models.IntegerField(
        choices=gender_choose,
        default=1,
        blank=True
    )
    dob = models.DateField()
    ENGLISH='EN'
    SPANISH='SP'
    HINDI='HI'
    ARABIC='AR'
    FRENCH='FR'
    RUSSIAN='FR'
    RUSSIAN='RU'
    lang_choose = [
        (ENGLISH , 'ENGLISH'),
        (ARABIC, 'ARABIC'),
        (SPANISH, 'SPANISH'),
        (HINDI, 'HINDI'),
        (FRENCH, 'FRENCH'),
        (RUSSIAN, 'RUSSIAN')
    ]
    preferred_language = models.CharField(
        max_length=2,
        choices=lang_choose,
        default=ENGLISH,
        blank=True
    )
    def __str__(self):
        return '%s ' % ( self.first_name )

class Instructor(models.Model):
    instructor_id = models.CharField(max_length=30 )
    instructor_first_name = models.CharField(max_length=300 )
    instructor_last_name = models.CharField(max_length=100,null=True)
    profile_pic = models.CharField(max_length=400 ,blank=True )
    email = models.EmailField(null=True , blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    salary = models.DecimalField(max_digits=6, decimal_places=2 , blank=True)
    commission = models.DecimalField(max_digits=6, decimal_places=2 , blank=True)
    date_hired = models.DateField()
    def __str__(self):
         return "%s " % (self.instructor_first_name)

class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=False)
    students = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=False)
    course_id = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    cost= models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField()
    def __str__(self):
        return "%s " % (self.title)

class Offering(models.Model):
    offering_id = models.CharField(max_length=30)
    instructor= models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=False)
    start_date= models.DateField()
    end_date = models.DateField()
    max_no_students = models.CharField(max_length=50)
    def __str__(self):
        return "%s " % (self.offering_id)


