from django.db import models
# Create your models here.
class Survey(models.Model):
    question1 = models.CharField(max_length = 100)
    question2 = models.CharField(max_length = 100)
    question3 = models.CharField(max_length = 100)
    question4 = models.CharField(max_length = 100)
    question5 = models.CharField(max_length = 100)
    question6 = models.CharField(max_length = 100)
    question7 = models.CharField(max_length = 100)
    question8 = models.CharField(max_length = 100)
    total  = models.IntegerField(blank=True, null=True)
    #the corressponding objects that have that thing will be deleted
    def __str__(self):
        return (question1, question2)

    def save(self, *args, **kwargs):
        self.total = int(self.question1) + int(self.question2) + int(self.question3) + int(self.question4) + int(self.question5) + int(self.question6) + int(self.question7) + int(self.question8)

        super(Survey, self).save(*args, **kwargs)
