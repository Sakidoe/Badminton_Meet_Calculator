import json
from datetime import datetime, timedelta

BOLD = '\033[1m'
END = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'


def load_schedule(filename):
    """Load the schedule from a JSON/txt file."""
    with open(filename, 'r') as f:
        return json.load(f)


def get_players_from_match(match_info):
    """Extract all players from a match."""
    players = []
    # match_info format: [event_code, [team1_players], [team2_players]]
    if len(match_info) >= 3:
        # Team 1 players
        for player in match_info[1]:
            players.append(player)
        # Team 2 players
        for player in match_info[2]:
            players.append(player)
    return players


def check_same_timeslot_conflicts(schedule):
    """Check for players playing multiple matches in the same timeslot."""
    conflicts = []
    
    for timeslot, courts in schedule.items():
        player_matches = {}  # {player_name: [list of court numbers]}
        
        for court_num, match_info in courts.items():
            players = get_players_from_match(match_info)
            
            for player in players:
                if player not in player_matches:
                    player_matches[player] = []
                player_matches[player].append({
                    'court': court_num,
                    'event': match_info[0],
                    'match': match_info
                })
        
        # Find players with multiple matches
        for player, matches in player_matches.items():
            if len(matches) > 1:
                conflicts.append({
                    'timeslot': timeslot,
                    'player': player,
                    'matches': matches
                })
    
    return conflicts


def parse_time(time_str):
    """Convert time string to datetime object for comparison."""
    try:
        # Handle both "10:00" and "01:00" formats
        return datetime.strptime(time_str, "%H:%M")
    except:
        # Try alternate format
        return datetime.strptime(time_str, "%I:%M")


def get_consecutive_timeslots(schedule):
    """Get list of timeslots in order."""
    timeslots = sorted(schedule.keys(), key=parse_time)
    return timeslots


def check_back_to_back_matches(schedule):
    """Check for players with back-to-back matches."""
    timeslots = get_consecutive_timeslots(schedule)
    back_to_back = []
    
    # Build a player -> timeslot mapping
    player_schedule = {}  # {player: [(timeslot, court, event, match_info)]}
    
    for timeslot, courts in schedule.items():
        for court_num, match_info in courts.items():
            players = get_players_from_match(match_info)
            
            for player in players:
                if player not in player_schedule:
                    player_schedule[player] = []
                player_schedule[player].append({
                    'timeslot': timeslot,
                    'court': court_num,
                    'event': match_info[0],
                    'match': match_info
                })
    
    # Check for consecutive timeslots
    for player, matches in player_schedule.items():
        # Sort by timeslot
        sorted_matches = sorted(matches, key=lambda x: parse_time(x['timeslot']))
        
        for i in range(len(sorted_matches) - 1):
            current_time = sorted_matches[i]['timeslot']
            next_time = sorted_matches[i + 1]['timeslot']
            
            # Check if they're consecutive
            current_idx = timeslots.index(current_time)
            next_idx = timeslots.index(next_time)
            
            if next_idx == current_idx + 1:
                back_to_back.append({
                    'player': player,
                    'first_match': sorted_matches[i],
                    'second_match': sorted_matches[i + 1]
                })
    
    return back_to_back, player_schedule


def suggest_alternative_slots(player, match_to_move, schedule, player_schedule):
    """Suggest alternative timeslots for a match."""
    timeslots = get_consecutive_timeslots(schedule)
    player_timeslots = [m['timeslot'] for m in player_schedule[player]]
    
    suggestions = []
    
    for timeslot in timeslots:
        # Skip if player already plays in this slot
        if timeslot in player_timeslots:
            continue
        
        # Check if this timeslot is adjacent to any of player's matches
        current_idx = timeslots.index(timeslot)
        is_adjacent = False
        
        for player_time in player_timeslots:
            player_idx = timeslots.index(player_time)
            if abs(current_idx - player_idx) == 1:
                is_adjacent = True
                break
        
        if not is_adjacent:
            # Check if the other players in the match also don't conflict
            match_info = match_to_move['match']
            all_players = get_players_from_match(match_info)
            
            conflict_free = True
            for p in all_players:
                if p in player_schedule:
                    if timeslot in [m['timeslot'] for m in player_schedule[p]]:
                        conflict_free = False
                        break
            
            if conflict_free:
                suggestions.append(timeslot)
    
    return suggestions


