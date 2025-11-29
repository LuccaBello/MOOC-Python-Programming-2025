from datetime import datetime, timedelta

filename = input("Filename: ")
start_date_str = input("Starting date: ")
days_count = int(input("How many days: "))

current_date = datetime.strptime(start_date_str, "%d.%m.%Y")

print("Please type in screen time in minutes on each day (TV computer mobile):")

daily_records = []
total_minutes = 0

for i in range(days_count):
    date_for_entry = current_date + timedelta(days=i)
    formatted_date = date_for_entry.strftime("%d.%m.%Y")

    entry_input = input(f"Screen time {formatted_date}: ")
    times = [int(x) for x in entry_input.split()]

    total_minutes += sum(times)
    formatted_times = "/".join(str(x) for x in times)

    daily_records.append((formatted_date, formatted_times))

end_date = current_date + timedelta(days=days_count - 1)
period_str = f"{current_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}"
average_minutes = total_minutes / days_count

with open(filename, "w") as file:
    file.write(f"Time period: {period_str}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {average_minutes:.1f}\n")
    for date_str, times_str in daily_records:
        file.write(f"{date_str}: {times_str}\n")

print(f"Data stored in file {filename}")