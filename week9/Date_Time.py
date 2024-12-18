import datetime

class Time:
    def __init__(self):
        time_entry = input('Enter a time in hh:mm:ss format: ')
        self.__hours, self.__minutes, self.__seconds = map(int, time_entry.split(':'))
        
    def __add__(self, other):
        # Convert both times to seconds
        total_seconds_self = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        total_seconds_other = other.__hours * 3600 + other.__minutes * 60 + other.__seconds
        
        # Sum the seconds
        total_seconds = total_seconds_self + total_seconds_other
        
        # Return the converted time as a string
        return Time.convert(total_seconds)
    
    @staticmethod
    def convert(seconds):
        # Convert the seconds into hours, minutes, and seconds
        seconds = seconds % (24 * 3600)  # Normalize to the range of 24 hours
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Create two Time objects
t1 = Time()
t2 = Time()

# Add the two Time objects and print the result
print(t1 + t2)

