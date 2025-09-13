import os
import re

# Define positive and negative word lists
positive_words = ["good", "excellent", "amazing", "happy", "love", "satisfied", "great", "fantastic"]
negative_words = ["bad", "poor", "terrible", "sad", "angry", "disappointed", "horrible", "worst"]

# Directory for storing reviews
REVIEW_DIR = "userreviews"

# Ensure the directory exists
if not os.path.exists(REVIEW_DIR):
    os.makedirs(REVIEW_DIR)

def analyze_review(content):
    """Check if a review is positive, negative, or neutral."""
    positive_count = len(re.findall(r"\b(" + "|".join(positive_words) + r")\b", content.lower()))
    negative_count = len(re.findall(r"\b(" + "|".join(negative_words) + r")\b", content.lower()))

    if positive_count > negative_count:
        return "Positive Review 😀"
    elif negative_count > positive_count:
        return "Negative Review 😞"
    else:
        return "Neutral Review 😐"

def read_reviews():
    """List all reviews and allow user to analyze them."""
    files = os.listdir(REVIEW_DIR)
    if not files:
        print("No reviews found.")
        return
    
    print("\nAvailable Reviews:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")

    choice = input("Enter the number of the review to analyze (or 'all' to analyze all): ")
    if choice.lower() == "all":
        for file in files:
            with open(os.path.join(REVIEW_DIR, file), "r") as f:
                content = f.read()
                print(f"\nFile: {file}\nSentiment: {analyze_review(content)}\n")
    else:
        try:
            index = int(choice) - 1
            file = files[index]
            with open(os.path.join(REVIEW_DIR, file), "r") as f:
                content = f.read()
                print(f"\nFile: {file}\nSentiment: {analyze_review(content)}\n")
        except (ValueError, IndexError):
            print("Invalid selection!")

def create_review():
    """Create a new review file."""
    filename = input("Enter review filename: ") + ".txt"
    content = input("Write your product review:\n")
    with open(os.path.join(REVIEW_DIR, filename), "w") as f:
        f.write(content)
    print(f"Review '{filename}' created successfully.")

def modify_review():
    """Edit an existing review."""
    files = os.listdir(REVIEW_DIR)
    if not files:
        print("No reviews to modify.")
        return

    print("\nAvailable Reviews:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")

    try:
        index = int(input("Enter the number of the review to modify: ")) - 1
        file = files[index]
        filepath = os.path.join(REVIEW_DIR, file)

        with open(filepath, "r") as f:
            print("\nCurrent Content:")
            print(f.read())

        new_content = input("\nEnter new review content:\n")
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Review '{file}' updated successfully.")

    except (ValueError, IndexError):
        print("Invalid selection!")

def main():
    while True:
        print("\n==== Product Review Classifier ====")
        print("1. Read & Analyze Reviews")
        print("2. Create New Review")
        print("3. Modify Existing Review")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            read_reviews()
        elif choice == "2":
            create_review()
        elif choice == "3":
            modify_review()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
