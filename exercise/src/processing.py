from typing import List, Dict

def stats(rows: List[Dict]) -> Dict:
    if not rows:
        return {"count": 0, "avg_age": 0, "by_city": {}}

    ages = [int(r["age"]) for r in rows if r["age"]]
    by_city = {}

    for r in rows:
        city = r["city"]
        by_city[city] = by_city.get(city, 0) + 1

    return {
        "count": len(rows),
        "avg_age": sum(ages) / len(ages),
        "by_city": by_city
    }

def build_report(st: Dict) -> str:
    lines = []
    lines.append("Rapor\n")
    lines.append(f"Geçerli kayıt sayısı: {st['count']}")
    lines.append(f"Ortalama yaş: {st['avg_age']:.2f}")
    lines.append("Şehir dağılımı:")

    for c, n in st["by_city"].items():
        lines.append(f"{c}: {n}")

    return "\n".join(lines) + "\n"
