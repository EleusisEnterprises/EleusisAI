require('dotenv').config();
const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios');

const client = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});

client.once('ready', async () => {
    console.log('Bot is online!');

    // Send welcome message on startup to a specific channel
    try {
        const prompt = 'Please greet the server in the style of Swiper from Dora the Explorer but say "sniper" instead of "swiper".';
        
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
    if (message.author.bot) return;

    // Handle !ask command in a specific channel
    if (message.content.startsWith('!ask') && message.channel.id === process.env.ASK_CHANNEL_ID) {
        const prompt = message.content.replace('!ask', '').trim() || 'What can I help you with?';
        if (prompt.length === 0) {
            message.reply('Please provide a question.');
            return;
        }

        try {
            const response = await axios.post(`${process.env.API_BASE_URL}/ask`, { prompt });
            message.reply(response.data.response);
        } catch (error) {
            console.error('Error calling API:', error);
            message.reply('Sorry, something went wrong with your request.');
        }
    }
});

client.login(process.env.DISCORD_BOT_TOKEN);
