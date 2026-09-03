import os
import re
import shutil

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Ensure en directory exists
os.makedirs('en', exist_ok=True)

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update image and video sources
    content = re.sub(r'src="([^"]+\.(?:png|jpg|jpeg|mp4))"', r'src="../\1"', content)
    
    # 2. Update TR|EN toggle for English pages
    # Desktop
    desktop_old = r'<li class="flex items-center gap-2 border-l border-klinik-border pl-4">\n                    <span class="text-klinik-accent font-bold cursor-default">TR</span>\n                    <span class="text-klinik-border">\|</span>\n                    <a href="en/[^"]+" class="text-gray-400 hover:text-klinik-dark transition">EN</a>\n                </li>'
    desktop_new = f'<li class="flex items-center gap-2 border-l border-klinik-border pl-4">\n                    <a href="../{f}" class="text-gray-400 hover:text-klinik-dark transition">TR</a>\n                    <span class="text-klinik-border">|</span>\n                    <span class="text-klinik-accent font-bold cursor-default">EN</span>\n                </li>'
    content = re.sub(desktop_old, desktop_new, content)
    
    # Mobile
    mobile_old = r'<div class="px-8 py-4 flex gap-4 text-sm font-medium border-b border-slate-100">\n                <span class="text-klinik-accent font-bold">TR</span>\n                <span class="text-klinik-border">\|</span>\n                <a href="en/[^"]+" class="text-gray-400 hover:text-klinik-dark transition">EN</a>\n            </div>'
    mobile_new = f'<div class="px-8 py-4 flex gap-4 text-sm font-medium border-b border-slate-100">\n                <a href="../{f}" class="text-gray-400 hover:text-klinik-dark transition">TR</a>\n                <span class="text-klinik-border">|</span>\n                <span class="text-klinik-accent font-bold cursor-default">EN</span>\n            </div>'
    content = re.sub(mobile_old, mobile_new, content)
    
    # 3. Global Menu Translations
    translations = {
        'Ana Sayfa': 'Home',
        'Hakkımda': 'About Me',
        'Çalışma Alanları': 'Specialties',
        'Sertifikalar': 'Certifications',
        'İletişim': 'Contact',
        'S.S.S.': 'FAQ',
        'Pediatrik Ergoterapi': 'Pediatric Occupational Therapy',
        'Duyu Bütünleme Terapisi': 'Sensory Integration Therapy',
        'SOS Beslenme Terapisi': 'SOS Feeding Therapy',
        'Askeri Ergoterapi': 'Military Occupational Therapy',
        'Nörolojik Ergoterapi': 'Neurological Occupational Therapy',
        'Psikiyatrik Ergoterapi': 'Psychiatric Occupational Therapy',
        'El Rehabilitasyonu': 'Hand Rehabilitation',
        'Uzman Ergoterapist': 'Specialist Occupational Therapist',
        'Sınırlı Sorumluluk Beyanı': 'Disclaimer',
        'Bize Yazın': 'Message Us',
        'Yukarı Çık': 'Scroll to Top'
    }
    
    for tr, en in translations.items():
        content = content.replace(tr, en)
        
    # Write to en/ folder
    with open(os.path.join('en', f), 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Generated {len(html_files)} English template files.")
