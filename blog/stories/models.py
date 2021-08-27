from django.db import models


class Story(models.Model):
    title = models.CharField("title", max_length=50)
    link = models.URLField("link")
    up_vote = models.IntegerField("up Vote", default=0)
    down_vote = models.IntegerField("down Vote", default=0)
    archive = models.BooleanField(default=False)
    created_on = models.DateTimeField("created On", auto_now_add=True)
    modified_on = models.DateTimeField("modified On", auto_now=True)

    class Meta:
        db_table = "story"

    def get_verbose_name(self):
        return self._meta.verbose_name


class Comment(models.Model):
    text = models.CharField("text",max_length=250)
    story = models.ForeignKey('Story', on_delete=models.CASCADE)
    posted_on = models.DateTimeField("posted On", auto_now_add=True)
    modified_on = models.DateTimeField("modified On", auto_now=True)

    class Meta:
        db_table = "comment"
