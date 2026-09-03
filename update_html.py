import os
import re

TR_NAVBAR = """<nav class="bg-white/80 backdrop-blur-md border-b border-klinik-border py-4 px-4 md:px-8 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto flex justify-between items-center">
        <a href="{root}index.html" class="flex items-center gap-3 md:gap-4 group">
            <img src="{root}amblem.png" alt="Hazal Pural Logo" class="h-10 md:h-12 w-auto object-contain group-hover:opacity-70 transition mr-1 md:mr-3">
            <div class="flex flex-col border-l border-klinik-border pl-3 md:pl-4">
                <span class="font-serif text-lg md:text-2xl font-semibold tracking-wide text-klinik-dark">Hazal PURAL</span>
                <span class="font-sans text-[9px] md:text-xs text-klinik-accent tracking-[0.2em] uppercase mt-0.5">Uzman Ergoterapist</span>
            </div>
        </a>
        <ul class="hidden md:flex items-center gap-8 lg:gap-10 text-sm font-medium tracking-wide">
            <li><a href="{root}index.html" class="hover:text-klinik-accent transition duration-300">Ana Sayfa</a></li>
            <li><a href="{root}index.html#hakkimda" class="hover:text-klinik-accent transition duration-300">Hakkımda</a></li>
            <li class="relative group py-2">
                <a href="{root}index.html#hizmetler" class="hover:text-klinik-accent transition duration-300 flex items-center gap-1.5 cursor-pointer">
                    Çalışma Alanları <i class="fa-solid fa-chevron-down text-[10px] ml-0.5"></i>
                </a>
                <div class="absolute left-0 top-full w-60 bg-white border border-klinik-border shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50">
                    <ul class="flex flex-col py-2">
                        <li><a href="{root}pediatrik.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Pediatrik Ergoterapi</a></li>
                        <li><a href="{root}duyu-butunleme.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Duyu Bütünleme Terapisi</a></li>
                        <li><a href="{root}yeme-bozuklugu.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">SOS Beslenme Terapisi</a></li>
                        <li><a href="{root}askeri.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Askeri Ergoterapi</a></li>
                        <li><a href="{root}norolojik.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Nörolojik Ergoterapi</a></li>
                        <li><a href="{root}psikiyatrik.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Psikiyatrik Ergoterapi</a></li>
                        <li><a href="{root}el-rehabilitasyonu.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">El Rehabilitasyonu</a></li>
                    </ul>
                </div>
            </li>
            <li><a href="{root}egitim.html" class="hover:text-klinik-accent transition duration-300">Sertifikalar</a></li>
            <li><a href="{root}index.html#sss-bolumu" class="hover:text-klinik-accent transition duration-300">S.S.S.</a></li>
            <li><a href="{root}index.html#iletisim" class="hover:text-klinik-accent transition duration-300">İletişim</a></li>
            <li class="flex items-center gap-2 border-l border-klinik-border pl-4">
                <span class="text-klinik-accent font-bold cursor-default">TR</span>
                <span class="text-klinik-border">|</span>
                <a href="{en_link}" class="text-gray-400 hover:text-klinik-dark transition">EN</a>
            </li>
        </ul>
        <button id="mobileMenuBtn" class="md:hidden text-klinik-dark text-2xl focus:outline-none p-2"><i class="fa-solid fa-bars"></i></button>
    </div>
    <div id="mobileMenu" class="hidden absolute top-full left-0 w-full bg-white border-t border-klinik-border shadow-lg flex-col md:hidden z-40">
        <a href="{root}index.html" class="mobil-link px-8 py-4 border-b border-slate-100 text-sm font-medium text-klinik-dark hover:bg-slate-50">Ana Sayfa</a>
        <a href="{root}index.html#hakkimda" class="mobil-link px-8 py-4 border-b border-slate-100 text-sm font-medium text-klinik-dark hover:bg-slate-50">Hakkımda</a>
        <a href="{root}index.html#hizmetler" class="mobil-link px-8 py-4 border-b border-slate-100 text-sm font-medium text-klinik-dark hover:bg-slate-50">Çalışma Alanları</a>
        <a href="{root}egitim.html" class="mobil-link px-8 py-4 border-b border-slate-100 text-sm font-medium text-klinik-dark hover:bg-slate-50">Sertifikalar</a>
        <a href="{root}index.html#sss-bolumu" class="mobil-link px-8 py-4 border-b border-slate-100 text-sm font-medium text-klinik-dark hover:bg-slate-50">S.S.S.</a>
        <a href="{root}index.html#iletisim" class="mobil-link px-8 py-4 text-sm font-medium text-klinik-dark hover:bg-slate-50">İletişim</a>
        <div class="px-8 py-4 flex gap-4 text-sm font-medium border-b border-slate-100">
            <span class="text-klinik-accent font-bold">TR</span>
            <span class="text-klinik-border">|</span>
            <a href="{en_link}" class="text-gray-400 hover:text-klinik-dark transition">EN</a>
        </div>
    </div>
</nav>"""

