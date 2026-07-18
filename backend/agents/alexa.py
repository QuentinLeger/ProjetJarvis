import asyncio
import os
from alexapy import AlexaLogin, AlexaAPI

alexa_key = os.getenv("ALEXA_KEY")
email_compte = "atomiccreeperboss@gmail.com"


async def obtenir_tous_les_appareils():
    # 1. Connexion directe au compte Amazon France
    login = AlexaLogin(url="amazon.fr", email=email_compte, password=alexa_key)
    await login.login()

    # 2. Récupération brute des données de l'API
    api = AlexaAPI(login)
    raw_devices = await api.get_devices()

    # 3. Extraction simple des noms des appareils
    noms_appareils = [d.get("accountName") for d in raw_devices if d.get("accountName")]

    print(f"Appareils Alexa trouvés : {noms_appareils}")
    return noms_appareils