def get_daterange_string(datetime, minutes=0, hours=0, days=0, weeks=0):
    date = datetime.datetime.now()
    past = str(date - datetime.timedelta(minutes=minutes, hours=hours, days=days, weeks=weeks))
    date = str(date)[0:-7]
    past = past[0:-7]
    dates = [past, date]
    return dates