EN_NAVBAR = """<nav class="bg-white/80 backdrop-blur-md border-b border-klinik-border py-4 px-4 md:px-8 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto flex justify-between items-center">
        <a href="{root}en/index.html" class="flex items-center gap-3 md:gap-4 group">
            <img src="{root}amblem.png" alt="Hazal Pural Logo" class="h-10 md:h-12 w-auto object-contain group-hover:opacity-70 transition mr-1 md:mr-3">
            <div class="flex flex-col border-l border-klinik-border pl-3 md:pl-4">
                <span class="font-serif text-lg md:text-2xl font-semibold tracking-wide text-klinik-dark">Hazal PURAL</span>
                <span class="font-sans text-[9px] md:text-xs text-klinik-accent tracking-[0.2em] uppercase mt-0.5">Occupational Therapist</span>
            </div>
        </a>
        <ul class="hidden md:flex items-center gap-8 lg:gap-10 text-sm font-medium tracking-wide">
            <li><a href="{root}en/index.html" class="hover:text-klinik-accent transition duration-300">Home</a></li>
            <li><a href="{root}en/index.html#hakkimda" class="hover:text-klinik-accent transition duration-300">About Me</a></li>
            <li class="relative group py-2">
                <a href="{root}en/index.html#hizmetler" class="hover:text-klinik-accent transition duration-300 flex items-center gap-1.5 cursor-pointer">
                    Services <i class="fa-solid fa-chevron-down text-[10px] ml-0.5"></i>
                </a>
                <div class="absolute left-0 top-full w-60 bg-white border border-klinik-border shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50">
                    <ul class="flex flex-col py-2">
                        <li><a href="{root}en/pediatrik.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Pediatric OT</a></li>
                        <li><a href="{root}en/duyu-butunleme.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Sensory Integration</a></li>
                        <li><a href="{root}en/yeme-bozuklugu.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">SOS Feeding Therapy</a></li>
                        <li><a href="{root}en/askeri.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Military OT</a></li>
                        <li><a href="{root}en/norolojik.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Neurological OT</a></li>
                        <li><a href="{root}en/psikiyatrik.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Psychiatric OT</a></li>
                        <li><a href="{root}en/el-rehabilitasyonu.html" class="block px-5 py-2.5 text-xs text-klinik-dark hover:bg-slate-50 transition">Hand Rehabilitation</a></li>
                    </ul>
                </div>
            </li>
            <li><a href="{root}en/egitim.html" class="hover:text-klinik-accent transition duration-300">Certifications</a></li>
            <li><a href="{root}en/index.html#iletisim" class="hover:text-klinik-accent transition duration-300">Contact</a></li>
            <li class="flex items-center gap-2 border-l border-klinik-border pl-4">
                <a href="{tr_link}" class="text-gray-400 hover:text-klinik-dark transition">TR</a>
                <span class="text-klinik-border">|</span>
                <span class="text-klinik-accent font-bold cursor-default">EN</span>
            </li>
        </ul>
        <button id="mobileMenuBtn" class="md:hidden text-klinik-dark text-2xl focus:outline-none p-2"><i class="fa-solid fa-bars"></i></button>
    </div>
    <div id="mobileMenu" class="hidden absolute top-full left-0 w-full bg-white border-t border-klinik-border shadow-lg flex-col md:hidden z-40">
        <a href="{root}en/index.html" class="mobil-link px-8 py-4 border-b border-slate-100 text-sm font-medium text-klinik-dark hover:bg-slate-50">Home</a>
        <a href="{root}en/index.html#hakkimda" class="mobil-link px-8 py-4 border-b border-slate-100 text-sm font-medium text-klinik-dark hover:bg-slate-50">About Me</a>
        <a href="{root}en/index.html#hizmetler" class="mobil-link px-8 py-4 border-b border-slate-100 text-sm font-medium text-klinik-dark hover:bg-slate-50">Services</a>
        <a href="{root}en/egitim.html" class="mobil-link px-8 py-4 border-b border-slate-100 text-sm font-medium text-klinik-dark hover:bg-slate-50">Certifications</a>
        <a href="{root}en/index.html#iletisim" class="mobil-link px-8 py-4 text-sm font-medium text-klinik-dark hover:bg-slate-50">Contact</a>
        <div class="px-8 py-4 flex gap-4 text-sm font-medium border-b border-slate-100">
            <a href="{tr_link}" class="text-gray-400 hover:text-klinik-dark transition">TR</a>
            <span class="text-klinik-border">|</span>
            <span class="text-klinik-accent font-bold cursor-default">EN</span>
        </div>
    </div>
</nav>"""

