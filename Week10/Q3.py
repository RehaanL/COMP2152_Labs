# ============================================================
#  WEEK 10 LAB — Q3: SECURITY AUDIT LOG + UNIT TESTS
#  COMP2152 — [Rehaan Lachporia]
# ============================================================

import sqlite3
import unittest


DB_NAME = "audit.db"


# --- Helpers (provided) — seeds the database with sample data ---
def seed_database():
    """Create and populate the audit_log table with sample security events."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS audit_log")
    cursor.execute("""CREATE TABLE audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        user TEXT,
        action TEXT,
        severity TEXT,
        details TEXT
    )""")
    sample_data = [
        ("2026-03-16 08:00:00", "admin",   "LOGIN",           "LOW",    "Successful login from 192.168.1.10"),
        ("2026-03-16 08:05:00", "root",    "FAILED_LOGIN",    "HIGH",   "Failed SSH attempt from 10.0.0.99"),
        ("2026-03-16 08:10:00", "admin",   "FILE_ACCESS",     "LOW",    "Read /etc/config.yaml"),
        ("2026-03-16 08:15:00", "root",    "FAILED_LOGIN",    "HIGH",   "Failed SSH attempt from 10.0.0.99"),
        ("2026-03-16 08:20:00", "guest",   "FILE_MODIFY",     "MEDIUM", "Modified /tmp/upload.csv"),
        ("2026-03-16 08:25:00", "admin",   "PERMISSION_CHANGE","HIGH",  "Changed permissions on /etc/shadow"),
        ("2026-03-16 08:30:00", "guest",   "LOGOUT",          "LOW",    "Session ended normally"),
        ("2026-03-16 08:35:00", "backup",  "FILE_ACCESS",     "LOW",    "Read /var/backups/db.sql"),
        ("2026-03-16 08:40:00", "guest",   "FILE_MODIFY",     "MEDIUM", "Modified /tmp/data.json"),
        ("2026-03-16 08:45:00", "admin",   "LOGOUT",          "LOW",    "Session ended normally"),
    ]
    cursor.executemany(
        "INSERT INTO audit_log (timestamp, user, action, severity, details) VALUES (?, ?, ?, ?, ?)",
        sample_data
    )
    conn.commit()
    conn.close()


def display_events(events):
    """Pretty-print a list of audit events."""
    if not events:
        print("  (no events)")
        return
    for row in events:
        print(f"  [{row[1]}]  {row[4]:<6}  {row[2]:<8}  {row[3]:<18}  {row[5]}")


# TODO: Complete get_events_by_severity(severity)
#   Connect to DB_NAME.
#   SELECT all rows from audit_log WHERE severity matches the parameter.
#   Fetch all rows, close the connection, and return the list.
def get_events_by_severity(severity):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM audit_log WHERE severity = ?""", (severity,))
    rows = cursor.fetchall()
    conn.close()
    return rows


# TODO: Complete get_recent_events(limit)
#   Connect to DB_NAME.
#   SELECT all rows from audit_log ORDER BY timestamp DESC LIMIT ?
#   Use the limit parameter for the LIMIT value.
#   Fetch all rows, close the connection, and return the list.
def get_recent_events(limit):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""SELECT * from audit_log ORDER BY timestamp DESC LIMIT ?""", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows


# TODO: Complete count_by_severity()
#   Connect to DB_NAME.
#   Execute: SELECT severity, COUNT(*) FROM audit_log
#            GROUP BY severity ORDER BY COUNT(*) DESC
#   Fetch all rows, close the connection, and return the list.
def count_by_severity():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""SELECT severity, COUNT(*) FROM audit_log GROUP BY severity ORDER BY COUNT(*) DESC""")
    rows = cursor.fetchall()
    conn.close()
    return rows


# TODO: Complete safe_query(query)
#   Connect to DB_NAME.
#   Try to execute the query using cursor.execute(query).
#   If successful, fetch all rows and return them.
#   If sqlite3.Error occurs, print f"Database error: {e}" and return [].
#   Always close the connection in a finally block.
def safe_query(query):
    conn = sqlite3.connect(DB_NAME)
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()



# ============================================================
#  UNIT TESTS — fill in the test methods
# ============================================================
class TestAuditLog(unittest.TestCase):

    def setUp(self):
        seed_database()

    def test_high_severity(self):
        events = get_events_by_severity("HIGH")
        self.assertEqual(len(events), 3)

    def test_recent_events(self):
        events = get_recent_events(5)
        self.assertEqual(len(events), 5)

    def test_count(self):
        counts = count_by_severity()
        self.assertIn(("HIGH", 3), counts)

    def test_safe_bad_query(self):
        result = safe_query("SELECT * FROM fake_table")
        self.assertEqual(result, [])

# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  SECURITY AUDIT LOG")
    print("=" * 60)

    seed_database()

    print("\n--- HIGH Severity Events ---")
    display_events(get_events_by_severity("HIGH"))

    print("\n--- 5 Most Recent Events ---")
    display_events(get_recent_events(5))

    print("\n--- Event Counts by Severity ---")
    counts = count_by_severity()
    if counts:
        for severity, count in counts:
            print(f"  {severity:<8}  {count}")
    else:
        print("  (none)")

    print("\n--- Safe Query (valid) ---")
    results = safe_query("SELECT user, action FROM audit_log WHERE severity = 'HIGH'")
    if results:
        for row in results:
            print(f"  {row[0]:<8}  {row[1]}")

    print("\n--- Safe Query (invalid — should not crash) ---")
    results = safe_query("SELECT * FROM nonexistent_table")
    print(f"  Returned: {results}")

    print("\n--- Running Unit Tests ---")
    unittest.main(verbosity=2, exit=False)

    print("\n" + "=" * 60)