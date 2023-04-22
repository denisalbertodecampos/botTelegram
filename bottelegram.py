import telebot

CHAVE_API = "5015649882:AAHBHQ-yU_Fa7_Sgh2-er274f-1piJ-Cvp0"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Escolha o projeto
    
    /Projeto_VW_Taos_Blank_125_126
    /Projeto_VW_Taos_Blank_833_144
    /Projeto_VW_Taos_Blank_803_299
    /Projeto_VW_Taos_Blank_803_143
    /Projeto_VW_Taos_Blank_437_438
    /Projeto_VW_Taos_Blank_609_610
    /Projeto_Toyota_Panel_Dash
    /Projeto_Toyota_Back_Door"""

    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Projeto_VW_Taos_Blank_125_126"])
def opcao1(mensagem):
    texto = """
        Projeto 125-126
  "https://docs.google.com/spreadsheets/d/e/2PACX-1vQGRs3KoDvJU2uqoGlSuDXbWIYL0ZFQsSNGXlKibDM1nU--Pl4GQBNPZN6-TPaD6NMLBn4L5lH4h8Yy/pub?output=pdf """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Projeto_VW_Taos_Blank_833_144"])
def opcao1(mensagem):
    texto = """

    Projeto 833-144
  "https://docs.google.com/spreadsheets/d/e/2PACX-1vTsVqAeuyatjc2qzi9ZaIV6j4CxDnIvtLjPpdo7QMzI4jM4vqUKjNA1cGyj6ClNnIjESd22x7V7ocXx/pub?output=pdf """

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Projeto_VW_Taos_Blank_803_299"])
def opcao1(mensagem):
    texto = """
    Projeto 803-299
  "https://docs.google.com/spreadsheets/d/e/2PACX-1vSe5MoxJWwrf7H3P9irQWT3Navsj_lAzfbz65Ijtrj-9B2WhQDVSZMpcadOySpCJV-TRSm-ZLZdIE4k/pub?output=pdf """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Projeto_VW_Taos_Blank_803_143"])
def opcao1(mensagem):
    texto = """
    Projeto 803-143
  "https://docs.google.com/spreadsheets/d/e/2PACX-1vQPXoOLQr-P1mtS4WGLlLX9tVf12hjE8gziWi7WpGasi_hnlQKYbU45n_pMjjwkCveO6Uxp3Ekz2H77/pub?output=pdf """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Projeto_VW_Taos_Blank_437_438"])
def opcao1(mensagem):
    texto = """
    Projeto 437-438
  "https://docs.google.com/spreadsheets/d/e/2PACX-1vTED4CFHEG0Ow8aNK1z1OMOj6BDkvtmP0Fkp5ZFBJ0eDzumkMmjfzo44-C-PCnIgLk2-7Azjnj95x-d/pub?output=pdf """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Projeto_VW_Taos_Blank_609_610"])
def opcao1(mensagem):
    texto = """
    Projeto 609-610
  "https://docs.google.com/spreadsheets/d/e/2PACX-1vSJhHkJ6_PZq81dXum2Ls9_VdsyT0Sjt5xzv14dIJJ03g5clnmND9U25PhERiVX0wLFPKAmDJ7f_FW3/pub?output=pdf """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Projeto_Toyota_Panel_Dash"])
def opcao1(mensagem):
    texto = """
    Projeto Panel Dash
  "https://docs.google.com/spreadsheets/d/e/2PACX-1vSl2VQ-rLzT1kZEQG4jxnAJEptNk1cFQTayIF_6JwY3n4e9C2g4G4Ow93LSzVmMvuCBCF1SaAGlRbKO/pub?output=pdf """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Projeto_Toyota_Back_Door"])
def opcao1(mensagem):
    texto = """
    Projeto Back Door
  "https://docs.google.com/spreadsheets/d/e/2PACX-1vTXsZnN8ZBHNazC1GJtwfk5dVttd75lZDfk763cwdLGScBvVV2Z2J0G8MDmlAxxMVA2FemVyMzQi9EG/pub?output=pdf """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """

    Fretes em tempo real
"https://docs.google.com/spreadsheets/d/e/2PACX-1vRjbHq77canXLqIcEtcm9M1hFSrrfJeDZcIS_clpbVukkN-Pyspx30-384eM197ZaoqPCEIEeQABchF/pub?gid=0&single=true&output=pdf """ 

    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """
    Fretes em tempo real
"https://docs.google.com/spreadsheets/d/1E_hxkuVgJTpePRUrWxnxbwZc8zK6z85SHgDgKCgJElU/edit#gid=0 """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    texto = """
    Fretes
"https://docs.google.com/spreadsheets/d/1DkQo3XT17MPSgC3JK3VOv7F4UocEwfqxvoMuT8_Vqw4/edit#gid=0 """

    bot.send_message(mensagem.chat.id, texto)

def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Clique na opção para continuar
    
     /opcao1 Componentes
     /opcao2 Fretes

     
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()


