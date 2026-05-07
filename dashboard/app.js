document.addEventListener('DOMContentLoaded', () => {
    // Lore Data Management
    const loreData = [
        {
            "kavram": "Gökbörü",
            "kaynak": "Oğuz Kağan Destanı",
            "analiz": "Işık içerisinden çıkan ilahi rehber. Stratejik keşif ve ordu yönetiminde navigasyonel bir veri kaynağı.",
            "kategori": "Navigasyon ve Rehberlik"
        },
        {
            "kavram": "Ergenekon Bozkurtu",
            "kaynak": "Ergenekon Destanı",
            "analiz": "Sıkışmış bir toplumu özgürlüğe taşıyan çıkış algoritması. Demir dağın eritilmesinin ardından beliren rehber.",
            "kategori": "Kurtarıcı ve Yol Gösterici"
        },
        {
            "kavram": "Türeyiş Kurdu",
            "kaynak": "Türeyiş Destanı",
            "analiz": "Soyun ilahi ve güçlü bir kökene dayandırılması. Tanrı'nın kurt suretinde yeryüzüne inerek soyu başlatması.",
            "kategori": "Ontoloji ve Köken"
        },
        {
            "kavram": "Ergenekon Çıkış Algoritması",
            "kaynak": "Teknik Lore (JSON)",
            "analiz": "70 körüğün eşzamanlı çalışmasıyla demir dağın eritilmesi. Paralel işlem ve dikey ölçeklenebilirlik başarısı.",
            "kategori": "Sistem Mühendisliği"
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
        { prefix: 'STRATEGY', msg: 'Turan Taktiği aktif edildi.', type: 'info' },
        { prefix: 'WEATHER', msg: 'Hava durumu: KAR (Sıcaklık: -20°C)', type: 'info' },
        { prefix: 'ULUMA', msg: '"Kar yağıyor, izler siliniyor..."', type: 'success' },
        { prefix: 'BÖRÜ', msg: 'Sürü pusu moduna geçti (Range: 4)', type: 'info' },
        { prefix: 'SYSTEM', msg: 'Enerji sınırı kontrol ediliyor (Limit: 15)', type: 'info' },
        { prefix: 'ALERT', msg: 'Koyun sürüsü hilal çemberine girdi!', type: 'alert' },
        { prefix: 'ACTION', msg: 'Saldırı başlatıldı: %85 başarı olasılığı.', type: 'success' },
        { prefix: 'SYSTEM', msg: 'Av tamamlandı. Sürü enerjisi yenileniyor.', type: 'info' }
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
