$(document).ready(function(){

    $("header div.navcontainer").css("display", "none");

    $("header section.right a.navbar").on("click",function(e){
        e.preventDefault()
        $("header div.navcontainer").css("display", "block");
        function display() {
            $("header div.navcontainer").addClass("active") 
        }
        setTimeout(display,50)
    });

    $("header div.navcontainer div.hide, header div.navcontainer div.close span.close").on("click",function(){
        console.log("hello");
        
        function hide() {
            console.log("hello");
            $("header div.navcontainer").css("display", "none");
        }
  
        $("header div.navcontainer").removeClass("active");
        setTimeout(hide, 500);

    });


    $("section#plan ul li a, section#edit ul li a").on("click", function(event){
        event.preventDefault();});
       
    $("section#plan div.days ul li").on("click",function(){
        var $this = $(this);
        $this.addClass("active") 
        $this.siblings().removeClass("active")
       $this.addClass("active");

       var selectedDate = $(this).find("a").data("value");
       $("input#selected_date_input").val(selectedDate);

    });

    $("section#plan div.meals div.breakfast ul li, section#edit div.meals div.breakfast ul li").on("click",function(){
        var $this = $(this);
        $this.addClass("active") 
       $this.siblings().removeClass("active")
       $this.addClass("active");

       var sel_meal = $(this).find("a").data("value");
       $("input#selected_bf_input").val(sel_meal);

    });

    $("section#plan div.meals div.lunch ul li, section#edit div.meals div.lunch ul li").on("click",function(){
        var $this = $(this);
        $this.addClass("active") 
        $this.siblings().removeClass("active")
       $this.addClass("active");

       var sel_meal = $(this).find("a").data("value");
       $("input#selected_lc_input").val(sel_meal);

    });

    $("section#plan div.meals div.snack ul li, section#edit div.meals div.snack ul li").on("click",function(){
        var $this = $(this);
        $this.addClass("active") 
        $this.siblings().removeClass("active")
       $this.addClass("active");

       var sel_meal = $(this).find("a").data("value");
       $("input#selected_sk_input").val(sel_meal);

    });

    $("section#plan div.meals div.dinner ul li, section#edit div.meals div.dinner ul li").on("click",function(){
        var $this = $(this);
        $this.addClass("active") 
        $this.siblings().removeClass("active")
       $this.addClass("active");

       var sel_meal = $(this).find("a").data("value");
       $("input#selected_dr_input").val(sel_meal);
    });


    $("section#plan div.ready button").on("click", function(e) {
        e.preventDefault()

       let $this = $(this);
        let selected_date = $("input#selected_date_input").val();
        console.log(selected_date +"hello")
        $("input#selected_input_date").val(selected_date);

        let selected_breakfast = $("input#selected_bf_input").val();
        console.log(selected_breakfast +"hi")
        $("input#selected_input_breakfast").val(selected_breakfast);

        let selected_lunch = $("input#selected_lc_input").val();
        console.log(selected_breakfast +"hi")
        $("input#selected_input_lunch").val(selected_lunch);

        let selected_snack = $("input#selected_sk_input").val();
        console.log(selected_breakfast +"hi")
        $("input#selected_input_snack").val(selected_snack);

        let selected_dinner = $("input#selected_dr_input").val();
        console.log(selected_breakfast +"hi")
        $("input#selected_input_dinner").val(selected_dinner);
        
    });

    $("section#edit div.ready button").on("click", function(e) {
        e.preventDefault()

        let selected_breakfast = $("input#selected_bf_input").val();
        console.log(selected_breakfast +"hi")
        $("input#selected_input_breakfast").val(selected_breakfast);

        let selected_lunch = $("input#selected_lc_input").val();
        console.log(selected_breakfast +"hi")
        $("input#selected_input_lunch").val(selected_lunch);

        let selected_snack = $("input#selected_sk_input").val();
        console.log(selected_breakfast +"hi")
        $("input#selected_input_snack").val(selected_snack);

        let selected_dinner = $("input#selected_dr_input").val();
        console.log(selected_breakfast +"hi")
        $("input#selected_input_dinner").val(selected_dinner);
        
    });
    
    $("section#plan div.duplicate span, section#edit div.duplicate span").on("click", function(e) {
        var  $this = $(this);
        console.log("clear date")
        $this.siblings("input").val("");
    });

    $("section#food_menu div.tab_head a").on("click",function(){
        $this = $(this);
       $( "section#food_menu div.tab_head a").removeClass("active")
       $this.addClass("active")

       $("section#food_menu section.tab_body div").removeClass("active")
       let clicked_tab = $this.data("id")
       $(`#${clicked_tab}`).addClass("active");

    });

    $(document).on("submit", "form.ajax", function (e) {
        e.preventDefault()
    
       var $this  = $(this);
    
       document.onkeydown = function(evt){
        return false ;
        
       }
        var method =  $this.attr("method");
        var url =  $this.attr("action");
        var noLoader = $this.hasClass("no-loader");
        var noPopup = $this.hasClass("no-popup")
        var isRedirect = $this.hasClass("redirect");
        var isReload = $this.hasClass ("reload")
    
        if (!noLoader){
            Swal.showLoading()
        }
        $.ajax({
            method : method ,
            url : url,
            dataType : "json",
            data : new FormData (this),
            processData : false,
            contentType : false,
            Cache : false,
            success: function(data){
                if (!noLoader){
                    Swal.hideLoading()
                }
                var message = data["message"];
                var title = data["title"];
                var status = data["status"];
                var redirect = data["redirect"]
                var redirect_url = data["redirect_url"]
                var stable = data["stable"];
    
                if (status === "success"){
                    if (title){
                        title = title;
                    }
                    else{
                        title = 'success'
                    }
                    function doAfter(){
                        if (stable != "yes") {
                            if (isRedirect && redirect == "yes") {
                                window.location.href = redirect_url;
                            }
                            if (isReload) {
                                window.location.reload();
                            }
                        }
                    }
    
                    if (noPopup){
                        doAfter();
                    }
                    else{
                        Swal.fire({
                            icon: status,
                            title: title,
                            html: message,
                        }).then((result) =>{
                            console.log(result.isConfirmed)
                            if(result.isConfirmed){
                                doAfter();
    
                            }
                        })
                    }
                    document.onkeydown= function(evt){
                        return true ;
    
                    };
                }
                else {
                    if (title) {
                        title = title;
                    } else {
                        title = "An Error Occurred";
                    }
    
                    Swal.fire(title, message, "error");
    
                    if (stable != "true") {
                        window.setTimeout(function () {}, 2000);
                    }
                    document.onkeydown = function (evt) {
                        return true;
                    };
                }
            },
    
            error: function(data){
    
                Swal.hideLoading();
                var title = "An error occurred";
                var message = "An error occurred. Please try again later.";
                document.onkeydown = function (evt) {
                    return true;
                };
                Swal.fire(title, message, "error");
            }
        })
    });

    $("a.action-button").on("click",function(e){
        e.preventDefault();
        console.log("helo")
        var $this = $(this);
        var text = $this.attr("data-text");
        var title = $this.attr("data-title");
        var confirmButtonText = "Yes";
        var confirmButtonColor = "#DD6B55";
        var type = "warning";
        var url = $this.attr("href");
        if (!title){
            title = "are you sure ?";
        }
        var isReload = $this.hasClass("reload");
        var isRedirect = $this.hasClass("redirect");
        var noResponsePopup = $this.hasClass("no-response-popup");
        swal.fire({
            icon : type,
            title: title,
            text: text,
            showCancelButton: true,
            confirmButtonText: confirmButtonText,
            confirmButtonColor: confirmButtonColor,
        }).then((result) =>{
            if (result.isConfirmed){
                Swal.showLoading();
                window.setTimeout(function(){
                    $.ajax({
                        type : "get",
                        url : url,
                        dataType: "json",
                        success: function(data){
                            var message = data["message"]
                            var status = data["status"]
                            var redirect = data["redirect"]
                            var redirect_url = data["redirect_url"]
                            var stable = data["stable"]
                            var title = data["title"]

                            Swal.hideLoading();
                            if (status == "success") {
                                if (title) {
                                    title = title;
                                } else {
                                    title = "Success";
                                }

                                if (!noResponsePopup) {
                                    Swal.fire({
                                        icon: "success",
                                        title: title,
                                        text: message,
                                        type: "success",
                                    }).then((result) => {
                                        if (stable != "yes") {
                                            if (isRedirect && redirect == "yes") {
                                                window.location.href = redirect_url;
                                            }
                                            if (isReload) {
                                                window.location.reload();
                                            }
                                        }
                                    });
                                }

                            }else {
                                if (title) {
                                    title = title;
                                } else {
                                    title = "An Error Occurred";
                                }

                                Swal.fire(title, message, "error");

                                if (stable != "true") {
                                    window.setTimeout(function () {}, 2000);
                                }
                            }
                        },
                        error: function(data){
                            Swal.hideLoading();
                            var title = "An error occurred";
                            var message =
                                "An error occurred. Please try again later.";
                            Swal.fire(title, message, "error");
                        }
                    })
                },100)
            }
        }) 
        });
})