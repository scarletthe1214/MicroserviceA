Microservice Communication Contract
Introduction
This microservice provides various functions to convert time zones, durations, and calculate due dates. It is designed to process requests from a client and send responses back. The goal is to offer clear and reliable communication between the microservice and any client interacting with it.

Communication Contract
The microservice handles requests for time zone conversion, duration conversion, days calculation, and due date calculation. The client can programmatically request data, and the microservice will respond with the requested results.

1. Requesting Data from the Microservice
To request data from the microservice, you will need to send a request in the correct format to the service endpoint. The microservice listens for requests from an input.txt file, which contains the specific actions to be performed.
Example Request:
convert_time_zones 2025-02-21-12:40:00 PST America/New_York
convert_duration 2 hours minutes
calculate_days 2025-02-24
calculate_due_date 5 days

Each line of the input.txt corresponds to a different action and will be processed accordingly. Here’s what each request means:
convert_time_zones: Converts the provided time from one time zone to another.
convert_duration: Converts a duration from one unit to another (e.g., from hours to minutes).
calculate_days: Calculates how many days are left from today to the given date.
calculate_due_date: Adds the given duration (e.g., 5 days, 10 hours) to today’s date and returns the resulting date.

You can write your own code to send these requests to input.txt.
Example Request (Programmatically)
If you're writing a Python script to request data from the microservice, you would simply write the actions into input.txt, like so:
# Example Python script to request data from the microservice
# Write the request data to input.txt
with open('input.txt', 'w') as f:
    f.write("convert_time_zones 2025-02-21-12:40:00 PST America/New_York\n")
    f.write("convert_duration 2 hours minutes\n")
    f.write("calculate_days 2025-02-24\n")
    f.write("calculate_due_date 5 days\n")

2. Receiving Data from the Microservice
After the microservice processes the data, it writes the results to output.txt. The results will be written one per line in the same order as the requests.
Example Response (in output.txt):
2025-02-21-15:40:00-EST
120
3
2025-02-26 00:00:00
2025-02-21 22:40:00
2025-02-21 14:40:00

The response corresponds to the results of the following actions:
Time Zone Conversion: 2025-02-21 15:40:00 EST (converted from 2025-02-21 12:40:00 PST).
Duration Conversion: 120 (2 hours converted to minutes).
Days Calculation: 3 (from 2025-02-21 to 2025-02-24).
Due Date Calculation: The due date after adding 5 days, 10 hours, and 120 minutes to today.
You can use a Python script to read output.txt like this:
# Example Python script to read the output from the microservice

with open('output.txt', 'r') as f:
    response = f.readlines()

for line in response:
    print(line.strip())  # Print each line of the response
