from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    options = models.CharField(max_length=255)  # Consider using a better structure for options

    def __str__(self):
        return self.question_text
