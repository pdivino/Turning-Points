events = [
    {"minute": 1, "team": "Blue", "type": "pass", "successful": True},
    {"minute": 2, "team": "Red", "type": "shot", "successful": False},
    {"minute": 3, "team": "Blue", "type": "turnover", "successful": None}, 
    {"minute": 4, "team": "Red", "type": "pass", "successful": True}, 
    {"minute": 5, "team": "Red", "type": "shot", "successful": False}, 
    {"minute": 6, "team": "Blue", "type": "pass", "successful": False}, 
    {"minute": 7, "team": "Blue", "type": "turnover", "successful": None}, 
    {"minute": 8, "team": "Red", "type": "pass", "successful": True}, 
    {"minute": 9, "team": "Red", "type": "pass", "successful": True}, 
    {"minute": 10, "team": "Red", "type": "pass", "successful": True}, 
    {"minute": 11, "team": "Red", "type": "shot", "successful": False}, 
    {"minute": 12, "team": "Blue", "type": "pass", "successful": True}, 
    {"minute": 13, "team": "Blue", "type": "pass", "successful": True}, 
    {"minute": 14, "team": "Blue", "type": "pass", "successful": True}, 
    {"minute": 15, "team": "Blue", "type": "shot", "successful": False}, 
    {"minute": 16, "team": "Red", "type": "pass", "successful": False}, 
    {"minute": 17, "team": "Red", "type": "turnover", "successful": None}, 
    {"minute": 18, "team": "Blue", "type": "shot", "successful": False},
    {"minute": 19, "team": "Red", "type": "pass", "successful": True}, 
    {"minute": 20, "team": "Red", "type": "pass", "successful": True}, 

] 

# event count
def count_events(events, team, event_type):
    count = 0

    for event in events:
        if event["team"] == team and event["type"] == event_type:
            count += 1

    return count  

# pass completion count
def count_completed_passes(events, team):
    completed = 0

    for event in events:
        if event["type"] == "pass" and event["team"] == team and event["successful"] is True:
            completed += 1

    return completed

print(len(events)) 
print(events[0]) 
print(events[19]["team"])  

# Shot counter total
shots = 0 

for event in events: 
    if event["type"] == "shot": 
        shots += 1 

print("Total shots:", shots)  

# Shot counter Blue Team 
Blue_Shots = count_events(events, "Blue", "shot") 

# Shot counter Red Team 
Red_Shots = count_events(events, "Red", "shot") 

# Total passes
passes = 0 

for event in events: 
    if event["type"] == "pass": 
        passes += 1 

print("Total passes:", passes)  

# Blue team pass attempts
Blue_Passes = count_events(events, "Blue", "pass")

# Blue completed passes
blue_completed_passes = count_completed_passes(events, "Blue")

# Blue pass percentage
if Blue_Passes > 0:
    blue_pass_percentage = (blue_completed_passes / Blue_Passes) * 100
    print(f"Blue pass completion: {blue_pass_percentage:.1f}%")
else:
    print("Blue pass completion: N/A")

# Red team pass attempts
Red_Passes = count_events(events, "Red", "pass")
print("Total Red Team pass attempts:", Red_Passes)

# Red completed passes
red_completed_passes = count_completed_passes(events, "Red")

# Red pass percentage
if Red_Passes > 0:
    red_pass_percentage = (red_completed_passes / Red_Passes) * 100
    print(f"Red pass completion: {red_pass_percentage:.1f}%")
else:
    print("Red pass completion: N/A") 

# Total turnovers
turnovers = 0 

for event in events: 
    if event["type"] == "turnover": 
        turnovers += 1 

print("Total turnovers:", turnovers) 
print("Blue shots:", count_events(events, "Blue", "shot"))
print("Red shots:", count_events(events, "Red", "shot"))
print("Blue turnovers:", count_events(events, "Blue", "turnover"))
print("Red turnovers:", count_events(events, "Red", "turnover")) 

# First half events
first_half_events = []

for event in events:
    if event["minute"] <= 10:
        first_half_events.append(event)

print("Events in minutes 1–10:", len(first_half_events))  
print("Blue early shots:", count_events(first_half_events, "Blue", "shot"))
print("Red early shots:", count_events(first_half_events, "Red", "shot")) 

# Second half events 
second_half_events = [] 

for event in events: 
    if event["minute"] > 10: 
        second_half_events.append(event) 

print("Events in minutes 11-20:", len(second_half_events)) 
print("Blue late shots:", count_events(second_half_events, "Blue", "shot")) 
print("Red late shots:", count_events(second_half_events, "Red", "shot")) 

# Change shot attempts Blue Team
blue_early_shots = count_events(first_half_events, "Blue", "shot")
blue_late_shots = count_events(second_half_events, "Blue", "shot")

blue_shot_change = blue_late_shots - blue_early_shots

print("Change in Blue shots:", blue_shot_change) 

# Change shot attempts Red Team
red_early_shots = count_events(first_half_events, "Red", "shot")
red_late_shots = count_events(second_half_events, "Red", "shot")

red_shot_change = red_late_shots - red_early_shots

print("Change in Red shots:", red_shot_change) 

# Shot analysis portion (Blue team)
if blue_shot_change > 0:
    print(f"Blue's shots increased from {blue_early_shots} to {blue_late_shots} in the later period.")
elif blue_shot_change < 0:
    print("Blue took fewer shots in the later period.")
else:
    print("Blue took the same number of shots in both periods.") 

# Shot analysis portion (Red team) 
if red_shot_change > 0: 
    print("Red took more shots later in the period.") 
elif red_shot_change < 0: 
     print(f"Red's shots decreased from {red_early_shots} to {red_late_shots} in the later period.")
else: 
    print("Red took the same number of shots in both periods.") 