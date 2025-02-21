import argparse
from datetime import datetime, timedelta
import pytz
import time

def convert_time_zones(event_time_str, from_tz, to_tz):
    # Convert event time from one time zone to another
    from_time = datetime.strptime(event_time_str, '%Y-%m-%d-%H:%M:%S')
    
    # Using pytz to handle time zone conversion
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    
    # Localize the datetime to the 'from' timezone
    from_time = from_zone.localize(from_time)
    to_time = from_time.astimezone(to_zone)

    return to_time.strftime('%Y-%m-%d-%H:%M:%S-%Z')

def convert_duration(duration, from_unit, to_unit):
    # Convert duration from one unit to another
    if from_unit == 'hours' and to_unit == 'minutes':
        return duration * 60
    elif from_unit == 'days' and to_unit == 'hours':
        return duration * 24
    elif from_unit == 'days' and to_unit == 'minutes':
        return duration * 24 * 60
    return duration

def calculate_days_to_due_date(due_date_str):
    # Calculate days from today to due date, excluding today
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()  # Convert to date object
    today = datetime.now().date()  # Only date part, ignoring time part for accurate comparison

    # Subtract the current day from the due date
    days_difference = (due_date - today).days
    return days_difference

def calculate_due_date_from_duration(duration, unit):
    # Calculate due date from today's date by adding the duration
    today = datetime.now()

    if unit == 'days':
        due_date = today + timedelta(days=duration)
    elif unit == 'hours':
        due_date = today + timedelta(hours=duration)
    elif unit == 'minutes':
        due_date = today + timedelta(minutes=duration)
    else:
        return "Invalid unit. Please specify days, hours, or minutes."

    return due_date.strftime('%Y-%m-%d %H:%M:%S')

def process_input_line(line):
    parts = line.strip().split()
    
    # Extract action from the line
    action = parts[0]
    
    if action == 'convert_time_zones':
        event_time = parts[1]
        from_timezone = parts[2]
        to_timezone = parts[3]
        result = convert_time_zones(event_time, from_timezone, to_timezone)
    
    elif action == 'convert_duration':
        duration = float(parts[1])
        from_unit = parts[2]
        to_unit = parts[3]
        result = convert_duration(duration, from_unit, to_unit)
    
    elif action == 'calculate_days':
        due_date = parts[1]
        result = calculate_days_to_due_date(due_date)
    
    elif action == 'calculate_due_date':
        duration = float(parts[1])
        unit = parts[2]  # 'days', 'hours', or 'minutes'
        result = calculate_due_date_from_duration(duration, unit)
    
    return result

def main():
    while True:
        # Open input.txt to read conversion requests
        with open('input.txt', 'r') as input_file, open('output.txt', 'a') as output_file:
            lines = input_file.readlines()
            
            if lines:  # If there are lines in the input file
                for line in lines:
                    if line.strip():  # Ignore empty lines
                        result = process_input_line(line)
                        output_file.write(f'{result}\n')

        # Sleep for a few seconds before checking for new requests in input.txt
        print("Waiting for new requests...")
        time.sleep(5)  # Delay for 5 seconds before checking for new input

if __name__ == '__main__':
    main()
