# -*- coding: utf-8 -*-
# bot_core.py — ядро бота (aiogram 3.x) без запуска polling/webhook.
# Экспортирует: rt (Router) и set_bot_commands(bot)

import logging
from typing import Optional

from aiogram import F, Router
from aiogram.types import (
    Message, CallbackQuery, BotCommand,
    InlineKeyboardMarkup, InlineKeyboardButton
)

log = logging.getLogger("loi-bot-core")

# ==========================
# РОУТЕР (НЕ Dispatcher!)
# ==========================
rt = Router()

# ==========================
# ТЕКСТЫ/ССЫЛКИ
# ==========================
TEXT_WELCOME = "Привет! 👋 Это бот <b>Legends of Interactions</b>. Выберите раздел:"

# FAQ
TEXT_FAQ_MENU = "❓ <b>FAQ — Часто задаваемые вопросы</b>\nВыберите интересующий вопрос:"

FAQ_Q1 = "С какого возраста можно играть в Игру?"
FAQ_A1 = (
    "👶 <b>С какого возраста можно играть в Игру?</b>\n\n"
    "Играть могут люди практически с любого возраста — главное, чтобы человек мог ходить и держать телефон, "
    "чтобы собирать ресурсы через экран гаджета."
)

FAQ_Q2 = "Можно ли заработать на Игре?"
FAQ_A2 = (
    "💰 <b>Можно ли заработать на Игре?</b>\n\n"
    "Да, в Игре можно заработать всем участникам игрового процесса. Выбери свою роль."
)

FAQ_Q3 = "Сколько можно заработать на Игре?"
FAQ_A3 = (
    "📈 <b>Сколько можно заработать на Игре?</b>\n\n"
    "Со слов разработчиков Игры, каждый участок, где активно играют пользователи, может приносить доход до "
    "<b>10 € в месяц и выше</b>."
)

FAQ_Q4 = "Кто может стать Маркетмейкером (ММ)?"
FAQ_A4 = (
    "🏦 <b>Кто может стать Маркетмейкером (ММ)?</b>\n\n"
    "-."
)

FAQ_Q5 = "Кто может стать Мастером игры (MOG)?"
FAQ_A5 = (
    "👑 <b>Кто может стать Мастером игры (MOG)?</b>\n\n"
    "Мастером игры может стать любой участник, который владеет игровыми участками."
)

FAQ_Q6 = "Как зарабатывают Мастера игры?"
FAQ_A6 = (
    "🧭 <b>Как зарабатывают Мастера игры?</b>\n\n"
    "1. Вы покупаете участки земли в игре на реальной карте — это ваш ключ к миру, где вы можете зарабатывать.\n\n"
    "В игре существует зависимость потенциала дохода от количества и качества участков земли во владении.\n\n"
    "2. Вы получаете право размещать игровые объекты на своих территориях.\n\n"
    "3. Вы получаете процент с каждого взаимодействия, проходящего через вашу территорию. Чем больше активность — тем выше ваш доход.\n\n"
    "4. Вы контролируете рынок ресурсов и рынок крафтинга."
)

FAQ_Q7 = "Как превратить землю в прибыльный актив?"
FAQ_A7 = (
    "🌍 <b>Как превратить землю в прибыльный актив?</b>\n\n"
    "• Выбирайте стратегически важные точки: центры городов, популярные места, ключевые районы — они дорожают быстрее.\n"
    "• Создавайте уникальные игровые механики: чем выше вовлечённость игроков, тем выше ценность вашей территории.\n"
    "• Продавайте доступ к игрокам: бизнесу нужны клиенты, а у вас есть способ приводить их на свою территорию."
)

FAQ_Q8 = "Как купить игровые земельные участки?"
FAQ_A8 = (
    "🛒 <b>Как купить игровые земельные участки?</b>\n\n"
    "Для покупки участков нужна монета <b>НЕХА</b>. Её можно приобрести у Мастеров игры (МОГ) или у Маркетмейкеров (ММ) на любую сумму.\n\n"
    "Также можно купить <b>7ПИН</b> или <b>9ПИН</b> токены и начать фармить монеты самостоятельно.\n\n"
    "👉 Для этого откройте раздел <b>Личная консультация</b>."
)

