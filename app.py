import config
from devgpt import GPT4

# Create a GPT4 instance
gpt4 = GPT4(config.OPENAI_API_KEY)

# Update the initial system message to request code in the specified format
gpt4.add_message("Act as a senior python dev and provide code in the following format: \n\n```bash\n(required dependencies)\n```\n\n```python\n(Python code)\n```\n\nProvide instructions on how to run the code in the response.", role="system")

gpt4.add_message("Do not use any APIs that require a key and do not import any local files. always output the full code.alays keep the code as 1 file that can be run from main", role="system")

output_saved = False

# Prompt the user to add more messages until they enter "quit" or "exit"
while True:
    message_text = input("Enter a new message (or type 'quit' to exit): ")
    if message_text.lower() in ["quit", "exit"]:
        break

    gpt4.add_message(message_text)
    
    if not output_saved:
        gpt4.extract_filename_from_query(str(gpt4.session.messages[-1]))
        output_saved = True
    

    # Generate and save response
    gpt4.generate_and_save_response()

    # Run code and add output to messages
    gpt4.run_code_and_add_output_to_messages()

# Save session
gpt4.session.save_to_file("session.json")