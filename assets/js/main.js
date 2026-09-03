document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Logic
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    const mobileLinks = document.querySelectorAll('.mobil-link');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            mobileMenu.classList.toggle('flex');
        });

        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                mobileMenu.classList.remove('flex');
            });
        });
    }

    // 2. FAQ (SSS) Accordion
    const tetikleyiciler = document.querySelectorAll('.sss-tetikleyici');
    if (tetikleyiciler.length > 0) {
        tetikleyiciler.forEach(buton => {
            buton.addEventListener('click', () => {
                const icerik = buton.nextElementSibling;
                const ikon = buton.querySelector('i');
                const kart = buton.parentElement;

                if (icerik.style.maxHeight && icerik.style.maxHeight !== '0px') {
                    icerik.style.maxHeight = '0px'; 
                    ikon.style.transform = 'rotate(0deg)'; 
                    kart.classList.remove('shadow-sm', 'border-slate-400');
                } else {
                    tetikleyiciler.forEach(digerButon => {
                        const digerIcerik = digerButon.nextElementSibling; 
                        const digerIkon = digerButon.querySelector('i'); 
                        const digerKart = digerButon.parentElement;
                        digerIcerik.style.maxHeight = '0px'; 
                        digerIkon.style.transform = 'rotate(0deg)'; 
                        digerKart.classList.remove('shadow-sm', 'border-slate-400');
                    });
                    icerik.style.maxHeight = icerik.scrollHeight + 'px'; 
                    ikon.style.transform = 'rotate(180deg)'; 
                    kart.classList.add('shadow-sm', 'border-slate-400');
                }
            });
        });
    }

    // 3. Scroll to Top
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');
    if (scrollToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) { 
                scrollToTopBtn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-4'); 
                scrollToTopBtn.classList.add('opacity-100', 'pointer-events-auto', 'translate-y-0'); 
            } else { 
                scrollToTopBtn.classList.remove('opacity-100', 'pointer-events-auto', 'translate-y-0'); 
                scrollToTopBtn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-4'); 
            }
        });
        scrollToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // 4. Dynamic Search on Index
    const searchInput = document.getElementById('hizmet-arama');
    const allCards = document.querySelectorAll('.hizmet-karti');
    
    if (searchInput && allCards.length > 0) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            allCards.forEach(card => {
                const title = card.querySelector('h4').textContent.toLowerCase();
                const desc = card.querySelector('p').textContent.toLowerCase();
                if (title.includes(query) || desc.includes(query)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }
});

// Global functions (used in onclick attributes)
window.highlightCards = function(cardIds) {
    const firstCardId = cardIds[0];
    const firstCard = document.getElementById(firstCardId);
    const allCards = document.querySelectorAll('.hizmet-karti');
    if (firstCard) { 
        const y = firstCard.getBoundingClientRect().top + window.scrollY - 100; 
        window.scrollTo({ top: y, behavior: 'smooth' }); 
    }
    allCards.forEach(card => { 
        card.style.opacity = '0.4'; 
        card.classList.remove('scale-105', 'shadow-2xl', 'border-klinik-dark', 'relative', 'z-10'); 
    });
    setTimeout(() => {
        cardIds.forEach(id => {
            const card = document.getElementById(id);
            if(card) {
                card.style.opacity = '1';
                card.classList.add('scale-105', 'shadow-2xl', 'border-klinik-dark', 'relative', 'z-10');
                setTimeout(() => { 
                    card.classList.remove('scale-105', 'shadow-2xl', 'border-klinik-dark', 'relative', 'z-10'); 
                    allCards.forEach(c => c.style.opacity = '1'); 
                }, 2500);
            }
        });
    }, 300);
};

window.toggleTags = function() {
    const hiddenTags = document.querySelectorAll('.gizli-etiket');
    const btn = document.getElementById('toggleBtn');
    let isExpanded = false;
    hiddenTags.forEach(tag => {
        if (tag.classList.contains('hidden')) { 
            tag.classList.remove('hidden'); 
            isExpanded = true; 
        } else { 
            tag.classList.add('hidden'); 
            isExpanded = false; 
        }
    });
    if (isExpanded) { 
        btn.innerHTML = 'Daha Az Göster -'; 
    } else { 
        btn.innerHTML = 'Tümünü Gör +'; 
    }
};

window.openCertModal = function(imgSrc) {
    const modal = document.getElementById('certModal');
    const img = document.getElementById('certModalImg');
    if (modal && img) {
        img.src = imgSrc;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        setTimeout(() => { modal.classList.remove('opacity-0'); }, 10);
    }
};

window.closeCertModal = function() {
    const modal = document.getElementById('certModal');
    if (modal) {
        modal.classList.add('opacity-0');
        setTimeout(() => { 
            modal.classList.add('hidden'); 
            modal.classList.remove('flex');
        }, 300);
    }
};

// Video Modal Logic
window.openVideoModal = function(videoSrc) {
    const modal = document.getElementById('videoModal');
    const videoElem = document.getElementById('modalVideoPlayer');
    if (modal && videoElem) {
        videoElem.src = videoSrc;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        setTimeout(() => { modal.classList.remove('opacity-0'); }, 10);
        videoElem.play();
    }
};

window.closeVideoModal = function() {
    const modal = document.getElementById('videoModal');
    const videoElem = document.getElementById('modalVideoPlayer');
    if (modal && videoElem) {
        videoElem.pause();
        videoElem.currentTime = 0;
        modal.classList.add('opacity-0');
        setTimeout(() => { 
            modal.classList.add('hidden'); 
            modal.classList.remove('flex');
        }, 300);
    }
};
