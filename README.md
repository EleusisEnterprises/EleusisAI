# EleusisAI

## Overview

**EleusisAI** is an ambitious AI project that integrates advanced natural language processing (NLP) models to interact with users in real-time through platforms like Discord. The project is designed to leverage the power of AI to create seamless and intelligent conversations, with a modular architecture that allows for easy expansion and customization.

## Vision

Our vision for EleusisAI is to create an AI platform that goes beyond simple interactions, enabling meaningful conversations that adapt to individual users' needs. By integrating various AI models and databases, we aim to provide a system that learns, adapts, and grows with each interaction. This project is the foundation of a more connected and intelligent digital future, where AI can assist, entertain, and educate in ways that feel natural and personalized.

### Future Expansion

As we move forward, we envision several key areas of expansion:

1. **Integration with Additional Platforms**:
   - Beyond Discord, we plan to extend EleusisAI's capabilities to other platforms such as Slack, Microsoft Teams, and web-based interfaces.

2. **Enhanced AI Models**:
   - We aim to incorporate more specialized AI models, such as sentiment analysis, content moderation, and context-aware recommendation systems, to improve interaction quality.

3. **Modular Plugins**:
   - The development of modular plugins that can be easily added or removed will allow users to customize their AI interactions to fit specific use cases, such as customer support, tutoring, or gaming.

4. **Advanced Data Analytics**:
   - Integrating advanced data analytics to track and analyze user interactions, providing insights that can help refine the AI’s responses and better meet user needs.

5. **Community Contributions**:
   - Encouraging community-driven development where users can contribute their modules, datasets, or improvements to the AI, fostering an ecosystem of shared knowledge and innovation.

## Repository Structure

The repository is divided into two main directories, each with specific responsibilities:

### 1. ElGen

The `ElGen` directory contains tools for data generation, analysis, and tracking, crucial for developing and refining the AI models used in EleusisAI.

#### Key Components:

- **ElgenAnalysis**:
  - Scripts and notebooks for analyzing generated data. This analysis helps refine AI models by providing statistical summaries, visualizations, and other insights.

- **ElgenTrack**:
  - Tools for tracking the performance and characteristics of the data generated. This includes logs, metrics, and other tracking information that ensure data quality and model effectiveness.

- **track**:
  - A script or configuration file related to tracking data or model performance. It defines parameters or processes essential for monitoring the AI’s data processing capabilities.

### 2. EleusisChat

The `EleusisChat` directory is the core of the AI chat system, housing various modules that manage different aspects of the chatbot's functionality.

#### Key Components:

- **CandleAI**:
  - A module responsible for specific AI functionalities, such as dialog management or NLP processing. This might involve handling the core logic behind user interactions.

- **Elly**:
  - Another chat-related module, possibly focused on managing user intents, responses, or conversation flow. It may serve as the brain behind the AI’s conversational capabilities.

- **MindPalace**:
  - This module likely handles memory management, helping the AI remember and recall user information, conversation history, or context across sessions.

- **OpenAI**:
  - Integrates with OpenAI’s API to leverage advanced language models like GPT-4, enabling high-quality and context-aware responses.

- **WebIntegration**:
  - Manages web-based components, including frontend integrations or APIs necessary for deploying the chatbot on web platforms.

- **docker-compose.yml**:
  - A Docker Compose configuration file that defines how the various services within the `EleusisChat` module are built and connected. This file is crucial for setting up the chatbot in a containerized environment.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.7+**: Required for running Python scripts and managing dependencies.
- **Node.js 14+**: Needed for services like `Elly`, which uses JavaScript.
- **Docker & Docker Compose**: For containerizing and running the services efficiently.

### Installation

#### Cloning the Repository

Start by cloning the EleusisAI repository and navigating to the project directory:

```bash
git clone https://github.com/EleusisEnterprises/EleusisAI.git
cd EleusisAI
```

#### Setting Up the OpenAI Service

1. **Navigate to the OpenAI Directory**:

   ```bash
   cd EleusisChat/OpenAI
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv venv
   # For Windows:
   .\venv\Scripts\activate
   # For macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Python Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   Create an `.env` file in the `OpenAI` directory with your OpenAI API key and other necessary variables:

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=your_password
   ```

### Running the Chatbot

#### Starting the OpenAI Service

To start the OpenAI service, navigate to the `OpenAI` directory and run:

```bash
python main.py
```

This command will start the service, typically accessible at `http://localhost:6000`.

#### Running the Discord Bot (Elly)

Navigate to the `Elly` directory and install Node.js dependencies:

```bash
cd EleusisChat/Elly
npm install
```

Set up your environment variables in an `.env` file, then start the bot:

```bash
node index.js
```

This will launch the Discord bot, which should be connected to your Discord server and ready to interact with users.

### Docker Setup

If you prefer to run the services using Docker, follow these steps:

#### Running with Docker Compose

From the root directory of the repository:

```bash
docker-compose up --build
```

This command builds and starts all defined services, including the OpenAI service and Discord bot, in their respective containers.

### Contributing

We welcome contributions to EleusisAI! Here’s how you can contribute:

1. **Fork the repository**: Create a personal fork of the project on GitHub.
2. **Make your changes**: Work on your forked repository, making the necessary changes.
3. **Submit a pull request**: Once your changes are ready, submit a pull request for review.

### Customization

EleusisChat is designed to be flexible and customizable. Here’s how you can modify or extend its functionality:

1. **Modify Bot Commands**:
   - Edit the `index.js` file in the `Elly` directory to add or change bot commands.
   
2. **Change AI Behavior**:
   - Customize how the AI responds by modifying prompts and logic in the `OpenAI` module’s `main.py` script.

3. **Expand Functionality**:
   - Integrate other platforms or add new features by extending the current architecture.

## License

EleusisChat is licensed under the MIT License, allowing for personal and commercial use. For more details, see the [LICENSE](./LICENSE) file in the EleusisAI repository.