from django.db import models

# Create your models here.
class Employee(models.Model):
    class RoleChoice(models.TextChoices):
        SOFTWARE_ENGINEER = "software_engineer", "Software Engineer"
        JUNIOR_SOFTWARE_ENGINEER = "junior_software_engineer", "Junior Software Engineer"
        SENIOR_SOFTWARE_ENGINEER = "senior_software_engineer", "Senior Software Engineer"
        LEAD_ENGINEER = "lead_engineer", "Lead Engineer"
        
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True, max_length=100)
    age = models.IntegerField()
    role = models.CharField(max_length=50, choices=RoleChoice.choices, default=RoleChoice.JUNIOR_SOFTWARE_ENGINEER)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    join_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
        