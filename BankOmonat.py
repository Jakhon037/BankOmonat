from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler

# Bosqichlar
AMOUNT, RATE, PERIOD = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Omonat hisoblash uchun, iltimos, omonat miqdorini kiriting:")
    return AMOUNT

async def get_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['amount'] = float(update.message.text)
    await update.message.reply_text("Yillik foiz stavkasini kiriting (masalan, 20):")
    return RATE

async def get_rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['rate'] = float(update.message.text)
    await update.message.reply_text("Omonat muddati necha yilga?:")
    return PERIOD

async def get_period(update: Update, context: ContextTypes.DEFAULT_TYPE):
    period = float(update.message.text)
    amount = context.user_data['amount']
    rate = context.user_data['rate']

    total_profit = amount * (rate / 100) * period
    final_amount = amount + total_profit

    await update.message.reply_text(
        f"Hisob-kitob natijasi:\n"
        f"Boshlang'ich omonat: {amount}\n"
        f"Yillik foiz: {rate}%\n"
        f"Muddat: {period} yil\n\n"
        f"Umumiy foyda: {total_profit:.2f}\n"
        f"Yakuniy balans: {final_amount:.2f}"
    )
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hisoblash bekor qilindi.")
    return ConversationHandler.END

# Botni ishga tushurish
if name == '__main__':
    import asyncio

    async def main():
        app = ApplicationBuilder().token("BOT_TOKENINGNI_BUYERGA_QO'Y").build()

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_amount)],
                RATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_rate)],
                PERIOD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_period)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        )

        app.add_handler(conv_handler)

        print("Bot ishga tushdi...")
        await app.run_polling()

    asyncio.run(main())from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler

# Bosqichlar
AMOUNT, RATE, PERIOD = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Omonat hisoblash uchun, iltimos, omonat miqdorini kiriting:")
    return AMOUNT

async def get_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['amount'] = float(update.message.text)
    await update.message.reply_text("Yillik foiz stavkasini kiriting (masalan, 20):")
    return RATE

async def get_rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['rate'] = float(update.message.text)
    await update.message.reply_text("Omonat muddati necha yilga?:")
    return PERIOD

async def get_period(update: Update, context: ContextTypes.DEFAULT_TYPE):
    period = float(update.message.text)
    amount = context.user_data['amount']
    rate = context.user_data['rate']

    total_profit = amount * (rate / 100) * period
    final_amount = amount + total_profit

    await update.message.reply_text(
        f"Hisob-kitob natijasi:\n"
        f"Boshlang'ich omonat: {amount}\n"
        f"Yillik foiz: {rate}%\n"
        f"Muddat: {period} yil\n\n"
        f"Umumiy foyda: {total_profit:.2f}\n"
        f"Yakuniy balans: {final_amount:.2f}"
    )
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hisoblash bekor qilindi.")
    return ConversationHandler.END

# Botni ishga tushurish
if name == '__main__':
    import asyncio

    async def main():
        app = ApplicationBuilder().token("BOT_TOKENINGNI_BUYERGA_QO'Y").build()

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_amount)],
                RATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_rate)],
                PERIOD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_period)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        )

        app.add_handler(conv_handler)

        print("Bot ishga tushdi...")
        await app.run_polling()

    asyncio.run(main()