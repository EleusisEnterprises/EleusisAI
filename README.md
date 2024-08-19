# EleusisAI

**EleusisAI** is a versatile AI-driven platform designed to integrate multiple specialized services, each contributing to a sophisticated ecosystem for human-computer interaction. This repository contains the core elements of EleusisAI, which is built to enhance user experience across different domains, including natural language processing and financial analysis, through the use of advanced AI models like GPT-4.

## Overview

EleusisAI is composed of two main applications:

1. **EleusisChat**: A communication-focused service that integrates OpenAI's language models with platforms like Discord to provide real-time, AI-driven responses and interactions.
   
2. **ElGen**: A specialized Pine Script-based application that enhances trading strategies with advanced technical analysis tools.

These applications are designed to be modular, allowing for easy expansion and integration of new features and AI models as the project evolves.

## Key Features

- **Modular Design**: Each component of EleusisAI is developed independently, allowing for flexibility and scalability as the platform grows.
- **AI-Driven**: Leveraging GPT-4 and other advanced models to provide intelligent responses and analyses across various domains.
- **Cross-Platform Integration**: Initial focus on Discord, with plans to extend to other platforms like Slack, Telegram, and web interfaces.
- **Customizable**: Both EleusisChat and ElGen can be customized and extended to meet specific user needs, making the platform adaptable to various use cases.

## Applications

### EleusisChat

EleusisChat is a powerful communication tool that combines the capabilities of OpenAI’s language models with popular communication platforms. The initial implementation focuses on integrating with Discord, allowing the bot to provide real-time, context-aware responses, manage conversations, and perform automated tasks within a server environment.

Key components include:
- **OpenAI Service**: Handles natural language processing tasks using GPT-4.
- **Discord Bot (Elly)**: Manages user interactions on Discord, responding to commands, and facilitating conversations.

[Detailed README for EleusisChat](./EleusisChat/README.md) - (To be created)

### ElGen

ElGen is a specialized tool aimed at traders and financial analysts. It utilizes Pine Script within TradingView to develop advanced technical indicators and strategies. The current focus is on enhancing the EMA cross strategy with additional visual and analytical features to improve trading decisions.

Key components include:
- **Pine Script Indicator**: Implements the core logic for the enhanced EMA cross strategy.
- **Modular Architecture**: Allows users to easily customize and extend the strategy with additional features.

[Detailed README for ElGen](./ElGen/README.md) - (To be created)

## Vision and Future Development

The long-term vision for EleusisAI is to create an AI-powered ecosystem that can adapt to various domains and platforms. As the project evolves, we aim to:

- Integrate additional specialized AI models for tasks like image processing, sentiment analysis, and task automation.
- Develop a working memory system that allows the AI to reference past interactions, enhancing its contextual understanding and decision-making capabilities.
- Expand the platform to support multiple communication endpoints, ensuring consistent and intelligent responses across all platforms.

## Contribution

Contributions to EleusisAI are welcome! Whether you want to improve existing features, add new ones, or help with documentation, your input is valuable. Please follow the standard GitHub process: fork the repository, make your changes, and submit a pull request for review.

For specific contributions to EleusisChat or ElGen, please refer to their respective READMEs.

## License

EleusisAI is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
