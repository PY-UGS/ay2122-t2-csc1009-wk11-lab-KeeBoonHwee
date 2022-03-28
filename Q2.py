
#-----------------------------------------------------------------------------------------------------------------------------------------------
class clockTime:
    # Define a clockTime class, with attributes hours, minutes, seconds, and methods
    # setHours(), setMinutes(), setSeconds(), setTime(), and showTime().
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def setHours(self, hours : int):       # (a) setHours(): only set hours’ value.
        self.hours = hours % 24

    def setMinutes(self, minutes : int):   # (b) setMinutes(): only set minutes’ value.
        self.minutes = minutes % 60
 
    def setSeconds(self, seconds : int):   # (c)  setSeconds(): only set seconds’ value
        self.seconds = seconds % 60

    def setTime(self, hours : int, minutes : int , seconds : int):  # (d) setTime(): set hours’, minutes’, seconds’ values.
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)

    def showTime(self):                     # (e) showTime(): display the time in the format of hours:minutes:seconds.
        result = str(self.hours).zfill(2) + ":" +  str(self.minutes).zfill(2) + ":" + str(self.seconds).zfill(2) 
        print( result )
#-----------------------------------------------------------------------------------------------------------------------------------------------

hours   = int(input("Please enter hours : "))
minutes = int(input("Please enter minutes : "))
seconds = int(input("Please enter seconds : "))

timeclock = clockTime()                   # Create an object for clockTime class.
timeclock.setTime(hours,minutes,seconds)  # Set the time by keyboard inputs for hours’ value, 
                                          # minutes’ value, and seconds’ value.
timeclock.showTime()                      # Then display the time after setting of the new time.
#-----------------------------------------------------------------------------------------------------------------------------------------------