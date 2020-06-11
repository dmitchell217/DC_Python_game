from run_day import run_day

def run_time(days):
    elapsed = 0
    while elapsed < days:
        run_day()
        elapsed +=1

