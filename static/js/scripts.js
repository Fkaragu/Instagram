$(document).ready(function () {
    var navbarCollapse = function () {
        if ($("#navMain").offset().top > 40) {
            $("#navMain").addClass("navbar-shrink");
        } else {
            $("#navMain").removeClass("navbar-shrink");
        }
    };
    navbarCollapse();
    $(window).scroll(navbarCollapse);
})
