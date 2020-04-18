from django.db import models

semester = ((1,"First"),(2,"Second"),(3,"Third"),(4,"Fourth"),(5,"Fifth"),(6,"Sixth"),(7,"Seventh"),(8,"eighth"))
nature = (("Theory + Practical","Theory + Practical"),("Theory","Theory"),("Practical","Practical"))
# Create your models here.
class Course(models.Model):
    course_name = models.CharField(verbose_name="Course Name", unique=True, max_length=30)

    def __str__(self):
        return self.course_name

class Subject(models.Model):
    subject_name = models.CharField(verbose_name="Subject Name",max_length=100)
    image = models.ImageField(null=True,blank=True,upload_to='subject/')
    subject_number = models.CharField(verbose_name="Subject code",max_length=10)
    credit_hours = models.CharField(verbose_name='Credit Hours',default=3,max_length=3)
    nature = models.CharField(verbose_name="Subject Nature",max_length=50,choices=nature)
    description = models.TextField(verbose_name="Short Description")
    syllabus = models.URLField(verbose_name="Google Drive link of Syllabus PDF")
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    semester = models.IntegerField(verbose_name="Semester",choices=semester)


    class Meta:
        unique_together =('subject_number','course')


    def __str__(self):
        return self.subject_name

class OldQuestion(models.Model):
    title = models.CharField(verbose_name="Title",max_length=50)
    year = models.CharField(verbose_name='Year',blank=True,null=True,max_length=100)
    link = models.URLField(verbose_name="Link of PDF/ Docs")
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Notes(models.Model):
    title = models.CharField(verbose_name="Title",max_length=50)
    link = models.URLField(verbose_name="Link of PDF/ Docs")
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(verbose_name="Title",max_length=50)
    link = models.URLField(verbose_name="Link of PDF/ Docs")
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LabManual(models.Model):
    title = models.CharField(verbose_name="Title",max_length=10)
    link = models.URLField(verbose_name="Link of PDF/ Docs")
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class PractiseQuestion(models.Model):
    title = models.CharField(verbose_name="Title",max_length=50)
    link = models.URLField(verbose_name="Link of PDF/ Docs")
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
