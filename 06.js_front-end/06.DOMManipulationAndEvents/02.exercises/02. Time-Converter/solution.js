function attachEventsListeners() {
    const daysElement = document.getElementById('days');
    const hrsElement = document.getElementById('hours');
    const minElement = document.getElementById('minutes');
    const secElement = document.getElementById('seconds');
    const daysButtonElement = document.getElementById('daysBtn');
    const hrsButtonElement = document.getElementById('hoursBtn');
    const minButtonElement = document.getElementById('minutesBtn');
    const secButtonElement = document.getElementById('secondsBtn');

    daysButtonElement.addEventListener('click', () => {
        hrsElement.value = Number(daysElement.value)*24;
        minElement.value = Number(hrsElement.value)*60;
        secElement.value = Number(minElement.value)*60;
    })
    hrsButtonElement.addEventListener('click', () => {
        daysElement.value = Number(hrsElement.value)/24;
        minElement.value = Number(hrsElement.value)*60;
        secElement.value = Number(minElement.value)*60;
    })
    minButtonElement.addEventListener('click', () => {
        hrsElement.value = Number(minElement.value)/60;
        daysElement.value = Number(hrsElement.value)/24;
        secElement.value = Number(minElement.value)*60;
    })
    secButtonElement.addEventListener('click', () => {
        minElement.value = Number(secElement.value)/60;
        hrsElement.value = Number(minElement.value)/60;
        daysElement.value = Number(hrsElement.value)/24;
    })
}