from faker import Faker
fake = Faker()
import random
from vege.models import *

def seed_vege(n=10):
    for _ in range (n):
        Department_obj=Department.objects.all()
        random_idx=random.randint(0,len(Department_obj)-1)
        department=Department_obj[random_idx]
        student_id=f"STU-{random.randint(101,999)}"
        student_name=fake.name()
        student_email=fake.email()
        student_age=random.randint(18,25)
        student_address=fake.address()
        
        student_id_object = StudentID.objects.create(student_id=student_id)

        
        student_obj=Student(
            department=department,
            student_id=student_id_object,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address
            )
        student_obj.save()

        
    return 
        
            
            

        