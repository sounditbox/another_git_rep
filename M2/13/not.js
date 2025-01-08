
if (Notification.permission === 'granted') {
  const options = {
    body: 'This is a notification body',
    icon: 'icon.png',
    data: { url: 'https://example.com' }
  };
  const notification = new Notification('Hello, world!', options);


  notification.onclick = (event) => {
    event.preventDefault();
    window.open(notification.data.url, '_blank');
  };
}