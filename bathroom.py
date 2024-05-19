import csv
from faker import Faker
import random
from datetime import datetime, timedelta

def generate_random_time(start_time, end_time):
    """Generate a random time between two given times."""
    delta = end_time - start_time
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start_time + timedelta(seconds=random_seconds)

def main():
    fake = Faker()
    num_lines = int(input("Enter the number of lines: "))

    with open('fake_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['First Name', 'Last Name', 'Date', 'Time Out', 'Time In'])

        start_time = datetime.strptime('07:40', '%H:%M')
        end_time = datetime.strptime('14:10', '%H:%M')
        max_time_difference = timedelta(minutes=10)

        start_date = datetime.strptime('2024-05-01', '%Y-%m-%d')
        end_date = datetime.strptime('2024-05-16', '%Y-%m-%d')

        for _ in range(num_lines):
            first_name = fake.first_name()
            last_name = fake.last_name()
            date = generate_random_date(start_date, end_date)
            time_out = generate_random_time(start_time, end_time)
            latest_time_in = time_out + max_time_difference
            time_in = generate_random_time(time_out, min(latest_time_in, end_time))
            writer.writerow([first_name, last_name, date, time_out.strftime('%H:%M'), time_in.strftime('%H:%M')])

def generate_random_date(start_date, end_date):
    """Generate a random date between two given dates, excluding weekends."""
    delta = end_date - start_date
    while True:
        random_days = random.randint(0, delta.days)
        random_date = start_date + timedelta(days=random_days)
        if random_date.weekday() < 5:  # 0 is Monday, 6 is Sunday
            return random_date.strftime('%Y-%m-%d')

if __name__ == "__main__":
    main()
