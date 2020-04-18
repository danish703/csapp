from rest_framework import serializers
from course.models import Subject,OldQuestion,Notes,Book,LabManual,PractiseQuestion

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','subject_name','image','subject_number','nature','credit_hours','description','syllabus','course','semester']


class OldQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldQuestion
        fields =['id','title','year','link','subject']



class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields =['id','title','link','subject']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields =['id','title','link','subject']


class LabManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabManual
        fields =['id','title','link','subject']

class PractisQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractiseQuestion
        fields =['id','title','link','subject']