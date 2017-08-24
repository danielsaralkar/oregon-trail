var OregonTrail = {};


$(document).ready(function(){
    $(".img-rounded").click(function(){
        $(".img-rounded").css({"border":"0px"}).removeClass("selected");
        $(this).css({"border":"3px solid blue"}).addClass("selected");
    });

    $(".advance").click(function(){
        $(".part1").hide();
        $(".part2").show();
        $.get("/supplies", function(result){
            
        });
    });

    
})
    

