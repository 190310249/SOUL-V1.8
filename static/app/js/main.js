$(document).ready(function () {
    $("#purpose-carousel").owlCarousel({
        loop: true,
        margin: 30,
        autoplay: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            1200: {
                items: 3
            }
        }

    });
})

$(document).ready(function () {
    $("#testimonial-carousel").owlCarousel({
        loop: true,
        margin: 70,
        autoplay: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            992: {
                items: 2
            }
        }

    });
})

$(document).ready(function () {
    $("#project-carousel").owlCarousel({
        loop: true,
        margin: 30,
        autoplay: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            1200: {
                items: 3
            }
        }

    });
})

$(document).ready(function () {
    $("#volunteers-carousel").owlCarousel({
        loop: true,
        margin: 30,
        autoplay: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            1200: {
                items: 3
            },

        }

    });
})

// Disable scroll on body 

$(document).ready(function disableBody() {
    let checkbox = document.getElementById("check")
    var body = document.body;

    checkbox.addEventListener('change', () => {
        if (checkbox.checked) {
            body.style.overflow = "hidden";
        } else {
            body.style.overflow = "scroll";
        }
    })
})