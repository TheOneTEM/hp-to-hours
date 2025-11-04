import math


language = input("Select a language / Välj ett språk: [e]nglish / [s]venska: ")

one_HP_in_hours = 40/1.5

if language[0].lower() == 'e':
    hp_input_message = "Enter the amount of Högskolepoäng / ECTS points for your course: "
    study_speed_input_message = "Enter the study speed of your course: "
    input_failure_message = "Invalid input. Please try again."
    study_recommendation = "You should study "
    per_week = " each week."
    hours_text = " hours"
    minutes_text = " minutes"
    and_text = " and "
    
elif language[0].lower() == 's':
    hp_input_message = "Skriv antalet högskolepoäng för din kurs: "
    study_speed_input_message = "Skriv studiehastigheten för din kurs: "
    input_failure_message = "Ogiltig inmatning. Försök igen."
    study_recommendation = "Du ska plugga "
    per_week = " varje vecka."
    hours_text = " timmar"
    minutes_text = " minuter"
    and_text = " och "

while True:
    try:
        hp = float(input(hp_input_message))
        break
    except ValueError:
        print(input_failure_message)


while True:
    try:
        study_speed = input(study_speed_input_message)
        if '%' in study_speed:
            study_speed = study_speed[:-1]
        study_speed = int(study_speed)
        break
    except ValueError:
        print(input_failure_message)

hours = (one_HP_in_hours * hp) * (study_speed/100)

hours_int = int(math.floor(hours))
minutes = int((hours_int - hours) * 60)

time_text = str(hours_int) + hours_text

if minutes > 0:
    time_text += and_text + str(minutes) + minutes_text

print(study_recommendation + time_text + per_week)

