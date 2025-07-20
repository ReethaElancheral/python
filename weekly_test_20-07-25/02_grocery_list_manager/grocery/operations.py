

def add_item(item, category, data):
    item_tuple = (item, category)
    data.setdefault(category, []).append(item_tuple)

def remove_item(item, data):
    for cat in data:
        data[cat] = [i for i in data[cat] if i[0] != item]

def mark_bought(item, bought_set):
    bought_set.add(item)

def search_item(keyword, data):
    results = []
    for cat, items in data.items():
        for item in items:
            if keyword.lower() in item[0].lower():
                results.append(item)
    return results
