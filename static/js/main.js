$(document).ready(function() {

  $('.albums img').click(function(e) {
    var img = $(e.target);
    var imgsrc = img.attr('src');
    
    console.log(imgsrc);

    $('#album-cover').attr('src',imgsrc);
    $('#background').css('background-image',"url('"+imgsrc+"')");

  });
});
