from .timeranges import timeranges
from .timerange_select_dialogue import timerange_select_dialogue
from ..helpers.clear_out import clear_out

def timerange_select(name, system, granularity):
    clear_out(name, system)
    match granularity:
        case "S5":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 1 Minute\n[2] 5 Minutes\n[3] 10 Minutes\n", timeranges[1], timeranges[2], timeranges[3], name, system)
            return timerange
        case "S30":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 5 Minutes\n[2] 15 Minutes\n[3] 30 Minutes\n", timeranges[2], timeranges[4], timeranges[5], name, system)
            return timerange
        case "M1":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 10 Minutes\n[2] 30 Minutes\n[3] 1 Hour\n", timeranges[3], timeranges[5], timeranges[6], name, system)
            return timerange
        case "M5":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 1 Hour\n[2] 2 Hours\n[3] 4 Hours\n", timeranges[6], timeranges[7], timeranges[8], name, system)
            return timerange
        case "M15":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 4 Hours\n[2] 8 Hours\n[3] 12 Hours\n", timeranges[8], timeranges[10], timeranges[11], name, system)
            return timerange
        case "M30":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 6 Hours\n[2] 12 Hours\n[3] 1 Day\n", timeranges[9], timeranges[11], timeranges[12], name, system)
            return timerange
        case "H1":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 12 Hours\n[2] 24 Hours\n[3] 48 Hours\n", timeranges[11], timeranges[12], timeranges[13], name, system)
            return timerange
        case "H4":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 3 days\n[2] 5 days\n[3] 1 week\n", timeranges[14], timeranges[15], timeranges[16], name, system)
            return timerange
        case "H6":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 5 Days\n[2] 1 Week\n[3] 2 Weeks\n", timeranges[15], timeranges[16], timeranges[17], name, system)
            return timerange
        case "H12":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 1 Week\n[2] 2 Weeks\n[3] 1 Month\n", timeranges[16], timeranges[17], timeranges[18], name, system)
            return timerange
        case "D":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 2 Weeks\n[2] 1 Month\n[3] 2 Months\n", timeranges[17], timeranges[18], timeranges[19], name, system)
            return timerange
        case "W":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 4 Months\n[2] 6 Months\n[3] 1 Year\n", timeranges[20], timeranges[21], timeranges[22], name, system)
            return timerange
        case "M":
            timerange = timerange_select_dialogue(timeranges, "--Amount of data--\n[1] 1 Year\n[2] 5 Years\n[3] 10 Years\n", timeranges[22], timeranges[23], timeranges[24], name, system)
            return timerange
