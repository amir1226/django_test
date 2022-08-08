# from django.test import TestCase
import pytest
from hypothesis import strategies as st, given
from hypothesis.extra.django import TestCase

from classroom.models import Student, Classroom
from mixer.backend.django import mixer

# @pytest.mark.django_db ----If not use hypothesis TestCase
# class TestStudentModel(TestCase):
class TestStudentModel(TestCase):
    # def setUp(self):
    #     self.student_1 = Student.objects.create(
    #         first_name="Pepe",
    #         last_name="Perez",
    #         age=10,
    #         admission_number=12345,
    #     )

    def test_add_a_plus_b(self):
        a = 1
        b = 2
        assert a + b  == 3

    def test_student_can_be_created(self):
        student_1 = mixer.blend(Student)

        student_result = Student.objects.last()

        # self.assertEqual(student_result.first_name, "Pepe")
        assert student_result.first_name == student_1.first_name

    def test_str_return(self):

        student_1 = mixer.blend(Student)

        student_result = Student.objects.last()

        # self.assertEqual(
        #     str(student_result), f"{student_1.first_name} {student_1.last_name}"
        # )
        assert str(
            student_result) == f"{student_1.first_name} {student_1.last_name}"
     
    """     @given(st.characters())   
    def test_slugify(self, name):
        student_1 = mixer.blend(Student, first_name=name)
        student_result = Student.objects.last()
        print(student_result)

        assert len(str(student_result.username)) == len(name) 
    """


    @given(st.floats(min_value=0, max_value=40, exclude_max=True))
    def test_grade_fail(self, fail_score):
        student_1 = mixer.blend(Student, average_score=fail_score)
        student_result = Student.objects.last()

        # self.assertEqual(student_result.get_grade(), "Fail")
        assert student_result.get_grade() == "Fail"
        
    @given(st.floats(min_value=40, max_value=70, exclude_max=True))
    def test_grade_pass(self, pass_score):
        student_1 = mixer.blend(Student, average_score=pass_score)
        student_result = Student.objects.last()

        # self.assertEqual(student_result.get_grade(), "Pass")
        assert student_result.get_grade() == "Pass"

    @given(st.floats(min_value=70, max_value=100))
    def test_grade_excellent(self,pass_score):
        student_1 = mixer.blend(Student, average_score=pass_score)
        student_result = Student.objects.last()

        # self.assertEqual(student_result.get_grade(), "Excellent")
        assert student_result.get_grade() == "Excellent"

    @given(st.floats(min_value=101))
    def test_grade_error(self, pass_score):
        student_1 = mixer.blend(Student, average_score=pass_score)
        student_result = Student.objects.last()

        # self.assertEqual(student_result.get_grade(), "Error")
        assert student_result.get_grade() == "Error"


    @given(st.floats(max_value=-1))
    def test_grade_error(self, pass_score):
        student_1 = mixer.blend(Student, average_score=pass_score)
        student_result = Student.objects.last()

        # self.assertEqual(student_result.get_grade(), "Error")
        assert student_result.get_grade() == "Error"
        
class TestClassroomModel(TestCase):
    def test_classroom_create(self):
        classroom = mixer.blend(Classroom, name="maths")
        classroom_result = Classroom.objects.last()
        
        assert(str(classroom_result) == "maths")