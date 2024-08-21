require('dotenv').config();
const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios');

// Create a new client instance
const client = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});

client.once('ready', async () => {
    console.log('Bot is online!');

    // Function to check if the OpenAI server is ready
    const checkServerHealth = async () => {
        try {
            const response = await axios.get(`${process.env.API_BASE_URL}/health`);
            return response.status === 200;
        } catch (error) {
            console.error('OpenAI server health check failed:', error.message || error);
            return false;
        }
    };

    // Poll the health check endpoint until the server is ready
    let serverReady = false;
    while (!serverReady) {
        serverReady = await checkServerHealth();
        if (!serverReady) {
            console.log('Waiting for the OpenAI server to be ready...');
            await new Promise(resolve => setTimeout(resolve, 5000)); // Wait for 5 seconds before checking again
        }
    }

    console.log('OpenAI server is ready. Sending welcome message...');

    // Send shortened welcome message to a specific channel once the server is ready
    try {
        const prompt = 'As you enter the server, greet it with a warm and thoughtful tone. Keep the greeting friendly and brief, offering a positive start to the day or interaction. at the end mention that they can ask you anything in the ask channel by using the command !ask';

        // Call the OpenAI service to generate the welcome message
        const response = await axios.post(`${process.env.API_BASE_URL}/ask`, { prompt });

        const channel = await client.channels.fetch(process.env.ANNOUNCEMENTS_CHANNEL_ID);
        if (channel) {
            await channel.send(`${response.data.response} @everyone`);
            console.log('Welcome message sent successfully.');
        } else {
            console.error('Channel not found for sending the welcome message.');
        }
    } catch (error) {
        console.error('Error generating or sending welcome message:', error.message || error);
    }
});

client.on('messageCreate', async (message) => {
    if (message.author.bot) return; // Ignore messages from bots

    console.log(`Received message: ${message.content} in channel: ${message.channel.id}`);

    // Handle !ask command in a specific channel
    if (message.content.startsWith('!ask') && message.channel.id === process.env.ASK_CHANNEL_ID) {
        console.log('!ask command detected');

        const userPrompt = message.content.replace('!ask', '').trim();

        if (userPrompt.length === 0) {
            message.reply('Please provide a question.');
            console.log('No prompt provided by the user.');
            return;
        }

        console.log(`User prompt extracted: ${userPrompt}`);

        // Combine the guidance prompt with the user's prompt
        const prompt = `When responding to a user's !ask command, ensure the answer is crafted with both deep understanding and simplicity. First, understand the user's question thoroughly. Then, provide an answer that captures the essence of the topic with clarity, avoiding unnecessary complexity. If applicable, use analogies or examples to make the explanation more relatable and easier to grasp. User's question: "${userPrompt}"`;

        try {
            console.log(`Sending prompt to API: ${prompt}`);
            const response = await axios.post(`${process.env.API_BASE_URL}/ask`, { prompt });
            console.log('Full API response:', response.data);
            console.log('API response received:', response.data.response);

            // Check if the response has a valid content
            if (response.data && response.data.response) {
                message.reply(response.data.response);
                console.log('Message sent to Discord.');
            } else {
                console.error('API response did not contain expected data.');
                message.reply('Sorry, I did not receive a valid response from the API.');
            }
        } catch (error) {
            console.error('Error calling API:', error.message || error);
            message.reply('Sorry, something went wrong with your request.');
        }
    }

    // Handle !pic command in any channel
    if (message.content.startsWith('!img')) {
        console.log('!img command detected');

        const userPrompt = message.content.replace('!pic', '').trim();

        if (userPrompt.length === 0) {
            message.reply('Please provide a prompt for the image.');
            console.log('No prompt provided by the user.');
            return;
        }

        console.log(`User prompt for DALL·E extracted: ${userPrompt}`);

        try {
            console.log(`Sending DALL·E prompt to API: ${userPrompt}`);
            const response = await axios.post(`${process.env.API_BASE_URL}/generate-image`, { prompt: userPrompt });
            console.log('Full API response:', response.data);

            // Check if the response has a valid content
            if (response.data && response.data.image_url) {
                message.reply(response.data.image_url);
                console.log('Image URL sent to Discord.');
            } else {
                console.error('API response did not contain expected data.');
                message.reply('Sorry, I did not receive a valid response from the API.');
            }
        } catch (error) {
            console.error('Error calling DALL·E API:', error.message || error);
            message.reply('Sorry, something went wrong with your image request.');
        }
    }
});

// Log in to Discord with your bot's token
client.login(process.env.DISCORD_BOT_TOKEN);
