# EleusisAI

**EleusisAI** is a dual-service application that integrates an OpenAI-powered service with a Discord bot. The OpenAI service handles natural language processing tasks, while the Discord bot interacts with users on a Discord server, providing AI-driven responses and functionalities.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Services](#running-the-services)
- [Docker Setup](#docker-setup)
- [Future Expansion Plans](#future-expansion-plans)
- [Debugging](#debugging)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.7+](https://www.python.org/downloads/)
- [Node.js 14+](https://nodejs.org/)
- [Docker](https://www.docker.com/) (optional, for running with Docker Compose)
- [Visual Studio Code](https://code.visualstudio.com/) (recommended for development)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/EleusisEnterprises/EleusisAI.git
cd EleusisAI
```

### 2. Setting Up the Python Environment (OpenAI Service)

Navigate to the `EleusisChat/OpenAI` directory:

```bash
cd EleusisChat/OpenAI
```

Create and activate a virtual environment:

```bash
python -m venv venv
# Activate the virtual environment
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Setting Up the Node.js Environment (Swiper Bot)

Navigate to the `EleusisChat/Swiper` directory:

```bash
cd ../Swiper
```

Install the Node.js dependencies:

```bash
npm install
```

## Configuration

Create `.env` files in the `OpenAI` and `Swiper` directories to store environment variables.

### For `OpenAI` Service (`EleusisChat/OpenAI/.env`):

```env
OPENAI_API_KEY=your_openai_api_key
```

### For `Swiper` Bot (`EleusisChat/Swiper/.env`):

```env
DISCORD_BOT_TOKEN=your_discord_bot_token
API_BASE_URL=http://localhost:6000
```

## Running the Services

### Running the OpenAI Service

From the `EleusisChat/OpenAI` directory:

```bash
python main.py
```

This will start the Flask server, typically on `http://localhost:6000`.

### Running the Swiper Bot

From the `EleusisChat/Swiper` directory:

```bash
node index.js
```

This will start the Discord bot, which should be online in your Discord server if configured correctly.

## Docker Setup

You can also run both services using Docker Compose.

### Running with Docker Compose

From the root directory of the repository:

```bash
docker-compose up
```

This will build and start both services in their respective containers.

## Future Expansion Plans

### Vision and Goals

The ultimate goal of **EleusisAI** is to create a versatile AI platform that uses GPT-4 as a central mediator between various specialized models, allowing for sophisticated and contextually aware interactions between different human endpoints. The first step in this journey is the integration with a Discord bot, but the vision extends far beyond that.

### Planned Features

1. **Specialized AI Models**:
   - We plan to integrate specialized AI models for various tasks (e.g., image processing, sentiment analysis, task automation). GPT-4 will serve as the orchestrator, delegating tasks to these models and synthesizing their outputs into coherent, actionable responses.

2. **Working Memory Database**:
   - We aim to create a dynamic database that functions as a "working memory" for GPT-4. This memory will allow the system to reference past interactions and context, enabling more robust decision-making, better continuity in conversations, and the ability to handle ongoing subjects with greater depth and accuracy.

3. **Multi-Endpoint Integration**:
   - Beyond Discord, EleusisAI will support multiple communication endpoints, such as Slack, Telegram, web interfaces, and even voice-based systems. Each endpoint will interact seamlessly with GPT-4 and the specialized models, providing consistent and intelligent responses across platforms.

4. **Contextual Awareness**:
   - The integration of a working memory database will significantly enhance GPT-4's contextual awareness. By storing and retrieving relevant data from past interactions, the system will be able to maintain a more human-like understanding of long-term conversations.

5. **Scalability and Performance**:
   - We plan to optimize the system for scalability, allowing it to handle multiple requests from different endpoints concurrently. This includes implementing distributed processing, load balancing, and efficient data storage mechanisms.

### Long-Term Vision

The long-term vision for EleusisAI is to create an AI-powered ecosystem where specialized models, guided by GPT-4, work together to provide advanced, contextually aware assistance across various domains and platforms. This ecosystem will evolve to include more specialized models, improved memory systems, and more sophisticated integration capabilities, ultimately becoming a powerful tool for both individual users and organizations.

## Debugging

### Python (OpenAI Service)

- Set up a Python debug configuration in VS Code for `main.py`.
- Use the VS Code debugger to run the service with breakpoints.

### Node.js (Swiper Bot)

- Set up a Node.js debug configuration in VS Code for `index.js`.
- Use the VS Code debugger for real-time debugging.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for review.

### Reporting Issues

If you encounter any issues, please open an [issue on GitHub](https://github.com/EleusisEnterprises/EleusisAI/issues).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```