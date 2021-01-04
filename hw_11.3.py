# Print out only the top 3 results

# Now that we removed the score_list.sort() line (because it doesn't work with dictionaries in the list), we have to find another way to sort the scores.
# There are many ways how to do it. Use your imagination (and Google) and try to figure out at least one of them. :)

import random
import json
import datetime

current_time = datetime.datetime.now()

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

for score_dict in new_score_list:
    print(str(score_dict["attempts"]) + " attempts, player: ", str(score_dict["name"]) + ", secret number: " + str(score_dict["secret"]) + ", date: " + score_dict.get("date") + ", unsuccesful attempts: " + str(score_dict["wrong_guesses"]))

wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        name = input("Please state your name for the score list: ")



        score_list.append({"attempts": attempts, "name": name, "secret": secret, "date": str(datetime.datetime.now()), "wrong_guesses": wrong_guesses})

        with open ("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)