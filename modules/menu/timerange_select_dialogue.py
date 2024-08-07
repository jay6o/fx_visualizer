from ..helpers.clear_out import clear_out

def timerange_select_dialogue(timeranges, dialogue, option1, option2, option3, name, system):
    clear_out(name, system)
    try:
        timerange = int(input(dialogue))
        options = {1: option1,
                2: option2,
                3: option3}
        try:
            timerange = options[timerange]
            return timerange
        except KeyError:
            return(timerange_select_dialogue(timeranges, dialogue, option1, option2, option3, name, system))
        except Exception as e:
            return(timerange_select_dialogue(timeranges, dialogue, option1, option2, option3, name, system))
    except ValueError:
            return(timerange_select_dialogue(timeranges, dialogue, option1, option2, option3, name, system))
    except Exception as e:
            return(timerange_select_dialogue(timeranges, dialogue, option1, option2, option3, name, system))
