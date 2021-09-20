import telebot
from telebot import types

bot = telebot.TeleBot('1212395833:AAErAMhnQ_DDC4DmbxweBsuBi_R-q2F9p0U')

@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Kran Saytlar ⛏️', callback_data='kransaytlar')
    item = types.InlineKeyboardButton('🤖 Botlar', callback_data='botlar')
    item2 = types.InlineKeyboardButton("👨‍💻 Admin & 📞Bog'lanish", callback_data='admin')
    item3 = types.InlineKeyboardButton('🧰 Kashalok Ochish!', callback_data='kashalok ochish')
    item4 = types.InlineKeyboardButton('🤖 CryptoBotlar!', callback_data='cryptobotlar1')
    item5 = types.InlineKeyboardButton('📲 Android dasturlar', callback_data= 'androidapps')
    markup.add(item1, item3, item, item4, item2, item5)
    
    mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
    
    bot.send_message(message.chat.id,  f'''<b> 🌠 Assalomu Aleykum!, {mention}! \n\n🙋 Internet orqali pul ishlashingiz mumkin bo'lgan barcha ma'lumotlar shu yerda...</b> \n\n\n<em><u>Kerakli tugmalardan birini tanlang!</u> \n👇👇👇👇👇👇👇👇👇</em>''',  parse_mode= 'HTML', reply_markup=markup)
    
    
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
      if call.data == 'botlar':
        botlarbuttons = types.InlineKeyboardMarkup()
        botlarbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
        botlarbuttons.add(botlarbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= ''' <b>🔥 Siz ushbu botlar orqali Rubl ishlaysiz!!!\n❗Botlar sinalgan va 100% toʻlaydi...✅✅\n
👉 https://t.me/ZezikBot?start=427322790  (#zezikbot)
👉 https://t.me/Vipserfbot?start=427322790   (#vipserfbot)    
👉 https://t.me/TegMoRobot?start=427322790  (#tegmorobot)
👉 https://t.me/Toptgmoney_bot?start=427322790
(#toptgmoney)
👉 https://t.me/tgprime_bot?start=427322790 (#tgprime) 
👉 https://t.me/CorpBisbot_newbot?start=427322790 (#corpbisbot)
👉 https://t.me/money_eazy_bot?start=427322790 (#preazymoney)
👉 https://t.me/ProPrRobot?start=427322790 (#proprrobot)
👉 https://t.me/LD_ibot?start=427322790 
👉 https://t.me/Flibasta_Bot?start=427322790
👉 https://t.me/RocketK07_bot?start=427322790

#bots

•••  Tarqalamiz...🤟
👉 @millyardchatv</b>''', parse_mode='HTML', reply_markup=botlarbuttons)
             
      if call.data == 'kransaytlar':
        buttons = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("BTC kranlar ▶️", callback_data="btckranlar")
        back1 = types.InlineKeyboardButton('LTC kranlar ▶️', callback_data='ltckranlar')
        back2 = types.InlineKeyboardButton('DOGE kranlar ▶️', callback_data='dogekranlar')
        back3 =types.InlineKeyboardButton('Faucet Pay kranlar ▶️', callback_data='faucetpaykranlar')
        backbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
        buttons.add(back, back1, back2, back3, backbut)
            
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '''<b><u>🤑 Mana o'sha siz izlagan eng yaxshi kriptovalyuta kran saytlar!</u></b>\n<em>Bu yerda joylashgan barcha kran saytlar 100% to'laydi...✅✅✅</em>  
  \n''', parse_mode='HTML', reply_markup=buttons)
         
      elif call.data == 'admin':
              adminbuttons = types.InlineKeyboardMarkup(row_width=1)
              backbutton1 = types.InlineKeyboardButton(text="🏠 Bosh Sahifa", callback_data="mainmenu")
              adminbuttons.add(backbutton1)
              bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text='''☑️ <b>Sahifalarimiz:</b>

📢 <b>Telegram kanal:</b> 👉 @millyardchatv
👥 <b>Guruhimiz:</b> 👉 @millyardchatvchat
👁 <b>Admin:</b> 👉 @millyardcha
🗣 <b>Spamlar uchun:</b> 👉 @millyardchatv_bot ''', parse_mode='HTML', reply_markup=adminbuttons)
             
             
      elif call.data == 'btckranlar':
        btcbuttons = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text='◀️ Orqaga', callback_data='orqaga')
        backbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
        btcbuttons.add(but, backbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '''<em>🙋‍♂ Ushbu kran saytlar orqali siz BTC kriptovalyutasini ishlab olasiz! Hozirgi kunda eng faol saytlar!</em> 
    \n<b>Saytlar 100% to'laydi..✅✅✅

1⃣ FreeBitcoin (Har soatda 0.05 BTC)
✏️ Sayt silkasi: https://bit.ly/36lPOMg
🎬 Sayt haqida videorolik: https://youtu.be/mujhX0VvvKM

2⃣ BtcMaker (Har soatda 0.05)
 ✏️ Sayt silkasi: https://bit.ly/2Sbu7pV
📽️ Sayt haqida to'liq videorolik: https://youtu.be/FvXccuSz8Ng

3⃣ BitShark (Har soatda 0.1 BTC)
✏️ Sayt silkasi: https://bit.ly/30nYVYR
🎬 Sayt haqida videorolik: https://youtu.be/F9CaiWDdLVo

4⃣ BitKing (Har soatda 0.001 BTC)
✏️ Sayt Silkasi: https://bit.ly/2Jdy3Wf
🎬 Sayt haqida videorolik: https://youtu.be/gdZm3Dgiaas

5⃣ OurBitcoin (Har soatda 0.01 BTC)
✏️ Sayt manzili: https://bit.ly/3rCGpIE
🎬 Sayt haqida videorolik: https://youtu.be/918ExiODr_o

6⃣ ✏️ Sayt silkasi: https://bit.ly/3fHTnA5
🎬 Sayt haqida videorolik: https://youtu.be/4y3m16qO6BY

•••  Tarqalamiz...🤟
👉 @millyardchatv</b>
  ''', parse_mode='HTML', reply_markup=btcbuttons)
      
      elif call.data == 'orqaga':
        buttons = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("BTC kranlar ▶️", callback_data="btckranlar")
        back1 = types.InlineKeyboardButton('LTC kranlar ▶️', callback_data='ltckranlar')
        back2 = types.InlineKeyboardButton('DOGE kranlar ▶️', callback_data='dogekranlar')
        back3 =types.InlineKeyboardButton('Faucet Pay kranlar ▶️', callback_data='faucetpaykranlar')
        backbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
        buttons.add(back, back1, back2, back3, backbut)
            
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '''<b><u>🤑 Mana o'sha siz izlagan eng yaxshi kriptovalyuta kran saytlar!</u></b>\n<em>Bu yerda joylashgan barcha kran saytlar 100% to'laydi...✅✅✅</em>  
  \n''', parse_mode='HTML', reply_markup=buttons)
        
      elif call.data == 'mainmenu':
              markup1 = types.InlineKeyboardMarkup(row_width=2)
              item1 = types.InlineKeyboardButton('Kran Saytlar ⛏️', callback_data='kransaytlar')
              item = types.InlineKeyboardButton('🤖 Botlar', callback_data='botlar')
              item2 = types.InlineKeyboardButton("👨‍💻 Admin & 📞Bog'lanish", callback_data='admin')
              item3 = types.InlineKeyboardButton('🧰 Kashalok Ochish!', callback_data='kashalok ochish')
              item4 = types.InlineKeyboardButton('🤖 CryptoBotlar!', callback_data='cryptobotlar1')
              item5 = types.InlineKeyboardButton('📲 Android dasturlar', callback_data= 'androidapps')
              markup1.add(item1, item3, item, item4, item2, item5)
    
              bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text='''<b> 🌠 Assalomu Aleykum! \n\n🙋 Internet orqali pul ishlashingiz mumkin bo'lgan barcha ma'lumotlar shu yerda...</b> \n\n\n<em><u>Kerakli tugmalardan birini tanlang!</u> \n👇👇👇👇👇👇👇👇👇</em>''',  parse_mode= 'HTML', reply_markup=markup1)
        
      elif call.data == 'cryptobotlar1':
        cryptobuttons = types.InlineKeyboardMarkup()
        botlarbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
        cryptobuttons.add(botlarbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '''<b><em>🔥 Ushbu botlar orqali siz KRIPTOVALYUTA ishlaysiz!
Va ushbu botlarda VAQTINCHALIK saqlasangiz bo'ladi!</em> 

Botlar 100% to'laydi...✅✅✅

👉 https://t.me/Litecoin_click_bot?start=WioC
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3327) (LTC)\n
👉 https://t.me/BCH_clickbot?start=vVLT (Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3485) (BCH)\n
👉 https://t.me/Dogecoin_click_bot?start=G6N9
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3236 (Doge)\n
👉 https://t.me/Zcash_click_bot?start=6YwA
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3238) (Zcash)\n
👉 https://t.me/BitcoinClick_bot?start=PHWe (BTC)\n
👉 https://t.me/tron_clickearn_bot?start=427322790 ( TRX )</b>
''', parse_mode='HTML', reply_markup=cryptobuttons)
        
      elif call.data == 'kashalok ochish':
        kashalokbuttons = types.InlineKeyboardMarkup()
        kashalokbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
        kashalokbuttons.add(kashalokbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '''☺️<b> Sizga kerakli bo'luvchi online kashaloklar 👇👇👇👇👇👇

1️⃣ 🅿️ Payeer kashalok ochish: https://youtu.be/DmHB0idrOu4
2️⃣ 🛄 Faucet Pay Kashalok Ochish: https://youtu.be/YAZIfynHhds
3️⃣ 🤑 Coinbase kashalok ochish:  https://youtu.be/IcVyfzswm8U
4️⃣ 🔑Fkwallet ochish: https://youtu.be/PinrYupggdI
          \n\n•••  Tarqalamiz...🤟
          👉 @millyardchatv</b>''', parse_mode='HTML', reply_markup=kashalokbuttons)

      elif call.data == 'ltckranlar':
        ltcbuttons = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text='◀️ Orqaga', callback_data='orqaga')
        backbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
        ltcbuttons.add(but, backbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''<em>🔥 Ushbu kran saytlar orqali siz LTC kriptovalyutasini SARMOYASIZ ishlab olasiz! Eng Aktual saytlar!</em>

<b><u>Saytlar 100% to'laydi...✅✅✅</u>

1⃣ Free - Litecoin ( Har soatda 2 LTC)
✏️ Sayt silkasi: https://bit.ly/34eAmyv
🎬 Sayt haqida videorolik: https://youtu.be/5fttImJt9ac

2⃣ LitePick (Har soatda 0.02 LTC)
✏️ Sayt silkasi: https://bit.ly/2S57kiq
🎬 Sayt haqida videorolik: https://youtu.be/ioA2qY32YpM

3⃣ Litking (Har soatda 0.2 LTC)
✏️ Sayt silkasi: https://bit.ly/38GpCML
🎬 Sayt haqida videorolik: https://youtu.be/zx_7inCHn1Y

•••  Tarqalamiz...🤟
👉 @millyardchatv
</b>''', parse_mode='HTML', reply_markup=ltcbuttons)
          
      elif call.data == 'dogekranlar':
        dogebuttons = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text='◀️ Orqaga', callback_data='orqaga')
        backbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
        dogebuttons.add(but, backbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''<b><u>😜 Eng Aktual Dogecoin kranlar!</u></b>

<b>Saytlar 100% to'laydi...✅✅✅

1⃣ Free Dogecoin (Har soatda 1000 Doge)
✏️ Sayt manzili: https://bit.ly/2UVGknE
🎬 Sayt haqida videorolik: https://youtu.be/5nj_etNFNQg

2⃣ DogePick (Har soatda 10 Doge)
✏️  Sayt silkasi: https://bit.ly/3jACaLI
🎬 Sayt haqida videorolik: https://youtu.be/_rAlvNodXG4

3⃣ Free Dogecoin
✏️ Sayt silkasi: https://bit.ly/3rESzzc
🎬 Sayt haqida videorolik: https://youtu.be/2d24vsUaBAE

4⃣ Ad Doge (Har soatda 500 Doge)
✏️ Sayt silkasi: http://bit.ly/3pbP8i4
🎬 Sayt haqida videorolik: https://youtu.be/I_KTvgMYWvg

•••  Tarqalamiz...🤟
👉 @millyardchatv
</b>''', parse_mode='HTML', reply_markup=dogebuttons)
        
      elif call.data == 'androidapps':
        androidbuttons = types.InlineKeyboardMarkup()
        botlarbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
        androidbuttons.add(botlarbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''<b><u>🏃‍♂ Kriptovalyuta ishlash mumkin bo'lgan android dasturlar!</u></b>

<b>Dasturlar 100% to'laydi...✅✅✅

1⃣ Free Litecoin App
✏️ Dastur manzili: https://bitcoinaliens.com/?ref=803266&game=8&pf=2
📽️ Dastur orqali ko'proq pul ishlash: https://youtu.be/7ZeRscFjq10
📽️ Telegram orqali kochirib olish: https://t.me/millyardchatv/2515
🤖 LTC Click Botga chiqarib olish 👉 https://t.me/millyardchatv/4166
🅿️ Payeer ga chiqarib olish: https://youtu.be/voTt-FRkZbI

2⃣ Free Bitcoin Cash App
✏️ https://bitcoinaliens.com/?ref=803266&game=7&pf=2
📽️ Dastur orqali ko'proq pul ishlash: https://youtu.be/tuL3Rx2gPSM
📽️ Telegram orqali kochirib olish: https://t.me/millyardchatv/2532

3⃣ Free Litecoin app
✏️ Dastur manzili: https://bit.ly/3yQphS4
⚽ Referal Code: millyardcha
🎬 Dastur haqida videorolik: https://youtu.be/bmTHgZ9Mbbs

4⃣ Free Bitcoin Cash app
✏️ Dastur manzili: https://bit.ly/3BdMj7k
⚽ Referal Code: millyardcha
🎬 Dastur haqida videorolik: https://youtu.be/XGBcr8pvgMc

5⃣ Crypto Fast app
✏️ Dastur silkasi: https://bit.ly/3tVaEKj
🎬 Dastur haqida videorolik: https://youtu.be/4FsTYCEXprU

6⃣ Pop Stellar
✏️ Dastur silkasi: https://bit.ly/3aDKEMP
🎬 Dastur haqida videorolik: https://youtu.be/vUbu6l1daUc

7⃣ MiniLitecoin
✏️ Dastur silkasi: "Mini Games - Free Litecoin"
https://bit.ly/3ihGYBh
Referal Code: A93595
🎬 Dastur haqida videorolik: https://youtu.be/3mHS3XcSpZY

8⃣ CryptoRize 
✏️Dastur manzili:  https://bit.ly/30lveaU 
Referal Code: L5YS6J
📽️ Dastur haqida to'liq videorolik: https://youtu.be/tLnk4nn95pE
🎬 Dastur haqida videorolik: https://youtu.be/obgO5XHFmrM

9⃣ Vktarget
✏️ Sayt silkasi: https://bit.ly/36qnfxf
📽Sayt haqida videorolik:  https://youtu.be/qN_VIXZDiEk

1⃣0⃣ CryptoTab Browser
✏️ Dastur manzili: https://bit.ly/3sHXEc0
📽 Dastur haqida videorolik: https://youtu.be/Kgl8WG-hypM

•••  Tarqalamiz...🤟
👉 @millyardchatv
</b>''', parse_mode='HTML', reply_markup=androidbuttons)
      
      elif call.data == 'faucetpaykranlar':
        fpbuttons = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text='◀️ Orqaga', callback_data='orqaga')
        backbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
        fpbuttons.add(but, backbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''<em>❗️ Ushbu saytlar Faucet Pay kashalogiga srazi to'laydi...✅✅✅</em>

<b>1⃣ ClaimCliks LTC
✏️ Sayt silkasi: https://bit.ly/2QbL0Tw
🎬 Sayt haqida videorolik: https://youtu.be/lyl2zEo5SBw

2⃣ClaimCliks DOGE
✏️ Sayt silkasi: https://bit.ly/2OLBXbG
🎬Sayt haqida videorolik: https://youtu.be/b3_cyAckf2I

3⃣ ClaimCliks TRX
✏️ Sayt silkasi: https://bit.ly/3diQPaR
🎬 Sayt haqida videorolik:
https://youtu.be/Qa4st7lh5Sc

4⃣ ClaimFreeCoins LTC
✏️ Sayt silkasi: http://bit.ly/2M4xEqn
🎬 Sayt haqida videorolik: https://youtu.be/KLn4PoRewtY

6⃣ ClaimFreeCoins DOGE
✏️ Sayt silkasi: https://bit.ly/2NP6yVb
🎬 Sayt haqida videorolik: https://youtu.be/oF3MqRbfqxQ

7⃣ IqFaucet
✏️ Sayt manzili: https://bit.ly/3xjiLlN
🎬 Sayt haqida videorolik: https://youtu.be/OrWqGdATBOs

8⃣ SoonDogeCoin
✏️ Sayt manzili: https://bit.ly/3jwCRFs
🎬 Sayt haqida videorolik: https://youtu.be/Q8jtOldtmP4

9️⃣ ClaimFreeCoins TRX
✏️ Sayt silkasi: https://bit.ly/3i1Uvjp
🎬 Sayt haqida videorolik: https://youtu.be/pwl3X3J__zw</b>

•••  Tarqalamiz...🤟
👉 @millyardchatv''', parse_mode='HTML', reply_markup=fpbuttons)
        
