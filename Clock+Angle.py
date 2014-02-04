#!/usr/bin/env python

hour = 3
minute = 20
print float(float(minute) * (30.0/60))
hour_finger = float(hour) * (360 /12) + (float(minute) * float(30 / 60))
minutes_finger = float(minute) * float(360 /60)
angle_diff = hour_finger - minutes_finger


print hour_finger, minutes_finger, abs(angle_diff)


