import db

def get_input(week):
    hrs_sleep = input("How many hours of sleep did you get last night? ")
    hrs_exercise = input("How many hours did you exercise today? ")
    hrs_study = input("How many hours did you study today? ")
    #should only get this question if 
    progress = input("How much progress did you make in your project today, as a percent ")
    #need better system for mood - probably define categories
    mood = input("On a scale of 1-10, 10 being the best, what was your average mood today? ")
    stress = input("What, if anything, stressed you out today ")
    input_list = [hrs_sleep, hrs_study, progress, hrs_exercise, mood, stress,]
    db.insert_to_table(input_list, week)

def main():
    week = 1
    choice = input("Would you like to add new data or view your data? Choose ADD or VIEW: ")
    if choice == "ADD":
        get_input(week)
    #if choice == "VIEW":
        #do something else

if __name__ == "__main__":
    main()