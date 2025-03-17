// Document Ready Function
document.addEventListener('DOMContentLoaded', function() {
    // Navigation
    const navLinks = document.querySelectorAll('.nav-link, .footer-nav-link');
    const pages = document.querySelectorAll('.page');
    
    // Add click event listener to each navigation link
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Get the page ID from the data attribute
            const pageId = this.getAttribute('data-page');
            
            // Remove active class from all navigation links
            navLinks.forEach(navLink => {
                navLink.classList.remove('active');
            });
            
            // Add active class to clicked navigation link
            document.querySelectorAll(`[data-page="${pageId}"]`).forEach(navLink => {
                navLink.classList.add('active');
            });
            
            // Hide all pages
            pages.forEach(page => {
                page.classList.remove('active-page');
            });
            
            // Show the selected page
            document.getElementById(pageId).classList.add('active-page');
            
            // Scroll to top
            window.scrollTo(0, 0);
        });
    });
    
    // View Work Button - Scrolls to projects section
    const viewWorkBtn = document.getElementById('view-work-btn');
    if (viewWorkBtn) {
        viewWorkBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const projectsSection = document.querySelector('.projects');
            projectsSection.scrollIntoView({ behavior: 'smooth' });
        });
    }
    
    // Contact Form Submission
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value;
            
            // Validate form (basic validation)
            if (!name || !email || !subject || !message) {
                alert('Please fill out all fields.');
                return;
            }
            
            // Simulate form submission (in a real application, this would be an AJAX request)
            alert('Thank you for your message! I will get back to you soon.');
            contactForm.reset();
        });
    }
    
    // Newsletter Form Submission
    const newsletterForm = document.getElementById('newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get email value (using querySelector since the input doesn't have an ID)
            const email = newsletterForm.querySelector('input[type="email"]').value;
            
            // Validate email (basic validation)
            if (!email) {
                alert('Please enter your email address.');
                return;
            }
            
            // Simulate form submission
            alert('Thank you for subscribing to my newsletter!');
            newsletterForm.reset();
        });
    }
    
    // Add skill animation on scroll
    const skillCards = document.querySelectorAll('.skill-card');
    
    // Function to check if element is in viewport
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    // Function to animate progress bars when they come into view
    function animateProgressBars() {
        skillCards.forEach(card => {
            if (isInViewport(card)) {
                const progressBar = card.querySelector('.progress');
                progressBar.style.width = '0';
                setTimeout(() => {
                    const width = progressBar.getAttribute('style').split(':')[1].trim();
                    progressBar.style.transition = 'width 1s ease-in-out';
                    progressBar.style.width = width;
                }, 100);
            }
        });
    }
    
    // Initial check and add scroll listener
    animateProgressBars();
    window.addEventListener('scroll', animateProgressBars);
    
    // Project hover effects
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Service card hover effects are handled in CSS, but we could add additional effects here
    
    // Smooth scrolling for all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Skip if it's a navigation link (already handled)
            if (this.classList.contains('nav-link') || this.classList.contains('footer-nav-link')) {
                return;
            }
            
            // Skip if href is just "#"
            if (href === '#') {
                e.preventDefault();
                return;
            }
            
            e.preventDefault();
            
            // Scroll to the element
            document.querySelector(href).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});