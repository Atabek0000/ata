document.addEventListener('DOMContentLoaded', () => {
    const contactsList = document.getElementById('contacts-list');
    const contactForm = document.getElementById('contact-form');
    const chatForm = document.getElementById('chat-form');
    const chatBox = document.getElementById('chat-box');
    const messageInput = document.getElementById('message-input');
    const contactNameInput = document.getElementById('contact-name');

    let contacts = [];
    let currentContact = null;

    // Добавление нового контакта
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const contactName = contactNameInput.value.trim();
        if (contactName === '') return;

        const contact = { name: contactName, messages: [] };
        contacts.push(contact);
        addContactToList(contact);
        contactNameInput.value = '';
    });

    // Отправка сообщения
    chatForm.addEventListener('submit', (e) => {
        e.preventDefault();

        if (!currentContact) {
            alert('Выберите контакт перед отправкой сообщения');
            return;
        }

        const messageText = messageInput.value.trim();
        if (messageText === '') return;

        addMessage(messageText, 'sent');
        currentContact.messages.push({ text: messageText, type: 'sent' });
        messageInput.value = '';

        setTimeout(() => {
            const replyText = 'Спасибо за вашу проблему в данное время проверим';
            addMessage(replyText, 'received');
            currentContact.messages.push({ text: replyText, type: 'received' });
        }, 1000);
    });

    // Добавление контакта в список
    function addContactToList(contact) {
        const li = document.createElement('li');
        li.textContent = contact.name;
        li.addEventListener('click', () => {
            currentContact = contact;
            // Удаление предыдущего активного класса
            const activeContact = contactsList.querySelector('.active');
            if (activeContact) {
                activeContact.classList.remove('active');
            }
            // Установка нового активного класса
            li.classList.add('active');
            chatBox.innerHTML = '';
            currentContact.messages.forEach(msg => addMessage(msg.text, msg.type));
        });
        contactsList.appendChild(li);
    }

    // Добавление сообщения в чат
    function addMessage(text, type) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', type);
        messageElement.textContent = text;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});
