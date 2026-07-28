import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# إعدادات تسجيل الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# الأيدي الخاص بك لاستقبال إشعارات الإدارة (شحن/سحب)
ADMIN_ID = 5652303062

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    # رسالة ترحيبية
    welcome_text = (
        f"مرحباً بك يا {user.first_name} في CryptoNoon! 💎\n\n"
        "أبدأ التعدين الآن وقم بدعوة أصدقائك لزيادة سرعتك."
    )
    
    # رابط صفحة الويب (موقعك على جيت هاب أو محلي حالياً)
    # استبدل الرابط أدناه برابط صفحة الويب الخاصة بك على جيت هاب لاحقاً
    web_app_url = "https://your-github-username.github.io/CryptoNoonBot/" 

    keyboard = [
        [InlineKeyboardButton("🚀 فتح منصة التعدين", web_app=WebAppInfo(url=web_app_url))],
        [InlineKeyboardButton("🔗 رابط الإحالة الخاص بك", callback_data="get_ref")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # التحقق من الإحالة
    if context.args:
        referrer_id = context.args[0]
        if str(referrer_id) != str(user.id):
            await context.bot.send_message(
                chat_id=referrer_id,
                text=f"🎉 قام المستخدم {user.first_name} بالدخول عبر رابط الإحالة الخاص بك!"
            )

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "get_ref":
        user_id = query.from_user.id
        ref_link = f"https://t.me/CryptoNoon_bot?start={user_id}"
        await query.message.reply_text(f"🔗 رابط الإحالة الخاص بك:\n{ref_link}")

def main():
    # توكن البوت الخاص بك
    TOKEN = "7729605781:AAFC147t4v-6_kR0T8G2vP4U7Lh3Z8N9K_w" # (تأكد من وضع توكن بوتك الصحيح هنا)
    
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
