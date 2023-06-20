let input = document.getElementById('add');
$(document).ready(function(){
    $('#IMG_ADD_BLOCK').on('click', function (){
        add.value += '|imgBlock-(type,id1,di2)|\n';
    });
    $('#TITLE_ADD').on('click', function (){
        add.value += '|title-(text)|\n';
    });
    $('#TEXT_ADD').on('click', function (){
        add.value += '|text-(text)|\n';
    });
    $('#YOTUBE_VIDEO_ADD').on('click', function (){
        add.value += '|includeYT-(link)|\n';
    });
})