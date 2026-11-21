import csv, random
random.seed(7)
# True model: minutes = 8 + 2.5*dist + 1.2*items + 1.8*traffic + 5*rain - 0.15*experience + N(0, 4^2)
W = {"bias": 8, "dist": 2.5, "items": 1.2, "traffic": 1.8, "rain": 5, "exp": -0.15}
rows = []
for _ in range(600):
    dist = random.uniform(0.5, 12)          # km
    items = random.randint(1, 15)
    traffic = random.randint(1, 10)         # congestion index
    rain = 1 if random.random() < 0.25 else 0
    exp = random.uniform(1, 60)             # courier experience, months
    t = (W["bias"] + W["dist"]*dist + W["items"]*items + W["traffic"]*traffic
         + W["rain"]*rain + W["exp"]*exp + random.gauss(0, 4))
    rows.append([round(dist,2), items, traffic, rain, round(exp,1), round(t,1)])
with open("delivery_times.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["distance_km", "n_items", "traffic_index", "is_raining", "courier_exp_months", "delivery_min"])
    w.writerows(rows)
