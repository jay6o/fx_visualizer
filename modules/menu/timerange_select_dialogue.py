def timerange_select_dialogue(timeranges, dialogue, option1, option2, option3):
    try:
        timerange = int(input(dialogue))
        options = {1: option1,
                2: option2,
                3: option3}
        try:
            timerange = options[timerange]
            return timerange
        except KeyError:
            return(timerange_select_dialogue(timeranges, dialogue, option1, option2, option3))
        except Exception as e:
            return(timerange_select_dialogue(timeranges, dialogue, option1, option2, option3))
    except ValueError:
            return(timerange_select_dialogue(timeranges, dialogue, option1, option2, option3))
    except Exception as e:
            return(timerange_select_dialogue(timeranges, dialogue, option1, option2, option3))
