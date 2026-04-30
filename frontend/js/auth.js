// Handle Sign In (FIXED)
async function handleSignIn() {
    const username = document.getElementById('signin-username').value;
    const password = document.getElementById('signin-password').value;

    if (!username || !password) {
        showToast('Please fill in all fields', 'error');
        return;
    }

    try {
        // ✅ IMPORTANT FIX: use URLSearchParams instead of FormData
        const formData = new URLSearchParams();
        formData.append('username', username);
        formData.append('password', password);

        const response = await fetch(`${BASE_URL}/auth/login/form`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('token_type', data.token_type);

            showToast('Sign in successful! Redirecting...', 'success');

            setTimeout(() => {
                window.location.href = 'dashboard.html';
            }, 1500);
        } else {
            showToast(data.detail || 'Sign in failed', 'error');
        }
    } catch (error) {
        console.error('Sign in error:', error);
        showToast('Network error. Please try again.', 'error');
    }
}