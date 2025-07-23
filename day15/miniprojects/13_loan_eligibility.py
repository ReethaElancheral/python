# 13. Loan Eligibility Checker

# Use Case: Accept income, credit score, and validate. 
# Exception Handling Goals:
# Raise LowCreditScoreError
# Handle ValueError for non-numeric inputs
# Use try-else to display eligibility
# Use assert for positive income

# Custom Exception
class LowCreditScoreError(Exception):
    pass

def loan_eligibility_checker():
    try:
        income_input = input("Enter your monthly income (₹): ")
        credit_score_input = input("Enter your credit score (300-850): ")

        income = float(income_input)
        assert income > 0, "Income must be a positive number."

        credit_score = int(credit_score_input)

        if credit_score < 600:
            raise LowCreditScoreError("Credit score too low for loan eligibility.")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
    except AssertionError as ae:
        print(f"❌ {ae}")
    except LowCreditScoreError as le:
        print(f"❌ {le}")
    else:
        print("✅ Congratulations! You are eligible for a loan.")
    finally:
        print("📝 Loan eligibility check complete.")

if __name__ == "__main__":
    loan_eligibility_checker()

