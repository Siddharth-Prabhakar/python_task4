def chatbot():
    print("Type 'hello', 'how are you', or 'bye'. Otherwise, I won't understand.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Hi!")
        elif user_input == "how are you":
            print("I'm fine, thanks!")
        elif user_input == "bye":
            print("Goodbye!")
            break
        else:
            print("I don't understand that.")

chatbot() 