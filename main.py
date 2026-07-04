from agent import run_agent

def main():
    print("===== AI Agent =====")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = run_agent(user_input)

        print("\nAI Agent:")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()