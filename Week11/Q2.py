# ============================================================
#  WEEK 11 LAB — Q2: PASSWORD STRENGTH CHECKER
#  COMP2152 — [Rehaan Lachporia]
# ============================================================
#
#  For the term project, you'll be looking for weak passwords
#  on 0x10.cloud. This class helps you understand what makes
#  a password weak or strong.
#
# ============================================================


class PasswordChecker:

    # TODO: Write the constructor
    #   Create a list self.common_passwords with:
    #     "admin", "password", "123456", "root", "guest", "letmein", "welcome"
    #   Create an empty list self.history
    def __init__(self):
        self.common_passwords = ["admin", "password", "123456", "root", "guest", "letmein", "welcome"]
        self.history = []

    # TODO: Write check_common(self, password)
    #   Return True if password.lower() is in self.common_passwords
    #   Return False otherwise
    def check_common(self, password):
        if password.lower() in self.common_passwords:
            return True
        else:
            return False

    # TODO: Write check_strength(self, password)
    #   has_length = len(password) >= 8
    #   has_digit = any(c.isdigit() for c in password)
    #   has_special = any(c in "!@#$%^&*" for c in password)
    #   Return a dictionary: {"length": has_length, "digit": has_digit, "special": has_special}
    def check_strength(self, password):
        has_length = len(password) >=8
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)
        return {"length": has_length,
                "digit": has_digit,
                "special": has_special}

    # TODO: Write evaluate(self, password)
    #   1. If check_common(password) is True:
    #        result = "WEAK (common password)"
    #   2. Otherwise, call check_strength(password)
    #        Count how many values in the dictionary are True: sum(strength.values())
    #        0 or 1 True = "WEAK"
    #        2 True = "MEDIUM"
    #        3 True = "STRONG"
    #   3. Append (password, result) to self.history
    #   4. Return result
    def evaluate(self, password):
        if self.check_common(password):
            result = "WEAK (common password)"
        else:
            self.check_strength(password)
            count = sum(self.check_strength(password).values())
            if count == 0 or 1:
                result = "WEAK"

            if count == 2:
                result = "MEDIUM"

            if count == 3:
                result = "STRONG"
        self.history.append((password, result))
        return result






# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: PASSWORD STRENGTH CHECKER")
    print("=" * 60)

    checker = PasswordChecker()

    test_passwords = ["admin", "hello", "hello123", "MyP@ss99", "p@ssw0rd!", "root"]

    print("\n--- Checking Passwords ---")
    for pw in test_passwords:
        result = checker.evaluate(pw)
        if result:
            print(f"  {pw:<15} → {result}")

    print("\n--- Check History ---")
    if hasattr(checker, 'history') and checker.history:
        for pw, result in checker.history:
            print(f"  {pw:<15} : {result}")
    else:
        print("  (no history)")

    print("\n" + "=" * 60)