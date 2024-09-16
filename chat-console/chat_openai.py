from openai import OpenAI
import os

# Retrieve the API key from the environment variable
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']  # this is also the default, it can be omitted
)

def chat_with_gpt(prompt):
    try:
        # Sending request to ChatGPT with the provided prompt
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Choose the model you want to use
            messages=[
                {"role": "system", "content": "You are an helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )

        # Extracting the response from the ChatGPT response
        reply = response.choices[0].message.content  
        return reply

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # User prompt
    prompt = "Explain the concept of machine learning."
    
    # Get response from ChatGPT
    result = chat_with_gpt(prompt)
    
    # Display the result
    print("AI Response:")
    print(result)
