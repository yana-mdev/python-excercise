class Time:
    max_hours: int = 23
    max_minutes: int = 59
    max_seconds: int = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def set_time(self, new_hours, new_minutes, new_seconds):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        if self.seconds > Time.max_seconds:
            self.minutes += self.seconds // 60
            self.seconds %= 60
        if self.minutes > Time.max_minutes:
            self.hours += self.minutes // 60
            self.minutes %= 60
        if self.hours > Time.max_hours:
            self.hours %= 24
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        self.seconds += 1

        return self.get_time()



time = Time(9, 30, 59)

print(time.next_second())

