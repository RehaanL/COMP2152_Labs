# ============================================================
#  WEEK 13 LAB — Q2: ASCII DASHBOARD
#  COMP2152 — [Rehaan Lachporia - 101594859]
# ============================================================

import csv


SAMPLE_FILE = "scan_results.csv"


# --- Helper (provided) ---
def load_findings(filename):
    """Load CSV findings (from Q1)."""
    with open(filename, "r") as f:
        return list(csv.DictReader(f))


# TODO: Complete bar_chart(data, title, max_width=30)
#   Print the title
#   Find the max value in data for scaling: max_val = max(count for _, count in data)
#   For each (label, count) in data:
#     Calculate bar length: int((count / max_val) * max_width)
#     Print: f"  {label:<15} {'█' * bar_length} {count}"
def bar_chart(data, title, max_width=30):
    print(f"{title}")
    max_value = max(count for _, count in data)
    for label, count in data:
        bar_length = int((count / max_value) * max_width)
        print(f"    {label:<15} {'█' * bar_length} {count}")



# TODO: Complete severity_summary(findings)
#   Count findings per severity (HIGH, MEDIUM, LOW)
#   Return as a list of (severity, count) tuples
#   Order: HIGH first, then MEDIUM, then LOW
def severity_summary(findings):
    count = {}
    for f in findings:
        severity = f["severity"]
        count[severity] = count.get(severity, 0) + 1
    order = ["HIGH", "MEDIUM", "LOW"]
    return [(severity, count.get(severity, 0)) for severity in order if severity in count]







# TODO: Complete timeline(findings)
#   Count findings per date (use the "date" field)
#   Return as a list of (date, count) tuples, sorted by date ascending
def timeline(findings):
    count = {}
    for f in findings:
        date = f["date"]
        count[date] = count.get(date, 0) + 1
    return sorted(count.items())


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: ASCII DASHBOARD")
    print("=" * 60)

    findings = load_findings(SAMPLE_FILE)

    print()
    sev = severity_summary(findings)
    if sev:
        bar_chart(sev, "SEVERITY BREAKDOWN")

    print()
    dates = timeline(findings)
    if dates:
        bar_chart(dates, "FINDINGS BY DATE")

    print()
    # Count by type for a third chart
    type_counts = {}
    for f in findings:
        t = f["type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    type_data = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
    if type_data:
        bar_chart(type_data, "VULNERABILITY TYPES")

    print("\n" + "=" * 60)