document.addEventListener('DOMContentLoaded', function() {
    // Get all launch buttons
    const launchButtons = document.querySelectorAll('.launch-btn');
    
    launchButtons.forEach(button => {
        button.addEventListener('click', function() {
            const appKey = this.getAttribute('data-app-key');
            const port = this.getAttribute('data-port');
            
            // Disable button and show loading state
            this.disabled = true;
            this.classList.add('btn-loading');
            this.innerHTML = 'Launching...';
            
            // Make AJAX request to launch the app
            fetch(`/launch/${appKey}`)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Success state
                        this.classList.remove('btn-loading');
                        this.classList.add('launched');
                        this.innerHTML = '✓ App Launched!';
                        
                        // Show success notification
                        showToast('Success', `App launched successfully on port ${port}`, 'success');
                        
                        // Reset button after 3 seconds
                        setTimeout(() => {
                            this.disabled = false;
                            this.classList.remove('launched');
                            this.innerHTML = 'Launch Application';
                        }, 3000);
                        
                    } else {
                        // Error state
                        this.classList.remove('btn-loading');
                        this.classList.add('failed');
                        this.innerHTML = 'Launch Failed';
                        
                        // Show error notification
                        showToast('Error', data.message, 'error');
                        
                        // Reset button after 3 seconds
                        setTimeout(() => {
                            this.disabled = false;
                            this.classList.remove('failed');
                            this.innerHTML = 'Launch Application';
                        }, 3000);
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    
                    // Error state
                    this.classList.remove('btn-loading');
                    this.classList.add('failed');
                    this.innerHTML = 'Launch Failed';
                    
                    // Show error notification
                    showToast('Error', 'Failed to launch application', 'error');
                    
                    // Reset button after 3 seconds
                    setTimeout(() => {
                        this.disabled = false;
                        this.classList.remove('failed');
                        this.innerHTML = 'Launch Application';
                    }, 3000);
                });
        });
    });
});

// Toast notification function
function showToast(title, message, type) {
    // Create toast container if it doesn't exist
    let toastContainer = document.querySelector('.toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.className = 'toast-container';
        document.body.appendChild(toastContainer);
    }
    
    // Create toast element
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    
    // Set toast content based on type
    const bgClass = type === 'success' ? 'bg-success' : 'bg-danger';
    const icon = type === 'success' ? '✓' : '✗';
    
    toast.innerHTML = `
        <div class="toast-header ${bgClass} text-white">
            <span class="me-2">${icon}</span>
            <strong class="me-auto">${title}</strong>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            ${message}
        </div>
    `;
    
    // Add toast to container
    toastContainer.appendChild(toast);
    
    // Initialize and show toast
    const bsToast = new bootstrap.Toast(toast, {
        autohide: true,
        delay: 5000
    });
    bsToast.show();
    
    // Remove toast element after it's hidden
    toast.addEventListener('hidden.bs.toast', function() {
        toast.remove();
    });
}
