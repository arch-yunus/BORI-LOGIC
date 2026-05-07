import time
import random
import os
import sys
from interpreter import UluyiInterpreter

class Entity:
    def __init__(self, char, x, y, color):
        self.char = char
        self.x = x
        self.y = y
        self.color = color
        self.energy = 100

    def move(self, width, height, weather="acik"):
        # Weather effects
        speed = 1
        if weather == "kar": speed = 0.5
        elif weather == "firtina": speed = 0.3
        
        if random.random() < speed:
            self.x = max(0, min(width - 1, self.x + random.randint(-1, 1)))
            self.y = max(0, min(height - 1, self.y + random.randint(-1, 1)))
        
        self.energy -= 0.5

class Wolf(Entity):
    def __init__(self, x, y):
        super().__init__('W', x, y, '\033[91m') # Red
        self.energy = 150
        self.state = "hunting" # hunting, ambushing

    def hunt(self, sheeps, width, height, config):
        strategy = config.get("strategy", "standart")
        weather = config.get("weather", "acik")
        ambush_range = config.get("ambush_range", 5)
        
        if not sheeps:
            self.move(width, height, weather)
            return

        # Find closest sheep
        target = min(sheeps, key=lambda s: (s.x - self.x)**2 + (s.y - self.y)**2)
        dist_sq = (target.x - self.x)**2 + (target.y - self.y)**2
        
        move_x = 0
        move_y = 0

        if strategy == "turan":
            # Turan strategy: Try to flank and split
            if dist_sq > 49: # Far away, circle and close in
                if target.x > self.x: move_x = 1
                elif target.x < self.x: move_x = -1
                move_y = random.choice([-1, 0, 1])
            elif dist_sq > ambush_range**2: # Medium range, prepare ambush
                self.state = "ambushing"
                if target.x > self.x: move_x = 1
                elif target.x < self.x: move_x = -1
                if target.y > self.y: move_y = 1
                elif target.y < self.y: move_y = -1
            else: # Strike
                self.state = "hunting"
                if target.x > self.x: move_x = 1
                elif target.x < self.x: move_x = -1
                if target.y > self.y: move_y = 1
                elif target.y < self.y: move_y = -1
        else:
            # Standart: Direct chase
            if target.x > self.x: move_x = 1
            elif target.x < self.x: move_x = -1
            if target.y > self.y: move_y = 1
            elif target.y < self.y: move_y = -1

        # Weather slowdown
        if weather in ["kar", "firtina"] and random.random() > 0.7:
            move_x, move_y = 0, 0

        self.x = max(0, min(width - 1, self.x + move_x))
        self.y = max(0, min(height - 1, self.y + move_y))
        self.energy -= 1

class Sheep(Entity):
    def __init__(self, x, y):
        super().__init__('s', x, y, '\033[92m') # Green

def run_simulation(config, logs=[]):
    width = config["width"]
    height = config["height"]
    strategy = config.get("strategy", "standart")
    weather = config.get("weather", "acik")
    energy_limit = config.get("energy_limit", 10)
    
    wolves = [Wolf(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(config["wolf_count"])]
    sheeps = [Sheep(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(config["sheep_count"])]
    
    for i in range(config["iterations"]):
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        weather_icon = "[ACIK]" if weather == "acik" else "[KAR]" if weather == "kar" else "[FIRTINA]"
        print(f"\033[93m--- {config['title']} --- {weather_icon} Dongu: {i+1}/{config['iterations']}\033[0m")
        print(f"Strateji: {strategy.upper()} | Boru: {len(wolves)} | Koyun: {len(sheeps)} | Hava: {weather.upper()}")
        
        if logs and i < len(logs):
            print(f"\033[94mULUMA: \"{logs[i]}\"\033[0m")
        elif logs:
            print(f"\033[90mFisilti: {logs[-1]}\033[0m")

        # Grid representation
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Place entities
        for s in sheeps:
            if 0 <= s.y < height and 0 <= s.x < width:
                grid[s.y][s.x] = f"{s.color}{s.char}\033[0m"
        
        for w in wolves:
            if 0 <= w.y < height and 0 <= w.x < width:
                char = w.char if w.state == "hunting" else 'P' # P for Pusu
                grid[w.y][w.x] = f"{w.color}{char}\033[0m"

        # Print grid
        print("+" + "-" * width + "+")
        for row in grid:
            print("|" + "".join(row) + "|")
        print("+" + "-" * width + "+")
        
        # Status
        avg_energy = sum(w.energy for w in wolves) / len(wolves) if wolves else 0
        print(f"Boru Ortalama Enerji: {avg_energy:.1f} | Limit: {energy_limit}")

        # Logic
        for w in wolves[:]:
            w.hunt(sheeps, width, height, config)
            # Catch sheep
            for s in sheeps[:]:
                if w.x == s.x and w.y == s.y:
                    sheeps.remove(s)
                    w.energy += 40 # Reward
            
            if w.energy <= energy_limit:
                wolves.remove(w)
        
        for s in sheeps:
            s.move(width, height, weather)

        if not sheeps:
            print("\033[91mAV TAMAMLANDI. Suru doydu ve bozkir sessizlesti.\033[0m")
            break
        
        if not wolves:
            print("\033[91mBORULER TUKENDI. Doga dengesini kaybetti.\033[0m")
            break
            
        time.sleep(0.05)

if __name__ == "__main__":
    uluy_file = os.path.join(os.path.dirname(__file__), "kadim_strateji.uluy")
    if len(sys.argv) > 1:
        uluy_file = sys.argv[1]
        
    interp = UluyiInterpreter()
    data = interp.parse(uluy_file)
    if data:
        config, logs = data
        run_simulation(config, logs)
