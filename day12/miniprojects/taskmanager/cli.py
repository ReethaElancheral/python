# taskmanager/cli.py

import argparse
import uuid
from datetime import datetime

from .tasks import add_task, update_task, delete_task, list_tasks
from .priority import validate
from .calendar_view import print_month

def main():
    p = argparse.ArgumentParser("Task Manager")
    sub = p.add_subparsers(dest="cmd")

    add = sub.add_parser("add")
    add.add_argument("title")
    add.add_argument("--due", required=True, help="YYYY-MM-DD")
    add.add_argument("--priority", default="medium")

    upd = sub.add_parser("update")
    upd.add_argument("id")
    upd.add_argument("--title")
    upd.add_argument("--due")
    upd.add_argument("--priority")

    d = sub.add_parser("delete")
    d.add_argument("id")

    lst = sub.add_parser("list")

    cal = sub.add_parser("calendar")
    cal.add_argument("--year", type=int, default=datetime.now().year)
    cal.add_argument("--month", type=int, default=datetime.now().month)

    args = p.parse_args()
    try:
        if args.cmd == "add":
            due = datetime.fromisoformat(args.due)
            pr = validate(args.priority)
            tid = uuid.uuid4().hex[:8]
            add_task(tid, args.title, due, pr)
            print(f"Added {tid}")
        elif args.cmd == "update":
            kwargs = {}
            if args.title:
                kwargs["title"] = args.title
            if args.due:
                kwargs["due"] = datetime.fromisoformat(args.due)
            if args.priority:
                kwargs["priority"] = validate(args.priority)
            update_task(args.id, **kwargs)
            print("Updated")
        elif args.cmd == "delete":
            delete_task(args.id)
            print("Deleted")
        elif args.cmd == "list":
            for tid, t in list_tasks().items():
                print(f"{tid}: {t['title']} – due {t['due'].date()} prio:{t['priority']}")
        elif args.cmd == "calendar":
            print_month(args.year, args.month)
        else:
            p.print_help()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
