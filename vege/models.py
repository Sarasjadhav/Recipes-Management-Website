from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipes(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL ,null=True,blank=True)
    recipe_name=models.CharField( max_length=50)
    recipe_description=models.TextField()
    recipe_image=models.ImageField( upload_to="Recipe")
    recipe_view_count=models.IntegerField(default=1)
    
    def __str__(self):
        return self.recipe_name
 
class Department(models.Model):
    department=models.CharField(max_length=100)
    
    class Meta:
        ordering= ['department']
        
        
    def __str__(self):
        return self.department
    
class StudentID(models.Model):                          
    student_id=models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_id
    
class Student(models.Model):
    department=models.ForeignKey(Department,related_name="depart" ,on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentID,related_name="depart" ,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()
    
    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering=['student_name']
        verbose_name='student'
        
class Subject(models.Model):
    subject_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.subject_name
    
    
    

    
    