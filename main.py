import telebot
from telebot import types

bot = telebot.TeleBot('1212395833:AAErAMhnQ_DDC4DmbxweBsuBi_R-q2F9p0U')

@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Kran Saytlar βοΈ', callback_data='kransaytlar')
    item = types.InlineKeyboardButton('π€ Botlar', callback_data='botlar')
    item2 = types.InlineKeyboardButton("π¨βπ» Admin & πBog'lanish", callback_data='admin')
    item3 = types.InlineKeyboardButton('π§° Kashalok Ochish!', callback_data='kashalok ochish')
    item4 = types.InlineKeyboardButton('π€ CryptoBotlar!', callback_data='cryptobotlar1')
    item5 = types.InlineKeyboardButton('π² Android dasturlar', callback_data= 'androidapps')
    markup.add(item1, item3, item, item4, item2, item5)
    
    mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
    
    bot.send_message(message.chat.id,  f'''<b> π  Assalomu Aleykum!, {mention}! \n\nπ Internet orqali pul ishlashingiz mumkin bo'lgan barcha ma'lumotlar shu yerda...</b> \n\n\n<em><u>Kerakli tugmalardan birini tanlang!</u> \nπππππππππ</em>''',  parse_mode= 'HTML', reply_markup=markup)
    
    
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
      if call.data == 'botlar':
        botlarbuttons = types.InlineKeyboardMarkup()
        botlarbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
        botlarbuttons.add(botlarbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= ''' <b>π₯ Siz ushbu botlar orqali Rubl ishlaysiz!!!\nβBotlar sinalgan va 100% toΚ»laydi...ββ\n
π https://t.me/ZezikBot?start=427322790Β  (#zezikbot)
π https://t.me/Vipserfbot?start=427322790Β Β  (#vipserfbot)    
π https://t.me/TegMoRobot?start=427322790Β  (#tegmorobot)
π https://t.me/Toptgmoney_bot?start=427322790
(#toptgmoney)
π https://t.me/tgprime_bot?start=427322790 (#tgprime) 
π https://t.me/CorpBisbot_newbot?start=427322790 (#corpbisbot)
π https://t.me/money_eazy_bot?start=427322790 (#preazymoney)
π https://t.me/ProPrRobot?start=427322790 (#proprrobot)
π https://t.me/LD_ibot?start=427322790 
π https://t.me/Flibasta_Bot?start=427322790
π https://t.me/RocketK07_bot?start=427322790

#bots

β’β’β’  Tarqalamiz...π€
π @millyardchatv</b>''', parse_mode='HTML', reply_markup=botlarbuttons)
             
      if call.data == 'kransaytlar':
        buttons = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("BTC kranlar βΆοΈ", callback_data="btckranlar")
        back1 = types.InlineKeyboardButton('LTC kranlar βΆοΈ', callback_data='ltckranlar')
        back2 = types.InlineKeyboardButton('DOGE kranlar βΆοΈ', callback_data='dogekranlar')
        back3 =types.InlineKeyboardButton('Faucet Pay kranlar βΆοΈ', callback_data='faucetpaykranlar')
        backbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
        buttons.add(back, back1, back2, back3, backbut)
            
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '''<b><u>π€ Mana o'sha siz izlagan eng yaxshi kriptovalyuta kran saytlar!</u></b>\n<em>Bu yerda joylashgan barcha kran saytlar 100% to'laydi...βββ</em>  
  \n''', parse_mode='HTML', reply_markup=buttons)
         
      elif call.data == 'admin':
              adminbuttons = types.InlineKeyboardMarkup(row_width=1)
              backbutton1 = types.InlineKeyboardButton(text="π  Bosh Sahifa", callback_data="mainmenu")
              adminbuttons.add(backbutton1)
              bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text='''βοΈ <b>Sahifalarimiz:</b>

π’ <b>Telegram kanal:</b> π @millyardchatv
π₯ <b>Guruhimiz:</b> π @millyardchatvchat
π <b>Admin:</b> π @millyardcha
π£ <b>Spamlar uchun:</b> π @millyardchatv_bot ''', parse_mode='HTML', reply_markup=adminbuttons)
             
             
      elif call.data == 'btckranlar':
        btcbuttons = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text='βοΈ Orqaga', callback_data='orqaga')
        backbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
        btcbuttons.add(but, backbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '''<em>πββ Ushbu kran saytlar orqali siz BTC kriptovalyutasini ishlab olasiz! Hozirgi kunda eng faol saytlar!</em> 
    \n<b>Saytlar 100% to'laydi..βββ

1β£ FreeBitcoin (Har soatda 0.05 BTC)
βοΈ Sayt silkasi: https://bit.ly/36lPOMg
π¬ Sayt haqida videorolik: https://youtu.be/mujhX0VvvKM

2β£ BtcMaker (Har soatda 0.05)
 βοΈ Sayt silkasi: https://bit.ly/2Sbu7pV
π½οΈ Sayt haqida to'liq videorolik: https://youtu.be/FvXccuSz8Ng

3β£ BitShark (Har soatda 0.1 BTC)
βοΈ Sayt silkasi: https://bit.ly/30nYVYR
π¬ Sayt haqida videorolik: https://youtu.be/F9CaiWDdLVo

4β£ BitKing (Har soatda 0.001 BTC)
βοΈ Sayt Silkasi: https://bit.ly/2Jdy3Wf
π¬ Sayt haqida videorolik: https://youtu.be/gdZm3Dgiaas

5β£ OurBitcoin (Har soatda 0.01 BTC)
βοΈ Sayt manzili: https://bit.ly/3rCGpIE
π¬ Sayt haqida videorolik: https://youtu.be/918ExiODr_o

6β£ βοΈ Sayt silkasi: https://bit.ly/3fHTnA5
π¬ Sayt haqida videorolik: https://youtu.be/4y3m16qO6BY

β’β’β’  Tarqalamiz...π€
π @millyardchatv</b>
  ''', parse_mode='HTML', reply_markup=btcbuttons)
      
      elif call.data == 'orqaga':
        buttons = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton("BTC kranlar βΆοΈ", callback_data="btckranlar")
        back1 = types.InlineKeyboardButton('LTC kranlar βΆοΈ', callback_data='ltckranlar')
        back2 = types.InlineKeyboardButton('DOGE kranlar βΆοΈ', callback_data='dogekranlar')
        back3 =types.InlineKeyboardButton('Faucet Pay kranlar βΆοΈ', callback_data='faucetpaykranlar')
        backbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
        buttons.add(back, back1, back2, back3, backbut)
            
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '''<b><u>π€ Mana o'sha siz izlagan eng yaxshi kriptovalyuta kran saytlar!</u></b>\n<em>Bu yerda joylashgan barcha kran saytlar 100% to'laydi...βββ</em>  
  \n''', parse_mode='HTML', reply_markup=buttons)
        
      elif call.data == 'mainmenu':
              markup1 = types.InlineKeyboardMarkup(row_width=2)
              item1 = types.InlineKeyboardButton('Kran Saytlar βοΈ', callback_data='kransaytlar')
              item = types.InlineKeyboardButton('π€ Botlar', callback_data='botlar')
              item2 = types.InlineKeyboardButton("π¨βπ» Admin & πBog'lanish", callback_data='admin')
              item3 = types.InlineKeyboardButton('π§° Kashalok Ochish!', callback_data='kashalok ochish')
              item4 = types.InlineKeyboardButton('π€ CryptoBotlar!', callback_data='cryptobotlar1')
              item5 = types.InlineKeyboardButton('π² Android dasturlar', callback_data= 'androidapps')
              markup1.add(item1, item3, item, item4, item2, item5)
    
              bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text='''<b> π  Assalomu Aleykum! \n\nπ Internet orqali pul ishlashingiz mumkin bo'lgan barcha ma'lumotlar shu yerda...</b> \n\n\n<em><u>Kerakli tugmalardan birini tanlang!</u> \nπππππππππ</em>''',  parse_mode= 'HTML', reply_markup=markup1)
        
      elif call.data == 'cryptobotlar1':
        cryptobuttons = types.InlineKeyboardMarkup()
        botlarbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
        cryptobuttons.add(botlarbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '''<b><em>π₯ Ushbu botlar orqali siz KRIPTOVALYUTA ishlaysiz!
Va ushbu botlarda VAQTINCHALIK saqlasangiz bo'ladi!</em> 

Botlar 100% to'laydi...βββ

π https://t.me/Litecoin_click_bot?start=WioC
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3327) (LTC)\n
π https://t.me/BCH_clickbot?start=vVLT (Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3485) (BCH)\n
π https://t.me/Dogecoin_click_bot?start=G6N9
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3236 (Doge)\n
π https://t.me/Zcash_click_bot?start=6YwA
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3238) (Zcash)\n
π https://t.me/BitcoinClick_bot?start=PHWe (BTC)\n
π https://t.me/tron_clickearn_bot?start=427322790 ( TRX )</b>
''', parse_mode='HTML', reply_markup=cryptobuttons)
        
      elif call.data == 'kashalok ochish':
        kashalokbuttons = types.InlineKeyboardMarkup()
        kashalokbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
        kashalokbuttons.add(kashalokbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '''βΊοΈ<b> Sizga kerakli bo'luvchi online kashaloklar ππππππ

1οΈβ£ πΏοΈ Payeer kashalok ochish: https://youtu.be/DmHB0idrOu4
2οΈβ£ π Faucet Pay Kashalok Ochish: https://youtu.be/YAZIfynHhds
3οΈβ£ π€ Coinbase kashalok ochish:  https://youtu.be/IcVyfzswm8U
4οΈβ£ πFkwallet ochish: https://youtu.be/PinrYupggdI
          \n\nβ’β’β’  Tarqalamiz...π€
          π @millyardchatv</b>''', parse_mode='HTML', reply_markup=kashalokbuttons)

      elif call.data == 'ltckranlar':
        ltcbuttons = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text='βοΈ Orqaga', callback_data='orqaga')
        backbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
        ltcbuttons.add(but, backbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''<em>π₯ Ushbu kran saytlar orqali siz LTC kriptovalyutasini SARMOYASIZ ishlab olasiz! Eng Aktual saytlar!</em>

<b><u>Saytlar 100% to'laydi...βββ</u>

1β£ Free - Litecoin ( Har soatda 2 LTC)
βοΈ Sayt silkasi: https://bit.ly/34eAmyv
π¬ Sayt haqida videorolik: https://youtu.be/5fttImJt9ac

2β£ LitePick (Har soatda 0.02 LTC)
βοΈ Sayt silkasi: https://bit.ly/2S57kiq
π¬ Sayt haqida videorolik: https://youtu.be/ioA2qY32YpM

3β£ Litking (Har soatda 0.2 LTC)
βοΈ Sayt silkasi: https://bit.ly/38GpCML
π¬ Sayt haqida videorolik: https://youtu.be/zx_7inCHn1Y

4β£ FREELTC ( Har soatda 1000 litoshi ) 
βοΈ Sayt silkasi: https://bit.ly/3DhgYS0
π½οΈ Sayt haqida videorolik: https://youtu.be/KwJENuCIVK0
πΆβπ« Saytdan pul chiqarib olish: https://youtu.be/uAcfMaHnUn8


β’β’β’  Tarqalamiz...π€
π @millyardchatv
</b>''', parse_mode='HTML', reply_markup=ltcbuttons)
          
      elif call.data == 'dogekranlar':
        dogebuttons = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text='βοΈ Orqaga', callback_data='orqaga')
        backbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
        dogebuttons.add(but, backbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''<b><u>π Eng Aktual Dogecoin kranlar!</u></b>

<b>Saytlar 100% to'laydi...βββ

1β£ Free Dogecoin (Har soatda 1000 Doge)
βοΈ Sayt manzili: https://bit.ly/2UVGknE
π¬ Sayt haqida videorolik: https://youtu.be/5nj_etNFNQg

2β£ DogePick (Har soatda 10 Doge)
βοΈ  Sayt silkasi: https://bit.ly/3jACaLI
π¬ Sayt haqida videorolik: https://youtu.be/_rAlvNodXG4

3β£ Free Dogecoin
βοΈ Sayt silkasi: https://bit.ly/3rESzzc
π¬ Sayt haqida videorolik: https://youtu.be/2d24vsUaBAE

4β£ Ad Doge (Har soatda 500 Doge)
βοΈ Sayt silkasi: http://bit.ly/3pbP8i4
π¬ Sayt haqida videorolik: https://youtu.be/I_KTvgMYWvg

β’β’β’  Tarqalamiz...π€
π @millyardchatv
</b>''', parse_mode='HTML', reply_markup=dogebuttons)
        
      elif call.data == 'androidapps':
        androidbuttons = types.InlineKeyboardMarkup()
        botlarbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
        androidbuttons.add(botlarbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''<b><u>πββ Kriptovalyuta ishlash mumkin bo'lgan android dasturlar!</u></b>

<b>Dasturlar 100% to'laydi...βββ

1β£ Free Litecoin App
βοΈ Dastur manzili: https://bitcoinaliens.com/?ref=803266&game=8&pf=2
π½οΈ Dastur orqali ko'proq pul ishlash: https://youtu.be/7ZeRscFjq10
π½οΈ Telegram orqali kochirib olish: https://t.me/millyardchatv/2515
π€ LTC Click Botga chiqarib olish π https://t.me/millyardchatv/4166
πΏοΈ Payeer ga chiqarib olish: https://youtu.be/voTt-FRkZbI

2β£ Free Bitcoin Cash App
βοΈ https://bitcoinaliens.com/?ref=803266&game=7&pf=2
π½οΈ Dastur orqali ko'proq pul ishlash: https://youtu.be/tuL3Rx2gPSM
π½οΈ Telegram orqali kochirib olish: https://t.me/millyardchatv/2532

3β£ Free Litecoin app
βοΈ Dastur manzili: https://bit.ly/3yQphS4
β½ Referal Code: millyardcha
π¬ Dastur haqida videorolik: https://youtu.be/bmTHgZ9Mbbs

4β£ Free Bitcoin Cash app
βοΈ Dastur manzili: https://bit.ly/3BdMj7k
β½ Referal Code: millyardcha
π¬ Dastur haqida videorolik: https://youtu.be/XGBcr8pvgMc

5β£ Crypto Fast app
βοΈ Dastur silkasi: https://bit.ly/3tVaEKj
π¬ Dastur haqida videorolik: https://youtu.be/4FsTYCEXprU

6β£ Pop Stellar
βοΈ Dastur silkasi: https://bit.ly/3aDKEMP
π¬ Dastur haqida videorolik: https://youtu.be/vUbu6l1daUc

7β£ MiniLitecoin
βοΈ Dastur silkasi: "Mini Games - Free Litecoin"
https://bit.ly/3ihGYBh
Referal Code: A93595
π¬ Dastur haqida videorolik: https://youtu.be/3mHS3XcSpZY

8β£ CryptoRize 
βοΈDastur manzili:  https://bit.ly/30lveaU 
Referal Code: L5YS6J
π½οΈ Dastur haqida to'liq videorolik: https://youtu.be/tLnk4nn95pE
π¬ Dastur haqida videorolik: https://youtu.be/obgO5XHFmrM

9β£ Vktarget
βοΈ Sayt silkasi: https://bit.ly/36qnfxf
π½Sayt haqida videorolik:Β  https://youtu.be/qN_VIXZDiEk

1β£0β£ CryptoTab Browser
βοΈ Dastur manzili: https://bit.ly/3sHXEc0
π½ Dastur haqida videorolik: https://youtu.be/Kgl8WG-hypM

β’β’β’  Tarqalamiz...π€
π @millyardchatv
</b>''', parse_mode='HTML', reply_markup=androidbuttons)
      
      elif call.data == 'faucetpaykranlar':
        fpbuttons = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text='βοΈ Orqaga', callback_data='orqaga')
        backbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
        fpbuttons.add(but, backbut)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''<em>βοΈ Ushbu saytlar Faucet Pay kashalogiga srazi to'laydi...βββ</em>

<b>1β£ ClaimCliks LTC
βοΈ Sayt silkasi: https://bit.ly/2QbL0Tw
π¬ Sayt haqida videorolik: https://youtu.be/lyl2zEo5SBw

2β£ClaimCliks DOGE
βοΈ Sayt silkasi: https://bit.ly/2OLBXbG
π¬Sayt haqida videorolik: https://youtu.be/b3_cyAckf2I

3β£ ClaimCliks TRX
βοΈ Sayt silkasi: https://bit.ly/3diQPaR
π¬ Sayt haqida videorolik:
https://youtu.be/Qa4st7lh5Sc

4β£ ClaimFreeCoins LTC
βοΈ Sayt silkasi: http://bit.ly/2M4xEqn
π¬ Sayt haqida videorolik: https://youtu.be/KLn4PoRewtY

6β£ ClaimFreeCoins DOGE
βοΈ Sayt silkasi: https://bit.ly/2NP6yVb
π¬ Sayt haqida videorolik: https://youtu.be/oF3MqRbfqxQ

7β£ IqFaucet
βοΈ Sayt manzili: https://bit.ly/3xjiLlN
π¬ Sayt haqida videorolik: https://youtu.be/OrWqGdATBOs

8β£ SoonDogeCoin
βοΈ Sayt manzili: https://bit.ly/3jwCRFs
π¬ Sayt haqida videorolik: https://youtu.be/Q8jtOldtmP4

9οΈβ£ ClaimFreeCoins TRX
βοΈ Sayt silkasi: https://bit.ly/3i1Uvjp
π¬ Sayt haqida videorolik: https://youtu.be/pwl3X3J__zw</b>

β’β’β’  Tarqalamiz...π€
π @millyardchatv''', parse_mode='HTML', reply_markup=fpbuttons)
        
