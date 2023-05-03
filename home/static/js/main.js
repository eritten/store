window.addEventListener("load", ()=>{
    // mobile nav
    const navList = document.querySelector(".nav-list")
    const menuBtn = document.querySelector(".menu-icon")

    menuBtn.addEventListener("click", toggleNav)

    function toggleNav() {
        navList.classList.toggle("active")
    }
    function removeMenu() {
      navList.classList.remove("active")
    }
    const allLinks = document.querySelectorAll(".nav-list a")
          allLinks.forEach(link => {
            link.addEventListener("click", ()=>{
              removeMenu()
            })
          });
    // navbar on scroll
    $(window).on('scroll',function(){
        if($(window).scrollTop() > 70){
          $('nav').css({'background':'#6C5CE7','box-shadow':'0 .2rem .5rem rgba(0,0,0,.4)'});
        }else{
          $('nav').css({'background':'none','box-shadow':'none'});
        }
      });
      // faq accordion
      $('.accordion-header').click(function(){
        $('.accordion .accordion-body').slideUp();
        $(this).next('.accordion-body').slideDown();
        $('.accordion .accordion-header span').text('+');
        $(this).children('span').text('-');
      });
    
    
    
})