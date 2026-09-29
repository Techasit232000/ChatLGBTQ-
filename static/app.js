const form = document.querySelector('#chat-form');
const input = document.querySelector('#message-input');
const messages = document.querySelector('#messages');
const resetButton = document.querySelector('#reset-button');

function addMessage(role, text) {
  const wrapper = document.createElement('div');
  wrapper.className = `message ${role}`;
  const label = document.createElement('span');
  label.className = 'message-label';
  label.textContent = role === 'user' ? 'You' : 'ChatLGBTQ+';
  const paragraph = document.createElement('p');
  paragraph.textContent = text;
  wrapper.append(label, paragraph);
  messages.appendChild(wrapper);
  messages.scrollTop = messages.scrollHeight;
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  addMessage('user', message);
  input.value = '';
  input.disabled = true;

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message }),
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Unable to get a response.');
    addMessage('assistant', data.response);
  } catch (error) {
    addMessage('assistant', `Sorry, something went wrong: ${error.message}`);
  } finally {
    input.disabled = false;
    input.focus();
  }
});

resetButton.addEventListener('click', async () => {
  await fetch('/api/reset', { method: 'POST' });
  messages.innerHTML = '';
  addMessage('assistant', 'New chat started. How can I help?');
  input.focus();
});
