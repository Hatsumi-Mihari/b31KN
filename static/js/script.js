// let selector = document
function burgerMenu(selector){
    let menu = $(selector);
    let button = menu.find ('.burger-menu__btn');
    let subMenu = menu.find ('.subMain');
    let overlay = menu.find ('.burger-menu__overlay');
  
    button.on('click', (e) => {
        e.preventDefault();
        toggleMenu();
    });
  
    // overlay.on('click', () => toggleMenu());
  
    function toggleMenu() {
        menu.toggleClass('burger-menu__active');
    
        if(menu.hasClass('burger-menu__active')){
            $('body').css('overflow', 'hidden');
        }else{
            $('body').css('overflow', 'visible');
        }
    }

}

burgerMenu('.burger-menu');
$(document).ready(function(){
    $('#hidenMenu0').on('click', function(){
        $('.subMain0').toggle();
    });

    $('#hidenMenu1').on('click', function(){
        $('.subMain1').toggle();
    });

    $('#hidenMenu2').on('click', function(){
        $('.subMain2').toggle();
    });

    $('#hidenMenu3').on('click', function(){
        $('.subMain3').toggle();
    });

    $('#hidenMenu4').on('click', function(){
        $('.subMain4').toggle();
    });

    $('#hidenMenu5').on('click', function(){
        $('.subMain5').toggle();
    });

    $('#hidenMenu6').on('click', function(){
        $('.subMain6').toggle();
    });

    $('#hidenMenu7').on('click', function(){
        $('.subMain7').toggle();
    });

    $('#hidenMenu8').on('click', function(){
        $('.subMain8').toggle();
    });

    $('#hidenMenu9').on('click', function(){
        $('.subMain9').toggle();
    });

    $('#hidenMenu10').on('click', function(){
        $('.subMain10').toggle();
    });

    $('#hidenMenu11').on('click', function(){
        $('.subMain11').toggle();
    });


});                