# budget/cli.py

import argparse
from .planner import set_budget
from .tracker import add_expense
from .report import monthly_report

def main():
    parser = argparse.ArgumentParser("Budget Planner")
    sub = parser.add_subparsers(dest="cmd")

    b = sub.add_parser("budget", help="Set budget")
    b.add_argument("category")
    b.add_argument("amount", type=float)
    b.add_argument("--month")

    ex = sub.add_parser("expense", help="Add expense")
    ex.add_argument("category")
    ex.add_argument("amount", type=float)
    ex.add_argument("--date")

    r = sub.add_parser("report", help="Show monthly report")
    r.add_argument("--month")

    args = parser.parse_args()

    if args.cmd == "budget":
        m, c, amt = set_budget(args.category, args.amount, args.month)
        print(f"Budget set for {c} in {m}: ${amt:.2f}")
    elif args.cmd == "expense":
        d, c, amt = add_expense(args.category, args.amount, args.date)
        print(f"Expense added on {d}: {c} – ${amt:.2f}")
    elif args.cmd == "report":
        print(monthly_report(args.month))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
