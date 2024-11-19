# Telegram Translator Bot

A simple Telegram bot that automatically translates messages into Chinese.

## Features

- Automatic source language detection
- Translation into Chinese
- Simple command interface
- Support for long text translation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Caedan-W/telegram-translator-bot.git
cd telegram-translator-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
   - Create a `.env` file
   - Add your Telegram Bot Token:
```plaintext
TELEGRAM_BOT_TOKEN=your_token_here
```

## Getting a Telegram Bot Token

1. Find [@BotFather](https://t.me/BotFather) on Telegram
2. Send the `/newbot` command
3. Follow the prompts to set up your bot's name and username
4. Copy the token to your `.env` file

## Usage

1. Run the bot:
```bash
python translator.py
```

2. Using in Telegram:
   - Search for your bot's username
   - Send `/start` to begin
   - Send any text message for automatic translation to Chinese

## Commands

- `/start` - Start using the bot
- Send any text - Automatically translate to Chinese

## Deployment Tips

### Running on Server

Using screen to keep the program running:
```bash
screen -S telegram-bot
python translator.py
```

Press `Ctrl+A+D` to detach the screen session

### Using systemd Service (Linux)

1. Create a service file:
```bash
sudo nano /etc/systemd/system/telegram-translator.service
```

2. Add the following content:
```ini
[Unit]
Description=Telegram Translator Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/telegram-translator-bot
Environment=PYTHONUNBUFFERED=1
ExecStart=/usr/bin/python3 translator.py
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Start the service:
```bash
sudo systemctl start telegram-translator
sudo systemctl enable telegram-translator
```

## Tech Stack

- Python 3.7+
- python-telegram-bot
- deep-translator
- python-dotenv

## Troubleshooting

1. **Bot Not Responding**
   - Check if TOKEN is correct
   - Verify network connection
   - Check program logs

2. **Translation Failed**
   - Check network connection
   - Verify text length is within limits
   - Check for special characters

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Contact

For issues or suggestions:
- Submit an [Issue](https://github.com/Caedan-W/telegram-translator-bot/issues)
- Email: [your_email]

## Changelog

### v1.0.0 (2024-11-19)
- Initial release
- Basic text translation functionality 