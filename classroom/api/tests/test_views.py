from urllib import response
from django.test import TestCase
from django.contrib.auth.models import User

import pytest
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from rest_framework.authtoken.models  import Token

from classroom.models import Student, Classroom
from mixer.backend.django import mixer


pytestmasrk = pytest.mark.django_db

class TestStudentApiViews(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.token = Token.objects.create(user=mixer.blend(User))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)     
        
    def test_student_list_works(self):
        # create student
        student = mixer.blend(Student, first_name = "John")
        list_url = reverse("student_list")
        #call the url
        response = self.client.get(list_url)
        
        #assertions
        
        assert response.json() != None
        assert response.status_code == 200
        
        
    def test_student_create_works(self):
        # data
        input_data = {
            "first_name": "Pepe",
            "last_name": "Test",
            "email": "pepe@test-email.com",
            "age": 20,
            "admission_number": 123456,
        }
        
        url_create = reverse("student_create")
        
        response = self.client.post(url_create, input_data)
        
        total_students = Student.objects.count()
        
        assert response.json() != None
        assert response.status_code == 201
        assert total_students == 1
    
    def test_student_detail_works(self):
        student = mixer.blend(Student, first_name = "John")
        student2 = mixer.blend(Student, first_name = "Jane")
        
        url = reverse("student_detail", kwargs={"pk": student2.id})
        
        response = self.client.get(url)
        
        assert response.status_code == 200
        assert response.json()["first_name"] == student2.first_name
        assert response.json()["username"] == student2.first_name.lower()
        
        
    def test_student_delete_works(self):
        student = mixer.blend(Student, first_name = "John")
        student2 = mixer.blend(Student, first_name = "Jane")
        
        url = reverse("student_delete", kwargs={"pk": student2.id})
        
        response = self.client.delete(url)
        
        assert response.status_code == 204
        assert Student.objects.count() == 1
        
class TestClassroomAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.token = Token.objects.create(user=mixer.blend(User))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    def test_classroom_qs_works(self):
        classroom = mixer.blend(Classroom, student_capacity=10)
        
        url = reverse("classroom_api", kwargs={"student_capacity": 10})
        url2 = reverse("classroom_api", kwargs={"student_capacity": 5})
        
        response = self.client.get(url)
        response2 = self.client.get(url2)
        
        assert response.status_code == 202
        assert len(response.json()) == 1
        assert response2.json() == []