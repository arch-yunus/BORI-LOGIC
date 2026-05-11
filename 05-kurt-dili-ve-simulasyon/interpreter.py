import sys
import os
import re

class AshinaInterpreter:
    """
    AŞİNA (Kurt Soyu) Interpreter
    Kadim bozkır stratejilerini işlemek için tasarlanmış profesyonel DSL motoru.
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
            "ambush_range": 5,
            "formation": "serbest",
            "terrain": "bozkir",
            "roles": {}
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

            # SÜRÜ (AUUUUUU) [Title]
            if line.startswith("SÜRÜ") or line.startswith("AUUUUUU"):
                match = re.search(r'"([^"]*)"', line)
                if match:
                    self.config["title"] = match.group(1)

            # NİZAM / TÖRE [Key] [Value]
            elif line.startswith("NİZAM") or line.startswith("TÖRE"):
                parts = line.split()
                if len(parts) >= 3:
                    key = parts[1].upper()
                    val = parts[2]
                    # Mapping Turkish config keys to internal keys
                    if key == "GENİŞLİK": self.config["width"] = int(val)
                    elif key == "YÜKSEKLİK": self.config["height"] = int(val)
                    elif key == "STRATEJİ": self.config["strategy"] = val.lower()
                    elif key == "HAVA_DURUMU": self.config["weather"] = val.lower()
                    elif key == "ENERJİ_SINIRI": self.config["energy_limit"] = int(val)

            # DİZİLİŞ [Formation]
            elif line.startswith("DİZİLİŞ"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["formation"] = parts[1].lower()

            # ZEMİN [Terrain]
            elif line.startswith("ZEMİN"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["terrain"] = parts[1].lower()

            # ROL [ID] [Role]
            elif line.startswith("ROL"):
                parts = line.split()
                if len(parts) >= 3:
                    try:
                        wolf_id = int(parts[1])
                        role = parts[2].lower()
                        self.config["roles"][wolf_id] = role
                    except ValueError:
                        pass

            # BÖRÜ [n] (BÖRÜ_SAYISI)
            elif line.startswith("BÖRÜ"):
                parts = line.split()
                if len(parts) >= 2:
                    # Check if it's BÖRÜ_SAYISI or just BÖRÜ
                    self.config["wolf_count"] = int(parts[1])

            # AV [n] (KOYUN_SAYISI)
            elif line.startswith("AV") or line.startswith("KOYUN_SAYISI"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["sheep_count"] = int(parts[1])

            # MÜDDET / DÖNGÜ [n]
            elif line.startswith("MÜDDET") or line.startswith("DÖNGÜ"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["iterations"] = int(parts[1])

            # PUSU [n] (PUSU_KUR)
            elif line.startswith("PUSU"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["ambush_range"] = int(parts[1])

            # ÇAĞRI / ULUMA [Message]
            elif line.startswith("ÇAĞRI") or line.startswith("ULUMA"):
                match = re.search(r'"([^"]*)"', line)
                if match:
                    self.logs.append(match.group(1))

            # SON (End signal)
            elif line.startswith("SON"):
                break

        return self.config, self.logs

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python interpreter.py <dosya.asina>")
    else:
        interp = AshinaInterpreter()
        conf, logs = interp.parse(sys.argv[1])
        print(f"--- AŞİNA Yapılandırması Yüklendi ---")
        for k, v in conf.items():
            print(f"{k}: {v}")
        if logs:
            print(f"--- Kadim Mesajlar (Çağrılar) ---")
            for msg in logs:
                print(f"🐺 {msg}")
