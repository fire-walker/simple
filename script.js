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

    $(".theme-switch").on("click", () => {
        darkTheme = !darkTheme;
        updateTheme();
        localStorage.setItem('theme', darkTheme ? 'dark' : 'light');
    });
});