# О компании
TEXT_COMPANY_MENU = "🏢 <b>О компании</b>\nВыберите подраздел:"
TEXT_COMPANY_HISTORY = (
    "📜 <b>О компании</b>\n\n"
    "Renaissance Space Labs — компания, создающая будущее Web 3.0\n"
    "На сегодняшний день Renaissance Space Labs — это мощный технологический холдинг, "
    "который разрабатывает и продвигает инновационные продукты и решения на основе Web 3.0.\n"
    "Компания уже более 15 лет успешно работает на международном рынке и за это время прошла впечатляющий путь: "
    "от небольшого интернет-магазина до современного бизнеса с капитализацией 60 миллиардов долларов. "
    "Это говорит о нашей финансовой устойчивости, надёжности и доверии инвесторов по всему миру.\n\n"
    "<b>Уникальная модель управления</b>\n"
    "Renaissance Space Labs использует гибридную структуру управления, сочетая традиционные финансовые инструменты "
    "и новейшие технологии блокчейна. Компания работает одновременно в реальном мире и в цифровой среде:\n"
    " • Классическая модель — акции компании;\n"
    " • Современная модель — DAO и управляющие криптомонеты.\n\n"
    "<b>История развития компании</b>\n"
    " • 2010 — старт в ОАЭ: интернет-магазин инвестиционных золотых слитков.\n"
    " • 2015 — ребрендинг, переход под юрисдикцию Швейцарии и запуск собственного бренда золота.\n"
    " • 2017 — выпуск и регистрация собственных ценных бумаг.\n"
    " • 2019 — запуск собственной платформы и приватного блокчейна.\n"
    " • 2020 — рост капитализации до 1 млрд $ и статус «единорога».\n"
    " • 2021 — запуск бизнес-метавселенной и криптовалюты GigoCoin.\n"
    " • 2022–2023 — создание DAO, выпуск Микоина, NFT, AI-разработки.\n"
    " • 2024 — переход на публичный блокчейн Netsbo.io.\n"
    " • 2025 — подготовка к запуску игры Legends of Interaction и маркетплейса услуг Интератум.\n\n"
    "<b>Инновации и технологии</b>\n"
    " • Блокчейн Netsbo — высокая скорость, надёжность и низкие комиссии;\n"
    " • DAO-сообщество;\n"
    " • Метавселенная с токенами и NFT;\n"
    " • GameFi и AR;\n"
    " • Искусственный интеллект.\n\n"
    "<b>Возможности для участников</b>\n"
    " • INT — монета маркетплейса услуг «Интератум»;\n"
    " • GameGos Coin — игровая монета;\n"
    " • Hexa Coin — покупка земель в метавселенной;\n"
    " • Dominion Coin — реклама в цифровом мире;\n"
    " • NFT Gallery — коллекционные токены.\n\n"
    "<b>Почему выбирают нас</b>\n"
    " • 60 млрд $ капитал;\n"
    " • 15+ лет опыта;\n"
    " • Инновационные продукты: Netsbo.io, DAO, AI, GameFi, метавселенная;\n"
    " • Прозрачная структура;\n"
    " • Юрисдикция Сейшел.\n\n"
    "<b>Заключение</b>\n"
    "История Renaissance Space Labs — доказательство того, что смелые идеи и технологии меняют мир. "
    "Мы знаем, куда движемся, и приглашаем вас стать частью будущего Web 3.0."
)
VIDEO_COMPANY_HISTORY: Optional[str] = "BAACAgEAAxkBAANgaM_WzYCmDD_mR7h5HDzq2eiUeOAAAnEFAAIeXoBGRb-PzWfZFJw2BA"
TEXT_COMPANY_GPT = "🤖 <b>Чат GPT о компании</b>"
VIDEO_COMPANY_GPT: Optional[str] = "BAACAgEAAxkBAAMZaM_AIdfrwa-TRsm-zY7fFMp9lYsAAssFAAIeXnhG52OiRs40E6E2BA"

