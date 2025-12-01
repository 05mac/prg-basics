def time_string(hours, minutes,time_format):
    cala_godzina = ""
    if 0 <= hours <= 23 and time_format == '24' and 1 <= minutes <= 59:

        return str(hours) + ":" + str(minutes)

    elif 0 <= hours <= 23 and time_format == '12' and 1<= minutes <= 59:
        
        if hours == 0:
            hours += 12

            return str(hours) + ":" + str(minutes) + "am"

        elif hours < 12:
            return str(hours) + ":" + str(minutes) + "am"
        elif hours >= 12:
            hours -= 12
            return str(hours) + ":" + str(minutes) + "pm"
print(time_string(15,38,'24'))

print(time_string(0,7,'12'))
print(time_string(7,30,'12'))
print(time_string(13,30,'12'))
print(time_string(19,30,'12'))


