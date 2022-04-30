function updateClock() {
    let now = new Date()
    let months = ['January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August', 'September',
        'October', 'November', 'December'];
    let time = String(now.getHours()).padStart(2, "0") + ':' + String(now.getMinutes()).padStart(2, "0") + ":" + String(now.getSeconds()).padStart(2, "0")

    let date = [now.getDate(),
        months[now.getMonth()],
        now.getFullYear()].join(' ');

    document.getElementById('time').innerHTML = [date, time].join(' / ');

    setTimeout(updateClock, 1000);
}

updateClock(); // initial call