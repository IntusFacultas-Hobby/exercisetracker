from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()


# Create your models here.
class WorkoutTemplate(models.Model):

    name = models.CharField("Name", max_length=256)
    user = models.ForeignKey(
        User, related_name="templates", on_delete=models.CASCADE)


class Activity(models.Model):
    name = models.CharField("Name", max_length=256)
    templates = models.ManyToManyField(
        WorkoutTemplate, related_name="activities")
    description = models.TextField("Description")
    user = models.ForeignKey(
        User, related_name="activities", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Activities"


class Unit(models.Model):
    unit = models.CharField("Unit", max_length=128)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="units")
    user = models.ForeignKey(
        User, related_name="units",
        on_delete=models.CASCADE
    )


class Workout(models.Model):
    date = models.DateTimeField("Date Created")
    name = models.CharField("Name", max_length=512)
    notes = models.TextField("Notes")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="workouts")

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = timezone.now()
        super(Workout, self).save(*args, **kwargs)


class Performance(models.Model):

    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="performances")
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, related_name="performances"
    )
    value = models.CharField("Value", max_length=256)
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="workouts")
