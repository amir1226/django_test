from rest_framework.serializers import ModelSerializer
from classroom.models import Student, Classroom

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class ClassroomSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'