@bot.message_handler(commands=['help', 'yordam'])
def button(message):
  bot.send_message(message.chat.id,  '''<b> 🌠 😄 Men siz uchun bir nechta foydali ma'lumotlarni taklif qilaman!</b><em>
-- Kran saytlar /kran buyrug'ida! yoki shunchaki <code>kran</code> deb yozing! ⛏
-- Botlar /bots buyrug'ida yoki <code>botlar</code> deb yozing!
-- Kashaloklar ochish /wallet buyrug'ida yoki <code>wallet</code> deb yozing!
-- Cryptobotlar /cryptobots buyrug'ida yoki <code>criptobotlar</code> deb yozing!
-- Mobil dasturlar /mobilapps buyrug'ida yoki <code>mobilapps</code> deb yozing!🤖</em>''',  parse_mode= 'HTML')      

@bot.message_handler(commands=['kran'])
def button(message):
  kranbuttons = types.InlineKeyboardMarkup(row_width=1)
  back = types.InlineKeyboardButton("BTC kranlar ▶️", callback_data="btckranlar")
  back1 = types.InlineKeyboardButton('LTC kranlar ▶️', callback_data='ltckranlar')
  back2 = types.InlineKeyboardButton('DOGE kranlar ▶️', callback_data='dogekranlar')
  back3 =types.InlineKeyboardButton('Faucet Pay kranlar ▶️', callback_data='faucetpaykranlar')
  backbut = types.InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data='mainmenu')
  kranbuttons.add(back, back1, back2, back3, backbut)
          
  bot.send_message(message.chat.id, text= '''<b><u>🤑 Mana o'sha siz izlagan eng yaxshi kriptovalyuta kran saytlar!</u></b>\n<em>Bu yerda joylashgan barcha kran saytlar 100% to'laydi...✅✅✅</em>  
  \n''', parse_mode='HTML', reply_markup=kranbuttons)
      
