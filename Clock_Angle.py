#!/usr/bin/env python

import math

def angles_diff(hour, minute):
        
    hour = hour if (hour < 12) else (hour - 12)
    hour_finger = hour * (360.0 /12) + minute * (30.0 / 60)
    
    minutes_finger = minute * (360.0 /60)
    #print hour_finger, minutes_finger
    return (hour_finger - minutes_finger) if (hour_finger - minutes_finger) < 180 else (360 - (hour_finger - minutes_finger))


#print hour_finger, minutes_finger, abs(angle_diff)

def main():
    time = raw_input().split(" ")
    i, j = int(time[0]), int(time[1])
    a = abs(angles_diff(i, j))
    print a
    
    
    return

if __name__ == "__main__":
    main()
    


