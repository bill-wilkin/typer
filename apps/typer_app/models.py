from django.db import models
from ..login_reg_app.models import User


class Target(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Note: the Targets will need to be added either programatically in the shell or through Django Admin.  The database has been omitted from the repo


class Session(models.Model):
    wpm = models.IntegerField()
    accuracy = models.FloatField()
    target = models.ForeignKey(
        Target, related_name='in_sessions', on_delete=models.CASCADE)
    taken_by = models.ForeignKey(
        User, related_name="sessions", on_delete=models.CASCADE)
    time = models.CharField(max_length=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
