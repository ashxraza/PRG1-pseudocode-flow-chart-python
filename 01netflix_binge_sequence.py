print("=== Netflix Binge Calculator ===")
    
# Input
series_name = input("Enter the series name: ")
episodes_per_season = int(input("Enter episodes per season: "))
number_of_seasons = int(input("Enter number of seasons: "))
episode_length_minutes = int(input("Enter episode length in minutes: "))


# Calculations
total_episodes = episodes_per_season * number_of_seasons
total_minutes = total_episodes * episode_length_minutes
total_hours = total_minutes / 60
total_days = total_hours / 24


# Output
print(f"\nTo binge-watch {series_name} you need:")
print(f"{total_hours:.1f} hours")
print(f"That's {total_days:.1f} full days of your life!")

if total_days > 7:
    episodes_per_day = total_days / 7
    print(f"That's {episodes_per_day:.0f} episodes per day!")
    print("⚠️ That's a long show, maybe do something else with your time!")
else:
    print("✅ This is a reasonable amount of time for a show")