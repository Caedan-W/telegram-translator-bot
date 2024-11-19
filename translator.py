# 导入必要的库
from telegram import Update  # 用于处理 Telegram 更新
from telegram.ext import Application, CommandHandler, MessageHandler, filters  # Telegram 机器人的核心组件
from deep_translator import GoogleTranslator  # Google 翻译API的封装
from dotenv import load_dotenv  # 用于加载环境变量
import asyncio  # 用于异步编程
import platform  # 用于检测操作系统类型
import os  # 用于处理环境变量

# 加载 .env 文件中的环境变量
load_dotenv()

# 获取 Telegram Bot Token
my_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not my_TOKEN:
    raise ValueError("未找到 TELEGRAM_BOT_TOKEN 环境变量")

# 处理 /start 命令的异步函数
async def start(update, context):
    """
    当用户发送 /start 命令时触发
    update: 包含用户消息的对象
    context: 回调上下文
    """
    await update.message.reply_text('你好！请发送要翻译的文本。')

# 处理文本消息的异步函数
async def translate(update, context):
    """
    处理用户发送的普通文本消息
    update: 包含用户消息的对象
    context: 回调上下文
    """
    # 获取用户发送的文本
    text = update.message.text
    
    # 创建翻译器实例，源语言自动检测，目标语言为中文
    translator = GoogleTranslator(source='auto', target='zh-CN')
    
    try:
        # 尝试翻译文本
        translated_text = translator.translate(text)
        # 发送翻译结果给用户
        await update.message.reply_text(translated_text)
    except Exception as e:
        # 如果翻译过程出错，发送错误信息给用户
        await update.message.reply_text(f"翻译出错：{str(e)}")

def run_bot():
    """
    机器人的主运行函数
    """
    # 创建机器人应用实例
    application = Application.builder().token(my_TOKEN).build()
    
    # 注册命令处理器
    application.add_handler(CommandHandler("start", start))  # 处理 /start 命令
    
    # 注册消息处理器，处理非命令的文本消息
    application.add_handler(MessageHandler(
        filters.TEXT &  # 只处理文本消息
        ~filters.COMMAND,  # 排除命令消息
        translate  # 处理函数
    ))
    
    # Windows 系统需要特殊处理事件循环
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # 启动机器人
    print("机器人启动中...")
    application.run_polling()  # 开始轮询获取更新

# 程序入口点
if __name__ == '__main__':
    try:
        # 运行机器人
        run_bot()
    except Exception as e:
        # 捕获并打印任何运行时错误
        print(f"发生错误: {e}")