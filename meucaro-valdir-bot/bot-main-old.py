'''
Done! Congratulations on your new bot. You will find it at t.me/meucaro_gerson_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
5702907950:AAEvTkGIQ8Co11jcL3UjdYdHhHUicToXpxM
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
'''

import telebot
from forex_python.converter import CurrencyRates
from random import choice
from datetime import date, datetime



# integração do BOT
CHAVE_API = "5611954668:AAFjmYBLqh8figyRN-uJ0lfANbYf14son0I"
bot = telebot.TeleBot(CHAVE_API)



# Comandos

# Jogo

@bot.message_handler (commands=['Conselho'])
def advice(message):

    phrases = [
        "Com calma e com jeito se come o cu de qualquer sujeito",
        "Com calma e com manha, é assim que se come boa Picanha",
        "Quem tá lendo é viado",
        "No fim, tudo da certo amigo, não importa o caminho que siga, vai chegar em algum lugar",
        "Deita e dorme, que amanhã é outro dia, e você vai ter uma chance de pensar melhor nisso",
        "Quem compra fiado paga dobrado",
        "Não se esqueça, se a vida anda amargurada, tome uma boa gelada!",
        "Coração magoado se cura com muito gelo, limão e vodka",
        "Se a vida te der limões, faça uma limonada",
        "Não viva somente do que faz sentido. Viva do que te faz feliz!",
        "Livre-se dos bajuladores. Mantenha perto de você pessoas que te avisem quando você erra",
        "Se você está andando no caminho certo e está disposto a continuar caminhando, eventualmente, você vai progredir",
        "Quem tem mais do que precisa ter quase sempre se convence que não tem o bastante, e fala demais por não ter nada a dizer",
        "Não busque a perfeição em ninguém, se não quiser que busquem em você",
        "É impossível encontrar a sua paixão sem perder a razão, já dizia Chorão",
        "Tem vários jeitos da gente matar uma pessoa, a indiferença é uma delas",
        "Sempre terá alguma “dor” em você, mas nunca desista. Você quer, você pode, é só superar",
        "Cuidado com o destino. Ele brinca com as pessoas",
        "Você nunca sabe quanto tempo você tem com alguém, então não esqueça de dizer eu te amo enquanto você pode",
        "Se você quer fazer do mundo um lugar melhor, olhe para si mesmo e faça uma mudança",
        "Acho que o melhor ainda virá, na minha humilde opinião",
        "Não importa sua vontade ou se suas intenções são boas, tem sempre um idiota querendo te derrubar",
        "Quanto maior a estrela, maior é o alvo",
        "Todo dia crie sua história",
        "Os tolos se multiplicam quando os sábios ficam em silêncio",
        "Você nunca deve ter medo do que está fazendo quando está certo",
        "Só porque você não pode ver nada, não significa que você deve fechar os olhos",
        "Nunca seja limitado pela imaginação limitada de outras pessoas",
        "Não viva para que a sua presença seja notada, mas para que a sua falta seja sentida",
        "A vida sem luta é um mar morto no centro do organismo universal",
        "Nossas dúvidas são traidoras e nos fazem perder o que, com frequência, poderíamos ganhar, por simples medo de arriscar",
        "Espera de teu filho o que fizeste com teu pai",
        "Muitas palavras não indicam necessariamente muita sabedoria",
        "Toma para ti o conselho que dá aos outros",
        "Nunca faças o que te desagrada ver fazer a outros",
        "Procure sempre uma ocupação; quando o tiver não pense em outra coisa além de procurar fazê-lo bem feito",
        "Nada é tão flexível como a língua da mulher, nada é tão pérfido como os seus remorsos, nada é mais terrível do que a sua maldade, nada é mais sensível do que as suas lágrimas",
        "Uma alegria tumultuosa anuncia uma felicidade medíocre e breve",
        "A mente é um fogo a ser aceso, não um vaso a preencher",
        "A alma mais forte e mais bem constituída é aquela que os sucessos não orgulham e que não se abate com os revezes",
        "Nada é permanente, salvo a mudança",
        "É estupidez pedir aos deuses aquilo que se pode conseguir sozinho",
        "O prazer não é um mal em si; mas certos prazeres trazem mais dor do que felicidade",
        "O prazer de fazer o bem, é maior do que recebê-lo",
        "Aquele que melhor goza a riqueza é aquele que menos necessidade dela tem",
        "O começo é a metade do todo"
    ]

    result = choice(phrases)

    bot.reply_to(message, result)

# Cotações de moedas

@bot.message_handler (commands=['Moeda'])
def currency(message):

    c = CurrencyRates()
    dollar_currency = c.get_rates('USD')
    brl_currency = c.get_rates('BRL')
    eur_currency = c.get_rates('EUR')
    gbp_currency = c.get_rates('GBP')

    brl = round(brl_currency['USD'], 2)
    dollar = round(dollar_currency['BRL'], 2)
    eur = round(eur_currency['BRL'], 2)
    gbp = round(gbp_currency['BRL'], 2)

    bot.reply_to(message , f'''
💸 Tabela Monetária Gerson Peres 💸
O Real está valendo {brl} dólares
O Dólar está valendo {dollar} reais
O Euro está valendo {eur} reais
A Libra está valendo {gbp} reais
    ''')

# Jogo

