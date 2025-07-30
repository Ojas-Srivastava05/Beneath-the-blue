document.addEventListener('DOMContentLoaded', function() {
    // Media Upload Preview
    const mediaInput = document.getElementById('post-media');
    const mediaPreview = document.getElementById('media-preview');
    
    if (mediaInput && mediaPreview) {
        mediaInput.addEventListener('change', function(e) {
            mediaPreview.innerHTML = '';
            mediaPreview.style.display = 'none';
            
            const file = e.target.files[0];
            if (!file) return;
            
            // Validate file type
            if (!file.type) {
                showToast('File type not recognized', 'error');
                return;
            }

            const fileType = file.type.split('/')[0];
            const validTypes = ['image', 'video'];
            
            if (!validTypes.includes(fileType)) {
                showToast('Unsupported file type. Please upload an image or video.', 'error');
                return;
            }

            const reader = new FileReader();
            
            reader.onload = function(e) {
                mediaPreview.innerHTML = '';
                
                if (fileType === 'image') {
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    img.alt = 'Upload preview';
                    mediaPreview.appendChild(img);
                } else if (fileType === 'video') {
                    const video = document.createElement('video');
                    video.src = e.target.result;
                    video.controls = true;
                    mediaPreview.appendChild(video);
                }
                
                mediaPreview.style.display = 'block';
                showToast('Media uploaded successfully!', 'success');
            };
            
            reader.onerror = function() {
                showToast('Error reading file', 'error');
                mediaPreview.innerHTML = '<p class="error-message">Error loading file</p>';
            };
            
            reader.readAsDataURL(file);
        });
    }
    
    // Like functionality
    document.querySelectorAll('.like-btn').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.getAttribute('data-post-id');
            const likeCount = this.querySelector('.like-count');
            const isLiked = this.classList.contains('liked');
            
            // Visual feedback
            const icon = this.querySelector('i');
            const originalIconClass = icon.className;
            icon.className = 'fas fa-spinner fa-spin';
            this.disabled = true;
            
            // Simulate API call
            setTimeout(() => {
                if (isLiked) {
                    this.classList.remove('liked');
                    likeCount.textContent = parseInt(likeCount.textContent) - 1;
                    icon.className = 'far fa-heart';
                    showToast('Post unliked', 'info');
                } else {
                    this.classList.add('liked');
                    likeCount.textContent = parseInt(likeCount.textContent) + 1;
                    icon.className = 'fas fa-heart';
                    showToast('Post liked!', 'success');
                }
                this.disabled = false;
            }, 800);
        });
    });
    
    // Comment submission
    document.querySelectorAll('.comment-form').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const input = this.querySelector('input');
            const commentText = input.value.trim();
            
            if (!commentText) {
                showToast('Please enter a comment', 'error');
                return;
            }
            
            // Visual feedback
            const button = this.querySelector('button');
            const originalButtonText = button.innerHTML;
            button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            button.disabled = true;
            
            // Simulate API call
            setTimeout(() => {
                const commentsList = this.closest('.comments-section').querySelector('.comments-list');
                const newComment = document.createElement('div');
                newComment.className = 'comment';
                newComment.innerHTML = `
                    <div class="comment-user">
                        <div class="avatar small" style="background-color: ${getRandomColor()}">
                            <i class="fas fa-user"></i>
                        </div>
                        <span class="comment-username">You</span>
                    </div>
                    <p class="comment-text">${commentText}</p>
                `;
                commentsList.appendChild(newComment);
                input.value = '';
                button.innerHTML = originalButtonText;
                button.disabled = false;
                showToast('Comment posted!', 'success');
            }, 1000);
        });
    });
    
    // View all comments
    document.querySelectorAll('.view-all-comments').forEach(button => {
        button.addEventListener('click', function() {
            showToast('Loading all comments...', 'info');
            // In a real app, you would fetch and display all comments here
        });
    });
    
    // Post options
    document.querySelectorAll('.post-options').forEach(button => {
        button.addEventListener('click', function() {
            showToast('Post options clicked', 'info');
            // In a real app, you would show a dropdown menu with options
        });
    });
    
    // Share button
    document.querySelectorAll('.share-btn').forEach(button => {
        button.addEventListener('click', function() {
            showToast('Share options will appear here', 'info');
            // In a real app, you would implement share functionality
        });
    });
    
    // Toast notification system
    function showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `
            <div class="toast-content">
                <i class="fas ${getToastIcon(type)}"></i>
                <span>${message}</span>
            </div>
            <i class="fas fa-times close-toast"></i>
        `;
        
        document.body.appendChild(toast);
        
        // Auto-remove after 3 seconds
        setTimeout(() => {
            toast.classList.add('fade-out');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
        
        // Manual close
        toast.querySelector('.close-toast').addEventListener('click', () => {
            toast.classList.add('fade-out');
            setTimeout(() => toast.remove(), 300);
        });
    }
    
    function getToastIcon(type) {
        switch(type) {
            case 'success': return 'fa-check-circle';
            case 'error': return 'fa-exclamation-circle';
            case 'info': return 'fa-info-circle';
            default: return 'fa-info-circle';
        }
    }
    
    // Helper function to generate random colors for avatars
    function getRandomColor() {
        const colors = [
            '#00587a', '#008891', '#00a8cc', '#a7ecee', 
            '#ff7e67', '#ffb347', '#0f3057', '#495057'
        ];
        return colors[Math.floor(Math.random() * colors.length)];
    }
    
    // Floating action button for new post
    const fab = document.createElement('div');
    fab.className = 'fab';
    fab.innerHTML = '<i class="fas fa-plus"></i>';
    fab.addEventListener('click', () => {
        document.querySelector('.create-post').scrollIntoView({ behavior: 'smooth' });
        document.querySelector('#post-content').focus();
    });
    document.body.appendChild(fab);
});