from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

- مرحبـاً بـك عزيـزي {}
- فـي بـوت كود تيرمكس$بايروجرام التابع لتيم جوكر سفن اكس

- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس والبايروجرام تم انشـاء هـذا البـوت بواسطـة : @J0KER7x
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("- بدأ استخراج الكود", callback_data="generate")],
        [InlineKeyboardButton(text=" الرجوع للرئيسية ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("- بدأ استخراج الكود", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("- بدأ الاستخراج الكود", callback_data="generate")],
        [InlineKeyboardButton("- قناة السورس", url="https://t.me/J0KER_7x")],
        [
            InlineKeyboardButton("- كيف تستخدمني ?", callback_data="help"),
            InlineKeyboardButton("- حول ", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - حول البوت
/help - لتسوي روحك كلشي متعرف
/start - حتى تشغل البوا
/generate - حتى تبدا بأستخراج البوت
/cancel - لألغاء الاستخراج
/restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
- حـول البـوت . 

- بـوت استخـراج كـود تيرمكـس خـاص بســورس جوكر سفن اكس
- قنـاة السـورس : @J0KER_7x

- المطور : @J0KER7x .

- لغـة البـوت : بـايثـون .
    """
