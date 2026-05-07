import sys
import os
import re

class UluyiInterpreter:
    """
    ULUYI (Kurt Dili) Interpreter
    Kadim bozkır algoritmalarını işlemek için tasarlanmış egzotik dil motoru.
    """
    def __init__(self):
        self.config = {
            "title": "Adsız Strateji",
            "width": 80,
            "height": 24,
            "wolf_count": 3,
            "sheep_count": 10,
            "iterations": 50,
            "speed": 1.0,
            "strategy": "standart",
            "weather": "acik",
            "energy_limit": 10,
            "ambush_range": 5
        }
        self.logs = []

    def parse(self, file_path):
        if not os.path.exists(file_path):
            print(f"HATA: {file_path} bulunamadı. Kurt izini kaybetti.")
            return False

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # AUUUUUU [Title]
            if line.startswith("AUUUUUU"):
                match = re.search(r'"([^"]*)"', line)
                if match:
                    self.config["title"] = match.group(1)

            # TÖRE [Key] [Value]
            elif line.startswith("TÖRE"):
                parts = line.split()
                if len(parts) >= 3:
                    key = parts[1].upper()
                    val = parts[2]
                    if key == "GENİŞLİK": self.config["width"] = int(val)
                    elif key == "YÜKSEKLİK": self.config["height"] = int(val)
                    elif key == "STRATEJİ": self.config["strategy"] = val.lower()
                    elif key == "HAVA_DURUMU": self.config["weather"] = val.lower()
                    elif key == "ENERJİ_SINIRI": self.config["energy_limit"] = int(val)

            # BÖRÜ_SAYISI [Int]
            elif line.startswith("BÖRÜ_SAYISI"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["wolf_count"] = int(parts[1])

            # KOYUN_SAYISI [Int]
            elif line.startswith("KOYUN_SAYISI"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["sheep_count"] = int(parts[1])

            # DÖNGÜ [Int]
            elif line.startswith("DÖNGÜ"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["iterations"] = int(parts[1])

            # PUSU_KUR [Range]
            elif line.startswith("PUSU_KUR"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["ambush_range"] = int(parts[1])

            # ULUMA [Message]
            elif line.startswith("ULUMA"):
                match = re.search(r'"([^"]*)"', line)
                if match:
                    self.logs.append(match.group(1))

        return self.config, self.logs

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python interpreter.py <dosya.uluy>")
    else:
        interp = UluyiInterpreter()
        conf, logs = interp.parse(sys.argv[1])
        print(f"--- ULUYI Yapılandırması Yüklendi ---")
        for k, v in conf.items():
            print(f"{k}: {v}")
        if logs:
            print(f"--- Kadim Mesajlar ---")
            for msg in logs:
                print(f"🐺 {msg}")
