import requests
import re
import time

# === CONFIGURATION ===
esp32_ip = "http://192.168.123.151"  # <-- Change to your ESP32 IP
log_file = "sensor_MQlog.csv"

# === WRITE HEADER TO FILE ===
with open(log_file, "w") as file:
    file.write("Reading,LPG GAS(ppm) \n")

# === FUNCTION TO EXTRACT VALUES FROM HTML ===
def extract_sensor_data(html):
    try:
        ppm = re.search(r"ppm:</strong>\s*([\d.]+)", html).group(1)
        return ppm
    except Exception as e:
        print("❌ Error parsing HTML:", e)
        return None, None, None

# === LOOP TO LOG 30 READINGS ===
for i in range(1, 31):
    try:
        response = requests.get(esp32_ip)
        if response.status_code == 200:
            ppm = extract_sensor_data(response.text)
            if ppm:
                print(f"{i}: ppm={ppm} ppm")
                with open(log_file, "a") as file:
                    file.write(f"{i},{ppm}\n")
            else:
                print(f"{i}: Incomplete data received")
        else:
            print(f"{i}: HTTP error {response.status_code}")
    except Exception as e:
        print(f"{i}: Failed to connect to ESP32 - {e}")
    
    time.sleep(5)  # Wait 2 seconds like ESP32 auto-refresh

print("✅ Data logging complete. Saved to:", log_file)
