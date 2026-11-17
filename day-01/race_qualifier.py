
names = []
times = []
minutes_list = []
seconds_list = []

# Input athlete information
name = input("Enter athlete's name (x to finish): ").strip()

while name.lower() != "x":

    minutes = input("Enter time in minutes: ").strip()
    seconds = input("Enter time in seconds: ").strip()

    if minutes.isdigit() and seconds.isdigit():

        minutes = int(minutes)
        seconds = int(seconds)

        if seconds >= 0 and seconds <= 59:

            total_seconds = minutes * 60 + seconds

            names.append(name)
            minutes_list.append(minutes)
            seconds_list.append(seconds)
            times.append(total_seconds)

            print("Athlete successfully added!")

        else:
            print("Invalid time. Seconds must be between 00 and 59.")

    else:
        print("Invalid input. Enter numbers only.")

    name = input("\nEnter athlete's name (x to finish): ").strip()


# Display all captured input data
print("\n========== ENTERED ATHLETE DATA ==========")

if len(names) == 0:

    print("No valid athletes were entered.")

else:

    print("Name\t\tMinutes\tSeconds\tTotal Seconds")

    for i in range(len(names)):
        print(names[i], "\t\t", minutes_list[i],
              "\t", seconds_list[i], "\t", times[i])


    # Find the winner
    lowest_time = times[0]

    for t in times:
        if t < lowest_time:
            lowest_time = t


    # Count qualifiers (25 minutes or less)
    qualified = 0

    for t in times:
        if t <= 25 * 60:
            qualified += 1


    # Find all winners in case of a tie
    winners = []

    for i in range(len(times)):
        if times[i] == lowest_time:
            winners.append(names[i])


    # Display race results
    print("\n========== RACE RESULTS ==========")

    if len(winners) == 1:
        print("Winner:", winners[0])
    else:
        print("Tie for first place:", ", ".join(winners))

    winner_minutes = lowest_time // 60
    winner_seconds = lowest_time % 60

    print("Winning time:", winner_minutes, "minutes and",
          winner_seconds, "seconds")

    print("Number of athletes:", len(names))
    print("Number of qualifiers:", qualified)
    print("Number not qualified:", len(names) - qualified)


    # Display individual athlete results
    print("\n========== INDIVIDUAL ATHLETE RESULTS ==========")

    for i in range(len(names)):

        print("\nAthlete:", names[i])
        print("Minutes:", minutes_list[i])
        print("Seconds:", seconds_list[i])
        print("Total time in seconds:", times[i])

        if times[i] <= 25 * 60:
            print("Status: QUALIFIED")
        else:
            print("Status: NOT QUALIFIED")


    print("\n========== END OF RACE REPORT ==========")
