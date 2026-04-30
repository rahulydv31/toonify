// ✅ IMPORTANT: Local backend URL
const BASE_URL = "https://toonify-1fjj.onrender.com";

// Handle Sign In
async function handleSignIn() {
    const username = document.getElementById('signin-username').value;
    const password = document.getElementById('signin-password').value;

    if (!username || !password) {
        showToast('Please fill in all fields', 'error');
        return;
    }

    try {
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

        // ⚠️ FIX: handle non-JSON safely
        let data;
        try {
            data = await response.json();
        } catch {
            data = {};
        }

        if (response.ok) {
            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('token_type', data.token_type);

            showToast('Sign in successful!', 'success');

            setTimeout(() => {
                window.location.href = 'dashboard.html';
            }, 1000);

        } else {
            showToast(data.detail || 'Invalid credentials', 'error');
        }

    } catch (error) {
        console.error('Sign in error:', error);
        showToast('Cannot connect to backend (is it running?)', 'error');
    }
}

// Toast fallback
function showToast(message, type = 'info') {
    alert(message);
}