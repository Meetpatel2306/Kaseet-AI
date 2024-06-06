import pyttsx3

def initialize_engine():
    """Initialize the TTS engine with custom settings."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change voice to female (if available)
    return engine

def main():
    print("Welcome to Kaseet AI Created by Meet Patel")

    # Initialize the text-to-speech engine
    engine = initialize_engine()

    # Greet the user
    engine.say("Welcome to Kaseet AI created by Meet Patel")
    engine.runAndWait()

    while True:
        try:
            # Get the text input from the user
            text_to_speak = input("What do you want me to speak: ")

            # Speak the input text
            engine.say(text_to_speak)
            engine.runAndWait()

            # Ask the user if they want to save the speech to a file
            save_option = input("Do you want to save the speech to a file (y/n): ").strip().lower()
            if save_option == 'y':
                filename = input("Enter the filename (without extension): ").strip()
                engine.save_to_file(text_to_speak, f"{filename}.mp3")
                engine.runAndWait()
                print(f"Speech saved to {filename}.mp3")

            # Ask the user if they want to continue
            continue_response = input("Do you want to continue (y/n): ").strip().lower()
            if continue_response == "n":
                # Speak a farewell message and exit the loop
                print("Thank you for using Kaseet AI. Goodbye Dear!")
                farewell_message = "Thank you for using Kaseet AI. Goodbye Dear!"
                engine.say(farewell_message)
                engine.runAndWait()
                break
        except Exception as e:
            print(f"An error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
