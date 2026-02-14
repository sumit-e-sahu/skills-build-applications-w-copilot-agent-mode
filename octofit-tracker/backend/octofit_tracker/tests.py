from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.email, 'test@example.com')
    def test_create_team(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='test@example.com', type='Run', duration=10)
        self.assertEqual(activity.type, 'Run')
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Marvel', points=10)
        self.assertEqual(lb.points, 10)
    def test_create_workout(self):
        workout = Workout.objects.create(name='TestWorkout', description='desc', suggested_for='Marvel')
        self.assertEqual(workout.name, 'TestWorkout')
