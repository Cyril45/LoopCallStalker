import callr, os, sys, time

api = callr.Api("Identifiant", "Mot de passe")

stalker = "+" + input("Entre le numéro du harceleur avec l'indicatif (33 pour la France) exemple 33123456789: ")
message = ['TTS|TTS_FR-FR_AUDREY|' + input("entre le message à envoyé : ")]


target = {
    'number': stalker,
    'timeout': 30
}

count = 0
while True :
    count += 1
    print(str(count) + " appel émis vers " + stalker)
    result = api.call('calls.broadcast_1', target, message, None)
    time.sleep(0.2)
