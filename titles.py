# titles.py
# A simple script that turns a video topic into 10 title ideas
# and saves them to a CSV file you can open in Excel or Google Sheets.

# "csv" is a built-in Python tool for reading and writing CSV files.
# Nothing to install!
import csv


# --- STEP 1: Ask for the topic -------------------------------------------
# input() shows a message and waits for you to type something and press Enter.
# .strip() removes accidental spaces at the start or end.
topic = input("What is your video topic? ").strip()

# If you pressed Enter without typing anything, stop and explain why.
if topic == "":
    print("You didn't type a topic. Please run the script again.")
    raise SystemExit  # This ends the program.


# --- STEP 2: Build the title ideas ---------------------------------------
# These are "templates". The {topic} part gets swapped for your topic.
# A list in Python is written with square brackets [ ], items separated by commas.
templates = [
    "{topic}: A Complete Beginner's Guide",
    "10 Mistakes Everyone Makes With {topic}",
    "I Tried {topic} for 30 Days - Here's What Happened",
    "The Truth About {topic} Nobody Tells You",
    "How to Get Started With {topic} (Step by Step)",
    "{topic} Explained in 5 Minutes",
    "Stop Doing {topic} Wrong! Do This Instead",
    "5 Simple Tips to Master {topic}",
    "Is {topic} Worth It? My Honest Review",
    "{topic}: What I Wish I Knew Sooner",
]

# We'll collect the finished titles in this empty list.
titles = []

# A "for loop" repeats the same action for every item in a list.
# Here, it takes each template and fills in your topic.
for template in templates:
    title = template.format(topic=topic)  # Swap {topic} for your real topic.
    titles.append(title)                  # Add the finished title to our list.


# --- STEP 3: Print the titles on screen ----------------------------------
print()  # Prints an empty line to keep things tidy.
print("Here are 10 title ideas for:", topic)
print("-" * 40)  # Prints a line of 40 dashes.

# enumerate(..., start=1) gives us a counter (1, 2, 3...) along with each title.
for number, title in enumerate(titles, start=1):
    print(f"{number}. {title}")


# --- STEP 4: Save the titles to titles.csv -------------------------------
# open(..., "w") creates the file (or replaces it if it already exists).
# newline="" and encoding="utf-8" prevent odd spacing and character problems.
# The "with" block closes the file automatically when we're done.
with open("titles.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)           # A helper that writes rows into the file.
    writer.writerow(["Number", "Title"])  # The first row: column headings.

    for number, title in enumerate(titles, start=1):
        writer.writerow([number, title])  # One row per title.

print()
print("Saved to titles.csv - look for it in the same folder as this script.")