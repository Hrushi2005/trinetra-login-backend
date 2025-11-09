from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)  # ✅ field must exist
    userid = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"
