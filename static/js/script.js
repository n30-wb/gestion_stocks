document.addEventListener('DOMContentLoaded', function() {
    // 1. Animation des messages Flash (déjà faite, mais on l'améliore)
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transform = "translateX(100%)";
            alert.style.opacity = "0";
            setTimeout(() => alert.remove(), 500);
        }, 3000);
    });

    // 2. Effet Focus sur les lignes du tableau
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach(row => {
        row.addEventListener('mouseenter', () => {
            rows.forEach(r => { if(r !== row) r.style.opacity = "0.5"; });
        });
        row.addEventListener('mouseleave', () => {
            rows.forEach(r => { r.style.opacity = "1"; });
        });
    });
});