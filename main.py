# main.py

from app.collectors.eth_collector import collect_transactions
from app.engine.scoring import evaluate_transaction
from app.data.logger import save_to_csv
from app.alerts.notifier import send_telegram_alert

def main():
    print("SafeScore iniciado. Coletando transações...\n")

    transactions = collect_transactions()
    transactions_with_scores = []

    for tx in transactions:
        print(f"Hash: {tx['hash']}")
        print(f"De: {tx['from']}")
        print(f"Para: {tx['to']}")
        print(f"Valor: {tx['value']} {tx['token']}")
        print(f"Timestamp: {tx['timestamp']}")
        print("-" * 40)

        score = evaluate_transaction(tx)
        print(f"Score de risco: {score}\n")

        # Adiciona o score ao dicionário
        tx['score'] = score
        transactions_with_scores.append(tx)

        # Envia alerta se score for menor que 50
        if score < 50:
            send_telegram_alert(tx)

    # Salvar no CSV
    save_to_csv(transactions_with_scores)

if __name__ == '__main__':
    main()
