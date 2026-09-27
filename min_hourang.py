'''Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
Answers within 10-5 of the actual value will be accepted as correct.

 
#sol

class Solution(object):
    def angleClock(self, hour, minutes):
        # Calculate the angles of hour and minute hands
        hour_angle = 30 * hour + 0.5 * minutes
        minute_angle = 6 * minutes

        # Find the difference between them
        angle = abs(hour_angle - minute_angle)

        # Return the smaller angle
        return min(angle, 360 - angle)'''