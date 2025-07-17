import csv
import statistics

def summarize_csv(path):
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        cols = {}
        for row in reader:
            for k, v in row.items():
                try:
                    v = float(v)
                except (TypeError, ValueError):
                    continue
                cols.setdefault(k, []).append(v)

    summary = {}
    for k, vals in cols.items():
        summary[k] = {
            "min": min(vals),
            "max": max(vals),
            "mean": statistics.mean(vals),
            "median": statistics.median(vals),
            "stdev": statistics.stdev(vals) if len(vals) > 1 else 0
        }
    return summary

if __name__ == "__main__":
    import pprint
    pprint.pprint(summarize_csv("data.csv"))