@bot.message_handler(commands=['help', 'yordam'])
def button(message):
  bot.send_message(message.chat.id,  '''<b> π  π Men siz uchun bir nechta foydali ma'lumotlarni taklif qilaman!</b><em>
-- Kran saytlar /kran buyrug'ida! yoki shunchaki <code>kran</code> deb yozing! β
-- Botlar /bots buyrug'ida yoki <code>botlar</code> deb yozing!
-- Kashaloklar ochish /wallet buyrug'ida yoki <code>wallet</code> deb yozing!
-- Cryptobotlar /cryptobots buyrug'ida yoki <code>criptobotlar</code> deb yozing!
-- Mobil dasturlar /mobilapps buyrug'ida yoki <code>mobilapps</code> deb yozing!π€</em>''',  parse_mode= 'HTML')      

@bot.message_handler(commands=['kran'])
def button(message):
  kranbuttons = types.InlineKeyboardMarkup(row_width=1)
  back = types.InlineKeyboardButton("BTC kranlar βΆοΈ", callback_data="btckranlar")
  back1 = types.InlineKeyboardButton('LTC kranlar βΆοΈ', callback_data='ltckranlar')
  back2 = types.InlineKeyboardButton('DOGE kranlar βΆοΈ', callback_data='dogekranlar')
  back3 =types.InlineKeyboardButton('Faucet Pay kranlar βΆοΈ', callback_data='faucetpaykranlar')
  backbut = types.InlineKeyboardButton(text='π  Bosh Sahifa', callback_data='mainmenu')
  kranbuttons.add(back, back1, back2, back3, backbut)
          
  bot.send_message(message.chat.id, text= '''<b><u>π€ Mana o'sha siz izlagan eng yaxshi kriptovalyuta kran saytlar!</u></b>\n<em>Bu yerda joylashgan barcha kran saytlar 100% to'laydi...βββ</em>  
  \n''', parse_mode='HTML', reply_markup=kranbuttons)
      
