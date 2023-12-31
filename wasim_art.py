import os
from datetime import datetime, timedelta

# Letter patterns (W,A,S,I,M) mapped to weeks of 2024
# 1 = Commit, 0 = No commit
letter_patterns = {
    # W (Weeks 1-8, Jan 1 - Feb 25)
    "W": [
        [1,0,0,0,1],  # Sun
        [1,0,0,0,1],  # Mon
        [1,0,0,0,1],  # Tue
        [1,0,1,0,1],  # Wed
        [1,1,0,1,1],  # Thu
        [1,0,0,0,1],  # Fri
        [1,0,0,0,1]   # Sat
    ],
    # A (Weeks 9-16, Feb 26 - Apr 21)
    "A": [
        [0,1,0],
        [1,0,1],
        [1,1,1],
        [1,0,1],
        [1,0,1],
        [1,0,1],
        [0,0,0]
    ],
    # S (Weeks 17-24, Apr 22 - Jun 16)
    "S": [
        [1,1,1],
        [1,0,0],
        [1,1,1],
        [0,0,1],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ],
    # I (Weeks 25-32, Jun 17 - Aug 11)
    "I": [
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1]
    ],
    # M (Weeks 33-52, Aug 12 - Dec 31)
    "M": [
        [1,0,0,0,1],
        [1,1,0,1,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1]
    ]
}

def generate_commits():
    start_date = datetime(2024, 1, 1)  # Start Jan 1, 2024
    total_weeks = 52
    week_starts = [start_date + timedelta(weeks=i) for i in range(total_weeks)]
    
    for week_num, week_start in enumerate(week_starts, 1):
        # Assign letter based on week range
        if 1 <= week_num <= 8:   letter = "W"
        elif 9 <= week_num <= 16: letter = "A"
        elif 17 <= week_num <= 24: letter = "S"
        elif 25 <= week_num <= 32: letter = "I"
        elif 33 <= week_num <= 52: letter = "M"
        else: continue
        
        pattern = letter_patterns[letter]
        week_days = [week_start + timedelta(days=i) for i in range(7)]
        
        for day_num, day in enumerate(week_days):
            day_pattern = pattern[day_num]
            for col in range(len(day_pattern)):
                if day_pattern[col] == 1:
                    commit_date = day + timedelta(weeks=col)
                    # Format date for Git
                    date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
                    # Create empty commit
                    os.system(f'git commit --allow-empty --date="{date_str}" -m "WASIM Art"')
    
    print("Done! Push to GitHub with: git push origin main")

if __name__ == "__main__":
    # Initialize Git repo if not exists
    if not os.path.exists(".git"):
        os.system("git init")
        os.system("git checkout -b main")
        with open("README.md", "w") as f:
            f.write("# GitHub Art Project: WASIM\n")
        os.system("git add . && git commit -m 'Initial commit'")
    
    generate_commits()