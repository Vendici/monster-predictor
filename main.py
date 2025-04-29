import time
import requests
import json

def fetch_nhl_matches():
    url = "https://site.api.365scores.com/api/v2/sport/icehockey/events/live"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        matches = []
        for event in data.get("events", []):
            competition = event.get("competition", {}).get("name", "")
            if "NHL" in competition:
                home = event.get("homeCompetitor", {}).get("name", "")
                away = event.get("awayCompetitor", {}).get("name", "")
                status = event.get("status", {}).get("description", "")
                matches.append({
                    "home": home,
                    "away": away,
                    "status": status
                })

        print(f"\n=== Обновление матчей NHL ===")
        for match in matches:
            print(f"{match['home']} vs {match['away']} — {match['status']}")

    except Exception as e:
        print(f"Ошибка загрузки матчей: {e}")

if __name__ == "__main__":
    while True:
        fetch_nhl_matches()
        time.sleep(30)  # обновлять каждые 30 секунд
