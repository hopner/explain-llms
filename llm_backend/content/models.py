from django.db import models

class Chapter(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Section(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='sections', on_delete=models.CASCADE)
    order = models.IntegerField()
    language = models.CharField(max_length=10, default='en')
    content_markdown = models.TextField()
    animation_state = models.CharField(max_length=100)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.chapter.title} - {self.order} ({self.language})"
