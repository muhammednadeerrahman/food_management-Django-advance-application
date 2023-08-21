$(document).ready(function(){

    $("section#plan div.days ul li a").on("click", function(event){
        event.preventDefault();});
       

    $("section#plan div.days ul li").on("click",function(){
        var $this = $(this);
        $this.addClass("active") 
       $( "section#plan div.days ul li").removeClass("active")
       $this.addClass("active");

       var selectedDate = $(this).find("a").data("value");
       $("input#selected_date_input").val(selectedDate);

    });

    // $("section#plan div.meals span.label").on("click",function(){
    //     var $this = $(this);
    //     $this.addClass("active") 
    //    $( "section#plan div.meals span.label").removeClass("active")
    //    $this.addClass("active");

    // });

    $("section#plan div.ready a.button").on("click", function(e) {
        e.preventDefault()

        $this = $(this);

        var selected_breakfast = $("section#plan div.meals div.item div.breakfast label.radio input").val();
        $("input#selected_input_breakfast").val(selected_breakfast);

        var selected_lunch = $("section#plan div.meals div.item div.lunch label.radio input").val();
        $("input#selected_input_lunch").val(selected_lunch);

        var selected_snack = $("section#plan div.meals div.item div.snack label.radio input").val();
        $("input#selected_input_snack").val(selected_snack);

        var selected_dinner = $("section#plan div.meals div.item div.dinner label.radio input").val();
        $("input#selected_input_dinner").val(selected_dinner);
    
    });
    $("section#plan div.duplicate a.b_delete").on("click", function(e) {
        e.preventDefault()
        var  $this = $(this);
        $("section#plan div.breakfast label.radio input").val("")
        $("input#selected_input_breakfast").val("");
    });




    // $("section#plan div.meals div.item div.breakfast label.radio").on("click", function() {
    //     console.log("Clicked on a breakfast option.");
    //     $this = $(this);
    //     var selected_dish = $(this).find("input").val();
    //     console.log(selected_dish)
    //     $("input#selected_input_breakfast").val(selected_dish);
    
    // });
  



    // $("section#plan div.meals div.item div.lunch label.radio").on("click", function() {
    //     console.log("Clicked on a lunch option.");
    //     $this = $(this);
    //     var selected_dish = $(this).find("input").val();
    //     console.log(selected_dish)
    //     $("input#selected_input_lunch").val(selected_dish);
    
    // });

    // $("section#plan div.meals div.item div.snack label.radio").on("click", function() {
    //     console.log("Clicked on a snack option.");
    //     $this = $(this);
    //     var selected_dish = $(this).find("input").val();
    //     console.log(selected_dish)
    //     $("input#selected_input_snack").val(selected_dish);
    
    // });

    // $("section#plan div.meals div.item div.dinner label.radio").on("click", function() {
    //     console.log("Clicked on a dinner option.");
    //     $this = $(this);
    //     var selected_dish = $(this).find("input").val();
    //     console.log(selected_dish)
    //     $("input#selected_input_dinner").val(selected_dish);
    
    // });

    // $("section#plan div.meals div.item div.breakfast label.radio").on("click",function(){
    //     $this = $(this);
    //     $this.addClass("active")
    //    var selected_dish = $(this).find("input").val();
    //     $("section#plan div.duplicate label.confirm").addClass(selected_dish);

    // });

    $("section#food_menu div.tab_head a").on("click",function(){
        $this = $(this);
       $( "section#food_menu div.tab_head a").removeClass("active")
       $this.addClass("active")

       $("section#food_menu section.tab_body div").removeClass("active")
       let clicked_tab = $this.data("id")
       $(`#${clicked_tab}`).addClass("active");

    });

})



// $("section#plan div.meals span.label").on("click",function(){
    //     var $this = $(this);
    //     $this.addClass("active") 
    //    $( "section#plan div.meals span.label").removeClass("active")
    //    $this.addClass("active");

    // });


    // $("section#plan div.meals div.item div.breakfast label.radio").on("click", function() {
    //     console.log("Clicked on a breakfast option.");
    //     $this = $(this);
    //     var selected_dish = $(this).find("input").val();
    //     console.log(selected_dish)
    //     $("input#selected_input_breakfast").val(selected_dish);
    
    // });
  



    // $("section#plan div.meals div.item div.lunch label.radio").on("click", function() {
    //     console.log("Clicked on a lunch option.");
    //     $this = $(this);
    //     var selected_dish = $(this).find("input").val();
    //     console.log(selected_dish)
    //     $("input#selected_input_lunch").val(selected_dish);
    
    // });

    // $("section#plan div.meals div.item div.snack label.radio").on("click", function() {
    //     console.log("Clicked on a snack option.");
    //     $this = $(this);
    //     var selected_dish = $(this).find("input").val();
    //     console.log(selected_dish)
    //     $("input#selected_input_snack").val(selected_dish);
    
    // });

    // $("section#plan div.meals div.item div.dinner label.radio").on("click", function() {
    //     console.log("Clicked on a dinner option.");
    //     $this = $(this);
    //     var selected_dish = $(this).find("input").val();
    //     console.log(selected_dish)
    //     $("input#selected_input_dinner").val(selected_dish);
    
    // });

    // $("section#plan div.meals div.item div.breakfast label.radio").on("click",function(){
    //     $this = $(this);
    //     $this.addClass("active")
    //    var selected_dish = $(this).find("input").val();
    //     $("section#plan div.duplicate label.confirm").addClass(selected_dish);

    // });