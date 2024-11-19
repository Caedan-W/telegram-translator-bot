# Telegram 翻译机器人 | Telegram Translator Bot

一个简单的 Telegram 翻译机器人，可以自动将消息翻译成中文。

A simple Telegram bot that automatically translates messages into Chinese.

## 功能特点 | Features

- 自动检测源语言 | Automatic source language detection
- 将任何语言翻译成中文 | Translation into Chinese
- 简单易用的命令接口 | Simple command interface
- 支持长文本翻译 | Support for long text translation

## 安装 | Installation

1. 克隆仓库 | Clone the repository:
```bash
git clone https://github.com/Caedan-W/telegram-translator-bot.git
cd telegram-translator-bot
```

2. 安装依赖 | Install dependencies:
```bash
pip install -r requirements.txt
```

3. 配置环境变量 | Configure environment variables:
   - 创建 `.env` 文件 | Create a `.env` file
   - 添加你的 Telegram Bot Token | Add your Telegram Bot Token:
```plaintext
TELEGRAM_BOT_TOKEN=your_token_here
```

## 获取 Telegram Bot Token | Getting a Telegram Bot Token

1. 在 Telegram 中找到 [@BotFather](https://t.me/BotFather) | Find @BotFather on Telegram
2. 发送 `/newbot` 命令 | Send the `/newbot` command
3. 按照提示设置机器人名称和用户名 | Follow the prompts to set up your bot's name and username
4. 复制获得的 token 到 `.env` 文件中 | Copy the token to your `.env` file

## 使用方法 | Usage

1. 运行机器人 | Run the bot:
```bash
python translator.py
```

2. 在 Telegram 中使用 | Using in Telegram:
   - 搜索你创建的机器人用户名 | Search for your bot's username
   - 发送 `/start` 开始使用 | Send `/start` to begin
   - 发送任何文本消息，机器人会自动翻译成中文 | Send any text message for automatic translation to Chinese

## 命令列表 | Commands

- `/start` - 开始使用机器人 | Start using the bot
- 直接发送文本 - 自动翻译成中文 | Send any text - Automatically translate to Chinese

## 部署建议 | Deployment Tips

### 在服务器上运行 | Running on Server

使用 screen 保持程序运行 | Using screen to keep the program running:
```bash
screen -S telegram-bot
python translator.py
```

按 `Ctrl+A+D` 分离 screen 会话 | Press `Ctrl+A+D` to detach the screen session

### 使用 systemd 服务（Linux）| Using systemd Service (Linux)

1. 创建服务文件 | Create a service file:
```bash
sudo nano /etc/systemd/system/telegram-translator.service
```

2. 添加以下内容 | Add the following content:
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

3. 启动服务 | Start the service:
```bash
sudo systemctl start telegram-translator
sudo systemctl enable telegram-translator
```

## 技术栈 | Tech Stack

- Python 3.7+
- python-telegram-bot
- deep-translator
- python-dotenv

## 常见问题 | Troubleshooting

1. **机器人无响应 | Bot Not Responding**
   - 检查 TOKEN 是否正确 | Check if TOKEN is correct
   - 确认网络连接正常 | Verify network connection
   - 查看程序运行日志 | Check program logs

2. **翻译失败 | Translation Failed**
   - 检查网络连接 | Check network connection
   - 确认文本长度是否在限制范围内 | Verify text length is within limits
   - 检查是否有特殊字符 | Check for special characters

## 贡献指南 | Contributing

1. Fork 本仓库 | Fork the repository
2. 创建新分支 | Create your feature branch: `git checkout -b feature/AmazingFeature`
3. 提交更改 | Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. 推送分支 | Push to the branch: `git push origin feature/AmazingFeature`
5. 提交 Pull Request | Open a Pull Request

## 许可证 | License

本项目采用 MIT 许可证 | This project is licensed under the MIT License - 查看 [LICENSE](LICENSE) 文件了解详情 | see the [LICENSE](LICENSE) file for details

## 联系方式 | Contact

如有问题或建议 | For issues or suggestions:
- 提交 [Issue](https://github.com/Caedan-W/telegram-translator-bot/issues) | Submit an Issue
- 发送邮件至 | Email: [wst421155149@163.com]

## 更新日志 | Changelog

### v1.0.0 (2024-11-19)
- 初始版本发布 | Initial release
- 支持基本的文本翻译功能 | Basic text translation functionality

