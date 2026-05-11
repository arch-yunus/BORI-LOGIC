document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('simCanvas');
    const ctx = canvas.getContext('2d');
    const logBody = document.getElementById('logBody');
    const codeContent = document.getElementById('code-content');
    const runBtn = document.getElementById('run-sim');
    const curX = document.getElementById('curX');
    const curY = document.getElementById('curY');

    // Resize Canvas
    function resize() {
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    // Simulation State
    let entities = [];
    let isRunning = false;
    let frame = 0;

    class Börü {
        constructor(x, y, isAlfa = false) {
            this.x = x;
            this.y = y;
            this.isAlfa = isAlfa;
            this.vx = (Math.random() - 0.5) * 2;
            this.vy = (Math.random() - 0.5) * 2;
            this.energy = 100;
        }
        update(targets) {
            if (targets.length > 0) {
                const target = targets[0];
                const dx = target.x - this.x;
                const dy = target.y - this.y;
                const dist = Math.sqrt(dx*dx + dy*dy);
                if (dist < 300) {
                    this.vx += dx * 0.001;
                    this.vy += dy * 0.001;
                }
            }
            this.x += this.vx;
            this.y += this.vy;
            
            // Friction
            this.vx *= 0.99;
            this.vy *= 0.99;

            // Bounds
            if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
            if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.isAlfa ? 6 : 4, 0, Math.PI*2);
            ctx.fillStyle = this.isAlfa ? '#d4af37' : '#ff4d4d';
            if (this.isAlfa) ctx.shadowBlur = 15, ctx.shadowColor = '#d4af37';
            ctx.fill();
            ctx.shadowBlur = 0;
        }
    }

    class Av {
        constructor(x, y) {
            this.x = x;
            this.y = y;
            this.vx = (Math.random() - 0.5) * 4;
            this.vy = (Math.random() - 0.5) * 4;
        }
        update() {
            this.x += this.vx;
            this.y += this.vy;
            if (Math.random() < 0.02) {
                this.vx = (Math.random() - 0.5) * 4;
                this.vy = (Math.random() - 0.5) * 4;
            }
            if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
            if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, 3, 0, Math.PI*2);
            ctx.fillStyle = '#2ecc71';
            ctx.fill();
        }
    }

    function initSim() {
        entities = [];
        for(let i=0; i<12; i++) entities.push(new Börü(Math.random()*canvas.width, Math.random()*canvas.height, i===0));
        for(let i=0; i<40; i++) entities.push(new Av(Math.random()*canvas.width, Math.random()*canvas.height));
        addLog('SİSTEM', 'AŞİNA v3.0 motoru başlatıldı.', 'gold');
        addLog('NİZAM', 'Strateji: KISKAÇ | Zemin: BOZKIR', 'info');
    }

    function addLog(prefix, msg, type='') {
        const time = new Date().toLocaleTimeString('tr-TR', {hour12:false});
        const line = document.createElement('div');
        line.className = `log-line ${type}`;
        line.innerHTML = `<span class="t">[${time}]</span> <span class="p">${prefix}:</span> <span class="m">${msg}</span>`;
        logBody.appendChild(line);
        logBody.scrollTop = logBody.scrollHeight;
    }

    function loop() {
        if (!isRunning) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw Grid
        ctx.strokeStyle = 'rgba(212, 175, 55, 0.05)';
        ctx.lineWidth = 1;
        for(let i=0; i<canvas.width; i+=50) { ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke(); }
        for(let i=0; i<canvas.height; i+=50) { ctx.beginPath(); ctx.moveTo(0, i); ctx.lineTo(canvas.width, i); ctx.stroke(); }

        const wolves = entities.filter(e => e instanceof Börü);
        const prey = entities.filter(e => e instanceof Av);

        entities.forEach(e => {
            e.update(e instanceof Börü ? prey : []);
            e.draw();
        });

        if (wolves.length > 0) {
            curX.innerText = Math.round(wolves[0].x);
            curY.innerText = Math.round(wolves[0].y);
        }

        if (frame % 120 === 0) {
            const msgs = [
                "Alfa hedefi işaretledi.",
                "Kıskaç daralıyor.",
                "Enerji dengesi optimize ediliyor.",
                "Türeye uygun manevra tespiti."
            ];
            addLog('CAGRI', msgs[Math.floor(Math.random()*msgs.length)]);
        }

        frame++;
        requestAnimationFrame(loop);
    }

    runBtn.addEventListener('click', () => {
        if (!isRunning) {
            isRunning = true;
            initSim();
            loop();
            runBtn.innerText = "DURDUR";
            runBtn.style.background = "#ff4d4d";
        } else {
            isRunning = false;
            runBtn.innerText = "SİSTEMİ TETİKLE";
            runBtn.style.background = "#d4af37";
        }
    });

    // Lore Codex
    const loreData = [
        { cat: "Liderlik", title: "Aşina Soyu", text: "Göktürk hanedanının ilahi liderlik algoritması. Sürüdeki Alfa biriminin karar alma yetkisi." },
        { cat: "Strateji", title: "Kama (Wedge)", text: "Düşman hattını merkezden yarmak için kullanılan yüksek enerjili saldırı formasyonu." },
        { cat: "Felsefe", title: "Kut Sistemi", text: "Teknolojik sistemin meşruiyeti. Başarı oranı arttıkça 'Kut' yükselir ve işlem hızı optimize olur." },
        { cat: "Düzen", title: "Tüz Dengesi", text: "Sistemdeki kaynak dağılımının evrensel dengesi. Yük dengeleme (Load Balancing) mantığının kadim kökeni." }
    ];

    const loreContainer = document.getElementById('lore-container');
    loreData.forEach(item => {
        const card = document.createElement('div');
        card.className = 'lore-card-mini';
        card.innerHTML = `<span class="cat">${item.cat}</span><h4>${item.title}</h4><p>${item.text}</p>`;
        loreContainer.appendChild(card);
    });
});
