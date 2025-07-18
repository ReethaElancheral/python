from decimal import Decimal, ROUND_HALF_UP

def calculate_split(members):
    total = sum(member['paid'] for member in members)
    count = len(members)
    share = (total / count).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    for member in members:
        member['owed'] = (share - member['paid']).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    return members, total, share
