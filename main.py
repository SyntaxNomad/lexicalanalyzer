from lexer import LexicalAnalyzer

def main():
    # Prompt the user to enter the input file name
    filename = input("Enter the name of the input file: ").strip()

    # Handle file not found or initialization errors
    try:
        lexer = LexicalAnalyzer(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the file path.")
        return
    except Exception as e:
        print(f"An error occurred while initializing the lexer: {e}")
        return

    while True:
        # Display menu
        print("\nMenu:")
        print("1. Call lex()")
        print("2. Show symbol table")
        print("3. Exit")

        # Get user input
        choice = input("Enter your choice: ").strip()

        # Handle user choices
        if choice == "1":
            try:
                print("Tokens:")
                while True:
                    token = lexer.lex()
                    if token is None:
                        print("End of file reached.")
                        break
                    else:
                        print(f"Token: {token}")
            except Exception as e:
                print(f"An error occurred while calling lex(): {e}")
        elif choice == "2":
            try:
                lexer.show_symbol_table()
            except Exception as e:
                print(f"An error occurred while showing the symbol table: {e}")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()