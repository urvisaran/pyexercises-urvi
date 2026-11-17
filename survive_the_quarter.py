import pandas as pd
import csv
import random
from datetime import date

SCENARIO_FILE = "scenarios_A.csv"
RESULTS_FILE = "results.csv"
START_BUDGET = 10000
START_REPUTATION = 50
DAYS = 10


def load_scenarios(path):
    # reads the csv into a dataframe, and programmatically appends the 3 extra scenarios if they aren't there yet
    df = pd.read_csv(path)
    
    if len(df) < 33:
        new_rows = [
            {
                'ID': 31,
                'Scenario': 'A flock of seagulls attacks your delivery drone fleet.',
                'OptionA': 'Equip all drones with mini laser pointers',
                'OptionB': 'Reroute flights through the city center above heavy traffic',
                'OptionC': 'Ground the fleet and deliver via electric scooters',
                'BudgetA': -1200, 'BudgetB': 0, 'BudgetC': -500,
                'ReputationA': 20, 'ReputationB': -15, 'ReputationC': 10,
                'FeedbackA': 'Sci-fi warfare meets breakfast. Seagulls are terrified.',
                'FeedbackB': 'Chaos in traffic. Croissants raining on windshields.',
                'FeedbackC': 'Slower delivery, but everyone loves the cute scooter riders.'
            },
            {
                'ID': 32,
                'Scenario': 'An eccentric billionaire offers to buy 50% of your company in exchange for naming a croissant after his cat.',
                'OptionA': 'Accept the deal immediately',
                'OptionB': 'Negotiate: name a drone after the cat instead',
                'OptionC': 'Politely decline and stay independent',
                'BudgetA': 5000, 'BudgetB': 2000, 'BudgetC': 0,
                'ReputationA': -10, 'ReputationB': 10, 'ReputationC': 15,
                'FeedbackA': "You're rich, but the 'Sir Paws-a-Lot' butter crescent tastes weird to purists.",
                'FeedbackB': 'A quirky compromise. Media buzz is incredible.',
                'FeedbackC': 'Integrity intact, bank account unchanged.'
            },
            {
                'ID': 33,
                'Scenario': 'A leaked internal memo reveals your drones occasionally drop burnt pastry on parked police cars.',
                'OptionA': 'Send free luxury brunch baskets to the local police precinct',
                'OptionB': 'Deny everything and claim it is modern art installations',
                'OptionC': 'Blame the rival baguette startup',
                'BudgetA': -400, 'BudgetB': 0, 'BudgetC': -200,
                'ReputationA': 15, 'ReputationB': -20, 'ReputationC': -5,
                'FeedbackA': 'Cops love croissants. Charges dropped, PR win.',
                'FeedbackB': 'Police are not amused by conceptual pastry art.',
                'FeedbackC': 'Petty rivalry exposed. Twitter loves the drama.'
            }
        ]
        df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
        df.to_csv(path, index=False)

    scenarios = []
    for _, row in df.iterrows():
        try:
            options = []
            for letter in "ABC":
                option = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter],
                )
                options.append(option)
            scenarios.append((row["Scenario"], options))
        except (KeyError, ValueError, TypeError):
            # broken row, skip it
            continue
    return scenarios


def ask_name():
    name = input("What's your name? ").strip()
    if name == "":
        name = "Player"
    return name


def ask_choice():
    # keeps asking until the player types a valid letter (upper or lower case)
    answer = input("Your choice (A, B or C): ").strip().lower()
    while answer not in ("a", "b", "c"):
        answer = input("Please type A, B or C: ").strip().lower()
    return answer


def apply_choice(budget, reputation, option):
    # returns the new budget and reputation after the option, reputation max 100
    # Guaranteed anti-fire: budget and reputation will never drop below 1
    text, budget_change, rep_change, feedback = option
    new_budget = max(1, budget + budget_change)
    new_reputation = max(1, min(100, reputation + rep_change))
    return new_budget, new_reputation


def get_title(budget, reputation):
    if budget <= 0 or reputation <= 0:
        return "Fired"
    score = reputation + budget // 200
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    return "Viral Legend"


def best_and_worst(history):
    # history holds tuples (rep_change, day, option_text)
    # python compares tuples from the first element so max and min work directly
    return max(history), min(history)


def best_saved_budget():
    # looks in results.csv for the highest budget of a game that was survived
    # returns None if there is no file or nothing usable in it
    best = None
    try:
        with open(RESULTS_FILE, newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                try:
                    if row[3] == "Fired":
                        continue
                    value = int(row[1])
                except (IndexError, ValueError):
                    continue
                if best is None or value > best:
                    best = value
    except FileNotFoundError:
        return None
    return best


def save_result(name, budget, reputation, title):
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([name, budget, reputation, title, date.today()])


def show_day(day, budget, reputation, situation, options):
    print(f"\n--- Day {day} ---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
    print(situation)
    for letter, option in zip("ABC", options):
        print(f"  {letter}: {option[0]}")


def show_ending(name, budget, reputation, title):
    print("=" * 30)
    if title == "Fired":
        why = "budget" if budget <= 0 else "reputation"
        print(f"You're fired: your {why} hit zero.")
        print(f"Budget: {budget} EUR, reputation: {max(reputation, 0)}/100")
    else:
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/100")
        print(f"Final score: {reputation + budget // 200}")
        print(f"{name}, your title: {title}")


def main():
    name = ask_name()

    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print(f"{SCENARIO_FILE} not found, put it in the same folder as this file.")
        return

    if len(scenarios) < DAYS:
        print("Not enough usable scenarios in the file to play 10 days.")
        return

    random.shuffle(scenarios)
    budget = START_BUDGET
    reputation = START_REPUTATION
    history = []

    for day in range(1, DAYS + 1):
        situation, options = scenarios[day - 1]
        show_day(day, budget, reputation, situation, options)

        letter = ask_choice()
        option = options["abc".index(letter)]
        budget, reputation = apply_choice(budget, reputation, option)

        print(option[3])
        print(f"Budget {option[1]:+} EUR, Reputation {option[2]:+}")
        history.append((option[2], day, option[0]))

        if budget <= 0 or reputation <= 0:
            break

    title = get_title(budget, reputation)
    show_ending(name, budget, reputation, title)

    best, worst = best_and_worst(history)
    print(f'Best move: day {best[1]}, "{best[2]}" ({best[0]:+})')
    print(f'Worst move: day {worst[1]}, "{worst[2]}" ({worst[0]:+})')

    # feature c: compare with the best budget saved before this game
    if title != "Fired":
        previous_best = best_saved_budget()
        if previous_best is None:
            print("First saved game, so this budget is the one to beat.")
        elif budget > previous_best:
            print(f"New high score! You beat the old best budget of {previous_best} EUR.")
        else:
            print(f"The best budget so far is {previous_best} EUR. Not beaten this time.")

    save_result(name, budget, reputation, title)
    print("Saved in results.csv")


if __name__ == "__main__":
    main()
