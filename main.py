import os
import telebot
from PIL import Image, ImageDraw

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

def generate_math_image(problem, result):
    img = Image.new('RGB', (700, 400), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.text((30, 40), "--- Math Solution ---", fill=(0, 102, 204))
    draw.text((30, 100), f"Question: {problem}", fill=(0, 0, 0))
    draw.text((30, 160), f"Answer   : {result}", fill=(34, 139, 34))
    draw.text((30, 240), "Steps:", fill=(0, 0, 0))
    draw.text((30, 280), f"1. Expression = {problem}", fill=(100, 100, 100))
    draw.text((30, 320), f"2. Final Value = {result}", fill=(100, 100, 100))
    
    img_path = "math_solution.png"
    img.save(img_path)
    return img_path

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ආයුබෝවන්! මට ගණිත ගැටලුවක් එවන්න (උදා: 25 * 4 + 10). මම එය විසඳා රූපයක් සාදා එවන්නම්.")

@bot.message_handler(func=lambda message: True)
def solve_math(message):
    text = message.text.strip()
    try:
        result = eval(text)
        img_path = generate_math_image(text, result)
        with open(img_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=f"විසඳුම: {result}")
    except Exception:
        bot.reply_to(message, "කණගාටුයි, නිවැරදි ගණිතමය ප්‍රකාශනයක් එවන්න.")

bot.infinity_polling()
