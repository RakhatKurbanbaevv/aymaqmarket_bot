awa it callback.message.answer('Введите ваше имя:')
    await dp.storage.set_data(callback.from_user.id, {'step': 'name'})

@dp.message()@dp.callback_query(lambda c: c.data == 'checkout')
async def checkout(callback: types.CallbackQuery):

async def handle_checkout(message: types.Message):
    data = await dp.storage.get_data(message.from_user.id)
    if not data or 'step' not in data:
        return

    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()

    if data['step'] == 'name':