@bot.message_handler(commands=['wallet'])
def button(message):
  bot.send_message(message.chat.id, '''☺️<b> Sizga kerakli bo'luvchi online kashaloklar 👇👇👇👇👇👇

1️⃣ 🅿️ Payeer kashalok ochish: https://youtu.be/DmHB0idrOu4

2️⃣ 🛄 Faucet Pay Kashalok Ochish: https://youtu.be/YAZIfynHhds

3️⃣ 🤑 Coinbase kashalok ochish:  https://youtu.be/IcVyfzswm8U

4️⃣ 🔑Fkwallet ochish: https://youtu.be/PinrYupggdI

#foydali
          \n\n•••  Tarqalamiz...🤟
          👉 @millyardchatv</b>''',  parse_mode= 'HTML')      
      
@bot.message_handler(commands=['bots'])
def button(message):
  bot.send_message(message.chat.id, '''<b>🔥 Siz ushbu botlar orqali Rubl ishlaysiz!!!
❗Botlar sinalgan va 100% toʻlaydi...✅✅✅

👉 https://t.me/ZezikBot?start=427322790  (#zezikbot)
👉 https://t.me/Vipserfbot?start=427322790   (#vipserfbot)
👉 https://t.me/TegMoRobot?start=427322790  (#tegmorobot)
👉 https://t.me/Toptgmoney_bot?start=427322790
(#toptgmoney)
👉 https://t.me/tgprime_bot?start=427322790 (#tgprime) 
👉 https://t.me/CorpBisbot_newbot?start=427322790 (#corpbisbot)
👉 https://t.me/money_eazy_bot?start=427322790 (#preazymoney)
👉 https://t.me/ProPrRobot?start=427322790 (#proprrobot)
👉 https://t.me/LD_ibot?start=427322790
👉 https://t.me/Flibasta_Bot?start=427322790
👉 https://t.me/RocketK07_bot?start=427322790

#bots

•••  Tarqalamiz...🤟
👉 @millyardchatv</b> \n\n\n\n🏠<em>Bosh sahifaga qaytish uchun /start ni bosing!</em>''', parse_mode='HTML')      
      