# Об игре
TEXT_GAME_MENU = "🎮 <b>Об игре Legends of Interactions</b>\nВыберите подраздел:"
TEXT_GAME_MECH = (
    "🎮 <b>Механика игры</b>\n\n"
    "В чём суть игры? 🤔\n"
    "Весь земной шар будет поделен на участки (≈259 м² каждый).\n\n"
    "📱 Игроки будут перемещаться со смартфонами в реальном мире и через камеру "
    "взаимодействовать с игровой вселенной:\n"
    " • искать и собирать ресурсы и предметы;\n"
    " • взаимодействовать с другими игроками в различных сценариях.\n\n"
    "📌 <b>Факты об игре и экосистеме</b>\n"
    " • Игра для мобильных устройств;\n"
    " • Уникальные игровые сценарии;\n"
    " • Интеграция с блокчейном;\n"
    " • Все ресурсы и объекты можно переносить из игры в блокчейн и обратно;\n"
    " • Маркетмейкеры получают специальные ресурсы прямо в блокчейне;\n"
    " • Продажа и обмен ресурсов между игроками напрямую или через Маркетплейс.\n\n"
    "✨ <b>Наша игра — бесплатная!</b>\n"
    "И она будет использовать дополненную реальность (AR)."
)
VIDEO_GAME_MECH: Optional[str] = "BAACAgEAAxkBAAMVaM_AFls3daZawqd512IDeJJh4kIAAskFAAIeXnhGXvONc7G6azE2BA"

TEXT_GAME_ADV = (
    "🚀 <b>Преимущества стартапа</b>\n\n"
    "Покупка активов на предстарте, ещё до выхода компании на биржу, "
    "является одним из самых перспективных вариантов для инвесторов.\n\n"
    "✨ Такая стратегия позволяет:\n"
    " • получить значительные преимущества;\n"
    " • зайти в проект по самым низким ценам;\n"
    " • максимизировать свою будущую прибыль.\n\n"
    "🚀 <b>Предстарт — шанс быть первым!</b>"
)
VIDEO_GAME_ADV: Optional[str] = "BAACAgEAAxkBAAMRaM-_4DxGybOGNE12aOzB7bGaOloAAscFAAIeXnhGrOaRaRRwpX82BA"

TEXT_GAME_MASTERS = (
    "🧙 <b>Станьте Мастером Игры!</b> 🎮\n\n"
    "Чтобы управлять своей цифровой империей, вам нужна <b>земля</b>! 🏞 "
    "Каждый участок — это не просто актив, а возможность зарабатывать, привлекая внимание игроков и бизнесов.\n\n"
    "📐 <b>Характеристики участка</b>\n"
    " • Шестиугольник со сторонами 10 м;\n"
    " • Площадь ≈ 260 м²;\n"
    " • Стоимость: от 300 до 600 рублей.\n\n"
    "📈 <b>Рост стоимости</b>\n"
    " • Пустые участки дорожают каждый месяц на 10%;\n"
    " • Развитые земли растут в цене в разы.\n\n"
    "💶 <b>Доходность</b>\n"
    "Каждый участок, где активно играют пользователи, приносит от 10 € в месяц.\n"
    " • 10 участков = ~100 € ежемесячно;\n"
    " • 100 участков = ~1000 € ежемесячно.\n\n"
    "Считайте сами, сколько вы хотите зарабатывать! 💰"
)

# ==========================
# КЛАВИАТУРЫ
# ==========================
def kb_main() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="О компании", callback_data="company")],
        [InlineKeyboardButton(text="Об игре Legends of Interactions", callback_data="game")],
        [InlineKeyboardButton(text="FAQ", callback_data="faq")],
        [InlineKeyboardButton(text="Перейти в чат игры", url="https://t.me/newGameLegendsofinteractions")],
        [InlineKeyboardButton(text="Личная консультация", callback_data="consult")],
    ])

def kb_back_only() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ В главное меню", callback_data="back_main")]
    ])

def kb_company_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="История компании", callback_data="company_history")],
        [InlineKeyboardButton(text="Чат GPT о компании", callback_data="company_gpt")],
        [InlineKeyboardButton(text="⬅️ В главное меню", callback_data="back_main")],
    ])