@bot.message_handler (commands=['Jogo'])
def gamesRoullete(message):

    games = [
        'Minecraft',
        'CSGO',
        'LoL',
        'Valorant',
        'Fortnite',
        'Among Us',
        'Roblox',
        'Rocketzin',
        'Habbo',
        'Gartic',
        'Brawhalla',
        'OSU'
    ]

    result = choice(games)

    bot.reply_to(message, f"Acho que por hoje {result} era uma boa")

# Apocalipse

@bot.message_handler (commands=['Apocalipse'])
def armageddon(message):
    # Faz a contagem de dias restantes até a data destinada
    today = date.today()
    finalday = date(2024, 1, 1) # Dia do segundo turno
    counter = (finalday - today).days
    
    if counter < 30:
        bot.reply_to(message, "Tá na hora de comprar a corda")
    else:
        bot.reply_to(message, f"Faltam {counter} dias 🥶")

# Eleições contagem

@bot.message_handler (commands=['Eleicao'])
def eleicao(message):
    # Faz a contagem de dias restantes até a data destinada
    today = date.today()
    finalday = date(2022, 10, 30) # Dia do segundo turno
    counter = (finalday - today).days
    
    if counter > 15:
        bot.reply_to(message, f"Faltam {counter} dias, tem é tempo ainda, parceiro ")
    elif counter == 13:
        bot.reply_to(message, f"Faltam {counter} dias, companheiro 🍖")
    elif counter > 10:
        bot.reply_to(message, f"Faltam {counter} AAAAAAAAAAA")
    elif counter > 5:
        bot.reply_to(message, f"Faltam {counter} dias, hora de apagar publicação de rede social hein")
    elif counter > 1:
        bot.reply_to(message, f"Faltam {counter} dias para o caos")
    elif counter == 1:
        bot.reply_to(message, f"Eu preciso mesmo dizer que é amanhã?")

# Cabaré

@bot.message_handler (commands=['Cabare'])
def temcabare(message):
    
    cabare = [
        'Não tem cabaré essa noite 🥹',
        'Tem cabaré essa noite! 🍺'
    ]

    bot.reply_to(message, choice(cabare))

# Dado

@bot.message_handler (commands=['6'])
def six_dice(message):

    num = [1, 2, 3, 4, 5, 6]
    result = choice(num)

    bot.reply_to(message, f"O resultado foi {result}")

@bot.message_handler (commands=['20'])
def twenty_dice(message):

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    result = choice(num)

    bot.reply_to(message, f"O resultado foi {result}")

@bot.message_handler (commands=['Dado'])
def diceoption(message):
    bot.reply_to(message, '''
/6 - Joga um dado de 6 lados
/20 - Joga um dado de 20 lados
    ''')

# Mensagem inicial

def firstcall(message):

    callmethods = [
        'campeão',
        'meu caro',
        'oh amigo',
        'ei valdir,',
        'ei valdir'
    ]

    boiadaAlert = [
        'dei ',
        'eu dou ',
        'eu dei ',
        'te dar ',
        'te dei ',
        'dar-ei ',
        'dar-lhe ',
        'vou dar ',
        'darei ',
        'pensando em dar ',
        'me passa ',
        'passar ',
        'me passaram ',
        'te passar ',
        'meu cu ',
        'meucu ',
        'quero é porra ',
        'quero dar ',
        'meu rabo ',
        'dá pra a gente ',
        'da pra mim ',
        'me dá ',
        'dar-me-ei ',
        'lhe-darei ',
        'te dou ',
        'da pra agente ',
        'dei pra ',
        'gosto de dar ',
        'cai na banana ',
        'vai dar '
    ]

    forbidden_minutes = [
        23,
        24,
        25,
    ]

    ms = (message.text).lower()
    message_time_stamp = message.date
    real_time_stamp = int(datetime.utcfromtimestamp(message_time_stamp).strftime('%M'))

    # Verifica o minuto do dia em que a mensagem foi enviada
    if real_time_stamp in forbidden_minutes:
        bot.reply_to(message, 'E isso é hora de mandar mensagem?')
        return False

    if ms in callmethods:
        return True
    else:
        # Sistema de verificação de boiadas
        for boiadaType in boiadaAlert:
            if boiadaType in ms: 
                bot.reply_to(message, 'Essas conversa viu, sei não...')
            else:
                return False

@bot.message_handler (func=firstcall)
def firstcallback(message):

    bot.reply_to(message, '''
Diga lá meu Patrão, o que vai querer?
/Dado - Jogar dado de 6 - 20 lados
/Moeda - Envia a última cotação do dólar e do euro
/Jogo - Escolhe um jogo em uma lista pré definida
/Cabare - Responde se tem ou não tem cabaré essa noite
/Conselho - Dá um conselhor de bar
/Eleicao - Contagem de dias para a eleição
/Apocalipse - Contagem de dias para o Armageddon
/Musica - Baixa músicas do Youtube
    ''')



# Faz com que o bot leia as mensagens infinitamente
bot.polling()

#   🤖🤖🤖 Comandos para o Jarvis:
# - Subjulgar mensagens enviadas no horário proibido
# - Baixar música pros mano
# - Previsao do tempo pro resto do dia/semana
# - Jornal diário automático (NÃO PROMETO)
# - Dar conselhos de bar (frases prontas tipo horóscopo que se encaixam pra qualquer problema