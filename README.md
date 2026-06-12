# Badminton Meet Calculator

A scheduling tool for collegiate badminton dual meets (2 teams), built by Richard Huang for the Badminton Club @ UC Davis. Give it two team rosters, your court count, and your time window — it generates a randomized, conflict-aware match schedule and exports it as a polished, scorekeeping-ready Excel sheet. If there is a need to schedule a Tri-Meet(3 team tournament), visit the [Badminton Trimeet Calculator](https://github.com/Sakidoe/Badminton-TriMeet-Calculator) Repo fully schedule an operational Tri-team meet.

## Input/ Output

Simply by putting in team rosters that are in .xlsx files aligned with this example:

<img width="328" height="964" alt="image" src="https://github.com/user-attachments/assets/4393cdc5-6fc7-4a13-801b-b507a6cc465c" />

And by configuring parameters, such as Time per match, Time range of Tournament, court numbers, and priority courts for top games, you can create an output .xlsx schedule, that is programmable and pre-formatted to track who wins games, and which matches should be played on what court.

<img width="1411" height="902" alt="image" src="https://github.com/user-attachments/assets/60f14216-c3e5-4754-80f4-a78ddeeba145" />

## Inspiration

Creating a meet schedule by hand, with rosters that could have 50+ players in each team can take 3+ hours, and includes a method of studying teams to see who has the most number of games, and assorting them in a certain fashion. This method was difficult to teach and implement flawlessly, so instead, beginning in 2022, I built this program as a replacement. The result is a robust and flawless program that works with data structures, Python, and algorithmic logic to merge two rosters, create a schedule, and check for conflicts all in < 5 minutes.

## What It Does

Running a dual meet means scheduling dozens of matches across five events — Men's Singles (MS), Men's Doubles (MD), Women's Singles (WS), Women's Doubles (WD), and Mixed Doubles (XD) — *without double-booking players* who compete in multiple events. This tool automates that:

- **Reads rosters directly from Excel** — each team submits a simple ranked lineup sheet
- **Validates feasibility** — checks that your courts × time window can actually fit every required match before scheduling
- **Avoids player conflicts** — won't schedule a player on two courts in the same timeslot, and flags unavoidable conflicts when they occur
- **Supports priority courts** — reserve your best courts (1–3) for top-seeded matchups
- **Exports a formatted Excel scoresheet** — color-coded schedule with per-match score entry, plus live A-Team and Overall tally formulas so the running team score updates as results come in
- **Audits the final schedule** — a standalone checker reports same-timeslot conflicts and back-to-back matches, with suggested alternative slots

## Tech Stack

**Language:** Python 3

| Library | Role |
|---|---|
| `openpyxl` | Reads team roster `.xlsx` files |
| `xlsxwriter` | Generates the formatted `result.xlsx` scoresheet (merged cells, color formats, SUM formulas) |
| `pandas` | Tabular data handling |
| `json` | Roster and schedule serialization (`save.txt`, `schedule.txt`) |
| `datetime` | Time-window math and timeslot generation |
| `random` | Match/rank selection during schedule generation |
| `msvcrt` / `termios` + `tty` (built-in) | Cross-platform arrow-key navigation for the interactive terminal menu |

Install dependencies:
```bash
pip3 install openpyxl xlsxwriter pandas
```

## How to Run

The pipeline runs in four stages, each feeding the next automatically:

**1. `Json_Team_Parser.py` — build the rosters.**
Prepare each team's roster as an `.xlsx` file: event headers (`MD`, `MS`, `XD`, `WS`, `WD`) followed by rank numbers and player names. Run the script, enter both team names, then use the arrow-key menu: **Add Roster** (`A`) for each team (you'll be prompted for the roster filename), then **Save** (`S`). Output: `save.txt` — both rosters in JSON.

**2. `Json_Schedule_Parser.py` — generate the schedule.**
Run it — it loads the rosters from `save.txt` automatically. Enter the time per game cycle, meet start/end times (24-hour format), number of courts, and optional priority courts. The script verifies the meet fits the time window, then builds a randomized conflict-aware schedule. Output: `schedule.txt`.

**3. `XLSX_Parser.py` — export to Excel.**
Run it — it loads `schedule.txt` and the team names automatically. Output: `result.xlsx`, the formatted meet scoresheet with score columns and automatic team tallies.

**4. `conflict_checker.py` — verify.**
Run it and enter `schedule.txt` when prompted. It reports same-timeslot conflicts and back-to-back matches, with suggested timeslot moves for each.

## Notes

- Designed for exactly **two teams** per meet.
- Run all scripts from the project folder so they can find `save.txt` and `schedule.txt`.
- Roster format reference: see `ucd.xlsx` / `ucsc.xlsx` in this repo.
