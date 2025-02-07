if ('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(
        (position) => {
            const { latitude, longitude } = position.coords;
            console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
            },
        (error) => {
            console.error('Error getting geolocation:', error);
            },
        {
            enableHighAccuracy: false, // Высокая точность
            timeout: 5000, // Таймаут ожидания ответа (мс)
            maximumAge: 0
            // Максимальное время, в течение которого можно использовать кэшированные данные (мс)
        });
    } else {
    console.log('Geolocation is not supported by this browser.');
    }