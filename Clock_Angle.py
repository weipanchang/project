#!/usr/bin/env python

hour = 13
minute = 30
hour = hour if (hour < 12) else (hour -12)
print hour
hour_finger = float(hour) * (360.0 /12) + (minute) * (30.0 / 60)

minutes_finger = float(minute) * (360.0 /60)
angle_diff = hour_finger - minutes_finger


print hour_finger, minutes_finger, abs(angle_diff)


