import re
import os

with open(r'c:\Users\ZhuFan\Desktop\AgencyWebsite\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open(r'c:\Users\ZhuFan\Desktop\AgencyWebsite\niche_data.js', 'r', encoding='utf-8') as f:
    js_data = f.read()

# 1. Update <style> block
new_styles = """
        /* Interactive Hover Effects */
        .card-hover {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card-hover:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }

        /* Fake WhatsApp Proof */
        .wa-wall {
            background-color: #EFEAE2;
            background-image: url('https://www.transparenttextures.com/patterns/cubes.png');
        }

        .wa-msg {
            background: #FFF;
            border-radius: 8px 0px 8px 8px;
            padding: 12px 16px;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
            position: relative;
            margin-bottom: 1rem;
            width: fit-content;
            max-width: 90%;
        }

        .wa-msg::after {
            content: '';
            position: absolute;
            top: 0;
            right: -8px;
            border-top: 0px solid transparent;
            border-left: 8px solid #FFF;
            border-bottom: 10px solid transparent;
        }

        /* Float Animation */
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
        }

        .floating-btn {
            animation: float 3s ease-in-out infinite;
        }

        /* Button Glow Animation */
        @keyframes glow {
            0% { box-shadow: 0 0 5px rgba(227, 0, 15, 0.2); }
            50% { box-shadow: 0 0 20px rgba(227, 0, 15, 0.7), 0 0 30px rgba(227, 0, 15, 0.5); }
            100% { box-shadow: 0 0 5px rgba(227, 0, 15, 0.2); }
        }

        .btn-glow {
            animation: glow 2s ease-in-out infinite;
        }
        
        /* Modal & Table Styles */
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.6);
            backdrop-filter: blur(4px);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .modal.show {
            display: flex;
            opacity: 1;
            align-items: center;
            justify-content: center;
        }
        .modal-content {
            background-color: #fff;
            margin: auto;
            border-radius: 12px;
            width: 95%;
            max-width: 1000px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            transform: scale(0.95);
            transition: transform 0.3s ease;
            display: flex;
            flex-direction: column;
            max-height: 90vh;
        }
        .modal.show .modal-content {
            transform: scale(1);
        }
        .table-container {
            overflow-x: auto;
            border-radius: 0 0 12px 12px;
            max-height: calc(90vh - 80px); /* header height */
            background-color: #f8f9fa;
        }
        .sheet-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            background: #fff;
        }
        .sheet-table th, .sheet-table td {
            border: 1px solid #e2e8f0;
            padding: 12px 16px;
            text-align: left;
            white-space: nowrap;
        }
        .sheet-table th {
            background-color: #f1f5f9;
            color: #475569;
            font-weight: 700;
            position: sticky;
            top: 0;
            z-index: 10;
        }
        .sheet-table tr:hover {
            background-color: #f8fafc;
        }
        .blur-text {
            filter: blur(3px);
            user-select: none;
            transition: filter 0.3s ease;
            cursor: pointer;
        }
        .blur-text:hover {
            filter: blur(1px);
        }
        .copy-icon {
            cursor: pointer;
            color: #94a3b8;
            transition: color 0.2s;
        }
        .copy-icon:hover {
            color: #111;
        }
        .tooltip {
            position: relative;
            display: inline-block;
        }
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 220px;
            background-color: #111;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 8px;
            position: absolute;
            z-index: 100;
            bottom: 125%;
            left: 50%;
            margin-left: -110px;
            opacity: 0;
            transition: opacity 0.3s;
            font-size: 12px;
            font-weight: bold;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        
        /* Tabs Styles */
        .tab-content {
            display: none;
            animation: fadeIn 0.4s ease;
        }
        .tab-content.active {
            display: block;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(5px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .tab-btn {
            border-bottom: 2px solid transparent;
            transition: all 0.3s;
        }
        .tab-btn.active {
            border-bottom-color: #E3000F;
            color: #E3000F;
            font-weight: 800;
        }

        /* Accordion Styles */
        .accordion-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease-out;
            background-color: #fff;
        }
        .accordion-header.active {
            background-color: #f8fafc;
            border-left: 4px solid #E3000F;
        }
        .accordion-header.active .icon-chevron {
            transform: rotate(180deg);
        }
"""
html = re.sub(r'/\* Interactive Hover Effects \*/.*?(?=</style>)', new_styles, html, flags=re.DOTALL)

# 2. Main content replacement
new_section = """
    <section class="py-16 px-4 bg-gray-50 border-y border-gray-200" id="library">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-black text-gerBlack mb-4">مكتبة DossierPro: كل ما تحتاجه للنجاح <span class="text-gerRed">مجاناً</span> 🎁</h2>
                <p class="text-gray-600 font-semibold text-lg max-w-2xl mx-auto">أدوات حصرية لمساعدتك في الحصول على عقد العمل. تصفح وحمل ما تحتاجه.</p>
            </div>

            <!-- 1. Interactive Spreadsheet Pop-up -->
            <div class="bg-white rounded-3xl p-8 md:p-10 shadow-sm border border-gray-200 mb-12">
                <div class="flex flex-col md:flex-row items-center justify-between gap-8">
                    <div class="text-right flex-1">
                        <div class="inline-block bg-green-100 text-green-700 font-bold px-3 py-1 rounded-full text-sm mb-4 font-inter">Live Preview</div>
                        <h3 class="text-2xl md:text-3xl font-black text-gerBlack mb-4">قاعدة بيانات الشركات النشطة (عينة 20 إيميل) 🏢</h3>
                        <p class="text-gray-600 font-semibold text-lg mb-6 leading-relaxed">
                            اختر التخصص ديالك وشوف عينة من الشركات الحقيقية لي كاتقلب على متدربين (Azubis) هاد السيمانة. اللائحة الكاملة (Profi-Liste) فيها 1000+ شركة.
                        </p>
                        
                        <div class="flex flex-wrap gap-3 justify-end dir-rtl">
                            <button onclick="openModal('Nursing')" class="bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 font-bold py-2.5 px-5 rounded-xl transition-all flex items-center gap-2"><i class="fa-solid fa-user-nurse"></i> Pflege (تمريض)</button>
                            <button onclick="openModal('IT')" class="bg-purple-50 hover:bg-purple-100 text-purple-700 border border-purple-200 font-bold py-2.5 px-5 rounded-xl transition-all flex items-center gap-2"><i class="fa-solid fa-code"></i> Informatik (IT)</button>
                            <button onclick="openModal('Mechatronics')" class="bg-orange-50 hover:bg-orange-100 text-orange-700 border border-orange-200 font-bold py-2.5 px-5 rounded-xl transition-all flex items-center gap-2"><i class="fa-solid fa-cogs"></i> Mechatronik (ميكاترونيك)</button>
                            <button onclick="openModal('Logistics')" class="bg-cyan-50 hover:bg-cyan-100 text-cyan-700 border border-cyan-200 font-bold py-2.5 px-5 rounded-xl transition-all flex items-center gap-2"><i class="fa-solid fa-box"></i> Logistik (لوجستيك)</button>
                            <button onclick="openModal('Gastronomy')" class="bg-rose-50 hover:bg-rose-100 text-rose-700 border border-rose-200 font-bold py-2.5 px-5 rounded-xl transition-all flex items-center gap-2"><i class="fa-solid fa-utensils"></i> Gastronomie (فندقة)</button>
                        </div>
                    </div>
                    <div class="w-full md:w-1/3 flex justify-center">
                        <div class="relative w-48 h-48 bg-gray-100 rounded-2xl flex items-center justify-center border-4 border-white shadow-xl transform rotate-3 hover:rotate-0 transition-all duration-300">
                            <i class="fa-solid fa-table text-5xl text-gray-400"></i>
                            <div class="absolute -top-3 -right-3 bg-gerRed text-white font-black w-10 h-10 flex items-center justify-center rounded-full shadow-lg">+20</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 2. German CV Muster Preview -->
            <div class="bg-gerBlack rounded-3xl p-8 md:p-10 shadow-lg text-white mb-12 relative overflow-hidden">
                <div class="absolute top-0 right-0 w-64 h-64 bg-gerGold opacity-10 rounded-full blur-3xl transform translate-x-1/2 -translate-y-1/2"></div>
                <h3 class="text-2xl md:text-3xl font-black mb-2 text-right">Standard German CV (Muster) 📄</h3>
                <p class="text-gray-400 font-semibold mb-8 text-right">الهيكل الصحيح الذي تقبله أنظمة ATS الألمانية (بدون زينة مبالغ فيها).</p>
                
                <div class="bg-white text-gerBlack rounded-xl p-1 font-inter overflow-hidden border border-gray-700 mb-6">
                    <table class="w-full text-left text-sm">
                        <tr class="border-b border-gray-100 bg-gray-50">
                            <th class="py-3 px-4 w-1/4 font-black">Abschnitt</th>
                            <th class="py-3 px-4 font-black">Inhalt (Content to Include)</th>
                        </tr>
                        <tr class="border-b border-gray-100">
                            <td class="py-3 px-4 font-bold text-gray-700">Persönliche Daten</td>
                            <td class="py-3 px-4 text-gray-600">Name, Address, Email, Phone, Date of Birth (optional), Nationality. <span class="text-xs bg-red-100 text-red-600 px-2 py-0.5 rounded font-bold ml-2">No Photo req.</span></td>
                        </tr>
                        <tr class="border-b border-gray-100 bg-gray-50">
                            <td class="py-3 px-4 font-bold text-gray-700">Schulbildung</td>
                            <td class="py-3 px-4 text-gray-600">Reverse chronological. High School Diploma, Equivalences, Exact Dates (MM.YYYY - MM.YYYY).</td>
                        </tr>
                        <tr class="border-b border-gray-100">
                            <td class="py-3 px-4 font-bold text-gray-700">Berufserfahrung</td>
                            <td class="py-3 px-4 text-gray-600">Internships, Part-time jobs. Focus on transferable skills relevant to the Ausbildung.</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 font-bold text-gray-700">Sprachkenntnisse & IT</td>
                            <td class="py-3 px-4 text-gray-600">Deutsch (B1/B2 - Goethe/Telc), English (Level). MS Office, Specific Software.</td>
                        </tr>
                    </table>
                </div>
                
                <div class="text-right">
                    <a href="#" class="inline-flex items-center gap-2 bg-gerGold hover:bg-yellow-400 text-gerBlack font-black py-3 px-6 rounded-xl transition-colors shadow-md">
                        <i class="fa-solid fa-file-pdf"></i> تحميل القالب (Word/PDF)
                    </a>
                </div>
            </div>

            <!-- 3. Motivation Letter Hub -->
            <div class="bg-white rounded-3xl p-8 shadow-sm border border-gray-200 mb-12">
                <h3 class="text-2xl md:text-3xl font-black text-gerBlack mb-2 text-right">أقوى قوالب الـ Anschreiben (رسالة التحفيز) 🖋️</h3>
                <p class="text-gray-600 font-semibold mb-8 text-right">رسالة التحفيز هي المفتاح. كل تخصص يحتاج لصياغة تركز على نقاط قوة معينة.</p>
                
                <div class="flex flex-row-reverse overflow-x-auto gap-1 mb-6 border-b border-gray-200 pb-2 hide-scrollbar font-inter font-bold" dir="ltr">
                    <button class="tab-btn active px-4 py-2 text-gray-500 whitespace-nowrap" onclick="switchTab('tab-pflege')">Pflege</button>
                    <button class="tab-btn px-4 py-2 text-gray-500 whitespace-nowrap" onclick="switchTab('tab-it')">Informatik</button>
                    <button class="tab-btn px-4 py-2 text-gray-500 whitespace-nowrap" onclick="switchTab('tab-mech')">Mechatronik</button>
                    <button class="tab-btn px-4 py-2 text-gray-500 whitespace-nowrap" onclick="switchTab('tab-log')">Logistik</button>
                    <button class="tab-btn px-4 py-2 text-gray-500 whitespace-nowrap" onclick="switchTab('tab-gastro')">Gastronomie</button>
                </div>
                
                <div class="bg-gray-50 rounded-xl p-6 font-inter text-left" dir="ltr">
                    <!-- Tab Pflege -->
                    <div id="tab-pflege" class="tab-content active">
                        <h4 class="text-xl font-black text-blue-700 mb-4 border-b border-blue-200 pb-2">Pflegefachmann/Pflegefachfrau Focus</h4>
                        <ul class="space-y-4 text-gray-700">
                            <li><strong class="text-gray-900">Einleitung (Intro):</strong> Focus on your deep desire to help people and your respect for the German healthcare system.</li>
                            <li><strong class="text-gray-900">Warum ich? (Why Me):</strong> Highlight empathy, patience, and 24/7 reliability. Mention any volunteering or family care experience.</li>
                            <li><strong class="text-gray-900">Warum dieser Beruf?:</strong> Explain your resilience and physical/mental fitness to handle stress and shift work.</li>
                            <li><strong class="text-gray-900">Schluss (Closing):</strong> Professional sign-off expressing readiness for a video interview.</li>
                        </ul>
                    </div>
                    <!-- Tab IT -->
                    <div id="tab-it" class="tab-content">
                        <h4 class="text-xl font-black text-purple-700 mb-4 border-b border-purple-200 pb-2">Fachinformatiker Focus</h4>
                        <ul class="space-y-4 text-gray-700">
                            <li><strong class="text-gray-900">Einleitung (Intro):</strong> Connect your passion for technology with the company's specific projects or stack.</li>
                            <li><strong class="text-gray-900">Warum ich? (Why Me):</strong> Focus on logical thinking, problem-solving skills, and self-taught programming languages or homelab setups.</li>
                            <li><strong class="text-gray-900">Warum dieser Beruf?:</strong> Emphasize continuous learning and your drive to build efficient digital solutions.</li>
                            <li><strong class="text-gray-900">Schluss (Closing):</strong> Link to a GitHub profile or portfolio if available, state availability.</li>
                        </ul>
                    </div>
                    <!-- Tab Mechatronics -->
                    <div id="tab-mech" class="tab-content">
                        <h4 class="text-xl font-black text-orange-700 mb-4 border-b border-orange-200 pb-2">Mechatroniker Focus</h4>
                        <ul class="space-y-4 text-gray-700">
                            <li><strong class="text-gray-900">Einleitung (Intro):</strong> Express fascination for the combination of mechanics, electronics, and IT.</li>
                            <li><strong class="text-gray-900">Warum ich? (Why Me):</strong> Highlight manual dexterity, spatial awareness, and precision in your work.</li>
                            <li><strong class="text-gray-900">Warum dieser Beruf?:</strong> Focus on your mechanical understanding and safety awareness.</li>
                            <li><strong class="text-gray-900">Schluss (Closing):</strong> Mention willingness to do a trial internship (Praktikum) if required.</li>
                        </ul>
                    </div>
                    <!-- Tab Logistics -->
                    <div id="tab-log" class="tab-content">
                        <h4 class="text-xl font-black text-cyan-700 mb-4 border-b border-cyan-200 pb-2">Fachkraft für Lagerlogistik Focus</h4>
                        <ul class="space-y-4 text-gray-700">
                            <li><strong class="text-gray-900">Einleitung (Intro):</strong> Highlight your understanding of precise supply chain operations.</li>
                            <li><strong class="text-gray-900">Warum ich? (Why Me):</strong> Focus on strict organization, physical stamina, and logical arrangement skills.</li>
                            <li><strong class="text-gray-900">Warum dieser Beruf?:</strong> Emphasize your ability to work accurately under time pressure.</li>
                            <li><strong class="text-gray-900">Schluss (Closing):</strong> State willingness to work in shift systems.</li>
                        </ul>
                    </div>
                    <!-- Tab Gastro -->
                    <div id="tab-gastro" class="tab-content">
                        <h4 class="text-xl font-black text-rose-700 mb-4 border-b border-rose-200 pb-2">Gastronomie / Hotelfach Focus</h4>
                        <ul class="space-y-4 text-gray-700">
                            <li><strong class="text-gray-900">Einleitung (Intro):</strong> Show passion for hospitality and delivering excellent guest experiences.</li>
                            <li><strong class="text-gray-900">Warum ich? (Why Me):</strong> Highlight strong communication skills, team-spirit, and an always-friendly demeanor.</li>
                            <li><strong class="text-gray-900">Warum dieser Beruf?:</strong> Address your flexibility with varied working hours and high stress tolerance.</li>
                            <li><strong class="text-gray-900">Schluss (Closing):</strong> Professional sign-off, ready to demonstrate skills in a trial shift.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- 4. The 20 Interview Master-Guide -->
            <div class="bg-white rounded-3xl p-8 shadow-sm border border-gray-200">
                <h3 class="text-2xl md:text-3xl font-black text-gerBlack mb-2 text-right">The 20 Interview Master-Guide 🎤</h3>
                <p class="text-gray-600 font-semibold mb-8 text-right">أهم الأسئلة التي تطرح في مقابلات الـ Ausbildung مقسمة إلى قسمين.</p>
                
                <div class="space-y-4 flex flex-col font-inter" dir="ltr">
                    <!-- Part A -->
                    <div class="border border-gray-200 rounded-xl overflow-hidden">
                        <button class="accordion-header w-full text-left p-5 font-black text-gray-800 bg-white hover:bg-gray-50 transition-colors flex justify-between items-center" onclick="toggleAccordion('acc-a', this)">
                            <span>PART A: Top 10 General Questions</span>
                            <i class="fa-solid fa-chevron-down text-gray-400 icon-chevron transition-transform duration-300"></i>
                        </button>
                        <div id="acc-a" class="accordion-content">
                            <div class="p-5 border-t border-gray-100 bg-gray-50">
                                <ol class="list-decimal pl-5 space-y-3 text-sm text-gray-700 font-medium">
                                    <li><strong class="text-black">Stellen Sie sich bitte kurz vor.</strong> (Introduce yourself)</li>
                                    <li><strong class="text-black">Warum möchten Sie eine Ausbildung in Deutschland machen?</strong> (Why Germany?)</li>
                                    <li><strong class="text-black">Warum haben Sie sich bei unserem Unternehmen beworben?</strong> (Why our company?)</li>
                                    <li><strong class="text-black">Was sind Ihre größten Stärken und Schwächen?</strong> (Strengths/Weaknesses)</li>
                                    <li><strong class="text-black">Wo sehen Sie sich in 3 bis 5 Jahren?</strong> (3-year goals)</li>
                                    <li>Wie gehen Sie mit Kritik um? (Handling criticism)</li>
                                    <li>Haben Sie bereits Erfahrung in diesem Bereich? (Previous experience)</li>
                                    <li>Wie gut ist Ihr Deutsch im Alltag? (Everyday German skills)</li>
                                    <li>Was machen Sie gern in Ihrer Freizeit? (Hobbies - looking for cultural fit)</li>
                                    <li>Haben Sie noch Fragen an uns? (Always have 2 questions prepared!)</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Part B -->
                    <div class="border border-gray-200 rounded-xl overflow-hidden">
                        <button class="accordion-header w-full text-left p-5 font-black text-gray-800 bg-white hover:bg-gray-50 transition-colors flex justify-between items-center" onclick="toggleAccordion('acc-b', this)">
                            <span>PART B: 10 Niche-Specific Questions</span>
                            <i class="fa-solid fa-chevron-down text-gray-400 icon-chevron transition-transform duration-300"></i>
                        </button>
                        <div id="acc-b" class="accordion-content">
                            <div class="p-5 border-t border-gray-100 bg-gray-50">
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm text-gray-700">
                                    <div>
                                        <h5 class="font-black text-blue-700 mb-2 border-b border-blue-200 pb-1">Pflege (Nursing)</h5>
                                        <ul class="list-disc pl-5 space-y-1">
                                            <li>Wie gehen Sie mit Stress und Notfallsituationen um?</li>
                                            <li>Wie reagieren Sie auf unzufriedene oder schwierige Patienten?</li>
                                        </ul>
                                    </div>
                                    <div>
                                        <h5 class="font-black text-purple-700 mb-2 border-b border-purple-200 pb-1">Informatik (IT)</h5>
                                        <ul class="list-disc pl-5 space-y-1">
                                            <li>Wie gehen Sie bei der Fehlersuche (Debugging) vor?</li>
                                            <li>Welche Programmiersprachen haben Sie sich selbst beigebracht?</li>
                                        </ul>
                                    </div>
                                    <div>
                                        <h5 class="font-black text-orange-700 mb-2 border-b border-orange-200 pb-1">Mechatronik</h5>
                                        <ul class="list-disc pl-5 space-y-1">
                                            <li>Was ist für Sie Sicherheit am Arbeitsplatz?</li>
                                            <li>Wie lösen Sie ein Problem, wenn eine Maschine nicht funktioniert?</li>
                                        </ul>
                                    </div>
                                    <div>
                                        <h5 class="font-black text-cyan-700 mb-2 border-b border-cyan-200 pb-1">Logistik</h5>
                                        <ul class="list-disc pl-5 space-y-1">
                                            <li>Wie behalten Sie den Überblick, wenn viele Aufgaben gleichzeitig anfallen?</li>
                                            <li>Haben Sie Erfahrung mit körperlich anstrengender Arbeit?</li>
                                        </ul>
                                    </div>
                                    <div class="md:col-span-2">
                                        <h5 class="font-black text-rose-700 mb-2 border-b border-rose-200 pb-1">Gastronomie (Kelner/Koch)</h5>
                                        <ul class="list-disc pl-5 space-y-1">
                                            <li>Wie reagieren Sie, wenn ein Gast sich über das Essen beschwert?</li>
                                            <li>Wie wichtig ist Teamarbeit in einer stressigen Schicht für Sie?</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Modal HTML Start -->
    <div id="spreadsheetModal" class="modal" dir="ltr">
        <div class="modal-content">
            <div class="p-5 border-b border-gray-200 flex justify-between items-center bg-white rounded-t-xl">
                <div>
                    <h3 id="modalTitle" class="text-xl font-black text-gray-800 font-inter">Live Company List</h3>
                    <p class="text-xs text-gray-500 font-semibold font-inter mt-1">Showing 20 verified HR contacts</p>
                </div>
                <button onclick="closeModal()" class="text-gray-400 hover:text-red-500 text-2xl transition-colors">&times;</button>
            </div>
            <div class="table-container">
                <table class="sheet-table">
                    <thead>
                        <tr>
                            <th>Company Name</th>
                            <th>City</th>
                            <th>Niche</th>
                            <th>Status</th>
                            <th>Email Contact</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody">
                        <!-- Instantiated by JS -->
                    </tbody>
                </table>
            </div>
            <div class="p-4 border-t border-gray-200 bg-gray-50 rounded-b-xl text-center">
                <p class="text-sm text-gray-600 font-semibold font-inter mb-3">Want access to the full dataset? (1000+ companies)</p>
                <a href="#packages" onclick="closeModal()" class="inline-block bg-gerBlack hover:bg-gray-800 text-white font-bold py-2 px-6 rounded-lg font-inter transition-colors">Upgrade to Die Profi-Liste &rarr;</a>
            </div>
        </div>
    </div>
    <!-- Modal HTML End -->
"""
html = re.sub(r'<section class="py-16 px-4 bg-gray-50 border-y border-gray-200">.*?</section>', new_section, html, flags=re.DOTALL)

# 3. Insert JS Logic at the end before </body>
js_logic = """
    <!-- Injected Niche Data -->
    <script>
        """ + js_data + """
        
        // Modal Logic
        const modal = document.getElementById('spreadsheetModal');
        const modalTitle = document.getElementById('modalTitle');
        const tableBody = document.getElementById('tableBody');

        function openModal(niche) {
            modalTitle.innerText = `${niche} - Verified Companies`;
            const data = nicheData[niche] || [];
            
            let html = '';
            data.forEach((row, index) => {
                html += `
                    <tr>
                        <td class="font-semibold text-gray-800">${row.company}</td>
                        <td class="text-gray-600">${row.location}</td>
                        <td><span class="bg-gray-100 text-gray-800 px-2 py-1 rounded text-xs font-bold">${row.niche}</span></td>
                        <td><span class="text-green-600 font-black"><i class="fa-solid fa-check-circle"></i> Active</span></td>
                        <td>
                            <div class="flex items-center gap-2">
                                <div class="tooltip">
                                    <span class="text-blue-600 font-semibold blur-text">${row.email}</span>
                                    <span class="tooltiptext">Upgrade to The Pro List for full access</span>
                                </div>
                                <div class="tooltip">
                                    <i class="fa-regular fa-copy copy-icon"></i>
                                    <span class="tooltiptext">Upgrade to copy full email</span>
                                </div>
                            </div>
                        </td>
                    </tr>
                `;
            });
            tableBody.innerHTML = html;
            modal.classList.add('show');
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        }

        function closeModal() {
            modal.classList.remove('show');
            document.body.style.overflow = 'auto'; // Restore background scrolling
        }

        // Close modal when clicking outside of it
        window.onclick = function(event) {
            if (event.target == modal) {
                closeModal();
            }
        }
        
        // Tab Logic
        function switchTab(tabId) {
            // Remove active classes
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            // Add to clicked
            event.currentTarget.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        }

        // Accordion Logic
        function toggleAccordion(contentId, btnElement) {
            const content = document.getElementById(contentId);
            const isActive = btnElement.classList.contains('active');
            
            // Close all
            document.querySelectorAll('.accordion-header').forEach(btn => {
                btn.classList.remove('active');
                btn.nextElementSibling.style.maxHeight = null;
            });
            
            // Toggle clicked
            if (!isActive) {
                btnElement.classList.add('active');
                content.style.maxHeight = content.scrollHeight + "px";
            }
        }
    </script>
"""
html = html.replace('</body>', js_logic + '\n</body>')

with open(r'c:\Users\ZhuFan\Desktop\AgencyWebsite\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated landing.html successfully.")
