print("=== Gaming Achievement Checker ===")

# Input
player_score = 0
time_played_hours = 0
enemies_defeated = 0

while player_score <=0 :
    print("Please enter a positive number for your player score")
    player_score = int(input("Enter your player score: "))
while time_played_hours <=0:
    print("Please enter a positive number for your time played")
    time_played_hours = int(input("Enter your time played: "))
while enemies_defeated <=0:
    print("Please enter a positive number for the amount of enemies defeated")
    enemies_defeated = int(input("Enter enemies defeated: "))

# Selection logic
if player_score >= 15000 and time_played_hours >= 100:
    achievement = "Legend"
elif player_score >= 10000 and time_played_hours >= 50:
    achievement = "Master Player"
elif enemies_defeated >= 1000:
    achievement = "Combat Expert"
elif time_played_hours >= 20:
    achievement = "Dedicated Gamer"
elif player_score >= 5000:
    achievement = "Rising Star"
else:
    achievement = "Newcomer"

# Output
print(f"\nCongratulations! You've earned: {achievement}")

if achievement == "Master Player":
    print("You've unlocked the secret bonus level!")