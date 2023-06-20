let zoom = 150;
let counted = 0;
let counted1 = 0;
let counted2 = 0;
$(document).ready(function(){
    let idObj;
    let o = 0;
    $('.img4x4').on('click', function (){
        idObj = $(this).prop('id');
    });

    $('.miniPicture').on('click', function (){
        idObj = $(this).prop('id');
    });

    $('.textModel').css('display', 'none');
    

    $('.img4x4').on('click', function(){
        $('#'+idObj).toggle();
        $('p#'+((Number(idObj)+999999999999999))).css('display', 'block');
        console.log((Number(idObj)+999999999999999));
        $("body").addClass("fixed");
        o = 1;
        $('.textModel').css('display', 'grid')
    });

    $('.miniPicture').on('click', function(){
        $('#'+idObj).toggle();
        $('p#'+((Number(idObj)+999999999999999))).css('display', 'block');
        console.log((Number(idObj)+999999999999999));
        $("body").addClass("fixed");
        o = 1;
        $('.textModel').css('display', 'grid')
    });

    $('.modileWindow').on('click', function(){
        $('#'+idObj).toggle();
        $('p#'+(Number(idObj)+999999999999999)).css('display', 'none');
        $("body").removeClass("fixed");
        o = 0;
        $('.textModel').css('display', 'none')
    });

    document.addEventListener('keyup', function(event){
        r = event.key;
        if (r == "Escape" && o == 1){
            $('#'+idObj).toggle();
            o = 0;
            $('p#'+(Number(idObj)+999999999999999)).css('display', 'none');
            $("body").removeClass("fixed");
            $('.textModel').css('display', 'none')
        }
    });

    $('.zoomButton').on('click', function(){
        

        if (counted == 0 && counted1 == 0 && counted2 == 0){
            counted += 1;
            $(".adaptIMG").css({"width": zoom + "%", 'margin-top':'5%'});
        }else if (counted == 1 && counted1 == 0 && counted2 == 0){
            counted1 += 1;
            zoom += 50;
            $(".adaptIMG").css({"width": zoom +"%", 'margin-top':'5%'});
        }else if (counted == 1 && counted1 == 1 && counted2 == 0){
            counted2 = 1;
            zoom += 200;
            $(".adaptIMG").css({"width": zoom +"%", 'margin-top':'5%'});
        }else if (counted == 1 && counted1 == 1 && counted2 == 1){
            counted = 0;
            counted2 = 0;
            counted1 = 0;
            zoom = 100;
        };
    });
   

    

    
    // $('.zoomButton').on('click', function(){
    //     $(".adaptIMG").css({"width": "300%", 'margin-top':'0'});
    // });

    $('.outZoomButton').on('click', function(){
        $(".adaptIMG").css({"width": "90%", 'margin-top':'5%'});
    });

});