@bot.message_handler(commands=['wallet'])
def button(message):
  bot.send_message(message.chat.id, '''βΊοΈ<b> Sizga kerakli bo'luvchi online kashaloklar ππππππ

1οΈβ£ πΏοΈ Payeer kashalok ochish: https://youtu.be/DmHB0idrOu4

2οΈβ£ π Faucet Pay Kashalok Ochish: https://youtu.be/YAZIfynHhds

3οΈβ£ π€ Coinbase kashalok ochish:  https://youtu.be/IcVyfzswm8U

4οΈβ£ πFkwallet ochish: https://youtu.be/PinrYupggdI

#foydali
          \n\nβ’β’β’  Tarqalamiz...π€
          π @millyardchatv</b>''',  parse_mode= 'HTML')      
      
@bot.message_handler(commands=['bots'])
def button(message):
  bot.send_message(message.chat.id, '''<b>π₯ Siz ushbu botlar orqali Rubl ishlaysiz!!!
βBotlar sinalgan va 100% toΚ»laydi...βββ

π https://t.me/ZezikBot?start=427322790Β  (#zezikbot)
π https://t.me/Vipserfbot?start=427322790Β Β  (#vipserfbot)
π https://t.me/TegMoRobot?start=427322790Β  (#tegmorobot)
π https://t.me/Toptgmoney_bot?start=427322790
(#toptgmoney)
π https://t.me/tgprime_bot?start=427322790 (#tgprime) 
π https://t.me/CorpBisbot_newbot?start=427322790 (#corpbisbot)
π https://t.me/money_eazy_bot?start=427322790 (#preazymoney)
π https://t.me/ProPrRobot?start=427322790 (#proprrobot)
π https://t.me/LD_ibot?start=427322790
π https://t.me/Flibasta_Bot?start=427322790
π https://t.me/RocketK07_bot?start=427322790

#bots

β’β’β’  Tarqalamiz...π€
π @millyardchatv</b> \n\n\n\nπ <em>Bosh sahifaga qaytish uchun /start ni bosing!</em>''', parse_mode='HTML')      
      
