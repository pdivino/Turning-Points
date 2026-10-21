# Synthetic match events
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


# Count a particular event type for a team.
def count_events(events, team, event_type):
    count = 0

    for event in events:
        if event["team"] == team and event["type"] == event_type:
            count += 1

    return count


# Count successful passes for a team.
def count_completed_passes(events, team):
    completed = 0

    for event in events:
        if (
            event["type"] == "pass"
            and event["team"] == team
            and event["successful"] is True
        ):
            completed += 1

    return completed


# Describe the difference between two periods' shot counts.
def describe_shot_change(team, early_shots, late_shots):
    change = late_shots - early_shots

    if change > 0:
        return f"{team}'s shots increased from {early_shots} to {late_shots}."
    elif change < 0:
        return f"{team}'s shots decreased from {early_shots} to {late_shots}."
    else:
        return f"{team} took {early_shots} shots in each period."


# Select events within a minute range, including both boundaries.
def filter_events_by_minute(events, start_minute, end_minute):
    selected_events = []

    for event in events:
        if start_minute <= event["minute"] <= end_minute:
            selected_events.append(event)

    return selected_events


# Select the two periods we want to compare.
early_events = filter_events_by_minute(events, 1, 10)
late_events = filter_events_by_minute(events, 11, 20)


# Display a report for each team.
print("\n=== MATCH REPORT ===")
print("Synthetic sample: minutes 1–20")
print("Shot comparison: minutes 1–10 versus 11–20")

for team in ["Blue", "Red"]:
    team_shots = count_events(events, team, "shot")
    team_turnovers = count_events(events, team, "turnover")
    team_passes = count_events(events, team, "pass")
    team_completed_passes = count_completed_passes(events, team)

    print(f"\n{team}")
    print(f"Shots: {team_shots}")
    print(f"Turnovers: {team_turnovers}")
    print(f"Pass attempts: {team_passes}")
    print(f"Completed passes: {team_completed_passes}")

    if team_passes > 0:
        completion_percentage = (team_completed_passes / team_passes) * 100
        print(f"Pass completion: {completion_percentage:.1f}%")
    else:
        print("Pass completion: N/A")

    early_shots = count_events(early_events, team, "shot")
    late_shots = count_events(late_events, team, "shot")

    print(describe_shot_change(team, early_shots, late_shots))


# Examine shorter periods.
window_events = filter_events_by_minute(events, 11, 15)

print("\n=== MINUTES 11–15 ===")
print("Blue shots:", count_events(window_events, "Blue", "shot"))
print("Red shots:", count_events(window_events, "Red", "shot"))

later_window_events = filter_events_by_minute(events, 16, 20)

print("\n=== MINUTES 16–20 ===")
print("Blue shots:", count_events(later_window_events, "Blue", "shot"))
print("Red shots:", count_events(later_window_events, "Red", "shot"))


# Check a single minute.
minute_15_events = filter_events_by_minute(events, 15, 15)

print("\n=== MINUTE 15 ===")
print("Blue shots:", count_events(minute_15_events, "Blue", "shot"))