import matplotlib.pyplot as plt

def plot_monthly_spending(monthly_report):
    months = sorted(monthly_report.keys())
    amounts = [monthly_report[m] for m in months]

    plt.bar(months, amounts)
    plt.title("Monthly Spending")
    plt.xlabel("Month")
    plt.ylabel("Amount Spent")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_category_spending(category_report):
    categories = list(category_report.keys())
    amounts = list(category_report.values())

    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Spending by Category")
    plt.show()
