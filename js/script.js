/*========== sticky navbar ========== */

window.onscroll = () => {
    console.log("ça marche.");
    let header = document.querySelector('.header');
    header.classList.toggle('sticky', window.scrollY> 100);
}
