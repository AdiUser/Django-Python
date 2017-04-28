from django.db import models

# Create your models here.


class Questions(models.Model):
    question_text = models.TextField()
    correct_ans = models.CharField(max_length=800)

    def __str__(self):
        return self.question_text


class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option = models.CharField(max_length=800)


    def __str__(self):
        return self.option


class myInfo(models.Model):
    my_first_name = models.CharField(max_length=300)
    my_last_name = models.CharField(max_length=300)

    def __str__(self):
        return self.my_first_name + " "+ self.my_last_name;


class mySchool(models.Model):
    my_id = models.ForeignKey(myInfo, on_delete= models.CASCADE)
    my_school_name = models.TextField()

    def __str__(self):
        return self.my_school_name;