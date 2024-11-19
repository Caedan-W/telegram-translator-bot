# Telegram 翻译机器人

一个简单的 Telegram 翻译机器人，可以自动将消息翻译成中文。

## 功能特点

- 自动检测源语言
- 将任何语言翻译成中文
- 简单易用的命令接口
- 支持长文本翻译

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/Caedan-W/telegram-translator-bot.git
cd telegram-translator-bot
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置环境变量：
   - 创建 `.env` 文件
   - 添加你的 Telegram Bot Token：
```plaintext
TELEGRAM_BOT_TOKEN=你的token
```

## 获取 Telegram Bot Token

1. 在 Telegram 中找到 [@BotFather](https://t.me/BotFather)
2. 发送 `/newbot` 命令
3. 按照提示设置机器人名称和用户名
4. 复制获得的 token 到 `.env` 文件中

## 使用方法

1. 运行机器人：
```bash
python translator.py
```

2. 在 Telegram 中使用：
   - 搜索你创建的机器人用户名
   - 发送 `/start` 开始使用
   - 发送任何文本消息，机器人会自动翻译成中文

## 命令列表

- `/start` - 开始使用机器人
- 直接发送文本 - 自动翻译成中文

## 部署建议

### 在服务器上运行

使用 screen 保持程序运行：
```bash
screen -S telegram-bot
python translator.py
```

按 `Ctrl+A+D` 分离 screen 会话

### 使用 systemd 服务（Linux）

1. 创建服务文件：
```bash
sudo nano /etc/systemd/system/telegram-translator.service
```

2. 添加以下内容：
```ini
[Unit]
Description=Telegram Translator Bot
After=network.target

[Service]
Type=simple
User=你的用户名
WorkingDirectory=/path/to/telegram-translator-bot
Environment=PYTHONUNBUFFERED=1
ExecStart=/usr/bin/python3 translator.py
Restart=always

[Install]
WantedBy=multi-user.target
```

3. 启动服务：
```bash
sudo systemctl start telegram-translator
sudo systemctl enable telegram-translator
```

## 技术栈

- Python 3.7+
- python-telegram-bot
- deep-translator
- python-dotenv

## 常见问题

1. **机器人无响应**
   - 检查 TOKEN 是否正确
   - 确认网络连接正常
   - 查看程序运行日志

2. **翻译失败**
   - 检查网络连接
   - 确认文本长度是否在限制范围内
   - 检查是否有特殊字符

## 贡献指南

1. Fork 本仓库
2. 创建新分支：`git checkout -b feature/AmazingFeature`
3. 提交更改：`git commit -m 'Add some AmazingFeature'`
4. 推送分支：`git push origin feature/AmazingFeature`
5. 提交 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 联系方式

如有问题或建议，请：
- 提交 [Issue](https://github.com/Caedan-W/telegram-translator-bot/issues)
- 发送邮件至 [你的邮箱]

## 更新日志

### v1.0.0 (2024-11-19)
- 初始版本发布
- 支持基本的文本翻译功能

