document.getElementById('fetch-data').addEventListener('click', function() {
    fetch('/data') //  Giả sử endpoint /data trả về dữ liệu JSON
        .then(response => response.json())
        .then(data => {
            document.getElementById('data-container').textContent = JSON.stringify(data);
        })
        .catch(error => console.error('Error fetching data:', error));
});