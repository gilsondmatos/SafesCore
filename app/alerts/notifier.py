# app/alerts/notifier.py

import requests

# Substitua pelo seu próprio token e chat_id
TELEGRAM_TOKEN = "7591133814:AAF_WaqDCDTXSuDZUFublFlxAi9VF0s76Ak"
TELEGRAM_CHAT_ID = "7621739362"  # <--- confirme esse é seu chat_id

def send_telegram_alert(tx):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("[ERRO] TELEGRAM_TOKEN ou TELEGRAM_CHAT_ID não configurado.")
        return

    message = (
        f"🚨 ALERTA DE RISCO 🚨\n"
        f"Hash: {tx['hash']}\n"
        f"De: {tx['from']}\n"
        f"Para: {tx['to']}\n"
        f"Valor: {tx['value']} {tx['token']}\n"
        f"Timestamp: {tx['timestamp']}\n"
        f"Score de Risco: {tx['score']}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}

    response = requests.post(url, data=data)

    if response.status_code != 200:
        print(f"[ERRO] Falha ao enviar alerta: {response.text}")
    else:
        print("[INFO] Alerta enviado com sucesso ao Telegram.")
