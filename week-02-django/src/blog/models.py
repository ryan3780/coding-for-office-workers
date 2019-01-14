from django.db import models

class Article(models.Model) :
    title = models.CharField(max_length=30)
    contents = models.TextField()
    view_count = models.IntegerField()

    def __str__(self) :
        return "{} ({})".format(self.title, self.view_count)

class Comment(models.Model) :
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=100)
