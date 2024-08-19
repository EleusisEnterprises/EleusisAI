require('dotenv').config();
const axios = require('axios');
const { Client, GatewayIntentBits } = require('discord.js');

const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

async function generateMessage(isWelcome) {
    try {
        const prompt = isWelcome 
            ? 'As the bot starts up, please say hello in the style of Swiper from Dora the Explorer but he uses sniper every single time he was going to say swiper.' 
            : 'As the bot shuts down, say goodbye in the style of Swiper from Dora the Explorer but he uses sniper every single time he was going to say swiper.';
        
        const response = await axios.post(`${process.env.API_BASE_URL}/ask`, { 
            prompt, 
            model: "gpt-4"
        });
        return response.data.response;
    } catch (error) {
        console.error('Error generating message:', error.message || error);
        return isWelcome 
            ? 'Sniper is here! Ready to snipe some trades!'
            : 'Sniper out! Until next time!';
    }
}

async function sendMessage(isWelcome) {
    try {
        const channelId = process.env.GOODBYE_CHANNEL_ID;  // Assuming the same channel for both
        const message = await generateMessage(isWelcome);
        const channel = await client.channels.fetch(channelId);

        if (channel) {
            await channel.send(message);
            console.log(`${isWelcome ? 'Welcome' : 'Goodbye'} message sent successfully.`);
        } else {
            console.error('Channel not found!');
        }
    } catch (error) {
        console.error(`Failed to send ${isWelcome ? 'welcome' : 'goodbye'} message:`, error.message || error);
    } finally {
        client.destroy();
        console.log('Discord client destroyed.');
        process.exit(0);  // Ensure the script exits
    }
}

client.once('ready', () => {
    const isWelcome = process.argv[2] === 'welcome';
    sendMessage(isWelcome);
});

client.login(process.env.DISCORD_BOT_TOKEN);
