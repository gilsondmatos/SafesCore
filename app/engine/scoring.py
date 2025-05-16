# app/engine/scoring.py

"""
Módulo de avaliação de risco das transações.
Regras:
- Score inicia em 100.
- Destinatários na BLACKLIST: -40 pontos.
- Valor acima de 5 ETH: -20 pontos.
- Horário fora do expediente (antes das 08:00 ou depois das 18:00): -10 pontos.
"""

from datetime import datetime

BLACKLIST = {"0xCarteiraRisco"}

def evaluate_transaction(tx: dict) -> int:
    """
    Calcula o score de risco (0 a 100) para uma transação.

    Args:
        tx (dict): dicionário com dados da transação.

    Returns:
        int: score de risco (0 é risco máximo, 100 é sem risco).
    """
    score = 100

    # Regra 1: carteira na blacklist
    if tx.get("to") in BLACKLIST:
        score -= 40

    # Regra 2: valor alto
    if tx.get("value", 0) > 5:
        score -= 20

    # Regra 3: horário suspeito
    try:
        hora = int(tx["timestamp"].split("T")[1].split(":")[0])
        if hora < 8 or hora > 18:
            score -= 10
    except Exception:
        # Caso o timestamp não esteja no formato esperado, ignoramos essa regra
        pass

    # Garante que o score não seja negativo
    return max(score, 0)
