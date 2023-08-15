$(document).ready(function(){

    $("section#food_menu div.tab_head a").on("click",function(){
        $this = $(this);
       $( "section#food_menu div.tab_head a").removeClass("active")
       $this.addClass("active")

       $("section#food_menu section.tab_body div").removeClass("active")
       let clicked_tab = $this.data("id")
       $(`#${clicked_tab}`).addClass("active");

    })

})
