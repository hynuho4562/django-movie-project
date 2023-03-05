$(document).ready(function() {
    $("#button-user-add").click(function() {
        $("#modal_add_feed").css({
            display: 'flex'
        });
    });

    $("#modal_close_click").click(function() {
        $("#modal_add_feed").css({
            display: 'none'
        });
    });

    $("#user_data_insert").click(function() {

        let name = $('#user-name').val()
        let email = $('#user-email').val()
        let hobby = $('#user-hobby').val()
        let movie = $('#user-movie').val()

        let formData = new FormData()
        
        formData.append('name', name)
        formData.append('email', email)
        formData.append("hobby", hobby)
        formData.append("movie", movie)

        $.ajax({
            method: "POST",
            url: "/moviePolls/user_add/",
            data: formData,
            processData: false,
            contentType: false,

            success: function (response) {
                console.log("성공")
            },

            error: function () { 
                console.log("실패")
             }
        });
    });
});