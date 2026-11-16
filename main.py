import pandas as pd

# Load railway booking data from the CSV file
df = pd.read_csv("bookings.csv")

print("RAILWAY RESERVATION ANALYZER")
print("----------------------------")

# Display all booking records
print("\nAll Bookings:")
print(df.to_string(index=False))

# Count total bookings
print("\nTotal Bookings:", len(df))

# Count confirmed bookings
confirmed = df[df["Status"] == "Confirmed"]
print("Confirmed Bookings:", len(confirmed))

# Count waiting bookings
waiting = df[df["Status"] == "Waiting"]
print("Waiting Bookings:", len(waiting))

# Count cancelled bookings
cancelled = df[df["Status"] == "Cancelled"]
print("Cancelled Bookings:", len(cancelled))
