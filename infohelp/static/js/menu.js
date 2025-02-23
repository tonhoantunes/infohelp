function menuShow() {
    let menuMobile = document.querySelector('.menu-mobile');
    if (menuMobile.classList.contains('open')) {
        menuMobile.classList.remove('open');
        let imgElemento = document.getElementById(".icon");
        let imgUrl = imgElemento.getAttribute("data-src");
        document.querySelector('.icon').src = imgUrl;
    } else {
        menuMobile.classList.add('open');
        let imgElemento = document.getElementById(".icon");
        let imgUrl = imgElemento.getAttribute("data-src");
        document.querySelector('.icon').src = '/';
    }
}