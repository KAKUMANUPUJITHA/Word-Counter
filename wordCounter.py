def word_count(text):
    """
    Count the number of words in the given text(sentence or paragraph).

    Args:
        text (str): The input text.

    Returns:
        int: The number of words in the text.
    """
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Return the length of the list of words
    return len(words)

def main():
    print("Welcome to the Word Counter!")
    
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Check if the input is empty or not?
    if not user_input:
        print("Error: No input provided.")
        return
    
    # Call the word_count function to count the words
    count = word_count(user_input)
    
    # Display the word count
    print(f"\nWord count: {count}")

if __name__ == "__main__":
    main()


