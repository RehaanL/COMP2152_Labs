# ============================================================
#  WEEK 10 LAB — Q1: PASSWORD VAULT
#  COMP2152 — [Rehaan Lachporia]
# ============================================================

import sqlite3

DB_NAME = "vault.db"

# --- Helpers (provided) ---
def setup_database():
    """Create the vault table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS vault (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT,
        username TEXT,
        password TEXT
    )""")
    conn.commit()
    conn.close()


def display_credentials(credentials):
    """Pretty-print a list of credential rows."""
    if not credentials:
        print("  (no results)")
        return
    for row in credentials:
        print(f"  {row[1]:<14} | {row[2]:<12} | {row[3]}")


# TODO: Complete add_credential(website, username, password)
#   Connect to DB_NAME.
#   INSERT a row into vault with: website, username, password.
#   Commit and close the connection.
def add_credential(website, username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO vault (website, username, password) VALUES (?, ?, ?)""",
                   (website, username, password))
    conn.commit()
    conn.close()


# TODO: Complete get_all_credentials()
#   Connect to DB_NAME.
#   SELECT all rows from vault, ordered by website ASC.
#   Fetch all rows, close the connection, and return the list.
def get_all_credentials():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM vault
                   ORDER BY website ASC""")
    results = cursor.fetchall()
    conn.close()
    return results


# TODO: Complete find_credential(website)
#   Connect to DB_NAME.
#   SELECT all rows from vault WHERE website matches the parameter.
#   Fetch all rows, close the connection, and return the list.
def find_credential(website):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM vault WHERE website = ?""", (website,))
    results = cursor.fetchall()
    conn.close()
    return results



# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  PASSWORD VAULT")
    print("=" * 60)

    setup_database()

    print("\n--- Adding Credentials ---")
    credentials = [
        ("github.com",  "admin",        "s3cur3P@ss"),
        ("google.com",  "maziar@gmail",  "MyP@ssw0rd"),
        ("netflix.com", "maziar",        "N3tfl1x!"),
        ("github.com",  "work_user",    "W0rkP@ss!"),
    ]
    for site, user, pw in credentials:
        add_credential(site, user, pw)
        print(f"  Saved: {site}" + (f" ({user.split('_')[0]})" if "_" in user else ""))

    print("\n--- All Credentials ---")
    display_credentials(get_all_credentials())

    print("\n--- Search for 'github.com' ---")
    display_credentials(find_credential("github.com"))

    print("\n--- Search for 'spotify.com' ---")
    display_credentials(find_credential("spotify.com"))

    print("\n" + "=" * 60)