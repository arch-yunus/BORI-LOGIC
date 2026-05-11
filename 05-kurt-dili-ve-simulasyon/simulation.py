import time
import random
import os
import sys
from interpreter import AshinaInterpreter

class Entity:
    def __init__(self, char, x, y, color):
        self.char = char
        self.x = x
        self.y = y
        self.color = color
        self.energy = 100

    def move(self, width, height, config):
        weather = config.get("weather", "acik")
        terrain = config.get("terrain", "bozkir")
        
        # Speed modifiers
        speed = 1.0
        if weather == "kar": speed *= 0.6
        elif weather == "firtina": speed *= 0.3
        
        if terrain == "orman": speed *= 0.8
        elif terrain == "dag": speed *= 0.5
        
        if random.random() < speed:
            self.x = max(0, min(width - 1, self.x + random.randint(-1, 1)))
            self.y = max(0, min(height - 1, self.y + random.randint(-1, 1)))
        
        self.energy -= 0.5

class Wolf(Entity):
    def __init__(self, x, y, wolf_id=0):
        super().__init__('W', x, y, '\033[91m') # Red
        self.id = wolf_id
        self.energy = 150
        self.state = "hunting" 
        self.role = "serbest"

    def hunt(self, sheeps, width, height, config):
        strategy = config.get("strategy", "standart")
        weather = config.get("weather", "acik")
        terrain = config.get("terrain", "bozkir")
        ambush_range = config.get("ambush_range", 5)
        formation = config.get("formation", "serbest")
        
        self.role = config.get("roles", {}).get(self.id, "serbest")
        
        if not sheeps:
            self.move(width, height, config)
            return

        # Find closest sheep or role-based target
        target = min(sheeps, key=lambda s: (s.x - self.x)**2 + (s.y - self.y)**2)
        dist_sq = (target.x - self.x)**2 + (target.y - self.y)**2
        
        move_x = 0
        move_y = 0

        # Strategy Logic
        if strategy == "turan":
            # Turan strategy: Flank and split
            if dist_sq > 64: # Far
                move_x = 1 if target.x > self.x else -1
                move_y = random.choice([-1, 0, 1])
            elif dist_sq > ambush_range**2: # Medium
                self.state = "ambushing"
                move_x = 1 if target.x > self.x else -1
                move_y = 1 if target.y > self.y else -1
            else: # Strike
                self.state = "hunting"
                move_x = 1 if target.x > self.x else -1
                move_y = 1 if target.y > self.y else -1

        elif strategy == "kiskac":
            # Pincer: Move to sides then close in
            if self.id % 2 == 0: # Left arm
                if self.x > target.x - 5: move_x = -1
                else: move_x = 0
            else: # Right arm
                if self.x < target.x + 5: move_x = 1
                else: move_x = 0
            move_y = 1 if target.y > self.y else -1

        elif strategy == "kama":
            # Wedge: Focused central push
            if self.role == "alfa":
                move_x = 1 if target.x > self.x else -1
                move_y = 1 if target.y > self.y else -1
            else:
                # Follow the leader or cluster
                move_x = 1 if target.x > self.x else -1
                move_y = 1 if target.y > self.y else -1

        else:
            # Standart: Direct chase
            move_x = 1 if target.x > self.x else -1
            move_y = 1 if target.y > self.y else -1

        # Terrain/Weather penalties
        penalty = 0.1
        if terrain == "dag": penalty += 0.3
        if weather == "firtina": penalty += 0.4
        
        if random.random() < penalty:
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
    terrain = config.get("terrain", "bozkir")
    energy_limit = config.get("energy_limit", 10)
    
    wolves = [Wolf(random.randint(0, width-1), random.randint(0, height-1), i) for i in range(config["wolf_count"])]
    sheeps = [Sheep(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(config["sheep_count"])]
    
    for i in range(config["iterations"]):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        weather_icon = "[ACIK]" if weather == "acik" else "[KAR]" if weather == "kar" else "[FIRTINA]"
        terrain_label = f"Zemin: {terrain.upper()}"
        print(f"\033[93m--- {config['title']} --- {weather_icon} {terrain_label} Dongu: {i+1}/{config['iterations']}\033[0m")
        print(f"Strateji: {strategy.upper()} | Boru: {len(wolves)} | Koyun: {len(sheeps)} | Hava: {weather.upper()}")
        
        if logs and i < len(logs):
            print(f"\033[94mCAGRI: \"{logs[i]}\"\033[0m")
        elif logs:
            print(f"\033[90mYankilan: {logs[-1]}\033[0m")

        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        for s in sheeps:
            if 0 <= s.y < height and 0 <= s.x < width:
                grid[s.y][s.x] = f"{s.color}{s.char}\033[0m"
        
        for w in wolves:
            if 0 <= w.y < height and 0 <= w.x < width:
                char = w.char
                if w.state == "ambushing": char = 'P'
                if w.role == "alfa": char = 'A'
                grid[w.y][w.x] = f"{w.color}{char}\033[0m"

        print("+" + "-" * width + "+")
        for row in grid:
            print("|" + "".join(row) + "|")
        print("+" + "-" * width + "+")
        
        avg_energy = sum(w.energy for w in wolves) / len(wolves) if wolves else 0
        print(f"Boru Ortalama Enerji: {avg_energy:.1f} | Limit: {energy_limit}")

        for w in wolves[:]:
            w.hunt(sheeps, width, height, config)
            for s in sheeps[:]:
                if w.x == s.x and w.y == s.y:
                    sheeps.remove(s)
                    w.energy += 40 
            
            if w.energy <= energy_limit:
                wolves.remove(w)
        
        for s in sheeps:
            s.move(width, height, config)

        if not sheeps:
            print("\033[91mAV TAMAMLANDI. Suru doydu ve bozkir sessizlesti.\033[0m")
            break
        
        if not wolves:
            print("\033[91mBORULER TUKENDI. Doga dengesini kaybetti.\033[0m")
            break
            
        time.sleep(0.05)

if __name__ == "__main__":
    uluy_file = os.path.join(os.path.dirname(__file__), "kadim_strateji.asina")
    if len(sys.argv) > 1:
        uluy_file = sys.argv[1]
        
    interp = AshinaInterpreter()
    data = interp.parse(uluy_file)
    if data:
        config, logs = data
        run_simulation(config, logs)
