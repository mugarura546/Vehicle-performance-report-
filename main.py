def highest_efficiency(vehicles):
    return max(vehicles, key=lambda v: v["efficiency"]) if vehicles else None

def average_efficiency(vehicles):
    if not vehicles:
        return None
    return sum(v["efficiency"] for v in vehicles) / len(vehicles)

def print_report(vehicles):
    print("VEHICLE PERFORMANCE REPORT")
    print(f"{'Registration':<14}{'Distance(km)':>13}{'Fuel(L)':>9}"
          f"{'km/L':>8}  Classification")
    for v in vehicles:
        print(f"{v['registration']:<14}{v['distance']:>13.1f}{v['fuel']:>9.1f}"
              f"{v['efficiency']:>8.2f}  {v['classification']}")
    best = highest_efficiency(vehicles)
    if best is None:
        print("No valid records.")
        return
    print(f"Valid records      : {len(vehicles)}")
    print(f"Highest efficiency : {best['efficiency']:.2f} km/L ({best['registration']})")
    print(f"Average efficiency : {average_efficiency(vehicles):.2f} km/L")
