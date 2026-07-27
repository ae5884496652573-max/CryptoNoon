
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Noon</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            background-color: #0b0808;
            color: #ffffff;
            font-family: Tahoma, sans-serif;
            margin: 0;
            padding: 10px;
            padding-bottom: 90px;
        }
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px;
            margin-bottom: 5px;
        }
        .profile-area {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .logo {
            width: 45px;
            height: 45px;
            background: linear-gradient(135deg, #e50914, #8b0000);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: #fff;
            font-size: 18px;
            box-shadow: 0 0 10px rgba(229, 9, 20, 0.5);
        }
        .title-text h2 { margin: 0; font-size: 16px; color: #ff3333; }
        .title-text p { margin: 0; font-size: 12px; color: #999; text-align: center; }
        
        .balance-card {
            background: linear-gradient(135deg, #170d0d, #0f0707);
            border: 1px solid #e5091444;
            border-radius: 16px;
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }
        .points-box h3 { margin: 0; font-size: 12px; color: #ff6666; }
        .points-box .num { font-size: 20px; font-weight: bold; color: #fff; direction: ltr; text-align: right; }
        
        .coin-icon {
            width: 55px;
            height: 55px;
            background: radial-gradient(circle, #ffee58 0%, #fdd835 70%, #fbc02d 100%);
            border: 4px solid #f57f17;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 900;
            color: #fffde7;
            font-size: 20px;
            text-shadow: 2px 2px 0px #b71c1c;
            box-shadow: 0 0 15px rgba(253, 216, 53, 0.6);
        }
        
        .section-title {
            text-align: center;
            color: #ff3333;
            margin-bottom: 15px;
            font-size: 16px;
            font-weight: bold;
        }
        
        .card-box {
            background-color: #120909;
            border: 1px solid #e5091433;
            border-radius: 14px;
            padding: 15px;
            margin-bottom: 15px;
            text-align: center;
        }

        .quest-card {
            background-color: #120909;
            border: 1px solid #e5091433;
            border-radius: 12px;
            padding: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .quest-left {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 13px;
        }
        .reward-badge {
            background-color: #240c0c;
            color: #ff6666;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 12px;
            border: 1px solid #e5091444;
        }
        .go-btn {
            background: linear-gradient(135deg, #e50914, #990000);
            color: #fff;
            border: none;
            padding: 8px 18px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            font-size: 13px;
        }
        .timer-btn {
            background: linear-gradient(135deg, #555, #333);
            color: #ffcc00;
            border: none;
            padding: 8px 12px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 11px;
            cursor: default;
        }
        .claim-btn {
            background: linear-gradient(135deg, #ff9800, #e65100);
            color: #fff;
            border: none;
            padding: 8px 14px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            font-size: 12px;
        }
        .done-btn {
            background-color: #222;
            color: #777;
            border: 1px solid #444;
            padding: 8px 18px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 12px;
            cursor: default;
        }
        
        .action-btn {
            background: linear-gradient(135deg, #e50914, #990000);
            color: #fff;
            border: none;
            padding: 12px;
            border-radius: 12px;
            font-weight: bold;
            cursor: pointer;
            font-size: 15px;
            width: 100%;
            box-shadow: 0 4px 15px rgba(229, 9, 20, 0.4);
        }
        .action-btn.disabled {
            background: #222;
            color: #666;
            cursor: not-allowed;
            box-shadow: none;
        }

        .page-content { display: none; }
        .page-content.active-page { display: block; }

        .nav-bar {
            position: fixed;
            bottom: 0; left: 0; right: 0;
            background-color: #0b0808;
            border-top: 1px solid #1f0e0e;
            display: flex;
            justify-content: space-around;
            padding: 10px 0;
            z-index: 100;
        }
        .nav-item { text-align: center; color: #666; font-size: 11px; cursor: pointer; }
        .nav-item.active { color: #e50914; }
        
        .copy-box-wrapper {
            display: flex;
            background: #080505;
            border: 1px solid #e5091444;
            border-radius: 10px;
            overflow: hidden;
            margin: 10px 0;
            align-items: center;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            background: transparent;
            border: none;
            color: #fff;
            text-align: right;
            font-size: 12px;
            outline: none;
        }
        .copy-icon-btn {
            background: linear-gradient(135deg, #e50914, #990000);
            border: none;
            color: #fff;
            padding: 10px 15px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div class="header">
        <div class="profile-area">
            <div class="logo">CN</div>
            <div class="title-text">
                <h2>Crypto Noon</h2>
                <p>تعدين سحابي</p>
            </div>
        </div>
    </div>

    <!-- صفحة التعدين -->
    <div id="page-mining" class="page-content active-page">
        <div class="section-title">⛏ التعدين</div>
        
        <div class="card-box" style="background: linear-gradient(135deg, #120909, #1c0a0a); border: 2px solid #e5091466;">
            <p style="color: #ff9999; font-size: 13px; margin: 0;">سرعة التعدين</p>
            <h3 style="color: #fff; font-size: 22px;" id="miningSpeedDisplay">1.0 درجة/ساعة ⚡</h3>
            <div style="font-size: 40px; margin: 15px 0;">⚡</div>
            <p style="color: #ff6666; font-size: 12px;" id="miningTimerText">جاهز لبدء التعدين!</p>
            
            <button class="action-btn" id="claimMiningBtn" onclick="claimMiningReward()">بدء التعدين ⚡</button>
        </div>

        <div class="balance-card">
            <div class="points-box">
                <h3>رصيدك الحالي</h3>
                <div class="num" id="userBalanceDisplay">0.0000000000000 LTC</div>
            </div>
            <div class="coin-icon">Ł</div>
        </div>
    </div>

    <!-- صفحة المهام -->
    <div id="page-tasks" class="page-content">
        <div class="section-title">📋 المهام</div>
        <div style="text-align: center; font-size: 12px; color: #aaa; margin-bottom: 10px;">أكمل المهام لزيادة سرعة التعدين (تتجدد كل 24 ساعة)</div>
        <div id="tasksListContainer"></div>
        
        <div class="card-box" style="margin-top: 15px;">
            <p style="font-size: 13px; color: #ff6666; margin: 0;">سرعة التعدين الحالية</p>
            <h3 style="color: #fff; font-size: 20px;" id="tasksSpeedFooter">1.0 درجة/ساعة ⚡</h3>
        </div>
    </div>

    <!-- صفحة دعوة الأصدقاء -->
    <div id="page-referral" class="page-content">
        <div class="section-title">👥 دعوة الأصدقاء</div>
        
        <div class="card-box">
            <p style="font-size: 13px; color: #ff9999; margin: 0;">إجمالي الأصدقاء المدعوين (أتموا 3 مهام)</p>
            <h3 style="color: #fff; font-size: 28px;" id="totalValidRefs">0</h3>
            <p style="font-size: 11px; color: #aaa;">كل صديق تدعوه ويفعل 3 مهام يزيد سرعة التعدين 1.5 درجة</p>
        </div>

        <div class="card-box" style="text-align: right;">
            <p style="font-size: 12px; color: #ff6666; margin-top: 0;">رابط دعوتك الفريد</p>
            <div class="copy-box-wrapper">
                <input type="text" readonly id="refLink">
                <button class="copy-icon-btn" onclick="copyRef()">📋</button>
            </div>
            <button class="go-btn" style="width: 100%; margin-top: 5px;" onclick="copyRef()">مشاركة الرابط</button>
        </div>
    </div>

    <!-- صفحة السحب -->
    <div id="page-withdraw" class="page-content">
        <div class="section-title">💰 السحب</div>

        <div class="balance-card">
            <div class="points-box">
                <h3>رصيدك الحالي</h3>
                <div class="num" id="withdrawBalanceDisplay">0.0000000000000 LTC</div>
            </div>
            <div class="coin-icon">Ł</div>
        </div>

        <div class="card-box" style="text-align: right; font-size: 11px; line-height: 1.8; color: #ccc;">
            <div style="color: #ff3333; font-weight: bold; margin-bottom: 5px;">شروط السحب:</div>
            • الحد الأدنى للسحب: 0.001 LTC<br>
            • يجب دعوة 3 أصدقاء أتموا 3 مهام لفتح السحب.<br>
            • دفع فوري ومراجعة يدوية.
        </div>

        <!-- شروط مغلقة -->
        <div class="card-box" id="withdrawLockedBox">
            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 10px;">
                <span style="color: #ff6666;">السحب مغلق</span>
                <span id="withdrawConditionsText">0 / 3 أصدقاء</span>
            </div>
            <!-- خانات العنوان والمبلغ مقفلة وغير مفعلة حتى اكتمال الشروط -->
            <input type="text" placeholder="عنوان محفظة LTC..." disabled style="border: 1px solid #444; border-radius: 8px; margin-bottom: 8px; background: #1a1a1a; text-align: left; direction: ltr; width: 100%; opacity: 0.5; cursor: not-allowed;">
            <input type="text" placeholder="المبلغ المراد سحبه..." disabled style="border: 1px solid #444; border-radius: 8px; margin-bottom: 10px; background: #1a1a1a; text-align: left; direction: ltr; width: 100%; opacity: 0.5; cursor: not-allowed;">
            <button class="action-btn disabled">🔒 أتمم الشروط والحد الأدنى لفتح السحب</button>
        </div>

        <!-- شروط مفتوحة -->
        <div class="card-box" id="withdrawActiveBox" style="display: none; border-color: #00ff6644;">
            <div style="color: #00ff66; font-weight: bold; font-size: 13px; margin-bottom: 8px;">🎉 مبروك! استوفيت كافة الشروط والحد الأدنى</div>
            <input type="text" id="ltcWalletInput" placeholder="عنوان محفظة LTC..." style="border: 1px solid #e5091444; border-radius: 8px; margin-bottom: 8px; background: #050b05; text-align: left; direction: ltr; width: 100%;">
            <input type="text" id="ltcAmountInput" placeholder="المبلغ المراد سحبه..." style="border: 1px solid #e5091444; border-radius: 8px; margin-bottom: 10px; background: #050b05; text-align: left; direction: ltr; width: 100%;">
            <button class="action-btn" onclick="submitWithdrawal()">تأكيد وإرسال السحب</button>
        </div>
    </div>

    <!-- شريط التنقل السفلي -->
    <div class="nav-bar">
        <div class="nav-item" id="nav-mining" onclick="switchPage('mining')">
            <div style="font-size: 16px;">⛏</div>
            <div>التعدين</div>
        </div>
        <div class="nav-item" id="nav-tasks" onclick="switchPage('tasks')">
            <div style="font-size: 16px;">📋</div>
            <div>المهام</div>
        </div>
        <div class="nav-item" id="nav-referral" onclick="switchPage('referral')">
            <div style="font-size: 16px;">👥</div>
            <div>دعوة الأصدقاء</div>
        </div>
        <div class="nav-item" id="nav-withdraw" onclick="switchPage('withdraw')">
            <div style="font-size: 16px;">💰</div>
            <div>السحب</div>
        </div>
    </div>

    <script>
        let tg = window.Telegram.WebApp;
        tg.expand();

        let userId = (tg.initDataUnsafe && tg.initDataUnsafe.user && tg.initDataUnsafe.user.id) ? tg.initDataUnsafe.user.id : 'user_' + Math.floor(Math.random() * 1000000);
        document.getElementById('refLink').value = `https://t.me/CryptoNoon_bot?start=${userId}`;

        let userBalance = parseFloat(localStorage.getItem(`balance_${userId}`)) || 0.0000000000000;
        let miningSpeed = parseFloat(localStorage.getItem(`speed_${userId}`)) || 1.0;
        let validReferrals = parseInt(localStorage.getItem(`valid_refs_${userId}`)) || 0;
        let completedTasksCount = parseInt(localStorage.getItem(`completed_tasks_count_${userId}`)) || 0;

        let miningActiveTime = parseInt(localStorage.getItem(`mining_active_${userId}`)) || 0;
        let dayDuration = 24 * 60 * 60 * 1000;

        // الـ 26 مهمة
        const tasksData = [
            { id: 1, name: "1", url: "https://www.effectivecpmnetwork.com/e1jv2pcy?key=77476a8369e329e1fa7ad6b0ae311ba1", rewardSpeed: 1.0 },
            { id: 2, name: "2", url: "https://cryptonoon1620.blogspot.com/2026/07/crypto-noon.html", rewardSpeed: 1.0 },
            { id: 3, name: "3", url: "https://www.effectivecpmnetwork.com/terq9a3knf?key=7a439631c15e62f5d4888121bf680877", rewardSpeed: 1.5 },
            { id: 4, name: "4", url: "https://cryptonoon1620.blogspot.com/2026/07/blog-post.html", rewardSpeed: 1.0 },
            { id: 5, name: "5", url: "https://www.effectivecpmnetwork.com/w0u75hpnp3?key=f8394ea18f3a85a12298d2957018b97d", rewardSpeed: 2.0 },
            { id: 6, name: "6", url: "https://cryptonoon1620.blogspot.com/2026/07/titulo-gana-litecoin-ltc-gratis-cada-24.html", rewardSpeed: 1.0 },
            { id: 7, name: "7", url: "https://www.effectivecpmnetwork.com/j3xv3g89p0?key=b2cc5150bbf296c877ddc3b288fec6a0", rewardSpeed: 1.0 },
            { id: 8, name: "8", url: "https://cryptonoon1620.blogspot.com/2026/07/usdt.html", rewardSpeed: 1.0 },
            { id: 9, name: "9", url: "https://www.effectivecpmnetwork.com/hu5guhh3u9?key=ba1544dab1fec964178780783a4a5190", rewardSpeed: 1.0 },
            { id: 10, name: "10", url: "https://cryptonoon1620.blogspot.com/2026/06/usdt-24-crypto-noon.html", rewardSpeed: 1.0 },
            { id: 11, name: "11", url: "https://www.effectivecpmnetwork.com/h5wyif9di?key=641c0529816c11fd32dc9e45c8fae79f", rewardSpeed: 1.0 },
            { id: 12, name: "12", url: "https://cryptonoon1620.blogspot.com/2026/06/usdt.html", rewardSpeed: 1.0 },
            { id: 13, name: "13", url: "https://www.effectivecpmnetwork.com/pemsfhpi5?key=81b5bc182d0e7d2fcec176be1c616de1", rewardSpeed: 1.0 },
            { id: 14, name: "14", url: "https://cryptonoon1620.blogspot.com/2026/06/ltc.html", rewardSpeed: 1.0 },
            { id: 15, name: "15", url: "https://www.effectivecpmnetwork.com/xqb3qn9u4y?key=f894c62084b213c3217d727e0a486771", rewardSpeed: 1.0 },
            { id: 16, name: "16", url: "https://www.effectivecpmnetwork.com/r0rja3wf75?key=3417547a6a65b4a22c818a23b8b23a7e", rewardSpeed: 1.0 },
            { id: 17, name: "17", url: "https://www.effectivecpmnetwork.com/ae3a455nh?key=37e28d5e64dfbb4e19333f02371c60c5", rewardSpeed: 1.0 },
            { id: 18, name: "18", url: "https://www.effectivecpmnetwork.com/ns0jm5q4j?key=7eb99e524eab56a0b81a052f402b6955", rewardSpeed: 1.0 },
            { id: 19, name: "19", url: "https://www.effectivecpmnetwork.com/hkk75b737?key=7f5b6b3e36bc30e21ae7f39359511d59", rewardSpeed: 1.0 },
            { id: 20, name: "20", url: "https://www.effectivecpmnetwork.com/xg72z66vc?key=01df2103694bafb9aa384cdcfc5bfce6", rewardSpeed: 1.0 },
            { id: 21, name: "21", url: "https://www.effectivecpmnetwork.com/xvp3c8hne?key=48617207cfe61c9343393efb8a1fea69", rewardSpeed: 1.0 },
            { id: 22, name: "22", url: "https://www.effectivecpmnetwork.com/icqhaii7ey?key=dd164c2d22476a976bd4e7f0d388c950", rewardSpeed: 1.0 },
            { id: 23, name: "23", url: "https://www.effectivecpmnetwork.com/hmbuzgyrk?key=ea132f5736904c5804a0fe84eaedb2cb", rewardSpeed: 1.0 },
            { id: 24, name: "24", url: "https://www.effectivecpmnetwork.com/xe20c05b?key=8b26036cd5da361c818e25029eb3cafc", rewardSpeed: 1.0 },
            { id: 25, name: "25", url: "https://www.effectivecpmnetwork.com/vyfm3c2a?key=0c1a0ee2d0a6d7b45fa82f8bd6d390ee", rewardSpeed: 1.0 },
            { id: 26, name: "26", url: "https://www.effectivecpmnetwork.com/e7awg98hn?key=dd81476a2a21061829d19c2b9fc16340", rewardSpeed: 1.0 }
        ];

        function updateUI() {
            document.getElementById('userBalanceDisplay').innerText = userBalance.toFixed(13) + " LTC";
            document.getElementById('withdrawBalanceDisplay').innerText = userBalance.toFixed(13) + " LTC";
            document.getElementById('miningSpeedDisplay').innerText = miningSpeed.toFixed(1) + " درجة/ساعة ⚡";
            document.getElementById('tasksSpeedFooter').innerText = miningSpeed.toFixed(1) + " درجة/ساعة ⚡";
            document.getElementById('totalValidRefs').innerText = validReferrals;

            localStorage.setItem(`balance_${userId}`, userBalance);
            localStorage.setItem(`speed_${userId}`, miningSpeed);
            localStorage.setItem(`valid_refs_${userId}`, validReferrals);
            localStorage.setItem(`completed_tasks_count_${userId}`, completedTasksCount);

            checkWithdrawStatus();
        }

        // تم جعل سرعة التعدين أبطأ بكثير جداً (أبطأ من السابق بكثير)
        setInterval(() => {
            let currentTime = new Date().getTime();
            let claimBtn = document.getElementById('claimMiningBtn');
            let timerText = document.getElementById('miningTimerText');

            if (miningActiveTime === 0) {
                timerText.innerText = "جاهز لبدء التعدين!";
                claimBtn.classList.remove('disabled');
                claimBtn.innerText = "بدء التعدين ⚡";
            } else {
                let elapsed = currentTime - miningActiveTime;
                let remaining = dayDuration - elapsed;

                if (remaining <= 0) {
                    timerText.innerText = "انتهى التعدين! اضغط لبدء دورة جديدة ✔";
                    claimBtn.classList.remove('disabled');
                    claimBtn.innerText = "بدء دورة جديدة ⚡";
                } else {
                    // تم تقليل معامل التعدين بشكل كبير ليكون بطيئاً جداً
                    userBalance += (miningSpeed * 0.000000000000005);
                    updateUI();

                    let hours = Math.floor((remaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    let minutes = Math.floor((remaining % (1000 * 60 * 60)) / (1000 * 60));
                    let seconds = Math.floor((remaining % (1000 * 60)) / 1000);
                    timerText.innerText = `جاري التعدين... ${hours.toString().padStart(2,'0')}:${minutes.toString().padStart(2,'0')}:${seconds.toString().padStart(2,'0')}`;
                    claimBtn.classList.add('disabled');
                    claimBtn.innerText = "قيد التعدين (24 ساعة)";
                }
            }
        }, 1000);

        function claimMiningReward() {
            let currentTime = new Date().getTime();
            if (miningActiveTime === 0 || (currentTime - miningActiveTime >= dayDuration)) {
                miningActiveTime = currentTime;
                localStorage.setItem(`mining_active_${userId}`, miningActiveTime);
                alert("🚀 تم بدء دورة التعدين بنجاح!");
            }
        }

        function renderTasks() {
            let container = document.getElementById('tasksListContainer');
            container.innerHTML = "";

            tasksData.forEach(task => {
                let state = localStorage.getItem(`task_state_${userId}_${task.id}`) || 'go';
                let btnHTML = "";

                if (state === 'go') {
                    btnHTML = `<button class="go-btn" onclick="startTask(${task.id}, '${task.url}')">ابدأ</button>`;
                } else if (state === 'waiting') {
                    btnHTML = `<button class="timer-btn" id="task_timer_${task.id}">انتظر 20 ثانية...</button>`;
                } else if (state === 'claim') {
                    btnHTML = `<button class="claim-btn" onclick="claimTask(${task.id}, ${task.rewardSpeed})">اضغط للاستلام</button>`;
                } else {
                    btnHTML = `<button class="done-btn">تم الاستلام ✔</button>`;
                }

                container.innerHTML += `
                    <div class="quest-card">
                        ${btnHTML}
                        <div class="quest-left">
                            <span class="reward-badge">+${task.rewardSpeed} سرعة</span>
                            <span>مهمة ${task.name}</span>
                        </div>
                    </div>
                `;
            });
        }

        function startTask(id, url) {
            window.open(url, '_blank');
            localStorage.setItem(`task_state_${userId}_${id}`, 'waiting');
            renderTasks();

            let timeLeft = 20;
            let btn = document.getElementById(`task_timer_${id}`);

            let timer = setInterval(() => {
                timeLeft--;
                if (btn) btn.innerText = `انتظر ${timeLeft} ثانية...`;
                if (timeLeft <= 0) {
                    clearInterval(timer);
                    localStorage.setItem(`task_state_${userId}_${id}`, 'claim');
                    renderTasks();
                }
            }, 1000);
        }

        function claimTask(id, rewardSpeed) {
            miningSpeed += rewardSpeed;
            completedTasksCount++;
            
            if (completedTasksCount >= 3) {
                validReferrals = Math.max(validReferrals, 3); 
            }

            localStorage.setItem(`task_state_${userId}_${id}`, 'done');
            updateUI();
            renderTasks();
            alert(`تم إضافة +${rewardSpeed} لسرعة التعدين بنجاح!`);
        }

        function checkWithdrawStatus() {
            let lockedBox = document.getElementById('withdrawLockedBox');
            let activeBox = document.getElementById('withdrawActiveBox');
            let textStatus = document.getElementById('withdrawConditionsText');

            // الشرط الصارم: يجب أن يصل الرصيد إلى 0.001 LTC على الأقل + 3 إحالات/مهام مقبولة
            if (userBalance >= 0.001 && validReferrals >= 3) {
                lockedBox.style.display = 'none';
                activeBox.style.display = 'block';
            } else {
                lockedBox.style.display = 'block';
                activeBox.style.display = 'none';
                textStatus.innerText = `${validReferrals} / 3 أصدقاء (${userBalance.toFixed(5)} / 0.001 LTC)`;
            }
        }

        function submitWithdrawal() {
            let wallet = document.getElementById('ltcWalletInput').value.trim();
            let amount = parseFloat(document.getElementById('ltcAmountInput').value.trim());

            if (!wallet || isNaN(amount)) {
                alert("الرجاء إدخال المحفظة والمبلغ المطلوب بشكل صحيح!");
                return;
            }

            // منع السحب نهائياً إذا كان المبلغ أقل من الحد الأدنى أو الرصيد لا يكفي
            if (amount < 0.001 || amount > userBalance) {
                alert("❌ عذراً، لا يمكن إتمام السحب. تأكد أن المبلغ لا يقل عن الحد الأدنى (0.001 LTC) وأنه متوفر في رصيدك!");
                return;
            }

            let now = new Date();
            let timeString = now.toLocaleTimeString();
            let dateString = now.toLocaleDateString();

            alert(`🔔 تم إرسال طلب السحب بنجاح!\n\n• المبلغ: ${amount} LTC\n• المحفظة: ${wallet}\n• الأيدي: ${userId}\n• الوقت: ${timeString} - ${dateString}`);
            
            userBalance -= amount;
            updateUI();
        }

        function copyRef() {
            let refInput = document.getElementById("refLink");
            refInput.select();
            navigator.clipboard.writeText(refInput.value);
            alert("تم نسخ رابط الدعوة الفريد الخاص بك بنجاح!");
        }

        function switchPage(pageName) {
            document.querySelectorAll('.page-content').forEach(p => p.classList.remove('active-page'));
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));

            document.getElementById(`page-${pageName}`).classList.add('active-page');
            document.getElementById(`nav-${pageName}`).classList.add('active');

            if (pageName === 'tasks') renderTasks();
        }

        updateUI();
        switchPage('mining');
    </script>
</body>
</html>