@bot.message_handler(commands=['cryptobots'])
def button(message):
  bot.send_message(message.chat.id, '''<b><em>🔥 Ushbu botlar orqali siz KRIPTOVALYUTA ishlaysiz!
Va ushbu botlarda VAQTINCHALIK saqlasamgiz bo'ladi!</em></b> 

<b>Botlar 100% to'laydi...✅✅✅</b>

👉 https://t.me/Litecoin_click_bot?start=WioC
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3327) (LTC)

👉 https://t.me/BCH_clickbot?start=vVLT (Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3485) (BCH)

👉 https://t.me/Dogecoin_click_bot?start=G6N9
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3236 (Doge)

👉 https://t.me/Zcash_click_bot?start=6YwA
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3238) (Zcash)

👉 https://t.me/BitcoinClick_bot?start=PHWe (BTC)

👉 https://t.me/tron_clickearn_bot?start=427322790 ( TRX )

 \n\n\n 🏠 <em>Iltimos bosh sahifaga qaytish uchun /start ni bosing</em>''', parse_mode='HTML')
  
@bot.message_handler(commands=['mobilapps'])
def button(message):
  bot.send_message(message.chat.id, '''<b><u>🏃‍♂ Kriptovalyuta ishlash mumkin bo'lgan android dasturlar!</u></b>

<b>Dasturlar 100% to'laydi...✅✅✅

1⃣ Free Litecoin App
✏️ Dastur manzili: https://bitcoinaliens.com/?ref=803266&game=8&pf=2
📽️ Dastur orqali ko'proq pul ishlash: https://youtu.be/7ZeRscFjq10
📽️ Telegram orqali kochirib olish: https://t.me/millyardchatv/2515
🤖 LTC Click Botga chiqarib olish 👉 https://t.me/millyardchatv/4166
🅿️ Payeer ga chiqarib olish: https://youtu.be/voTt-FRkZbI

2⃣ Free Bitcoin Cash App
✏️ https://bitcoinaliens.com/?ref=803266&game=7&pf=2
📽️ Dastur orqali ko'proq pul ishlash: https://youtu.be/tuL3Rx2gPSM
📽️ Telegram orqali kochirib olish: https://t.me/millyardchatv/2532

3⃣ Free Litecoin app
✏️ Dastur manzili: https://bit.ly/3yQphS4
⚽ Referal Code: millyardcha
🎬 Dastur haqida videorolik: https://youtu.be/bmTHgZ9Mbbs

4⃣ Free Bitcoin Cash app
✏️ Dastur manzili: https://bit.ly/3BdMj7k
⚽ Referal Code: millyardcha
🎬 Dastur haqida videorolik: https://youtu.be/XGBcr8pvgMc

5⃣ Crypto Fast app
✏️ Dastur silkasi: https://bit.ly/3tVaEKj
🎬 Dastur haqida videorolik: https://youtu.be/4FsTYCEXprU

6⃣ Pop Stellar
✏️ Dastur silkasi: https://bit.ly/3aDKEMP
🎬 Dastur haqida videorolik: https://youtu.be/vUbu6l1daUc

7⃣ MiniLitecoin
✏️ Dastur silkasi: "Mini Games - Free Litecoin"
https://bit.ly/3ihGYBh
Referal Code: A93595
🎬 Dastur haqida videorolik: https://youtu.be/3mHS3XcSpZY

8⃣ CryptoRize 
✏️Dastur manzili:  https://bit.ly/30lveaU 
Referal Code: L5YS6J
📽️ Dastur haqida to'liq videorolik: https://youtu.be/tLnk4nn95pE
🎬 Dastur haqida videorolik: https://youtu.be/obgO5XHFmrM

9⃣ Vktarget
✏️ Sayt silkasi: https://bit.ly/36qnfxf
📽Sayt haqida videorolik:  https://youtu.be/qN_VIXZDiEk

🏠<em>Bosh sahifaga qaytish uchun /start ni bosing!</em>

•••  Tarqalamiz...🤟
👉 @millyardchatv

#cryptoapps</b>''', parse_mode='HTML')
      
