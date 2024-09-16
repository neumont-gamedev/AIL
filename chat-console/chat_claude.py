import anthropic
import os

# Set your API key
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable.")

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=api_key)

# Function to send a message to Claude and get the response
def chat_with_claude(message, conversation_history):
    conversation_history.append({"role": "user", "content": message})
    
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=conversation_history
    )
    
    assistant_message = response.content[0].text
    conversation_history.append({"role": "assistant", "content": assistant_message})
    
    return assistant_message, conversation_history

# Main chat loop
def main():
    print("Welcome to the Claude Chat! Type 'quit' to exit.")
    conversation_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        response, conversation_history = chat_with_claude(user_input, conversation_history)
        print("Claude:", response)

if __name__ == "__main__":
    main()