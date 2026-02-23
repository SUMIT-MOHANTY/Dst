async function loadData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        document.getElementById('users').textContent = data.users;
        document.getElementById('messages').textContent = data.messages;
        document.getElementById('sales').textContent = '$' + data.sales;
    } catch (error) {
        console.error('Error loading data:', error);
    }
}
loadData();
