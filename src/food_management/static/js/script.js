$(document).ready(function(){

    $("section#plan div.days ul li a").on("click", function(event){
        event.preventDefault();})

    $("section#plan div.days ul li").on("click",function(){
        $this = $(this);
        $this.addClass("active")
       $( "section#plan div.days ul li").removeClass("active")
       $this.addClass("active");

       var selectedDate = $(this).find("a").data("value");
       $("input#selected_date_input").val(selectedDate);

    });
    $("section#plan div.days ul li a").ready(function(){
        

    });

    $("section#food_menu div.tab_head a").on("click",function(){
        $this = $(this);
       $( "section#food_menu div.tab_head a").removeClass("active")
       $this.addClass("active")

       $("section#food_menu section.tab_body div").removeClass("active")
       let clicked_tab = $this.data("id")
       $(`#${clicked_tab}`).addClass("active");

    })

})
