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
            $("body").removeClass("dynamic-body");
            $("body").addClass("static-body");

        } else {
            $("body").removeClass("dark-theme");
            $("body").removeClass("static-body");
            $("body").addClass("dynamic-body");
        }
    }

    $(".theme-switch").on("click", () => {
        darkTheme = !darkTheme;
        updateTheme();
        localStorage.setItem('theme', darkTheme ? 'dark' : 'light');
    });
});