print("DEBUG TELEGRAM TOKEN:", "OK" if TELEGRAM_TOKEN else "MISSING")
print("DEBUG TELEGRAM CHAT ID:", TELEGRAM_CHAT_ID)
from datetime import datetime, timezone, timedelta

CORTE_QUALIDADE = 70

mock_match = {
    "league": {
        "name": "UEFA Champions League",
        "country": "World",
    },
    "teams": {
        "home": {"name": "Real Madrid"},
        "away": {"name": "Manchester City"},
    },
    "fixture": {
        "date": (datetime.now(timezone.utc) + timedelta(hours=3)).isoformat(),
        "status": {"short": "NS"},
    },
}

def compute_quality(match):
    score = 0
    score += 40  # liga forte
    score += 40  # dois times grandes
    score += 10  # jogo não iniciado
    score += 10  # competição mundial
    return min(score, 100)

def main():
    print("TESTE DE DETECÇÃO DE SINAL")
    quality = compute_quality(mock_match)
    print(f"Score calculado: {quality}")

    if quality >= CORTE_QUALIDADE:
        print("🚨 SINAL DETECTADO")
    else:
        print("❌ Nenhum sinal detectado")

if __name__ == "__main__":
    main()
