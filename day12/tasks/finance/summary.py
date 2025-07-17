from .tax import calc_tax
from .profit import profit

def report(revenue, cost, tax_rate):
    p = profit(revenue, cost)
    t = calc_tax(p, tax_rate)
    net = p - t
    print(f"Profit: {p}, Tax: {t}, Net: {net}")
    return {"profit": p, "tax": t, "net": net}
