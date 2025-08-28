from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from . models import Course, Category, Lesson, Material, Enrollment, QuestionAnswer
from .serializers import CategorySerializer, CourseSerializer, LessonSerializer, MaterialSerializer,EnrollmentSerializer,QuestionAnswerSerializer

# Create your views here.
@api_view(['GET','POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.role != 'admin':
            return Response({'detail' : "only admin can create categories"}, status=403)
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.e, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])    
def course_list_create(request):
    if request.method == 'GET':
        if request.user.role in ['admin','student']:
            courses = Course.objects.all()
        elif request.user.role == 'teacher':
            courses = Course.objects.filter(instructor_id=request.user)
        else:
            return Response({'detail': 'Unauthorized role'},status=403)
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.user.role != 'teacher':
            return Response({'detail' : "only teachers can create courses"}, status=403)
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(instructor_id = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.e, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk = pk)

    except Course.DoesNotExist:
        return Response({'detail':'Course not found'},status=404)
    
    if request.method == 'GET':
        if request.user.role == 'admin' or request.user == 'course.instructor_id':
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        return Response({'detail': 'Permission denied!'}, status=404)
    elif request.method == 'PUT':
        if request.user.role != 'teacher' or request.user != course.instructor_id:
            return Response({'detail':'Only course tacher can update this course' }, status=403)
        serializer = CourseSerializer(course, data= request.data)
        if serializer.is_valid():
            serializer.save(instructor_id = request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        if request.user.role != 'teacher' or request.user != course.instructor_id:
            return Response({'detail':'Only course tacher can delete this course' }, status=403)
        course.delete()
        return Response({'detail': 'Course deleted'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])    
def lesson_list_create(request):
    if request.method == 'GET':
        categories = Lesson.objects.all()
        serializer = LessonSerializer(categories, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.role != 'admin':
            return Response({'detail' : "only admin can create categories"}, status=403)
        serializer = LessonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.e, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])    
def material_list_create(request):
    if request.method == 'GET':
        categories = Material.objects.all()
        serializer = MaterialSerializer(categories, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.role != 'admin':
            return Response({'detail' : "only admin can create categories"}, status=403)
        serializer = MaterialSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.e, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])    
def enrollment_list_create(request):
    if request.method == 'GET':
        categories = Enrollment.objects.all()
        serializer = EnrollmentSerializer(categories, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.role != 'admin':
            return Response({'detail' : "only admin can create categories"}, status=403)
        serializer = EnrollmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.e, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])    
def quesionanswer_list_create(request):
    if request.method == 'GET':
        categories = QuestionAnswer.objects.all()
        serializer = QuestionAnswerSerializer(categories, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.role != 'admin':
            return Response({'detail' : "only admin can create categories"}, status=403)
        serializer = QuestionAnswerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.e, status=status.HTTP_400_BAD_REQUEST)

