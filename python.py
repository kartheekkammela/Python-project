def Angle(h,m):
        if (h < 0 or m < 0 or h > 24 or m > 60):
            print('No Such Data Available')
         
        if (h == 12):
            h = 0
        if (m == 60):
            m = 0
            h += 1;
            if(h>12):
                   h = h-12;
                   
        hour_angle = 0.5 * (h * 60 + m)
        minute_angle = 6 * m
        angle = abs(minute_angle - hour_angle)
        angle = min(720-angle, angle)
         
        return angle 
h,m =input().split(':')
h =int(h)
m =int(m)
degree =Angle(h,m)
print(int(degree),chr(176),sep='')
