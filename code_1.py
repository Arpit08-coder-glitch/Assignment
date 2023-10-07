import re

# Function to read and parse the input file
def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data

# Function to find employees who worked for 7 consecutive days
def find_consecutive_days(data):
    employees = re.findall(r'Employee: (\w+)', data)
    shifts = re.findall(r'Shift: (\d+)', data)
    consecutive_days = {}
    current_employee = None
    consecutive_count = 0
    
    for employee, shift in zip(employees, shifts):
        if employee != current_employee:
            current_employee = employee
            consecutive_count = 1
        else:
            consecutive_count += 1
        
        if consecutive_count == 7:
            consecutive_days[employee] = int(shift) - 6  # Store the starting position
            
    return consecutive_days

# Function to find employees with less than 10 hours between shifts but greater than 1 hour
def find_short_breaks(data):
    employees = re.findall(r'Employee: (\w+)', data)
    shifts = re.findall(r'Shift: (\d+)', data)
    shift_times = {}
    short_breaks = {}
    
    for employee, shift in zip(employees, shifts):
        if employee not in shift_times:
            shift_times[employee] = [int(shift)]
        else:
            previous_shift = shift_times[employee][-1]
            if int(shift) - previous_shift < 10 and int(shift) - previous_shift > 1:
                short_breaks[employee] = int(shift)  # Store the shift position
            
            shift_times[employee].append(int(shift))
    
    return short_breaks

# Function to find employees who worked for more than 14 hours in a single shift
def find_long_shifts(data):
    employees = re.findall(r'Employee: (\w+)', data)
    shifts = re.findall(r'Shift: (\d+)', data)
    shift_times = {}
    long_shifts = {}
    
    for employee, shift in zip(employees, shifts):
        if employee not in shift_times:
            shift_times[employee] = [int(shift)]
        else:
            previous_shift = shift_times[employee][-1]
            if int(shift) - previous_shift > 14:
                long_shifts[employee] = int(shift)  # Store the shift position
            
            shift_times[employee].append(int(shift))
    
    return long_shifts

# Main function to analyze the file and print results
def main(input_file):
    data = read_file(input_file)
    
    consecutive_days = find_consecutive_days(data)
    short_breaks = find_short_breaks(data)
    long_shifts = find_long_shifts(data)
    
    # Print results
    print("Employees who worked for 7 consecutive days:")
    for employee, position in consecutive_days.items():
        print(f"Employee: {employee}, Position: {position}")
    
    print("\nEmployees with less than 10 hours between shifts but greater than 1 hour:")
    for employee, position in short_breaks.items():
        print(f"Employee: {employee}, Position: {position}")
    
    print("\nEmployees who worked for more than 14 hours in a single shift:")
    for employee, position in long_shifts.items():
        print(f"Employee: {employee}, Position: {position}")

if __name__ == "__main__":
    input_file = "input.txt"
    main(input_file)
