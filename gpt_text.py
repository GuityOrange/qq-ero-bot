from revChatGPT.V1 import Chatbot
from config import email, password, access_token

chatbot = Chatbot(config={
    "access_token": access_token
})


def start_chat():
    print('Welcome to ChatGPT CLI')
    while True:
        prompt = input('> ')

        response = ""

        for data in chatbot.ask(
                prompt
        ):
            response = data["message"]

        print(response)
        print(chatbot.get_conversations()[0]['id'])


if __name__ == "__main__":
    start_chat()