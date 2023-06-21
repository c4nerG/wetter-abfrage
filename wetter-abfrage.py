import requests
import matplotlib.pyplot as plt

API_KEY = "YOUR_API_KEY"
LATITUDE = "53.5502"
LONGITUDE = "9.9920"

request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}"

try:
    response = requests.get(request_url)
    response.raise_for_status()
    data = response.json()

    if response.status_code == 200:
        print(data)

        weather_description = data["weather"][0]["description"]
        print(f"\nWetterbeschreibung: {weather_description}")

        temperature = round(data["main"]["temp"] - 273.15)
        temperature_text = f"{temperature}°C"
        print(f"Es sind: {temperature_text}")

        city = data["name"]
        print(f"Stadt: {city}")

        fig, ax = plt.subplots()
        x_values = ["Temperatur"]
        y_values = [temperature]
        ax.bar(x_values, y_values, color="steelblue")
        ax.set_xlabel("Messwerte")
        ax.set_ylabel("Temperatur (°C)")
        ax.set_title(f"Aktuelle Temperatur in {city}")
        for i, v in enumerate(y_values):
            ax.text(i, v, str(v) + "°C", color="black", ha="center")
        fig.tight_layout()
        plt.show()

    else:
        print("Fehler beim Abrufen der Daten!")

except requests.exceptions.RequestException as e:
    print("Fehler bei der API-Anfrage:", e)

except (KeyError, IndexError) as e:
    print("Ungültige Datenstruktur:", e)