@bot.message_handler(commands=['cryptobots'])
def button(message):
  bot.send_message(message.chat.id, '''<b><em>π₯ Ushbu botlar orqali siz KRIPTOVALYUTA ishlaysiz!
Va ushbu botlarda VAQTINCHALIK saqlasamgiz bo'ladi!</em></b> 

<b>Botlar 100% to'laydi...βββ</b>

π https://t.me/Litecoin_click_bot?start=WioC
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3327) (LTC)

π https://t.me/BCH_clickbot?start=vVLT (Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3485) (BCH)

π https://t.me/Dogecoin_click_bot?start=G6N9
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3236 (Doge)

π https://t.me/Zcash_click_bot?start=6YwA
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3238) (Zcash)

π https://t.me/BitcoinClick_bot?start=PHWe (BTC)

π https://t.me/tron_clickearn_bot?start=427322790 ( TRX )

 \n\n\n π  <em>Iltimos bosh sahifaga qaytish uchun /start ni bosing</em>''', parse_mode='HTML')
  
@bot.message_handler(commands=['mobilapps'])
def button(message):
  bot.send_message(message.chat.id, '''<b><u>πββ Kriptovalyuta ishlash mumkin bo'lgan android dasturlar!</u></b>

<b>Dasturlar 100% to'laydi...βββ

1β£ Free Litecoin App
βοΈ Dastur manzili: https://bitcoinaliens.com/?ref=803266&game=8&pf=2
π½οΈ Dastur orqali ko'proq pul ishlash: https://youtu.be/7ZeRscFjq10
π½οΈ Telegram orqali kochirib olish: https://t.me/millyardchatv/2515
π€ LTC Click Botga chiqarib olish π https://t.me/millyardchatv/4166
πΏοΈ Payeer ga chiqarib olish: https://youtu.be/voTt-FRkZbI

2β£ Free Bitcoin Cash App
βοΈ https://bitcoinaliens.com/?ref=803266&game=7&pf=2
π½οΈ Dastur orqali ko'proq pul ishlash: https://youtu.be/tuL3Rx2gPSM
π½οΈ Telegram orqali kochirib olish: https://t.me/millyardchatv/2532

3β£ Free Litecoin app
βοΈ Dastur manzili: https://bit.ly/3yQphS4
β½ Referal Code: millyardcha
π¬ Dastur haqida videorolik: https://youtu.be/bmTHgZ9Mbbs

4β£ Free Bitcoin Cash app
βοΈ Dastur manzili: https://bit.ly/3BdMj7k
β½ Referal Code: millyardcha
π¬ Dastur haqida videorolik: https://youtu.be/XGBcr8pvgMc

5β£ Crypto Fast app
βοΈ Dastur silkasi: https://bit.ly/3tVaEKj
π¬ Dastur haqida videorolik: https://youtu.be/4FsTYCEXprU

6β£ Pop Stellar
βοΈ Dastur silkasi: https://bit.ly/3aDKEMP
π¬ Dastur haqida videorolik: https://youtu.be/vUbu6l1daUc

7β£ MiniLitecoin
βοΈ Dastur silkasi: "Mini Games - Free Litecoin"
https://bit.ly/3ihGYBh
Referal Code: A93595
π¬ Dastur haqida videorolik: https://youtu.be/3mHS3XcSpZY

8β£ CryptoRize 
βοΈDastur manzili:  https://bit.ly/30lveaU 
Referal Code: L5YS6J
π½οΈ Dastur haqida to'liq videorolik: https://youtu.be/tLnk4nn95pE
π¬ Dastur haqida videorolik: https://youtu.be/obgO5XHFmrM

9β£ Vktarget
βοΈ Sayt silkasi: https://bit.ly/36qnfxf
π½Sayt haqida videorolik:Β  https://youtu.be/qN_VIXZDiEk

π <em>Bosh sahifaga qaytish uchun /start ni bosing!</em>

β’β’β’  Tarqalamiz...π€
π @millyardchatv

#cryptoapps</b>''', parse_mode='HTML')
      
