def search_by_tag(entries, tag):
    return [e for e in entries if tag in e["tags"]]

def search_by_date(entries, date):
    return [e for e in entries if e["date"] == date]
