# app/collectors/eth_collector.py

def collect_transactions():
    """
    Simula a coleta de transações da blockchain Ethereum.
    Retorna uma lista de dicionários representando transações.
    """
    transactions = [
        {
            "hash": "0xabc123",
            "from": "0xGilson",
            "to": "0xCarteiraRisco",
            "value": 60.5,  # em ETH
            "token": "ETH",
            "timestamp": "2025-05-15T10:00:00"
        },
        {
            "hash": "0xdef456",
            "from": "0xDaniel",
            "to": "0xParceiroOficial",
            "value": 71.0,
            "token": "ETH",
            "timestamp": "2025-05-15T15:30:00"
        },
        {
            "hash": "0xabc124",
            "from": "0xArthur",
            "to": "0xCarteira",  
            "value": 80.5,
            "token": "ETH",
            "timestamp": "2025-05-15T10:00:00"
        },
        {
            "hash": "0xabc134",
            "from": "0xKelvin",
            "to": "0xCarteiraRisco",  # está na blacklist
            "value": 70.2,
            "token": "ETH",
            "timestamp": "2025-05-15T12:00:00"
        }
    ]
    return transactions
