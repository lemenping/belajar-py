# fungsi mengembalikan beberapa nilai seklaigus
def statistik(data):
    total = sum(data)
    rata = total / len(data)
    maksimum = max(data)
    minimum = min(data)
    return total, rata, maksimum, minimum

nilai = [75, 82, 90, 68, 95]
tot, avg, mn, mx = statistik(nilai)
print(f"Total: {tot} | rata: {avg} | min: {mn} | max: {mx}")
