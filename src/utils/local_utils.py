def adjust_epi_week(week):
    if int(week) <= 52:
        return week
    elif 100 < int(week) < 200:
        return int(week) - 48
    elif 200 < int(week) < 300:
        return int(week) - 48*2
    elif 300 < int(week) < 400:
        return int(week) - 48 *3