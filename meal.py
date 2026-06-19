def main() :

    time = input("what time is it? ")
    convert(time)

def convert(time) :

    t = time
    hours, minutes = t.split(":")
    new_minutes = float(minutes) / 60

    if 7 <= float(new_minutes) + float(hours) <= 8 :
        print("breakfast time")
    
    elif 12 <= float(new_minutes) + float(hours) <= 13 :
        print("lunch time")

    elif 18 <= float(new_minutes) + float(hours) <= 19 :
        print("dinner time")


main()