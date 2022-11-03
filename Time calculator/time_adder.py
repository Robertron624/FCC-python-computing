

def add_time(start, duration, starting_day=None):

    def getDaysLater(days):
        if days == 1:
            return " (next day)"
        elif days > 1:
            return f" ({days} days later)"
        else:
            return ""


    # Constants

    HOURS_IN_ONE_DAY = 24
    HOURS_IN_HALF_DAY = HOURS_IN_ONE_DAY / 2
    MINUTES_IN_AN_HOUR = 60

    WEEK_DAYS = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ]


    days_later = 0

    # Split data from inputs
    hours, minutes = start.split(":")

    minutes, period = minutes.split(" ")

    duration_hours, duration_minutes = duration.split(":")

    # Transform data to numbers

    hours = int(hours)
    minutes = int(minutes)
    duration_hours = int(duration_hours)
    duration_minutes = int(duration_minutes)
    period = period.strip().lower()

    ## Add hours and minutes
    total_hours = hours + duration_hours
    total_minutes = minutes + duration_minutes

    # Shift minutes in case it passes an hour
    if total_minutes > MINUTES_IN_AN_HOUR:
        total_hours += int(total_minutes / 60)
        total_minutes = int(total_minutes % 60)

    if duration_hours or duration_minutes:
        if period == "pm" and total_hours > HOURS_IN_HALF_DAY:
            if total_hours % HOURS_IN_ONE_DAY >= 1.0:
                days_later += 1

        if total_hours >= HOURS_IN_HALF_DAY:
            hours_left = total_hours / HOURS_IN_ONE_DAY
            days_later += int(hours_left)


        temp_hours =total_hours

        while True:
            # Reverse periods until total_hours are less than half a day
            if(temp_hours < HOURS_IN_HALF_DAY):
                break
            if period == "am":
                period = "pm"
            else:
                period = "am"
            temp_hours -= HOURS_IN_HALF_DAY


    remaining_hours = int(total_hours % HOURS_IN_HALF_DAY) or hours + 1
    remaining_minutes = int(total_minutes % MINUTES_IN_AN_HOUR)

    # Formatting final result

    result = f"{remaining_hours}:{remaining_minutes:02} {period.upper()}"

    if starting_day:
        starting_day = starting_day.strip().lower()
        selected_day = int((WEEK_DAYS.index(starting_day) + days_later) % 7)
        current_day =  WEEK_DAYS[selected_day]
        result += f", {current_day.title()}{getDaysLater(days_later)}"
    else:
        result = "".join((result, getDaysLater(days_later)))
    

    return result   


print(add_time("3:30 PM", "2:12", "Monday"))




# print(add_time("3:00 PM", "3:10"))  # -> 6:10 PM

# print(add_time("11:30 AM", "2:32", "Monday")) # ->  2:02 PM, Monday

# print(add_time("11:43 AM", "00:20"))  # -> 12:03 PM

# print(add_time("10:10 PM", "3:30"))  # -> 1:40 AM (next day)

# print(add_time("11:43 PM", "24:20", "tueSday")) # -> 12:03 AM, Thursday (2 days later)

# print(add_time("6:30 PM", "205:12")) #-> 7:42 AM (9 days later)





