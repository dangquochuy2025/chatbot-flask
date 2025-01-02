document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    var userMessage = document.getElementById('user-input').value;
    
    if (userMessage.trim() === "") return; // Không gửi nếu không có tin nhắn

    // Hiển thị tin nhắn người dùng
    appendMessage(userMessage, 'user-message');

    // Gửi tin nhắn đến server và nhận phản hồi
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        // Hiển thị phản hồi của chatbot
        appendMessage(data.response, 'bot-response');
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Xóa input sau khi gửi
    document.getElementById('user-input').value = '';
}

function appendMessage(message, className) {
    var chatlogs = document.getElementById('chatlogs');
    var messageDiv = document.createElement('div');
    messageDiv.classList.add('message', className);
    messageDiv.textContent = message;
    chatlogs.appendChild(messageDiv);
    chatlogs.scrollTop = chatlogs.scrollHeight; // Tự động cuộn xuống dưới khi có tin nhắn mới
}
