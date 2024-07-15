document.getElementById('adminLoginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const adminId = document.getElementById('adminId').value;
    const adminPassword = document.getElementById('adminPassword').value;

    if (adminId === 'admin' && adminPassword === 'admin') {
        window.location.href = '/admin';
    } else {
        alert('Invalid ID or Password');
    }
});