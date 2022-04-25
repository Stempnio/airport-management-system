// function updateClock(id) {
//     let now = new Date()
//     let months = ['January', 'February', 'March', 'April',
//         'May', 'June', 'July', 'August', 'September',
//         'October', 'November', 'December'];
//     let time = now.getHours() + ':' + now.getMinutes() + ":" + now.getSeconds()
//
//     let date = [now.getDate(),
//                 months[now.getMonth()],
//                 now.getFullYear()].join(' ');
//
//     document.getElementById(id).innerHTML = [date, time].join(' / ');
//
//     setTimeout(updateClock, 1000);
// }