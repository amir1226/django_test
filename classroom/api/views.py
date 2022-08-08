from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication

from classroom.models import Student
from .serializers import StudentSerializer, ClassroomSerializer

class StudendApiView(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class StudentListApiView(StudendApiView, generics.ListAPIView):
    pass
    
class StudentCreateApiView(StudendApiView, generics.CreateAPIView):
    pass

class StudentDeleteApiView(StudendApiView, generics.DestroyAPIView):
    pass

class StudentDetailApiView(StudendApiView, generics.RetrieveAPIView):
    pass

class ClassroomNumberApiView(APIView):
    serializer_class = ClassroomSerializer
    queryset = ClassroomSerializer.Meta.model.objects.all()
    
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    
    
    def get(self, request, student_capacity):
        classroom = ClassroomSerializer.Meta.model.objects.filter(student_capacity__lte=student_capacity)
        serializer = ClassroomSerializer(classroom, many=True)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
