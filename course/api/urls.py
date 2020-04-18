
from django.urls import path
from .views import getSubjects,getOldQuestion,getNotes,getBooks,getLabManual,getPractiseQuestion
urlpatterns = [
    path('subject/',getSubjects,name='subjects'),
    path('oldquestion/',getOldQuestion,name='oldQuestion'),
    path('notes/',getNotes,name='notes'),
    path('books/',getBooks,name='books'),
    path('lab-manual/',getLabManual,name='labmanual'),
    path('practise-question/',getPractiseQuestion,name='practiseQuestion')
]