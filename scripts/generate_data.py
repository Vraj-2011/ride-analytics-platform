from faker import Faker
import pandas as pd
import random

fake = Faker()

data = []

for _ in range(5000):
    data.append({
        "ride_id": fake.uuid4(),
        "city": random.choice(["Toronto", "Montreal", "Vancouver"]),
        "fare": round(random.uniform(5, 60), 2),
        "distance_km": round(random.uniform(1, 25), 2),
        "timestamp": fake.date_time_this_month()
    })

df = pd.DataFrame(data)
df.to_csv("data/rides.csv", index=False)

print("✅ Data generated")