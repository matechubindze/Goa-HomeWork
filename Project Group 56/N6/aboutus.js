document.addEventListener('DOMContentLoaded', () => {
    // მობილური მენიუს ღილაკები
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMobileMenu = document.getElementById('close-mobile-menu');
    const mobileMenuLinks = mobileMenu.querySelectorAll('a');

    // მობილური მენიუს ჩვენება/დამალვა
    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });

    // დახურვა X ღილაკით
    closeMobileMenu.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
    });

    // მენიუს დახურვა ლინკზე დაჭერისას
    mobileMenuLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
        });
    });

    // IntersectionObserver ანიმაციებისთვის
    const observerOptions = {
        root: null, // viewport - ხედვის არეალი
        rootMargin: '0px',
        threshold: 0.1 // აქტივაცია როცა ელემენტის 10% ჩანს
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                observer.unobserve(entry.target); // აღარ დავაკვირდეთ უკვე ანიმირებულ ელემენტს
            }
        });
    }, observerOptions);

    // გამოვიძახოთ ყველა ელემენტზე fade-in და fade-in-up
    document.querySelectorAll('.fade-in-up, .fade-in').forEach(element => {
        observer.observe(element);
    });

    // რბილი სქროლი ღილაკებზე დაჭერისას
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