@bot.message_handler(content_types=['text'])
def text(message):
  if message.text.lower() == 'kran' or message.text.lower() == 'kranlar':
     bot.send_message(message.chat.id, '<em>π Kran saytlarni bilish uchun /kran komandasini bosing!</em>', parse_mode='HTML')
  elif message.text.lower() == 'salom' or message.text.lower() == 'assalomu aleykum':
        bot.send_message(message.chat.id, '''<b>Assalomu Aleykum! π
Siz MilyardchaTV kanalining yordamchi botiga murojaat qildingiz!
Botning imkoniyatlari bilan tanishish uchun <em>π @Uzcryptocoin_bot</em> ga o'ting yoki <em>π /help</em> ni bosing!</b>''', parse_mode='HTML')
  elif message.text.lower() == 'wallet' or message.text.lower() == 'kashalok':
    bot.send_message(message.chat.id, '''βΊοΈ<b> Sizga kerakli bo'luvchi online kashaloklar ππππππ

1οΈβ£ πΏοΈ Payeer kashalok ochish: https://youtu.be/DmHB0idrOu4

2οΈβ£ π Faucet Pay Kashalok Ochish: https://youtu.be/YAZIfynHhds

3οΈβ£ π€ Coinbase kashalok ochish:  https://youtu.be/IcVyfzswm8U

4οΈβ£ πFkwallet ochish: https://youtu.be/PinrYupggdI

#foydali</b>

π <em>Bosh sahifaga qaytish uchun /start ni bosing!</em>

          \n\nβ’β’β’  Tarqalamiz...π€
          π @millyardchatv''', parse_mode='HTML')
  elif message.text.lower() == 'criptobotlar' or message.text.lower() == 'Cripto botlar':
    bot.send_message(message.chat.id, '''<b><em>π₯ Ushbu botlar orqali siz KRIPTOVALYUTA ishlaysiz!
Va ushbu botlarda VAQTINCHALIK saqlasamgiz bo'ladi!</em></b> 

<b>Botlar 100% to'laydi...βββ</b>

π https://t.me/Litecoin_click_bot?start=WioC
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3327) (LTC)

π https://t.me/BCH_clickbot?start=vVLT (Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3485) (BCH)

π https://t.me/Dogecoin_click_bot?start=G6N9
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3236 (Doge)

π https://t.me/Zcash_click_bot?start=6YwA
(Bot haqida to'liq ma'lumot: https://t.me/millyardchatv/3238) (Zcash)

π https://t.me/BitcoinClick_bot?start=PHWe (BTC)

π https://t.me/tron_clickearn_bot?start=427322790 ( TRX )

 \n\n\n π  <em>Iltimos bosh sahifaga qaytish uchun /start ni bosing</em>''', parse_mode='HTML')
  elif message.text.lower() == 'mobilapps' or message.text.lower() == 'mobil dasturlar':
    bot.send_message(message.chat.id, '''<b><u>πββ Kriptovalyuta ishlash mumkin bo'lgan android dasturlar!</u></b>

<b>Dasturlar 100% to'laydi...βββ

1β£ Free Litecoin App
βοΈ Dastur manzili: https://bitcoinaliens.com/?ref=803266&game=8&pf=2
π½οΈ Dastur orqali ko'proq pul ishlash: https://youtu.be/7ZeRscFjq10
π½οΈ Telegram orqali kochirib olish: https://t.me/millyardchatv/2515
π€ LTC Click Botga chiqarib olish π https://t.me/millyardchatv/4166
πΏοΈ Payeer ga chiqarib olish: https://youtu.be/voTt-FRkZbI

2β£ Free Bitcoin Cash App
βοΈ https://bitcoinaliens.com/?ref=803266&game=7&pf=2
π½οΈ Dastur orqali ko'proq pul ishlash: https://youtu.be/tuL3Rx2gPSM
π½οΈ Telegram orqali kochirib olish: https://t.me/millyardchatv/2532

3β£ Free Litecoin app
βοΈ Dastur manzili: https://bit.ly/3yQphS4
β½ Referal Code: millyardcha
π¬ Dastur haqida videorolik: https://youtu.be/bmTHgZ9Mbbs

4β£ Free Bitcoin Cash app
βοΈ Dastur manzili: https://bit.ly/3BdMj7k
β½ Referal Code: millyardcha
π¬ Dastur haqida videorolik: https://youtu.be/XGBcr8pvgMc

5β£ Crypto Fast app
βοΈ Dastur silkasi: https://bit.ly/3tVaEKj
π¬ Dastur haqida videorolik: https://youtu.be/4FsTYCEXprU

6β£ Pop Stellar
βοΈ Dastur silkasi: https://bit.ly/3aDKEMP
π¬ Dastur haqida videorolik: https://youtu.be/vUbu6l1daUc

7β£ MiniLitecoin
βοΈ Dastur silkasi: "Mini Games - Free Litecoin"
https://bit.ly/3ihGYBh
Referal Code: A93595
π¬ Dastur haqida videorolik: https://youtu.be/3mHS3XcSpZY

8β£ CryptoRize 
βοΈDastur manzili:  https://bit.ly/30lveaU 
Referal Code: L5YS6J
π½οΈ Dastur haqida to'liq videorolik: https://youtu.be/tLnk4nn95pE
π¬ Dastur haqida videorolik: https://youtu.be/obgO5XHFmrM

9β£ Vktarget
βοΈ Sayt silkasi: https://bit.ly/36qnfxf
π½Sayt haqida videorolik:Β  https://youtu.be/qN_VIXZDiEk

π <em>Bosh sahifaga qaytish uchun /start ni bosing!</em>

β’β’β’  Tarqalamiz...π€
π @millyardchatv

#cryptoapps</b>''', parse_mode='HTML')
  elif message.text.lower()=='yordam':
    bot.send_message(message.chat.id, '''<b> π  π Men siz uchun bir nechta foydali ma'lumotlarni taklif qilaman!</b><em>
-- Kran saytlar /kran buyrug'ida! yoki shunchaki <code>kran</code> deb yozing! β
-- Botlar /bots buyrug'ida yoki <code>botlar</code> deb yozing!
-- Kashaloklar ochish /wallet buyrug'ida yoki <code>wallet</code> deb yozing!
-- Cryptobotlar /cryptobots buyrug'ida yoki <code>criptobotlar</code> deb yozing!
-- Mobil dasturlar /mobilapps buyrug'ida yoki <code>mobilapps</code> deb yozing!π€</em>''',  parse_mode='HTML')
  elif message.text.lower()=='tezchange':
    bot.send_message(message.chat.id, '''<em>π₯Agar siz Qiwi Payeer Yoomoney Webmoney kashaloklaringizni to'ldirmoqchi bo'lsangiz sizga ishonchli TEZCHANGE botini taklif etaman! Bu bot bilan tez oson to'ldirib olasiz!</em> βΊοΈπ

<b>π€ Bot silkasi: http://t.me/Tezchangebot?start=427322790

π¬ Bot haqida videorolik: https://youtu.be/5SkZgqxKLlk

β’β’β’  Tarqalamiz...π€
π @millyardchatv</b>''', parse_mode='HTML')
  elif message.text.lower()=='coinbase':
    bot.send_message(message.chat.id, '''<em>π₯Ko'pchilik juda ko'p sΓ³raydi! Coinbase qanday ochiladi? 
Coinbase qanday identifikatsiya qilish mumkin!
Coinbase ocholmayabman deb! π³</em>

πββ<b>Endi sizning shu kabi savollaringizga manashu videorolik orqali javob topishingiz mumkin! 

π https://youtu.be/IcVyfzswm8U</b>

β’β’β’  Tarqalamiz...π€
π @millyardchatv''', parse_mode='HTML')
  elif message.text.lower()=='bestchange':
    bot.send_message(message.chat.id, '''<em>πKΓ³p obunachilar sΓ³raydi!...
Qanday Kriptovalyuta sotib olsam bΓ³ladi? π€
LTC click botga qanday pul solsam bΓ³ladi! π
Menda kriptovalyuta bor uni sotishim kerak!.... πΆβπ«</em>

<b>π₯Bunday savollar juda kΓ³p!
Videorolikni kΓ³ring va savollaringizga javob olasiz!ππ

π https://youtu.be/2WptCjY0ePQ

β’β’β’  Tarqalamiz...π€
π @millyardchatv</b>''', parse_mode='HTML')
  elif message.text.lower()=='seshanba':
    bot.send_message(message.chat.id, '''<b>βοΈEslatma</b> 

<em>Ushbu dasturlar orqali SARMOYASIZ LTC va BchCash kriptovalyutani ishlaysiz!
Dastur har seshanba aftomatik tarzda Coinbase ga to'laydi!
Dastur to'lashi uchun unga doim kirib turing! Bo'lmasa TO'LAMAYDI!</em> 

<b>Free Litecoin App
βοΈ Dastur manzili: https://bitcoinaliens.com/?ref=803266&game=8&pf=2
π½οΈ Dastur orqali ko'proq pul ishlash: https://youtu.be/7ZeRscFjq10
π½οΈ Telegram orqali kochirib olish: https://t.me/millyardchatv/2515
π€ LTC Click Botga chiqarib olish π https://t.me/millyardchatv/4166
πΏοΈ Payeer ga chiqarib olish: https://youtu.be/voTt-FRkZbI

<b>Free Bitcoin Cash App</b>
βοΈ Dastur manzili: https://bitcoinaliens.com/?ref=803266&game=7&pf=2
π½οΈ Dastur orqali ko'proq pul ishlash: https://youtu.be/tuL3Rx2gPSM
π½οΈ Telegram orqali kochirib olish: https://t.me/millyardchatv/2532</b>

β’β’β’Β  Tarqalamiz...π€
π @millyardchatv

#seshanba''', parse_mode='HTML')
  elif message.text.lower()=='faucetpaykranlar':
    bot.send_message(message.chat.id, '''<em>βοΈ Ushbu saytlar Faucet Pay kashalogiga srazi to'laydi...βββ</em>

<b>1β£ ClaimCliks LTC
βοΈ Sayt silkasi: https://bit.ly/2QbL0Tw
π¬ Sayt haqida videorolik: https://youtu.be/lyl2zEo5SBw

2β£ClaimCliks DOGE
βοΈ Sayt silkasi: https://bit.ly/2OLBXbG
π¬Sayt haqida videorolik: https://youtu.be/b3_cyAckf2I

3β£ ClaimCliks TRX
βοΈ Sayt silkasi: https://bit.ly/3diQPaR
π¬ Sayt haqida videorolik:
https://youtu.be/Qa4st7lh5Sc

4β£ ClaimFreeCoins LTC
βοΈ Sayt silkasi: http://bit.ly/2M4xEqn
π¬ Sayt haqida videorolik: https://youtu.be/KLn4PoRewtY

6β£ ClaimFreeCoins DOGE
βοΈ Sayt silkasi: https://bit.ly/2NP6yVb
π¬ Sayt haqida videorolik: https://youtu.be/oF3MqRbfqxQ

7β£ IqFaucet
βοΈ Sayt manzili: https://bit.ly/3xjiLlN
π¬ Sayt haqida videorolik: https://youtu.be/OrWqGdATBOs

8β£ SoonDogeCoin
βοΈ Sayt manzili: https://bit.ly/3jwCRFs
π¬ Sayt haqida videorolik: https://youtu.be/Q8jtOldtmP4

9οΈβ£ ClaimFreeCoins TRX
βοΈ Sayt silkasi: https://bit.ly/3i1Uvjp
π¬ Sayt haqida videorolik: https://youtu.be/pwl3X3J__zw</b>

β’β’β’  Tarqalamiz...π€
π @millyardchatv''', parse_mode='HTML')
  elif message.text.lower()=='fkwallet':
    bot.send_message(message.chat.id, '''<b>βΊοΈπ Sizlar uchun eng qulay bo'lgan kashalokni taklif qilaman! Uning nomi FKWALLET!!!</b>

<em>π₯Siz ushbu kashalok orqali juda ko'p saytlarga pul kiritishingiz mumkin va o'sha kashalokka chiqarib olsangiz ham bo'ladi! Siz ushbu kashalokda $ β¬ β½ ... va boshqa turli xildagi kriptovalyutalarni saqlashingiz mumkin!

πSiz ushbu kashalokdan Nvuti, Cabura saytlariga pul kiritishda va chiqarib olishda foydalansagiz bo'ladi! Albatta kashalok juda qulay va ishonchli! Hammaga tavsiya qilaman! βΊοΈπ</em>

<u><b>Batafsil ma'lumotlar videorolikda!</b></u>

<b>βοΈ Sayt silkasi: https://bit.ly/3dVGtyb
π¬ Kashalok haqida to'liq videorolik: https://youtu.be/PinrYupggdI</b>

β’β’β’  Tarqalamiz...π€
π @millyardchatv''', parse_mode='HTML')


bot.polling()
