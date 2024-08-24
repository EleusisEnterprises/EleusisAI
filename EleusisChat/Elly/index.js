require('dotenv').config();
const { Client, GatewayIntentBits, MessageAttachment } = require('discord.js');
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
        const prompt = 'As you enter the server, greet it with a warm and thoughtful tone. Keep the greeting friendly and brief, offering a positive start to the day or interaction. At the end mention that they can ask you anything in the ask channel by using the command !ask';

        // Call the OpenAI service to generate the welcome message
        const response = await axios.post(`${process.env.API_BASE_URL}/ask`, { prompt });

        const channel = await client.channels.fetch(process.env.ELEUSIS_ANNOUNCEMENTS_CHANNEL_ID);
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

// Function to split long messages into chunks
function splitMessage(message, maxLength = 2000) {
    const messageChunks = [];
    let start = 0;
    while (start < message.length) {
        let end = Math.min(start + maxLength, message.length);
        if (end < message.length) {
            // Find the last newline before the 2000 character limit
            const lastNewline = message.lastIndexOf('\n', end);
            if (lastNewline > start) {
                end = lastNewline;
            }
        }
        messageChunks.push(message.slice(start, end));
        start = end + 1; // Move past the last character in the current chunk
    }
    return messageChunks;
}

// Handle !ask command
client.on('messageCreate', async (message) => {
    if (message.author.bot) return; // Ignore messages from bots

    console.log(`Received message: ${message.content} in channel: ${message.channel.id}`);

    if (message.content.startsWith('!ask') && message.channel.id === process.env.ELEUSIS_ASK_CHANNEL_ID) {
        console.log('!ask command detected');

        const userPrompt = message.content.replace('!ask', '').trim();

        if (userPrompt.length === 0) {
            message.reply('Please provide a question.');
            console.log('No prompt provided by the user.');
            return;
        }

        console.log(`User prompt extracted: ${userPrompt}`);

        let prompt, response;
        if (["look up", "search for", "find information on", "reasearch this subject", "search the web"].some(keyword => userPrompt.toLowerCase().includes(keyword))) {
            // Search query detected, prepare a search prompt
            prompt = `search for ${userPrompt}`;
            console.log(`Sending search query to API: ${prompt}`);
            try {
                response = await axios.post(`${process.env.API_BASE_URL}/ask`, { prompt });
                console.log('Search API response received:', response.data.response);
            } catch (error) {
                console.error('Error calling search API:', error.message || error);
                message.reply('Sorry, something went wrong with your search request.');
                return;
            }
        } else {
            // General OpenAI GPT-4 prompt
            prompt = `When responding to a user's !ask command, ensure the answer is crafted with both deep understanding and simplicity. User's question: "${userPrompt}"`;
            console.log(`Sending prompt to OpenAI API: ${prompt}`);
            try {
                response = await axios.post(`${process.env.API_BASE_URL}/ask`, { prompt });
                console.log('OpenAI API response received:', response.data.response);
            } catch (error) {
                console.error('Error calling OpenAI API:', error.message || error);
                message.reply('Sorry, something went wrong with your request.');
                return;
            }
        }

        if (response.data && response.data.response) {
            const messageChunks = splitMessage(response.data.response);

            for (const chunk of messageChunks) {
                await message.channel.send(chunk);
            }
            console.log('Message sent to Discord.');
        } else {
            console.error('API response did not contain expected data.');
            message.reply('Sorry, I did not receive a valid response from the API.');
        }
    }
});

// Handle !img command in any channel
client.on('messageCreate', async (message) => {
    if (message.author.bot) return; // Ignore messages from bots

    if (message.content.startsWith('!img')) {
        console.log('!img command detected');

        const userPrompt = message.content.replace('!img', '').trim();

        if (userPrompt.length === 0) {
            message.reply('Please provide a prompt for the image.');
            console.log('No prompt provided by the user.');
            return;
        }

        console.log(`User prompt for DALL·E extracted: ${userPrompt}`);

        try {
            console.log(`Sending DALL·E prompt to API: ${userPrompt}`);
            const imageUrl = await generate_dalle_image(userPrompt);

            if (typeof imageUrl === 'string') {
                // Send the image URL as a fallback
                message.reply(`Here is your generated image: ${imageUrl}`);
            } else {
                // Send the image as an attachment
                const attachment = new MessageAttachment(imageUrl, 'generated_image.jpg');
                message.reply({ files: [attachment] });
                console.log('Image sent to Discord.');
            }
        } catch (error) {
            console.error('Error calling DALL·E API:', error.message || error);
            message.reply('Sorry, something went wrong with your image request.');
        }
    }
});

async function generate_dalle_image(prompt) {
    try {
        const response = await axios.post(`http://openai-service:80/generate-image`, {
            prompt: prompt,
            size: '1024x1024',
        });

        const imageUrl = response.data.url;
        const imageResponse = await axios.get(imageUrl, { responseType: 'arraybuffer' });
        const imageBuffer = Buffer.from(imageResponse.data, 'binary');

        return imageBuffer;
    } catch (error) {
        console.error('Error generating DALL·E image:', error.message || error);
        return null;
    }
}

// Log in to Discord with your bot's token
client.login(process.env.ELLY_BOT_TOKEN);
