from pymongo import MongoClient

def populate_test_data():
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']

    # Populate users collection
    users = db['users']
    user1 = users.insert_one({"email": "student1@example.com", "name": "Student One", "password": "password1"}).inserted_id
    user2 = users.insert_one({"email": "student2@example.com", "name": "Student Two", "password": "password2"}).inserted_id

    # Populate teams collection
    teams = db['teams']
    team1 = teams.insert_one({"name": "Team Alpha", "members": [user1, user2]}).inserted_id

    # Populate activities collection
    activities = db['activities']
    activities.insert_one({"user": user1, "type": "Running", "duration": 30, "date": "2025-04-20"})
    activities.insert_one({"user": user2, "type": "Cycling", "duration": 45, "date": "2025-04-21"})

    # Populate leaderboard collection
    leaderboard = db['leaderboard']
    leaderboard.insert_one({"team": team1, "score": 100})

    # Populate workouts collection
    workouts = db['workouts']
    workouts.insert_one({"name": "Push-ups", "description": "Do 20 push-ups"})
    workouts.insert_one({"name": "Squats", "description": "Do 30 squats"})

    print("Test data populated successfully.")