def kb_game_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Механика игры", callback_data="game_mechanics")],
        [InlineKeyboardButton(text="Преимущества стартапа", callback_data="game_advantages")],
        [InlineKeyboardButton(text="Мастера Игры", callback_data="game_masters")],
        [InlineKeyboardButton(text="Зарегистрироваться", callback_data="game_register")],
        [InlineKeyboardButton(text="⬅️ В главное меню", callback_data="back_main")],
    ])

def kb_register() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Зарегистрироваться", url="https://loi-masters.com?referral=671220287519")],
        [InlineKeyboardButton(text="Официальный сайт", url="https://legendsofinteractions.com/ru/")],
        [InlineKeyboardButton(text="⬅️ В главное меню", callback_data="back_main")],
    ])

def kb_faq_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=FAQ_Q1, callback_data="faq_q1")],
        [InlineKeyboardButton(text=FAQ_Q2, callback_data="faq_q2")],
        [InlineKeyboardButton(text=FAQ_Q3, callback_data="faq_q3")],
        [InlineKeyboardButton(text=FAQ_Q4, callback_data="faq_q4")],
        [InlineKeyboardButton(text=FAQ_Q5, callback_data="faq_q5")],
        [InlineKeyboardButton(text=FAQ_Q6, callback_data="faq_q6")],
        [InlineKeyboardButton(text=FAQ_Q7, callback_data="faq_q7")],
        [InlineKeyboardButton(text=FAQ_Q8, callback_data="faq_q8")],
        [InlineKeyboardButton(text="⬅️ В главное меню", callback_data="back_main")],
    ])

def kb_faq_back() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад в FAQ", callback_data="faq")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="back_main")],
    ])

# ==========================
# КОМАНДЫ БОТА (без global bot)
# ==========================
async def set_bot_commands(bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="menu", description="Главное меню"),
    ])

# ==========================
# ХЕНДЛЕРЫ (все на rt)
# ==========================
@rt.message(F.text.in_({"/start", "start"}))
async def on_start_text(message: Message):
    # Команды ещё можно поставить на старте webhook/polling через set_bot_commands(bot)
    await message.answer(TEXT_WELCOME, reply_markup=kb_main())

@rt.message(F.text == "/menu")
async def on_menu(message: Message):
    await message.answer(TEXT_WELCOME, reply_markup=kb_main())

# Главное меню
@rt.callback_query(F.data == "back_main")
async def cb_back_main(cb: CallbackQuery):
    try:
        await cb.message.edit_text(TEXT_WELCOME, reply_markup=kb_main())
    except Exception:
        await cb.message.answer(TEXT_WELCOME, reply_markup=kb_main())
    finally:
        await cb.answer()

@rt.callback_query(F.data == "company")
async def cb_company(cb: CallbackQuery):
    await cb.message.answer(TEXT_COMPANY_MENU, reply_markup=kb_company_menu())
    await cb.answer()

@rt.callback_query(F.data == "game")
async def cb_game(cb: CallbackQuery):
    await cb.message.answer(TEXT_GAME_MENU, reply_markup=kb_game_menu())
    await cb.answer()

# FAQ
@rt.callback_query(F.data == "faq")
async def cb_faq(cb: CallbackQuery):
    await cb.message.answer(TEXT_FAQ_MENU, reply_markup=kb_faq_menu())
    await cb.answer()

@rt.callback_query(F.data == "faq_q1")
async def cb_faq_q1(cb: CallbackQuery):
    await cb.message.answer(FAQ_A1, reply_markup=kb_faq_back()); await cb.answer()

@rt.callback_query(F.data == "faq_q2")
async def cb_faq_q2(cb: CallbackQuery):
    await cb.message.answer(FAQ_A2, reply_markup=kb_faq_back()); await cb.answer()

@rt.callback_query(F.data == "faq_q3")
async def cb_faq_q3(cb: CallbackQuery):
    await cb.message.answer(FAQ_A3, reply_markup=kb_faq_back()); await cb.answer()

@rt.callback_query(F.data == "faq_q4")
async def cb_faq_q4(cb: CallbackQuery):
    await cb.message.answer(FAQ_A4, reply_markup=kb_faq_back()); await cb.answer()

@rt.callback_query(F.data == "faq_q5")
async def cb_faq_q5(cb: CallbackQuery):
    await cb.message.answer(FAQ_A5, reply_markup=kb_faq_back()); await cb.answer()

