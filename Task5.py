def read_log_and_print_errors(log_file_path):
    try:
        with open(log_file_path, 'r') as log_file:
            # Read each line from the log file
            for line in log_file:
                # Check if the line contains an error message
                if 'ERROR' in line:
                    print(line.strip())  # Print the error message
    except FileNotFoundError:
        print(f"❌ The log file at {log_file_path} was not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Example usage
log_file_path = "resources/appium_logfile.log"  # Replace with the path to your log file
read_log_and_print_errors(log_file_path)
