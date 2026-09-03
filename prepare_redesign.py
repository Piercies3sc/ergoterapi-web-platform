import os
import re

html_files = [
    'askeri.html',
    'duyu-butunleme.html',
    'el-rehabilitasyonu.html',
    'norolojik.html',
    'pediatrik.html',
    'psikiyatrik.html',
    'yeme-bozuklugu.html'
]

data = {}

for f in html_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            # Extract main tag
            main_match = re.search(r'<main.*?>(.*?)</main>', content, re.DOTALL)
            if main_match:
                print(f"--- {f} ---")
                main_content = main_match.group(1)
                # Find h2
                h2 = re.search(r'<h2.*?>(.*?)</h2>', main_content)
                if h2: print(f"H2: {h2.group(1)}")
                # Find h3
                h3 = re.search(r'<h3.*?>(.*?)</h3>', main_content)
                if h3: print(f"H3: {h3.group(1)}")
                # Find img
                img = re.search(r'<img.*?src="(.*?)".*?>', main_content)
                if img: print(f"IMG: {img.group(1)}")
                print("\n")