def print_results(same_time_conflicts, back_to_back_conflicts, schedule, player_schedule):
    """Print formatted results."""
    print("\n" + "="*70)
    print(f"{BOLD}{'SCHEDULE CONFLICT CHECKER':^70}{END}")
    print("="*70 + "\n")
    
    # Same timeslot conflicts
    print(f"{BOLD}[1] SAME TIMESLOT CONFLICTS{END}")
    print("-"*70)
    
    if not same_time_conflicts:
        print(f"{GREEN}✓ No same-timeslot conflicts found! Schedule is conflict-free.{END}\n")
    else:
        print(f"{RED}✗ Found {len(same_time_conflicts)} same-timeslot conflicts:{END}\n")
        
        for i, conflict in enumerate(same_time_conflicts, 1):
            print(f"{BOLD}{i}. {conflict['player']}{END} at {YELLOW}{conflict['timeslot']}{END}")
            for match in conflict['matches']:
                print(f"   Court {match['court']}: {match['event']}")
            print()
    
    # Back-to-back conflicts
    print(f"\n{BOLD}[2] BACK-TO-BACK MATCH CONFLICTS{END}")
    print("-"*70)
    
    if not back_to_back_conflicts:
        print(f"{GREEN}✓ No back-to-back matches found!{END}\n")
    else:
        print(f"{YELLOW}⚠ Found {len(back_to_back_conflicts)} players with back-to-back matches:{END}\n")
        
        for i, conflict in enumerate(back_to_back_conflicts, 1):
            player = conflict['player']
            first = conflict['first_match']
            second = conflict['second_match']
            
            print(f"{BOLD}{i}. {player}{END}")
            print(f"   {RED}First match:{END}  {first['timeslot']} - Court {first['court']} - {first['event']}")
            print(f"   {RED}Second match:{END} {second['timeslot']} - Court {second['court']} - {second['event']}")
            
            # Suggest alternatives
            suggestions_first = suggest_alternative_slots(player, first, schedule, player_schedule)
            suggestions_second = suggest_alternative_slots(player, second, schedule, player_schedule)
            
            print(f"   {GREEN}Suggested moves:{END}")
            if suggestions_first:
                print(f"   • Move first match ({first['event']}) to: {', '.join(suggestions_first[:3])}")
            if suggestions_second:
                print(f"   • Move second match ({second['event']}) to: {', '.join(suggestions_second[:3])}")
            
            if not suggestions_first and not suggestions_second:
                print(f"   {YELLOW}• No conflict-free alternatives available{END}")
            
            print()
    
    print("="*70)


def main():
    """Main function."""
    filename = input(f"{BOLD}Enter the schedule filename (e.g., schedule.txt):{END} ")
    
    try:
        print(f"\n{BLUE}Loading schedule...{END}")
        schedule = load_schedule(filename)
        
        print(f"{BLUE}Checking for conflicts...{END}\n")
        
        # Check same timeslot conflicts
        same_time_conflicts = check_same_timeslot_conflicts(schedule)
        
        # Check back-to-back conflicts
        back_to_back_conflicts, player_schedule = check_back_to_back_matches(schedule)
        
        # Print results
        print_results(same_time_conflicts, back_to_back_conflicts, schedule, player_schedule)
        
    except FileNotFoundError:
        print(f"{RED}Error: File '{filename}' not found!{END}")
    except json.JSONDecodeError:
        print(f"{RED}Error: Invalid JSON format in file!{END}")
    except Exception as e:
        print(f"{RED}Error: {str(e)}{END}")


if __name__ == "__main__":
    main()