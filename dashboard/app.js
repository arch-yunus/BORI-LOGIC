document.addEventListener('DOMContentLoaded', () => {
    // Lore Data Management
    const loreData = [
        {
            "kavram": "Aşina (Ašina) Soyu",
            "kaynak": "Göktürk Kitabeleri",
            "analiz": "Göktürk Devleti'nin kurucu hanedanı. İlahi kurt soyundan geldiklerine inanılır. Sosyopolitik bir 'merkezi liderlik' algoritması.",
            "kategori": "Ontoloji ve Liderlik"
        },
        {
            "kavram": "Kama (Wedge) Stratejisi",
            "kaynak": "Bozkır Harp Doktrini",
            "analiz": "Düşman hattını merkezden yarmak için kullanılan V tipi formasyon. AŞİNA motorunda yüksek nüfuz gücüyle modellenir.",
            "kategori": "Askeri Doktrin"
        },
        {
            "kavram": "Ergenekon Çıkış Algoritması",
            "kaynak": "Ergenekon Destanı",
            "analiz": "70 körüğün eşzamanlı çalışmasıyla demir dağın eritilmesi. Paralel işlem ve dikey ölçeklenebilirlik başarısı.",
            "kategori": "Sistem Mühendisliği"
        },
        {
            "kavram": "Sürü Zekası (Swarm AI)",
            "kaynak": "Biyotaklit (Biomimicry)",
            "analiz": "Kurtların dağıtık ama eşgüdümlü hareket yeteneği. AŞİNA diliyle (DİZİLİŞ, ROL) simüle edilen temel mekanik.",
            "kategori": "Yapay Zeka"
        }
    ];

    const container = document.getElementById('lore-container');
    if (container) {
        container.innerHTML = '';
        loreData.forEach((item, index) => {
            const card = document.createElement('div');
            card.className = 'lore-card fade-in';
            card.style.transitionDelay = `${index * 0.1}s`;
            card.innerHTML = `
                <span class="meta">${item.kategori} | ${item.kaynak}</span>
                <h3>${item.kavram}</h3>
                <p>${item.analiz}</p>
            `;
            container.appendChild(card);
        });
    }

    // Terminal Simulation
    const terminal = document.getElementById('terminal');
    const logs = [
        { prefix: 'SYSTEM', msg: 'AŞİNA Interpreter v2.1 başlatıldı.', type: 'info' },
        { prefix: 'CONFIG', msg: 'Zemin: ORMAN | Strateji: KISKAC', type: 'info' },
        { prefix: 'CAGRI', msg: '"Alfa yerini aldı, pusu bekleniyor."', type: 'success' },
        { prefix: 'ACTION', msg: 'Formasyon: HİLAL nizamına geçiliyor.', type: 'info' },
        { prefix: 'ALERT', msg: 'Düşman birimleri (Av) %60 kuşatıldı.', type: 'alert' },
        { prefix: 'SYSTEM', msg: 'Zemin hızı optimizasyonu uygulandı (-%20).', type: 'info' },
        { prefix: 'STATUS', msg: 'Operasyon başarılı. Sürü doygunluğu: %92.', type: 'success' }
    ];

    let logIndex = 0;
    function addLog() {
        if (logIndex < logs.length) {
            const log = logs[logIndex];
            const now = new Date();
            const timeStr = `[${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}:${now.getSeconds().toString().padStart(2, '0')}]`;
            
            const line = document.createElement('div');
            line.className = `terminal-line fade-in ${log.type}`;
            line.innerHTML = `<span class="time">${timeStr}</span><span class="prefix">${log.prefix}</span><span class="msg">${log.msg}</span>`;
            terminal.appendChild(line);
            
            // Trigger animation
            setTimeout(() => line.classList.add('active'), 50);
            
            terminal.scrollTop = terminal.scrollHeight;
            logIndex++;
            setTimeout(addLog, 2000 + Math.random() * 3000);
        }
    }
    setTimeout(addLog, 2000);

    // Smooth Scroll & Fade-in Observer
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
});
