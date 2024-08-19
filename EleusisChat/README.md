# EleusisChat

**EleusisChat** is a dynamic communication tool that leverages OpenAI's language models to interact with users in real-time through platforms like Discord. It serves as a bridge between natural language processing and conversational AI, allowing for seamless and intelligent interaction within a server environment.

## Overview

EleusisChat is designed to bring the power of GPT-4 into chat environments, initially focusing on Discord. The application is composed of two main components:

1. **OpenAI Service**: A Flask-based API that handles natural language processing tasks using OpenAI's models.
   
2. **Discord Bot (Elly)**: A bot that interacts with users on Discord, facilitating conversations, managing commands, and providing AI-driven responses.

## Key Features

- **Real-Time Interaction**: Provides immediate, AI-driven responses to user queries and commands in a Discord server.
- **Customizable Bot Behavior**: The bot's responses and behavior can be tailored to fit the needs of your specific community or application.
- **Modular Design**: The components are designed to be easily extensible, allowing for future integrations with other platforms beyond Discord.

## Installation and Setup

### Prerequisites

To get started with EleusisChat, ensure you have the following installed:

- [Python 3.7+](https://www.python.org/downloads/)
- [Node.js 14+](https://nodejs.org/)
- [Docker](https://www.docker.com/) (optional, for running with Docker Compose)

### Cloning the Repository

Clone the EleusisAI repository and navigate to the EleusisChat directory:

```bash
git clone https://github.com/EleusisEnterprises/EleusisAI.git
cd EleusisAI/EleusisChat
```

### Setting Up the OpenAI Service

1. **Navigate to the OpenAI Directory**:

   ```bash
   cd OpenAI
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv venv
   # Activate the virtual environment
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Python Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   Create a `.env` file in the `OpenAI` directory:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

### Setting Up the Discord Bot (Elly)

1. **Navigate to the Elly Directory**:

   ```bash
   cd ../Elly
   ```

2. **Install Node.js Dependencies**:

   ```bash
   npm install
   ```

3. **Set Up Environment Variables**:

   Create a `.env` file in the `Elly` directory:

   ```env
   DISCORD_BOT_TOKEN=your_discord_bot_token
   API_BASE_URL=http://localhost:6000
   ANNOUNCEMENTS_CHANNEL_ID=your_channel_id
   ASK_CHANNEL_ID=your_ask_channel_id
   ```

## Running the Services

### Running the OpenAI Service

Start the OpenAI service by navigating to the `OpenAI` directory and running:

```bash
python main.py
```

This will start the Flask server, typically accessible at `http://localhost:6000`.

### Running the Discord Bot

Start the Discord bot by navigating to the `Elly` directory and running:

```bash
node index.js
```

The bot should now be online in your Discord server, ready to interact with users.

## Docker Setup

If you prefer to run the services using Docker, you can do so with Docker Compose.

### Running with Docker Compose

From the root directory of the repository:

```bash
docker-compose up
```

This command will build and start both the OpenAI service and the Discord bot in their respective containers.

## Customization

EleusisChat is designed to be flexible and customizable. Here are a few ways you can tailor it to your needs:

- **Modify Bot Commands**: You can add or modify the bot’s commands by editing the `index.js` file in the `Elly` directory.
- **Change AI Behavior**: Customize how the AI responds by adjusting the prompts and logic in the `openai_chat.py` script within the `OpenAI` directory.
- **Expand Functionality**: Integrate with other platforms or add new features by extending the current architecture.

## Contributing

Contributions to EleusisChat are welcome! Whether you're fixing bugs, adding features, or improving documentation, your contributions help improve the project. To contribute:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request for review.

## Future Plans

As part of the EleusisAI project, EleusisChat will continue to evolve. Planned future updates include:

- **Integration with Additional Platforms**: Beyond Discord, future integrations may include Slack, Telegram, and web interfaces.
- **Enhanced AI Models**: Incorporate more specialized AI models for tasks like sentiment analysis and content moderation.
- **Improved Contextual Awareness**: Implement memory systems that allow the bot to reference past interactions for more context-aware responses.

## License

EleusisChat is licensed under the MIT License, allowing for both personal and commercial use. For more details, see the [LICENSE](../LICENSE) file in the EleusisAI repository.