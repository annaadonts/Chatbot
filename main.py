import openai
openai.api_key = 'your api key'

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role': 'user', 'content': prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == '__main__':
    while True:
        user_imput = input('You: ')
        if user_imput.lower() in ['quit', 'exit', 'bye']:
            break

        response = chat_with_gpt(user_imput)
        print('Chatbot: ', response)