TR_FOOTER = """<footer id="iletisim" class="bg-klinik-dark text-white py-12 md:py-16 px-6 md:px-8 mt-auto border-t border-white/15">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-10 md:gap-12 border-b border-white/15 pb-10 md:pb-12">
        <div class="flex flex-col">
            <a href="{root}index.html" class="flex items-center gap-4 mb-6 group">
                <img src="{root}amblem.png" alt="Hazal Pural Logo" class="h-10 md:h-12 w-auto object-contain transition mr-1 md:mr-2 brightness-0 invert">
                <div class="flex flex-col border-l border-gray-500 pl-4">
                    <span class="font-serif text-xl md:text-2xl font-semibold tracking-wide text-white">Hazal PURAL</span>
                    <span class="font-sans text-[10px] md:text-xs text-gray-400 tracking-[0.2em] uppercase mt-0.5">Uzm. Ergoterapist</span>
                </div>
            </a>
            <a href="mailto:hazalpural@gmail.com" class="font-sans text-sm text-gray-300 hover:text-white transition inline-block mt-2"><i class="fa-regular fa-envelope mr-2"></i> hazalpural@gmail.com</a>
            <div class="flex gap-4 mt-6 md:mt-8">
                <a href="https://www.instagram.com/ergoterapist_hazalpural/" class="border border-white/20 w-10 h-10 flex items-center justify-center rounded-full hover:bg-white hover:text-klinik-dark transition text-gray-300"><i class="fa-brands fa-instagram text-sm"></i></a>
                <a href="https://www.linkedin.com/in/hazalpural/" class="border border-white/20 w-10 h-10 flex items-center justify-center rounded-full hover:bg-white hover:text-klinik-dark transition text-gray-300"><i class="fa-brands fa-linkedin-in text-sm"></i></a>
            </div>
        </div>
        <div>
            <div class="flex items-center gap-3 mb-4 md:mb-6">
                <img src="{root}amblem.png" alt="Hazal Pural Logo" class="h-8 md:h-10 w-auto object-contain mr-1 brightness-0 invert opacity-50">
                <h4 class="font-sans text-base md:text-lg font-semibold m-0 relative z-10">Sınırlı Sorumluluk Beyanı</h4>
            </div>
            <p class="font-sans text-xs md:text-sm text-gray-300 leading-relaxed font-light relative z-10">Web sitemizin içeriği, ziyaretçiyi bilgilendirmeye yönelik hazırlanmıştır. Sitede yer alan bilgiler, hiçbir zaman bir hekim tedavisinin ya da konsültasyonunun yerini alamaz. Bu kaynaktan yola çıkarak, ilaç tedavisine başlanması ya da mevcut tedavinin değiştirilmesi kesinlikle tavsiye edilmez.</p>
        </div>
        <div class="md:pl-12 relative z-10">
            <h4 class="font-sans text-base md:text-lg font-semibold mb-4 md:mb-6">Menü</h4>
            <ul class="flex flex-col gap-3 md:gap-4 font-sans text-sm text-gray-300 font-light">
                <li><a href="{root}index.html" class="hover:text-white transition flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> Anasayfa</a></li>
                <li><a href="{root}index.html#hakkimda" class="hover:text-white transition flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> Hakkımda</a></li>
                <li><a href="{root}egitim.html" class="hover:text-white transition flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> Sertifikalar</a></li>
                <li><a href="{root}index.html#hizmetler" class="hover:text-white transition flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> Çalışma Alanları</a></li>
                <li><a href="{root}index.html#iletisim" class="hover:text-white transition flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> İletişim</a></li>
            </ul>
        </div>
    </div>
    <div class="max-w-7xl mx-auto mt-6 md:mt-8 text-center text-gray-500 text-[10px] md:text-xs font-light relative z-10"><p>&copy; 2026 Uzm. Erg. Hazal Pural. Tüm hakları saklıdır.</p></div>
</footer>"""