@rt.callback_query(F.data == "faq_q6")
async def cb_faq_q6(cb: CallbackQuery):
    await cb.message.answer(FAQ_A6, reply_markup=kb_faq_back()); await cb.answer()

@rt.callback_query(F.data == "faq_q7")
async def cb_faq_q7(cb: CallbackQuery):
    await cb.message.answer(FAQ_A7, reply_markup=kb_faq_back()); await cb.answer()

@rt.callback_query(F.data == "faq_q8")
async def cb_faq_q8(cb: CallbackQuery):
    await cb.message.answer(FAQ_A8, reply_markup=kb_faq_back()); await cb.answer()

# Личная консультация (уведомление админу через cb.bot)
ADMIN_ID = 744828056  # замени на свой ID

@rt.callback_query(F.data == "consult")
async def cb_consult(cb: CallbackQuery):
    user = cb.from_user
    await cb.message.answer("🗣 Спасибо! С вами скоро свяжутся."); await cb.answer()
    try:
        tg_link = f"@{user.username}" if user.username else f"tg://user?id={user.id}"
        text = f"🔔 Пользователь {tg_link} запросил консультацию."
        await cb.bot.send_message(ADMIN_ID, text)
    except Exception as e:
        log.warning(f"Не удалось отправить уведомление админу: {e}")

# О компании
@rt.callback_query(F.data == "company_history")
async def cb_company_history(cb: CallbackQuery):
    await cb.message.answer(TEXT_COMPANY_HISTORY, reply_markup=kb_back_only())
    if VIDEO_COMPANY_HISTORY:
        try:
            await cb.message.answer_video(video=VIDEO_COMPANY_HISTORY)
        except Exception as e:
            log.warning(f"Не удалось отправить видео: {e}")
    await cb.answer()

@rt.callback_query(F.data == "company_gpt")
async def cb_company_gpt(cb: CallbackQuery):
    await cb.message.answer(TEXT_COMPANY_GPT, reply_markup=kb_back_only())
    if VIDEO_COMPANY_GPT:
        try:
            await cb.message.answer_video(video=VIDEO_COMPANY_GPT)
        except Exception as e:
            log.warning(f"Не удалось отправить видео: {e}")
    await cb.answer()

# Об игре
@rt.callback_query(F.data == "game_mechanics")
async def cb_game_mechanics(cb: CallbackQuery):
    await cb.message.answer(TEXT_GAME_MECH, reply_markup=kb_back_only())
    if VIDEO_GAME_MECH:
        try:
            await cb.message.answer_video(video=VIDEO_GAME_MECH)
        except Exception as e:
            log.warning(f"Не удалось отправить видео: {e}")
    await cb.answer()

@rt.callback_query(F.data == "game_advantages")
async def cb_game_advantages(cb: CallbackQuery):
    await cb.message.answer(TEXT_GAME_ADV, reply_markup=kb_back_only())
    if VIDEO_GAME_ADV:
        try:
            await cb.message.answer_video(video=VIDEO_GAME_ADV)
        except Exception as e:
            log.warning(f"Не удалось отправить видео: {e}")
    await cb.answer()

@rt.callback_query(F.data == "game_masters")
async def cb_game_masters(cb: CallbackQuery):
    await cb.message.answer(TEXT_GAME_MASTERS, reply_markup=kb_back_only()); await cb.answer()

@rt.callback_query(F.data == "game_register")
async def cb_game_register(cb: CallbackQuery):
    await cb.message.answer("📝 <b>Регистрация и сайт</b>:", reply_markup=(
        InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Зарегистрироваться", url="https://loi-masters.com?referral=671220287519")],
            [InlineKeyboardButton(text="Официальный сайт", url="https://legendsofinteractions.com/ru/")],
            [InlineKeyboardButton(text="⬅️ В главное меню", callback_data="back_main")],
        ])
    ))
    await cb.answer()

# Получение file_id видео
@rt.message(F.video)
async def get_video_id(message: Message):
    await message.answer(f"file_id этого видео:\n{message.video.file_id}")

# Фоллбек
@rt.message()
async def fallback(message: Message):
    await message.answer("Нажми команду /menu, чтобы открыть главное меню.")
