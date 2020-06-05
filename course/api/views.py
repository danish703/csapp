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
    course = request.GET.get('course')
    sem = request.GET.get('sem')
    if course != None and sem != None:
        id = Course.objects.get(course_name__iexact=course.rstrip()).id
        subject = Subject.objects.filter(course_id=id, semester=sem)
        oldQuestion = OldQuestion.objects.filter(subject__in=subject)
        serializer = OldQuestionSerializer(oldQuestion, many=True)
        return JsonResponse(serializer.data, safe=False)
    if course != None:
        id = Course.objects.get(course_name__iexact=course.rstrip()).id
        subject = Subject.objects.filter(course_id=id)
        oldQuestion = OldQuestion.objects.filter(subject__in=subject)
        serializer = OldQuestionSerializer(oldQuestion, many=True)
        return JsonResponse(serializer.data, safe=False)
    oldQuestion = OldQuestion.objects.all()
    if subject_id !=None:
        oldQuestion = OldQuestion.objects.filter(subject_id=subject_id)
    serializer = OldQuestionSerializer(oldQuestion,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET',])
def getNotes(request):
    subject_id = request.GET.get('subject')
    course = request.GET.get('course')
    sem = request.GET.get('sem')
    if course!=None and sem!=None:
        id = Course.objects.get(course_name__iexact=course.rstrip()).id
        subject = Subject.objects.filter(course_id=id,semester=sem)
        notes = Notes.objects.filter(subject__in=subject)
        serializer = NotesSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)
    if course!=None:
        id = Course.objects.get(course_name__iexact=course.rstrip()).id
        subject = Subject.objects.filter(course_id=id)
        notes = Notes.objects.filter(subject__in=subject)
        serializer = NotesSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)
    notes = Notes.objects.all()
    if subject_id !=None:
        notes = Notes.objects.filter(subject_id=subject_id)
    serializer = NotesSerializer(notes,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET',])
def getBooks(request):
    subject_id = request.GET.get('subject')
    course = request.GET.get('course')
    sem = request.GET.get('sem')
    if course!=None and sem!=None:
        id = Course.objects.get(course_name__iexact=course.rstrip()).id
        subject = Subject.objects.filter(course_id=id,semester=sem)
        books = Book.objects.filter(subject__in=subject)
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    if course!=None:
        id = Course.objects.get(course_name__iexact=course.rstrip()).id
        subject = Subject.objects.filter(course_id=id)
        books = Book.objects.filter(subject__in=subject)
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    books = Book.objects.all()
    if subject_id !=None:
        books = Book.objects.filter(subject_id=subject_id)
    serializer = BookSerializer(books,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET',])
def getLabManual(request):
    subject_id = request.GET.get('subject')
    course = request.GET.get('course')
    sem = request.GET.get('sem')
    if course!=None and sem!=None:
        id = Course.objects.get(course_name__iexact=course.rstrip()).id
        subject = Subject.objects.filter(course_id=id,semester=sem)
        lm = LabManual.objects.filter(subject__in=subject)
        serializer = LabManualSerializer(lm, many=True)
        return JsonResponse(serializer.data, safe=False)
    if course!=None:
        id = Course.objects.get(course_name__iexact=course.rstrip()).id
        subject = Subject.objects.filter(course_id=id)
        lm = LabManual.objects.filter(subject__in=subject)
        serializer = LabManualSerializer(lm, many=True)
        return JsonResponse(serializer.data, safe=False)
    lm = LabManual.objects.all()
    if subject_id !=None:
        lm = LabManual.objects.filter(subject_id=subject_id)
    serializer = LabManualSerializer(lm,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET',])
def getPractiseQuestion(request):
    subject_id = request.GET.get('subject')
    course = request.GET.get('course')
    sem = request.GET.get('sem')
    if course!=None and sem!=None:
        id = Course.objects.get(course_name__iexact=course.rstrip()).id
        subject = Subject.objects.filter(course_id=id,semester=sem)
        pq = PractiseQuestion.objects.filter(subject__in=subject)
        serializer = PractisQuestionSerializer(pq, many=True)
        return JsonResponse(serializer.data, safe=False)
    if course!=None:
        id = Course.objects.get(course_name__iexact=course.rstrip()).id
        subject = Subject.objects.filter(course_id=id)
        pq = PractiseQuestion.objects.filter(subject__in=subject)
        serializer = PractisQuestionSerializer(pq, many=True)
        return JsonResponse(serializer.data, safe=False)
    pq = PractiseQuestion.objects.all()
    if subject_id !=None:
        pq = PractiseQuestion.objects.filter(subject_id=subject_id)
    serializer = PractisQuestionSerializer(pq,many=True)
    return JsonResponse(serializer.data,safe=False)