EN_FOOTER = """<footer id="iletisim" class="bg-klinik-dark text-white py-12 md:py-16 px-6 md:px-8 mt-auto border-t border-white/15">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-10 md:gap-12 border-b border-white/15 pb-10 md:pb-12">
        <div class="flex flex-col">
            <a href="{root}en/index.html" class="flex items-center gap-4 mb-6 group">
                <img src="{root}amblem.png" alt="Hazal Pural Logo" class="h-10 md:h-12 w-auto object-contain transition mr-1 md:mr-2 brightness-0 invert">
                <div class="flex flex-col border-l border-gray-500 pl-4">
                    <span class="font-serif text-xl md:text-2xl font-semibold tracking-wide text-white">Hazal PURAL</span>
                    <span class="font-sans text-[10px] md:text-xs text-gray-400 tracking-[0.2em] uppercase mt-0.5">Occupational Therapist</span>
                </div>
            </a>
            <a href="mailto:hazalpural@gmail.com" class="font-sans text-sm text-gray-300 hover:text-white transition inline-block mt-2"><i class="fa-regular fa-envelope mr-2"></i> hazalpural@gmail.com</a>
            <div class="flex gap-4 mt-6 md:mt-8">
                <a href="https://www.instagram.com/ergoterapist_hazalpural/" class="border border-white/20 w-10 h-10 flex items-center justify-center rounded-full hover:bg-white hover:text-klinik-dark transition text-gray-300"><i class="fa-brands fa-instagram text-sm"></i></a>
                <a href="https://www.linkedin.com/in/hazalpural/" class="border border-white/20 w-10 h-10 flex items-center justify-center rounded-full hover:bg-white hover:text-klinik-dark transition text-gray-300"><i class="fa-brands fa-linkedin-in text-sm"></i></a>
            </div>
        </div>
        <div>
            <div class="flex items-center gap-3 mb-4 md:mb-6">
                <img src="{root}amblem.png" alt="Hazal Pural Logo" class="h-8 md:h-10 w-auto object-contain mr-1 brightness-0 invert opacity-50">
                <h4 class="font-sans text-base md:text-lg font-semibold m-0 relative z-10">Disclaimer</h4>
            </div>
            <p class="font-sans text-xs md:text-sm text-gray-300 leading-relaxed font-light relative z-10">The content of our website is prepared to inform the visitor. The information on the site can never replace a doctor's treatment or consultation. Based on this source, it is strictly not recommended to start medication or change the existing treatment.</p>
        </div>
        <div class="md:pl-12 relative z-10">
            <h4 class="font-sans text-base md:text-lg font-semibold mb-4 md:mb-6">Menu</h4>
            <ul class="flex flex-col gap-3 md:gap-4 font-sans text-sm text-gray-300 font-light">
                <li><a href="{root}en/index.html" class="hover:text-white transition flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> Home</a></li>
                <li><a href="{root}en/index.html#hakkimda" class="hover:text-white transition flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> About Me</a></li>
                <li><a href="{root}en/egitim.html" class="hover:text-white transition flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> Certifications</a></li>
                <li><a href="{root}en/index.html#hizmetler" class="hover:text-white transition flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> Services</a></li>
                <li><a href="{root}en/index.html#iletisim" class="hover:text-white transition flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> Contact</a></li>
            </ul>
        </div>
    </div>
    <div class="max-w-7xl mx-auto mt-6 md:mt-8 text-center text-gray-500 text-[10px] md:text-xs font-light relative z-10"><p>&copy; 2026 Hazal Pural. All rights reserved.</p></div>
</footer>"""

VIDEO_MODAL = """
    <!-- VIDEO MODAL -->
    <div id="videoModal" class="fixed inset-0 z-[100] hidden items-center justify-center bg-black/90 backdrop-blur-sm p-4 opacity-0 transition-opacity duration-300" onclick="closeVideoModal()">
        <div class="relative w-full max-w-4xl flex items-center justify-center">
            <button onclick="closeVideoModal()" class="absolute -top-12 right-0 text-white hover:text-klinik-accent text-3xl transition-colors cursor-pointer" title="Kapat">
                <i class="fa-solid fa-xmark"></i>
            </button>
            <div class="w-full aspect-video bg-black rounded shadow-2xl overflow-hidden" onclick="event.stopPropagation()">
                <video id="modalVideoPlayer" class="w-full h-full" controls playsinline>
                    <source src="" type="video/mp4">
                    Tarayıcınız video etiketini desteklemiyor.
                </video>
            </div>
        </div>
    </div>
"""

