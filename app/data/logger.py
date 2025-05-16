# app/data/logger.py

import csv
import os

def save_to_csv(transactions, filename="transacoes_com_score.csv"):
    """
    Salva uma lista de transações com score em um arquivo CSV.
    Cada transação deve conter os campos: hash, from, to, value, token, timestamp, score.
    """
    path = os.path.join("app", "data", filename)

    # Verifica se o arquivo já existe
    file_exists = os.path.isfile(path)

    with open(path, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["hash", "from", "to", "value", "token", "timestamp", "score"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escreve cabeçalho apenas uma vez
        if not file_exists:
            writer.writeheader()

        for tx in transactions:
            writer.writerow(tx)

    print(f"Transações salvas com sucesso em: {path}")
