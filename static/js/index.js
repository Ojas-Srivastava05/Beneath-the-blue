// ocean/static/ocean/js/main.js

// Tab functionality
function setupTabs() {
    const tabButtons = document.querySelectorAll('.tab-button');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            console.log('Tab clicked:', this.dataset.tab); // Debug log
            
            // Remove active class from all buttons and content
            document.querySelectorAll('.tab-button').forEach(btn => {
                btn.classList.remove('active');
            });
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            
            // Add active class to clicked button and corresponding content
            this.classList.add('active');
            const tabId = this.getAttribute('data-tab');
            const content = document.getElementById(tabId);
            if (content) {
                content.classList.add('active');
            } else {
                console.error('No content found for tab:', tabId);
            }
        });
    });
}

// Smooth scrolling
function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Video autoplay
function setupVideoAutoplay() {
    const video = document.getElementById('fullpage-video-bg');
    if (video) {
        video.play().catch(error => {
            console.log('Video autoplay prevented:', error);
        });
    }
}

// Navbar hide/show on scroll
function setupNavbarScroll() {
    let lastScroll = 0;
    const header = document.querySelector('header');
    const scrollThreshold = 100; // How far to scroll before hiding

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll <= 0) {
            // At top of page - always show header
            header.classList.remove('hide');
            return;
        }
        
        if (currentScroll > lastScroll && currentScroll > scrollThreshold) {
            // Scrolling down and past threshold - hide header
            header.classList.add('hide');
        } else if (currentScroll < lastScroll) {
            // Scrolling up - show header
            header.classList.remove('hide');
        }
        
        lastScroll = currentScroll;
    });
}

function setupFormHandler(formSelector, url) {
    const form = document.querySelector(formSelector);
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(form);

        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);
                form.reset();
            } else {
                console.error(data.errors);
                alert("Error: " + JSON.stringify(data.errors));
            }
        })
        .catch(error => {
            console.error("Error submitting form:", error);
            alert("Something went wrong.");
        });
    });
}


function setupFormHandlers() {
    setupFormHandler('#pledge-form', document.querySelector('#pledge-form').dataset.submitUrl);
    setupFormHandler('#idea-form', document.querySelector('#idea-form').dataset.submitUrl);
    setupFormHandler('#feedback-form', document.querySelector('#feedback-form').dataset.submitUrl);
    const newsletter = document.querySelector('#newsletter-form');
    if (newsletter) {
        setupFormHandler('#newsletter-form', newsletter.dataset.submitUrl);
    }
}

// Initialize all functionality
document.addEventListener('DOMContentLoaded', function() {
    setupTabs();
    setupSmoothScrolling();
    setupVideoAutoplay();
    setupNavbarScroll(); // <-- Added here
    setupFormHandlers();
});