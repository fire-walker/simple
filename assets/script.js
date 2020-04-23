var transition = {
    '-moz-transition': 'color 0.2s ease-in',
    '-o-transition': 'color 0.2s ease-in',
    '-webkit-transition': 'color 0.2s ease-in',
    'transition': 'color 0.2s ease-in'
};

var nothing = {
    '-moz-transition': 'none',
    '-o-transition': 'none',
    '-webkit-transition': 'none',
    'transition': 'none'   
}

$(document).ready(function () {
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

    function open_trans() {
        $("body").removeClass("dynamic-body");
        $("body").addClass("static-body");
        $("h1").css(nothing);
        $("p").css(nothing);
        
    }

    $(".theme-switch").on("click", () => {
        darkTheme = !darkTheme;
        updateTheme();
        localStorage.setItem('theme', darkTheme ? 'dark' : 'light');
        $("body").removeClass("static-body");
        $("body").addClass("dynamic-body");
        $("h1").css(transition);
        $("p").css(transition);
        setTimeout(open_trans, 3000)
    });
});