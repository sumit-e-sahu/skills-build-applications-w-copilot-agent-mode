from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Define models inline for demonstration; in a real app, these would be in models.py
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        Team.objects.all().delete()
        User.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User(name='Superman', email='superman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user_email='ironman@marvel.com', type='Running', duration=30),
            Activity(user_email='cap@marvel.com', type='Cycling', duration=45),
            Activity(user_email='spiderman@marvel.com', type='Swimming', duration=25),
            Activity(user_email='superman@dc.com', type='Running', duration=60),
            Activity(user_email='batman@dc.com', type='Cycling', duration=40),
            Activity(user_email='wonderwoman@dc.com', type='Swimming', duration=35),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel'),
            Workout(name='Power Yoga', description='Strength and flexibility', suggested_for='DC'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
