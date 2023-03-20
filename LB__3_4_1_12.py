class Timer:
    def __init__(self, hours, minutes, seconds):
        # Write code here
        self.hour = str(hours)
        self.minut = str(minutes)
        self.sec = str(seconds)

    def __str__(self):
        # Write code here
        return self.hour + ":" + self.minut + ":" + self.sec

    def next_second(self):
        # Write code here
        self.hour = '00'
        self.minut = '00'
        self.sec = '00'
        Timer.__str__(self)

    def prev_second(self):
        # Write code here
        self.hour = '23'
        self.minut = '59'
        self.sec = '59'
        Timer.__str__(self)


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
