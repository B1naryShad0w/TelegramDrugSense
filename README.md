# TrippinTips Telegram Bot

TrippinTips is a Telegram bot designed to provide advice on safe drug usage for students. Its primary goal is not to discourage drug use, but to educate on how to use them safely. The bot incorporates emojis, casual language, and NSFW humor to create a more engaging and relatable experience for users.

## Docker Installation

To run this bot in a Docker container, you will need [Docker](https://docs.docker.com/engine/install/ "Install Docker Engine") installed on your system. 

1. Clone the repository
```bash
git clone https://github.com/B1naryShad0w/trippintips.git
```
2. Build the Docker image by running the following command in the directory containing the Dockerfile:
```bash
docker build -t trippintips .
```
3. Once the image has been built, you can run the container with the following command:
```bash
docker run -d \
  --name=trippingtipsbot \
  -e API_OPENAI=<OPENAI_API_KEY> \
  -e API_TELEGRAM=<TELEGRAM_API_KEY> \
  --restart unless-stopped \
  trippintips
```
Please note that you need to replace <OPENAI_API_KEY> and <TELEGRAM_API_KEY> with your actual OpenAI and Telegram API keys.

## Usage
Use the bot in Telegram by starting a conversation with it.

## Functionality
The bot processes user messages and generates responses using OpenAI's GPT-3.5-turbo model, taking into account the system message and user input. It logs requests and responses to a file named "log" for debugging purposes.

## Handlers
The script contains two main handlers:
- start_handler: Handles the /start command, which sends a greeting message to the user.
- echo_handler: Handles text messages from users that are not commands, providing responses based on the user's input.

## Logging
The script uses Python's logging library to log messages related to requests, responses, and potential issues. The log messages are stored in a file called "log" in the same directory as the script.

## License
This project is open source and available under the MIT License.
