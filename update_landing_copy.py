import re

with open(r'c:\Users\ZhuFan\Desktop\AgencyWebsite\landing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Pricing Buttons
html = html.replace('اطلب اللائحة الآن', 'خود اللائحة دابا')
html = html.replace('ابدأ طريق النجاح الآن', 'بدا طريق النجاح دابا')

# 2. Update Standard German CV (Muster) Section
old_cv_section_regex = r'<h3 class="text-2xl md:text-3xl font-black mb-2 text-right">Standard German CV \(Muster\) 📄</h3>.*?(?=<div class="bg-white text-gerBlack)'
new_cv_section = """<h3 class="text-2xl md:text-3xl font-black mb-2 text-right" dir="rtl">قالب CV ألماني احترافي 📄</h3>
                <p class="text-gray-300 text-sm md:text-base font-semibold mb-8 text-right leading-relaxed" dir="rtl">
                    هذا هو الـ <strong class="text-gerGold">Tabellarischer Lebenslauf</strong> المعتمد رسمياً والمطلوب من طرف أرباب العمل في ألمانيا. الهيكل الصحيح الذي تقبله أنظمة ATS الألمانية (بدون زينة مبالغ فيها).
                </p>
                """
html = re.sub(old_cv_section_regex, new_cv_section, html, flags=re.DOTALL)

# Update CV download button
html = html.replace('<i class="fa-solid fa-file-pdf"></i> تحميل القالب (Word/PDF)', '<i class="fa-solid fa-file-pdf"></i> شارجي الملف فابور')

# 3. Update Modal Button and Text
old_modal_footer = r'<div class="p-4 border-t border-gray-200 bg-gray-50 rounded-b-xl text-center">.*?Upgrade to Die Profi-Liste &rarr;</a>\s*</div>'
new_modal_footer = """<div class="p-5 border-t border-gray-200 bg-gray-50 rounded-b-xl text-center" dir="rtl">
                <p class="text-base text-gray-800 font-bold font-cairo mb-4">بغيتي توصل للائحة كاملة فيها أكثر من 1000 شركة؟</p>
                <a href="#packages" onclick="closeModal()" class="inline-block bg-gerBlack hover:bg-gray-800 text-white font-bold py-3 px-8 rounded-xl font-cairo transition-colors text-lg shadow-md">خود اللائحة دابا <i class="fa-solid fa-arrow-left mr-2"></i></a>
            </div>"""
html = re.sub(old_modal_footer, new_modal_footer, html, flags=re.DOTALL)

# 4. Generate the Interview Master-Guide Section
def generate_qa_card(num, ger_q, ar_q, ger_a, ar_a):
    return f"""
        <div class="mb-4 bg-white border border-gray-100 rounded-lg shadow-sm overflow-hidden" dir="ltr">
            <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex items-start gap-3">
                <span class="bg-gerRed text-white text-xs font-black px-2 py-1 rounded">Q{num}</span>
                <div>
                    <h5 class="font-bold text-gray-900 text-base">{ger_q}</h5>
                    <p class="text-gray-500 text-sm dir-rtl font-cairo text-right mt-1" dir="rtl">{ar_q}</p>
                </div>
            </div>
            <div class="px-4 py-3 flex items-start gap-3">
                <span class="bg-green-100 text-green-700 text-xs font-black px-2 py-1 rounded">A{num}</span>
                <div>
                    <p class="text-gray-800 text-sm font-medium mb-2 border-l-2 border-green-400 pl-3 py-1 bg-green-50/30 rounded-r">{ger_a}</p>
                    <p class="text-gray-600 text-sm dir-rtl font-cairo text-right bg-blue-50/50 p-2 rounded" dir="rtl"><i class="fa-solid fa-lightbulb text-gerGold mr-1 ml-1"></i> {ar_a}</p>
                </div>
            </div>
        </div>
    """

gen_questions = [
    ("Erzählen Sie uns etwas über sich.", "حدثنا عن نفسك. (لخّص مسيرتك بإيجاز)", "Ich heiße [Name], bin [Alter] Jahre alt und komme aus Marokko. Ich habe mein Abitur gemacht und interessiere mich sehr für [Fachbereich].", "إجابة كلاسيكية: اذكر اسمك، عمرك، بلدك، وماذا درست، ولماذا أنت مهتم بهذا المجال بعيداً عن أوقات الفراغ."),
    ("Warum möchten Sie eine Ausbildung in Deutschland machen?", "لماذا تريد القيام بتدريب مهني في ألمانيا؟", "Das deutsche duale System ist weltweit anerkannt. Ich möchte Theorie und Praxis direkt verbinden und meine berufliche Zukunft auf ein solides Fundament stellen.", "ركز على جودة 'التكوين المزدوج' (Duales System) في ألمانيا، وليس على رغبتك في العيش في أوروبا اقتصادياً."),
    ("Warum haben Sie sich bei unserem Unternehmen beworben?", "لماذا تقدمت بطلب لشركتنا بالذات؟", "Ihr Unternehmen hat einen sehr guten Ruf in der Branche. Bei meiner Recherche hat mir besonders [Projekt/Wert des Unternehmens] gefallen.", "اثبت أنك قمت ببحث عن شركتهم (ذكر مشروع أو قيمة للشركة)."),
    ("Was sind Ihre größten Stärken?", "ما هي أكبر نقاط قوتك؟", "Ich bin sehr zuverlässig, lerne schnell und kann mich gut in ein Team integrieren. Außerdem bringe ich viel Motivation mit.", "اختر نقاط قوة حقيقية ومرتبطة بالتكوين: الموثوقية، سرعة التعلم، العمل الجماعي."),
    ("Was ist Ihre größte Schwäche?", "ما هي أكبر نقطة ضعف لديك؟", "Manchmal bin ich etwas ungeduldig, wenn Aufgaben nicht schnell vorangehen. Aber ich habe gelernt, mich besser zu strukturieren.", "تجنب الإجابات المثالية جداً مثل 'أنا أعمل بجد'. اذكر ضعفاً واقعياً (كقلة الصبر) وكيف تعمل على تحسينه."),
    ("Wo sehen Sie sich in 3 bis 5 Jahren?", "أين ترى نفسك بعد 3 إلى 5 سنوات؟", "Ich sehe mich als erfolgreich abgeschlossene Fachkraft in Ihrem Unternehmen, bereit, mehr Verantwortung zu übernehmen.", "هم يبحثون عن استقرار. أخبرهم أنك تطمح لإكمال التدريب والعمل معهم كمتخصص."),
    ("Wie gehen Sie mit Kritik um?", "كيف تتعامل مع النقد؟", "Kritik sehe ich als Chance, mich zu verbessern. Ich höre gut zu und versuche, die Fehler beim nächsten Mal zu vermeiden.", "النقد البناء في ألمانيا مهم جداً. أظهر أنك تتقبله كفرصة للتعلم."),
    ("Wie reagieren Sie auf Stresssituationen?", "كيف تتصرف في مواقف الضغط؟", "In stressigen Situationen bleibe ich ruhig. Ich priorisiere meine Aufgaben und arbeite sie Schritt für Schritt ab.", "التنظيم (Priorisierung) هو مفتاح الإجابة. أظهر أنك تحافظ على هدوئك وتنجز المهمات خطوة بخطوة."),
    ("Arbeiten Sie lieber im Team oder alleine?", "هل تفضل العمل في فريق أم بمفردك؟", "Ich arbeite sehr gerne im Team, da man sich gegenseitig unterstützen kann. Ich kann aber auch Aufgaben selbstständig und konzentriert erledigen.", "إجابة متوازنة: أنت تحب العمل الجماعي لكنك قادر تماماً على الإنجاز بشكل مستقل."),
    ("Haben Sie noch Fragen an uns?", "هل لديك أي أسئلة لنا (في نهاية المقابلة)؟", "Ja, mich würde interessieren: Wie sieht die Einarbeitungsphase in den ersten Wochen aus?", "يجب أن تسأل سؤالاً دائماً! هذا يظهر اهتمامك العميق. اسأل عن كيفية مرور الأسابيع الأولى أو فريق العمل.")
]

niche_questions = [
    # Pflege
    ("Pflege: Wie gehen Sie mit dem Tod oder dem Leiden von Patienten um?", "التمريض: كيف تتعامل مع الموت أو معاناة المرضى؟", "Es ist sicher emotional schwer, aber ich konzentriere mich darauf, dem Patienten in dieser Zeit so gut wie möglich zu helfen und professionell zu bleiben.", "الاحترافية مع التعاطف. يجب أن توضح أنك تركز على توفير الرعاية الجيدة دون الانهيار العاطفي."),
    ("Pflege: Sind Sie bereit für Schicht- und Wochenendarbeit?", "التمريض: هل أنت مستعد للعمل بنظام الورديات وعطلات نهاية الأسبوع؟", "Ja, absolut. Ich weiß, dass Pflege rund um die Uhr gebraucht wird, und bin auf flexible Arbeitszeiten vorbereitet.", "يجب أن تكون إجابتك حازمة 'نعم'، لأن هذا هو أساس العمل في القطاع الصحي."),
    # IT
    ("IT: Wie gehen Sie bei der Fehlersuche (Debugging) vor?", "البرمجة: كيف تقوم بالبحث عن الأخطاء وإصلاحها؟", "Zuerst versuche ich, das Problem zu reproduzieren. Dann analysiere ich die Fehlermeldungen und grenze den Fehler logisch ein, oft mit Hilfe von Dokumentationen.", "المنهجية: إعادة إنتاج الخطأ -> تحليل الرسالة -> التضييق المنطقي."),
    ("IT: Wie halten Sie Ihr Wissen auf dem neuesten Stand?", "البرمجة: كيف تحافظ على تحديث معلوماتك التقنية؟", "Ich lese Fachblogs, tausche mich in Foren aus und probiere neue Technologien gerne in kleinen privaten Projekten aus.", "إظهار الشغف الشخصي من خلال المشاريع الخاصة والتعلم الذاتي المستمر."),
    # Mechatronik
    ("Mechatronik: Was bedeutet Arbeitssicherheit für Sie?", "الميكاترونيك: ماذا تعني لك السلامة في العمل؟", "Arbeitssicherheit hat höchste Priorität. Es ist wichtig, Schutzkleidung zu tragen und alle Vorschriften genau zu befolgen, um sich und andere nicht zu gefährden.", "الشركات الألمانية صارمة جداً في السلامة. اعتبرها 'الأولوية القصوى' دائماً."),
    ("Mechatronik: Wie gehen Sie bei einer Maschinenstörung vor?", "الميكاترونيك: ماذا تفعل عند حدوث عطل في آلة؟", "Zuerst sichere ich die Maschine ab ('Not-Halt'). Dann dokumentiere ich das Problem und hole gegebenenfalls Unterstützung von einem erfahrenen Kollegen.", "الخطوة 1: تأمين الآلة (زر التوقف). الخطوة 2: الإبلاغ والتحليل."),
    # Logistik
    ("Logistik: Wie behalten Sie den Überblick bei vielen Aufgaben?", "اللوجستيك: كيف تحافظ على التركيز عند تراكم المهام؟", "Ich arbeite systematisch. Ich halte mich an die vorgegebenen Prozesse und nutze Checklisten, um keine Details zu übersehen.", "النظام والالتزام بالعمليات (Prozesse) واستخدام القوائم (Checklisten)."),
    ("Logistik: Haben Sie Erfahrung mit körperlich anstrengender Arbeit?", "اللوجستيك: هل لديك خبرة في العمل البدني المجهد؟", "Ja, ich bin körperlich fit und belastbar. Mir macht es nichts aus, aktiv mit anzupacken.", "الإثبات أنك لائق بدنياً ومستعد للعمل الشاق."),
    # Gastronomie
    ("Gastronomie: Wie reagieren Sie, wenn ein Gast sich beschwert?", "الفندقة/الطبخ: كيف تتصرف إذا اشتكى زبون من الطعام؟", "Ich höre dem Gast aufmerksam zu, bleibe freundlich und entschuldige mich. Dann suche ich sofort nach einer schnellen Lösung, um den Gast zufriedenzustellen.", "الإنصات، البقاء ودوداً، الاعتذار، وإيجاد حل فوري دون جدال."),
    ("Gastronomie: Wie wichtig ist Teamarbeit in einer stressigen Schicht?", "الفندقة/الطبخ: ما أهمية العمل الجماعي في وردية عمل مزدحمة؟", "Sehr wichtig! In der Gastronomie greift alles ineinander. Ohne klare Kommunikation und gegenseitige Hilfe im Team funktioniert es nicht.", "التواصل الواضح والمساعدة المتبادلة هي ما يجعل المطعم/الفندق ناجحاً في أوقات الذروة.")
]

part_a_html = "".join([generate_qa_card(i+1, g_q, a_q, g_a, a_a) for i, (g_q, a_q, g_a, a_a) in enumerate(gen_questions)])
part_b_html = "".join([generate_qa_card(i+1, g_q, a_q, g_a, a_a) for i, (g_q, a_q, g_a, a_a) in enumerate(niche_questions)])

new_accordion_html = f"""
                <div class="space-y-4 flex flex-col font-inter" dir="ltr">
                    <!-- Part A -->
                    <div class="border border-gray-200 rounded-xl overflow-hidden shadow-sm">
                        <button class="accordion-header w-full text-left p-5 font-black text-gray-800 bg-white hover:bg-gray-50 transition-colors flex justify-between items-center" onclick="toggleAccordion('acc-a', this)">
                            <span class="flex items-center gap-3"><span class="bg-gerBlack text-white w-8 h-8 rounded-full flex items-center justify-center text-sm shadow">A</span> 10 General Questions (Allgemeine Fragen)</span>
                            <i class="fa-solid fa-chevron-down text-gray-400 icon-chevron transition-transform duration-300"></i>
                        </button>
                        <div id="acc-a" class="accordion-content">
                            <div class="p-5 border-t border-gray-100 bg-white">
                                {part_a_html}
                            </div>
                        </div>
                    </div>
                    
                    <!-- Part B -->
                    <div class="border border-gray-200 rounded-xl overflow-hidden shadow-sm">
                        <button class="accordion-header w-full text-left p-5 font-black text-gray-800 bg-white hover:bg-gray-50 transition-colors flex justify-between items-center" onclick="toggleAccordion('acc-b', this)">
                            <span class="flex items-center gap-3"><span class="bg-gerRed text-white w-8 h-8 rounded-full flex items-center justify-center text-sm shadow">B</span> 10 Niche-Specific Questions (Fachspezifisch)</span>
                            <i class="fa-solid fa-chevron-down text-gray-400 icon-chevron transition-transform duration-300"></i>
                        </button>
                        <div id="acc-b" class="accordion-content">
                            <div class="p-5 border-t border-gray-100 bg-white">
                                {part_b_html}
                            </div>
                        </div>
                    </div>
                </div>
"""

old_accordion_regex = r'<div class="space-y-4 flex flex-col font-inter" dir="ltr">.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>'
html = re.sub(old_accordion_regex, new_accordion_html + "\n            </div>", html, flags=re.DOTALL)

with open(r'c:\Users\ZhuFan\Desktop\AgencyWebsite\landing.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated content and translations successfully.")