@bot.message_handler(content_types=['text'])
def text(message):
  if message.text.lower() == 'kran' or message.text.lower() == 'kranlar':
     bot.send_message(message.chat.id, '<em>🙋 Kran saytlarni bilish uchun /kran komandasini bosing!</em>', parse_mode='HTML')
  elif message.text.lower() == 'salom' or message.text.lower() == 'assalomu aleykum':
        bot.send_message(message.chat.id, '''<b>Assalomu Aleykum! 😊
Siz MilyardchaTV kanalining yordamchi botiga murojaat qildingiz!
Botning imkoniyatlari bilan tanishish uchun <em>👉 @Uzcryptocoin_bot</em> ga o'ting yoki <em>👉 /help</em> ni bosing!</b>''', parse_mode='HTML')
  elif message.text.lower() == 'wallet' or message.text.lower() == 'kashalok':
    bot.send_message(message.chat.id, '''☺️<b> Sizga kerakli bo'luvchi online kashaloklar 👇👇👇👇👇👇

1️⃣ 🅿️ Payeer kashalok ochish: https://youtu.be/DmHB0idrOu4

2️⃣ 🛄 Faucet Pay Kashalok Ochish: https://youtu.be/YAZIfynHhds

3️⃣ 🤑 Coinbase kashalok ochish:  https://youtu.be/IcVyfzswm8U

4️⃣ 🔑Fkwallet ochish: https://youtu.be/PinrYupggdI

#foydali</b>

🏠<em>Bosh sahifaga qaytish uchun /start ni bosing!</em>

          \n\n•••  Tarqalamiz...🤟
          👉 @millyardchatv''', parse_mode='HTML')
  elif message.text.lower() == 'criptobotlar' or message.text.lower() == 'Cripto botlar':
    bot.send_message(message.chat.id, '''<b><em>🔥 Ushbu botlar orqali siz KRIPTOVALYUTA ishlaysiz!
Va ushbu botlarda VAQTINCHALIK saqlasamgiz bo'ladi!</em></b> 

<b>Botlar 100% to'laydi...✅✅✅</b>

👉 https://t.me/Litecoin_click_bot?start=WioC
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3327) (LTC)

👉 https://t.me/BCH_clickbot?start=vVLT (Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3485) (BCH)

👉 https://t.me/Dogecoin_click_bot?start=G6N9
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3236 (Doge)

👉 https://t.me/Zcash_click_bot?start=6YwA
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3238) (Zcash)

👉 https://t.me/BitcoinClick_bot?start=PHWe (BTC)

👉 https://t.me/tron_clickearn_bot?start=427322790 ( TRX )

 \n\n\n 🏠 <em>Iltimos bosh sahifaga qaytish uchun /start ni bosing</em>''', parse_mode='HTML')
  elif message.text.lower() == 'mobilapps' or message.text.lower() == 'mobil dasturlar':
    bot.send_message(message.chat.id, '''<b><u>🏃‍♂ Kriptovalyuta ishlash mumkin bo'lgan android dasturlar!</u></b>

<b>Dasturlar 100% to'laydi...✅✅✅

1⃣ Free Litecoin App
✏️ Dastur manzili: https://bitcoinaliens.com/?ref=803266&game=8&pf=2
📽️ Dastur orqali ko'proq pul ishlash: https://youtu.be/7ZeRscFjq10
📽️ Telegram orqali kochirib olish: https://t.me/millyardchatv/2515
🤖 LTC Click Botga chiqarib olish 👉 https://t.me/millyardchatv/4166
🅿️ Payeer ga chiqarib olish: https://youtu.be/voTt-FRkZbI

2⃣ Free Bitcoin Cash App
✏️ https://bitcoinaliens.com/?ref=803266&game=7&pf=2
📽️ Dastur orqali ko'proq pul ishlash: https://youtu.be/tuL3Rx2gPSM
📽️ Telegram orqali kochirib olish: https://t.me/millyardchatv/2532

3⃣ Free Litecoin app
✏️ Dastur manzili: https://bit.ly/3yQphS4
⚽ Referal Code: millyardcha
🎬 Dastur haqida videorolik: https://youtu.be/bmTHgZ9Mbbs

4⃣ Free Bitcoin Cash app
✏️ Dastur manzili: https://bit.ly/3BdMj7k
⚽ Referal Code: millyardcha
🎬 Dastur haqida videorolik: https://youtu.be/XGBcr8pvgMc

5⃣ Crypto Fast app
✏️ Dastur silkasi: https://bit.ly/3tVaEKj
🎬 Dastur haqida videorolik: https://youtu.be/4FsTYCEXprU

6⃣ Pop Stellar
✏️ Dastur silkasi: https://bit.ly/3aDKEMP
🎬 Dastur haqida videorolik: https://youtu.be/vUbu6l1daUc

7⃣ MiniLitecoin
✏️ Dastur silkasi: "Mini Games - Free Litecoin"
https://bit.ly/3ihGYBh
Referal Code: A93595
🎬 Dastur haqida videorolik: https://youtu.be/3mHS3XcSpZY

8⃣ CryptoRize 
✏️Dastur manzili:  https://bit.ly/30lveaU 
Referal Code: L5YS6J
📽️ Dastur haqida to'liq videorolik: https://youtu.be/tLnk4nn95pE
🎬 Dastur haqida videorolik: https://youtu.be/obgO5XHFmrM

9⃣ Vktarget
✏️ Sayt silkasi: https://bit.ly/36qnfxf
📽Sayt haqida videorolik:  https://youtu.be/qN_VIXZDiEk

🏠<em>Bosh sahifaga qaytish uchun /start ni bosing!</em>

•••  Tarqalamiz...🤟
👉 @millyardchatv

#cryptoapps</b>''', parse_mode='HTML')
  elif message.text.lower()=='yordam':
    bot.send_message(message.chat.id, '''<b> 🌠 😄 Men siz uchun bir nechta foydali ma'lumotlarni taklif qilaman!</b><em>
-- Kran saytlar /kran buyrug'ida! yoki shunchaki <code>kran</code> deb yozing! ⛏
-- Botlar /bots buyrug'ida yoki <code>botlar</code> deb yozing!
-- Kashaloklar ochish /wallet buyrug'ida yoki <code>wallet</code> deb yozing!
-- Cryptobotlar /cryptobots buyrug'ida yoki <code>criptobotlar</code> deb yozing!
-- Mobil dasturlar /mobilapps buyrug'ida yoki <code>mobilapps</code> deb yozing!🤖</em>''',  parse_mode='HTML')
  elif message.text.lower()=='tezchange':
    bot.send_message(message.chat.id, '''<em>🔥Agar siz Qiwi Payeer Yoomoney Webmoney kashaloklaringizni to'ldirmoqchi bo'lsangiz sizga ishonchli TEZCHANGE botini taklif etaman! Bu bot bilan tez oson to'ldirib olasiz!</em> ☺️👍

<b>🤖 Bot silkasi: http://t.me/Tezchangebot?start=427322790

🎬 Bot haqida videorolik: https://youtu.be/5SkZgqxKLlk

•••  Tarqalamiz...🤟
👉 @millyardchatv</b>''', parse_mode='HTML')
  elif message.text.lower()=='coinbase':
    bot.send_message(message.chat.id, '''<em>🔥Ko'pchilik juda ko'p sóraydi! Coinbase qanday ochiladi? 
Coinbase qanday identifikatsiya qilish mumkin!
Coinbase ocholmayabman deb! 😳</em>

🙋‍♂<b>Endi sizning shu kabi savollaringizga manashu videorolik orqali javob topishingiz mumkin! 

👉 https://youtu.be/IcVyfzswm8U</b>

•••  Tarqalamiz...🤟
👉 @millyardchatv''', parse_mode='HTML')
  elif message.text.lower()=='bestchange':
    bot.send_message(message.chat.id, '''<em>👀Kóp obunachilar sóraydi!...
Qanday Kriptovalyuta sotib olsam bóladi? 🤔
LTC click botga qanday pul solsam bóladi! 🙄
Menda kriptovalyuta bor uni sotishim kerak!.... 😶‍🌫</em>

<b>💥Bunday savollar juda kóp!
Videorolikni kóring va savollaringizga javob olasiz!😊👇

👉 https://youtu.be/2WptCjY0ePQ

•••  Tarqalamiz...🤟
👉 @millyardchatv</b>''', parse_mode='HTML')
  elif message.text.lower()=='seshanba':
    bot.send_message(message.chat.id, '''<b>❗️Eslatma</b> 

<em>Ushbu dasturlar orqali SARMOYASIZ LTC va BchCash kriptovalyutani ishlaysiz!
Dastur har seshanba aftomatik tarzda Coinbase ga to'laydi!
Dastur to'lashi uchun unga doim kirib turing! Bo'lmasa TO'LAMAYDI!</em> 

<b>Free Litecoin App
✏️ Dastur manzili: https://bitcoinaliens.com/?ref=803266&game=8&pf=2
📽️ Dastur orqali ko'proq pul ishlash: https://youtu.be/7ZeRscFjq10
📽️ Telegram orqali kochirib olish: https://t.me/millyardchatv/2515
🤖 LTC Click Botga chiqarib olish 👉 https://t.me/millyardchatv/4166
🅿️ Payeer ga chiqarib olish: https://youtu.be/voTt-FRkZbI

<b>Free Bitcoin Cash App</b>
✏️ Dastur manzili: https://bitcoinaliens.com/?ref=803266&game=7&pf=2
📽️ Dastur orqali ko'proq pul ishlash: https://youtu.be/tuL3Rx2gPSM
📽️ Telegram orqali kochirib olish: https://t.me/millyardchatv/2532</b>

•••  Tarqalamiz...🤟
👉 @millyardchatv

#seshanba''', parse_mode='HTML')
  elif message.text.lower()=='faucetpaykranlar':
    bot.send_message(message.chat.id, '''<em>❗️ Ushbu saytlar Faucet Pay kashalogiga srazi to'laydi...✅✅✅</em>

<b>1⃣ ClaimCliks LTC
✏️ Sayt silkasi: https://bit.ly/2QbL0Tw
🎬 Sayt haqida videorolik: https://youtu.be/lyl2zEo5SBw

2⃣ClaimCliks DOGE
✏️ Sayt silkasi: https://bit.ly/2OLBXbG
🎬Sayt haqida videorolik: https://youtu.be/b3_cyAckf2I

3⃣ ClaimCliks TRX
✏️ Sayt silkasi: https://bit.ly/3diQPaR
🎬 Sayt haqida videorolik:
https://youtu.be/Qa4st7lh5Sc

4⃣ ClaimFreeCoins LTC
✏️ Sayt silkasi: http://bit.ly/2M4xEqn
🎬 Sayt haqida videorolik: https://youtu.be/KLn4PoRewtY

6⃣ ClaimFreeCoins DOGE
✏️ Sayt silkasi: https://bit.ly/2NP6yVb
🎬 Sayt haqida videorolik: https://youtu.be/oF3MqRbfqxQ

7⃣ IqFaucet
✏️ Sayt manzili: https://bit.ly/3xjiLlN
🎬 Sayt haqida videorolik: https://youtu.be/OrWqGdATBOs

8⃣ SoonDogeCoin
✏️ Sayt manzili: https://bit.ly/3jwCRFs
🎬 Sayt haqida videorolik: https://youtu.be/Q8jtOldtmP4

9️⃣ ClaimFreeCoins TRX
✏️ Sayt silkasi: https://bit.ly/3i1Uvjp
🎬 Sayt haqida videorolik: https://youtu.be/pwl3X3J__zw</b>

•••  Tarqalamiz...🤟
👉 @millyardchatv''', parse_mode='HTML')
  elif message.text.lower()=='fkwallet':
    bot.send_message(message.chat.id, '''<b>☺️👍 Sizlar uchun eng qulay bo'lgan kashalokni taklif qilaman! Uning nomi FKWALLET!!!</b>

<em>🔥Siz ushbu kashalok orqali juda ko'p saytlarga pul kiritishingiz mumkin va o'sha kashalokka chiqarib olsangiz ham bo'ladi! Siz ushbu kashalokda $ € ₽ ... va boshqa turli xildagi kriptovalyutalarni saqlashingiz mumkin!

😊Siz ushbu kashalokdan Nvuti, Cabura saytlariga pul kiritishda va chiqarib olishda foydalansagiz bo'ladi! Albatta kashalok juda qulay va ishonchli! Hammaga tavsiya qilaman! ☺️👊</em>

<u><b>Batafsil ma'lumotlar videorolikda!</b></u>

<b>✏️ Sayt silkasi: https://bit.ly/3dVGtyb
🎬 Kashalok haqida to'liq videorolik: https://youtu.be/PinrYupggdI</b>

•••  Tarqalamiz...🤟
👉 @millyardchatv''', parse_mode='HTML')


bot.polling()
