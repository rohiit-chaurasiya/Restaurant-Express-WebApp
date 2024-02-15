var swiper = new Swiper(".slide-content", {
        slidesPerView: 5,
        spaceBetween: 15,
        loop: true,
        centerSlide: 'true',
        fade: 'true',
        grabCursor: 'true',
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
          dynamicBullets: true,
        },
        navigation: {
          nextEl: ".next",
          prevEl: ".prev",
        },

        breakpoints:{
            0: {
                slidesPerView: 1,
            },
            294: {
                slidesPerView: 2,
            },
            588: {
                slidesPerView: 3,
            },
            882: {
                slidesPerView: 4,
            },
            1176: {
                slidesPerView: 5,
            },
        },
      });