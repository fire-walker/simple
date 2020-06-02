$(window).load(function () {
    $("body").removeClass("preload");
});


$(document).ready(function () {
    // dark and light theme switcher
    let darkTheme = localStorage.getItem('theme') === 'dark';
    updateTheme();

    window.addEventListener('storage', () => {
        darkTheme = localStorage.getItem('theme') === 'dark';
        updateTheme();
    });

    function updateTheme() {
        if (darkTheme) {
            $("body").addClass("dark-theme");
        } else {
            $("body").removeClass("dark-theme");
        }
    }

    $(".theme-switch").on("click", () => {
        darkTheme = !darkTheme;
        updateTheme();
        localStorage.setItem('theme', darkTheme ? 'dark' : 'light');
    });


    // index nav & tag nav
    window.onscroll = function() {
        scrollFunction();
    };

    var navbar = document.getElementById("tag-body-header-nav");
    var header = document.getElementById("tag-body-header-h1");
    var sticky = navbar.offsetTop;

    function scrollFunction() {
        if (window.pageYOffset >= sticky) {
            header.classList.add("sticky-head");
            navbar.classList.add("sticky");
        } 

        else if (window.pageYOffset < sticky) {
            header.classList.remove("sticky-head");
            navbar.classList.remove("sticky");
        } 

        else if (document.body.scrollTop > 150 || document.documentElement.scrollTop > 150) {
            document.getElementById("index-body-header-nav").style.top = "0";
        } 

        else {
            document.getElementById("index-body-header-nav").style.top = "-100px";
        }
    }

    // tag page nav - desktop
    var btnContainer = document.getElementById("tag-body-header-nav");
    var btns = btnContainer.getElementsByClassName("btn");

    for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
        // changing which tag is selected
        var current = document.getElementsByClassName("active");

        if (current.length > 0) {
            current[0].className = current[0].className.replace(" active", "");
        }

        this.className += " active";

        // changes the page when a tag is selected
        var pastCard = document.getElementsByClassName("active-cards");
        var currentCard = document.getElementsByClassName("inactive-cards");

        if (pastCard.length > 0) {
            pastCard[0].className = pastCard[0].className.replace(" active-cards", " inactive-cards");
        }

        for (var i = 0; i < currentCard.length; i++) {
            if (currentCard[i].classList[2] == this.classList[0].concat('-content')) {
                currentCard[i].className = currentCard[i].className.replace(" inactive-cards", " active-cards");
            }
        }
    });
    } 
});


