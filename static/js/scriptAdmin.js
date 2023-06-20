// let selector = document
function burgerMenu(selector){
    let menu = $(selector);
    let button = menu.find ('.burger-menu__btn_Admin');
    let subMenu = menu.find ('.subMain');
    let overlay = menu.find ('.burger-menu__overlay_Admin');
  
    button.on('click', (e) => {
        e.preventDefault();
        toggleMenu();
    });
  
    // overlay.on('click', () => toggleMenu());
  
    function toggleMenu() {
        menu.toggleClass('burger-menu__active_Admin');
    
        if(menu.hasClass('burger-menu__active_Admin')){
            $('.contents').css({'margin-left':'16%',
                                'width':'80%'});
            $('.contents_1').css({'margin-left':'16%',
                                'width':'80%'});
        }else{
            $('.contents').css({'margin-left':'5%',
                                'width':'90%'});
            $('.contents_1').css({'margin-left':'5%',
                                'width':'90%'});
        }
    }

}

burgerMenu('.burger-menu_Admin');
let widthScreen = window.screen.width;
$(document).ready(function(){
    $('#hidenMenu0').on('click', function(){
        $('.modileWin').css({'display':'grid','animation' : 'alternate 0.6s downWin', 'margin-top': '3%'});
        $('.closeB').css({'display':'grid'});
    });
    if (widthScreen < 600){
        $('#hidenMenu0').on('click', function(){
            $('.modileWin').css({'display':'grid','animation' : 'alternate 0.6s downWin', 'margin-top': '0%'});
            $('.closeB').css({'display':'grid'});
        });
    }

    $('.closeB').on('click', function(){
        $('.modileWin').css({'animation' : 'alternate 0.3s upWin', 'margin-top': '0%'});
        setTimeout(() => { $('.modileWin').css({'display':'none'});}, 200);
        setTimeout(() => { $('.closeB').css({'display':'none'});}, 350);
    });

    $('.btncls').on('click', function(){
        $('.modileWin').css({'animation' : 'alternate 0.3s upWin', 'margin-top': '0%'});
        setTimeout(() => { $('.modileWin').css({'display':'none'});}, 200);
        setTimeout(() => { $('.closeB').css({'display':'none'});}, 350);
    });

    $('.yesBTH').on('click', function(){
        refresh
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

    // $('#hidenMenu5').on('click', function(){
    //     $('.subMain5').toggle();
    // });

    $('#hidenMenu6').on('click', function(){
        $('.subMain6').toggle();
    });

    $('#hidenMenu7').on('click', function(){
        $('.subMain7').toggle();
    });
  
    $('#flexSwitchCheckDefault1').on('click', function(){
        $('.listAllMenu').toggle();
    });

    document.getElementById("formControlFile1").value = "";
});      

$('input[type=checkbox]').each(function () {
    if ($(this).prop('checked')) {
        
    }
});