CERT_MODAL = """
    <!-- CERTIFICATE MODAL -->
    <div id="certModal" class="fixed inset-0 z-[100] hidden items-center justify-center bg-black/90 backdrop-blur-sm p-4 opacity-0 transition-opacity duration-300" onclick="closeCertModal()">
        <div class="relative w-full max-w-4xl flex items-center justify-center">
            <button onclick="closeCertModal()" class="absolute -top-12 right-0 text-white hover:text-klinik-accent text-3xl transition-colors cursor-pointer" title="Kapat">
                <i class="fa-solid fa-xmark"></i>
            </button>
            <img id="certModalImg" src="" alt="Sertifika" class="max-w-full max-h-[85vh] object-contain rounded shadow-2xl" onclick="event.stopPropagation()">
        </div>
    </div>
"""

def get_html_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.html')]

def process_file(filepath, is_en):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    root_path = "../" if is_en else ""
    en_link = f"en/{filename}" if not is_en else ""
    tr_link = f"../{filename}" if is_en else ""

    # 1. Update Navbar
    nav_template = EN_NAVBAR if is_en else TR_NAVBAR
    nav_html = nav_template.format(root=root_path, en_link=en_link, tr_link=tr_link)
    content = re.sub(r'<nav.*?</nav>', nav_html, content, flags=re.DOTALL)

    # 2. Update Footer
    footer_template = EN_FOOTER if is_en else TR_FOOTER
    footer_html = footer_template.format(root=root_path)
    content = re.sub(r'<footer.*?</footer>', footer_html, content, flags=re.DOTALL)

    # 3. Clean old script/style blocks inside <head> and add standard links
    # Remove old tailwind script
    content = re.sub(r'<script>\s*tailwind\.config = \{.*?\};\s*</script>', '', content, flags=re.DOTALL)
    # Remove old inline styles
    content = re.sub(r'<style>\s*html \{ scroll-behavior: smooth; \}\s*body \{ background-color: #fcfcfc; \}\s*</style>', '', content, flags=re.DOTALL)

    head_links = f'\n    <link rel="stylesheet" href="{root_path}assets/css/style.css">\n    <script src="{root_path}assets/js/tailwind-config.js"></script>\n'
    if 'assets/css/style.css' not in content:
        content = content.replace('</head>', head_links + '</head>')

    # 4. Clean old scripts before </body>
    # Since we can't reliably catch all inline scripts without removing our own, we will just remove ALL `<script>...</script>` that contain inline JS
    content = re.sub(r'<script(?! src=").*?</script>', '', content, flags=re.DOTALL)
    
    # 5. Image lazy loading
    content = re.sub(r'<img(?!.*?loading=)(.*?)>', r'<img loading="lazy"\1>', content)

    # 6. Video Preview Card Replacement
    def video_replacer(match):
        video_block = match.group(0)
        src_match = re.search(r'src="([^"]+)"', video_block)
        if src_match:
            src = src_match.group(1)
        else:
            source_match = re.search(r'<source\s+src="([^"]+)"', video_block)
            src = source_match.group(1) if source_match else ''
        
        return f'''<div class="video-preview-wrapper" onclick="openVideoModal('{root_path}{src}')">
                        <div class="play-button"><i class="fa-solid fa-play"></i></div>
                    </div>'''
    
    content = re.sub(r'<video.*?</video>', video_replacer, content, flags=re.DOTALL)

    # Remove previously injected modals and scripts, including the literal \n mistakes
    content = re.sub(r'<!-- VIDEO MODAL -->.*</body>', '</body>', content, flags=re.DOTALL)
    # Also in case there's another script tag before it
    content = re.sub(r'<script src="[^"]+assets/js/main\.js"></script>\s*</body>', '</body>', content, flags=re.DOTALL)

    # Inject main.js + modals at the bottom AFTER replacing videos
    bottom_scripts = f'\n    {VIDEO_MODAL}\n    {CERT_MODAL}\n    <script src="{root_path}assets/js/main.js"></script>\n'
    content = content.replace('</body>', bottom_scripts + '</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Processing TR files...")
for f in get_html_files('.'):
    process_file(f, is_en=False)

print("Processing EN files...")
for f in get_html_files('./en'):
    process_file(f, is_en=True)

print("Done.")
