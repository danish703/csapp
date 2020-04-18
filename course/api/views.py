from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import (
    SubjectSerializer,
    OldQuestionSerializer,
    NotesSerializer,
    BookSerializer,
    LabManualSerializer,
    PractisQuestionSerializer
)
from course.models import Subject,Course,OldQuestion,Notes,Book,LabManual,PractiseQuestion


@api_view(['GET',])
def getSubjects(request):
    course = request.GET.get('course')
    semester = request.GET.get('sem')
    if course !=None and semester!=None:
        course=course.rstrip()
        semester=semester.rstrip()
    elif course!=None:
        course=course.rstrip()
    data = {}
    try:
        if course!=None:
            id = Course.objects.get(course_name__iexact=course).id
    except:
        data['errors'] = "You have do the bad request please check the url once and try again"
        return JsonResponse(data)
    if course != None and semester!=None:
        subjects = Subject.objects.filter(course_id=id, semester=semester)
    elif course!=None:
        subjects = Subject.objects.filter(course_id=id)
    else:
        subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True,context={"request": request})
    return JsonResponse(serializer.data,safe=False)


@api_view(['GET',])
def getOldQuestion(request):
    subject_id = request.GET.get('subject')
    oldQuestion = OldQuestion.objects.all()
    if subject_id !=None:
        oldQuestion = OldQuestion.objects.filter(subject_id=subject_id)
    serializer = OldQuestionSerializer(oldQuestion,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET',])
def getNotes(request):
    subject_id = request.GET.get('subject')
    notes = Notes.objects.all()
    if subject_id !=None:
        notes = Notes.objects.filter(subject_id=subject_id)
    serializer = NotesSerializer(notes,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET',])
def getBooks(request):
    subject_id = request.GET.get('subject')
    books = Book.objects.all()
    if subject_id !=None:
        books = Book.objects.filter(subject_id=subject_id)
    serializer = BookSerializer(books,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET',])
def getLabManual(request):
    subject_id = request.GET.get('subject')
    lm = LabManual.objects.all()
    if subject_id !=None:
        lm = LabManual.objects.filter(subject_id=subject_id)
    serializer = LabManualSerializer(lm,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET',])
def getPractiseQuestion(request):
    subject_id = request.GET.get('subject')
    pq = PractiseQuestion.objects.all()
    if subject_id !=None:
        pq = PractiseQuestion.objects.filter(subject_id=subject_id)
    serializer = PractisQuestionSerializer(pq,many=True)
    return JsonResponse(serializer.data,safe=False)