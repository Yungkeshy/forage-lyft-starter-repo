def battery_duration(current_date, add_period):
    duration = current_date.replace(year=current_date.year + add_period)
    return duration
