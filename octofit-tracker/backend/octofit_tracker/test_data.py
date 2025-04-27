from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

def populate_test_data():
    # Create test users
    user1 = User.objects.create(email="student1@example.com", name="Student One", password="password1")
    user2 = User.objects.create(email="student2@example.com", name="Student Two", password="password2")

    # Create test teams
    team1 = Team.objects.create(name="Team Alpha", members=[user1.id, user2.id])

    # Create test activities
    Activity.objects.create(user=user1, type="Running", duration=30, date="2025-04-20")
    Activity.objects.create(user=user2, type="Cycling", duration=45, date="2025-04-21")

    # Create test leaderboard
    Leaderboard.objects.create(team=team1, score=100)

    # Create test workouts
    Workout.objects.create(name="Push-ups", description="Do 20 push-ups")
    Workout.objects.create(name="Squats", description="Do 30 squats")

    print("Test data populated successfully.")
