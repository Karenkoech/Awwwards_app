from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project_pics',null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.title} Project'


class Rating(models.Model):
    design = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    usability = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    content = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
         return f'{self.user.username} {self.project.title} Rating'
