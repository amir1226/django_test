from django.db import models
from django.utils.text import slugify

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_negative(value):
    if value < 0:
        raise ValidationError(f"{value} is not a positive number")

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.SlugField(max_length=50, blank=True, null=True)

    age = models.IntegerField()
    admission_number = models.IntegerField(unique=True)

    is_qualified = models.BooleanField(default=False)
    average_score = models.FloatField(blank=True, null=True, validators=[validate_negative])

    def __str__(self):
        return self.first_name + " " + self.last_name
    def get_grade(self):
        if 0 <= self.average_score < 40:
            return "Fail"
        if 40 <= self.average_score < 70:
            return "Pass"
        if 70 <= self.average_score <= 100:
            return "Excellent"
        return "Error"

    def save(self, *args, **kwargs):	
        self.username = slugify(self.first_name)
        super(Student, self).save(*args, **kwargs)

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField("classroom.Student", blank=True)

    def __str__(self):
        return self.name
