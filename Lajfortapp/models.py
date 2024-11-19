from django.db import models

# Create your models here.

SUBJEECT_CHOICES = [
    ('mathematics','mathematics'),
    ('english','english'),
    ('physics','physics'),
    ('chemistry','chemistry'),
    ('biology','biology'),
    ('geography','geography'),
    ('further-mathematics','further-mathematics'),
    ('economics','economics'),
    ('agric','agric'),
    ('civic','civic'),
    ('marketing','marketing'),
    ('crs','crs'),
    ('government','government'),
    ('account','account'),
    ('commerce','commerce'),
    ('literature','literature'),
    ('yoruba','yoruba'),
    ('business-studies','business-studies'),
    ('basic-science','basic-science'),
    ('basic-technology','basic-technology'),
    ('p.h.e','p.h.e'),
    ('music','music'),
    ('french','french'),
    ('home-economics','home-economics'),
    ('c.c.a','c.c.a'),
    ('social-studies','social-studies'),
    ('security-education','security-education'),
    ('history','history'),
]

CLASS_CHIOCE = [
    ('JSS1','JSS1'),
    ('JSS2','JSS2'),
    ('JSS3','JSS3'),
    ('SSS1','SSS1'),
    ('SSS2','SSS2'),
    ('SSS3','SSS3')
]

class About(models.Model):
    about = models.TextField(max_length=1000000)
    image = models.ImageField(null=True,default='')
    vision = models.TextField(max_length=1000000)
    image2 = models.ImageField(null=True,default='')
    mission1 = models.TextField(max_length=200)
    mission2 = models.TextField(max_length=200)
    mission3 = models.TextField(max_length=200)
    mission4 = models.TextField(max_length=200)

class Gallerie(models.Model):
    image = models.ImageField(null=True,default='')

class Message(models.Model):
    name  = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000000)

class Principal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="Lajfort-default-profile.png")
    speech = models.TextField(max_length=300)

class Founder(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="Lajfort-profile-pics.png")
    speech = models.TextField(max_length=300)

class VicePrincipal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="Lajfort-default-profile.png")
    speech = models.TextField(max_length=300)

class HeadTeacher(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="Lajfort-default-profile.png")
    speech = models.TextField(max_length=300)

class Career(models.Model):
    content = models.TextField(max_length=1000000,null=True)

class Student(models.Model):
    name = models.CharField(max_length=500)
    clas = models.CharField(max_length=50,choices=CLASS_CHIOCE)

    def __str__(self):
        return self.name + ' in ' + self.clas + ' class'

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, choices=SUBJEECT_CHOICES)
    test_score = models.IntegerField()
    exam_score = models.IntegerField()
    grade = models.CharField(default='A1',max_length=50)

    def __str__(self):
        return self.student.name + ' ' + self.subject

class Overall_score(models.Model):
    total_score = models.IntegerField()
    percentage = models.CharField(max_length=50)
    principal_remark = models.TextField(max_length=1000)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student.name + ' ' + self.percentage