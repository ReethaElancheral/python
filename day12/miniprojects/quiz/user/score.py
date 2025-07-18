# quiz/user/score.py

def calculate_score(results, elapsed):
    correct = sum(results)
    total = len(results)
    percent = correct / total * 100
    return {
        'correct': correct,
        'total': total,
        'percent': percent,
        'time_sec': int(elapsed)
    }

def display_score(report):
    print("\n=== Quiz Results ===")
    print(f"Score: {report['correct']} / {report['total']} ({report['percent']:.1f}%)")
    print(f"Time: {report['time_sec']} seconds")
