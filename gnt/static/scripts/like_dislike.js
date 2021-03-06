// $(document).ready(function() {
//     var anchor = $(".thumbsup");
//     // Add click listener to each thumbs up button
//     anchor.each(function likeDrink(index, element) {
//         $(this).on("click", function likeDrink() {
//             var user = $(this).attr("user");
//             var drink_id = $(this).attr("drinkid");
//             var url = APPURL + "/like_drink/";
//             var payload = {
//                 drink_id: drink_id,
//                 user: user
//             };
//             var csrftoken = getCookie("csrftoken");
//             var thumbsup = $("a[drinkid='" + drink_id + "']:first");
//             var thumbsdown = $("a[drinkid='" + drink_id + "']:last");
//             $.ajax({
//                 url: url,
//                 method: "POST",
//                 headers: { "X-CSRFToken": csrftoken },
//                 data: payload,
//                 dataType: "json",
//                 success: function(data) {
//                     if (data["status"] == 201) {
//                         console.log("Drink liked!");
//                         likeDrinkAnimation(thumbsup, thumbsdown);
//                     } else if (data["status"] == 422) {
//                         console.log("Already liked");
//                     } else {
//                         console.log(data["status"]);
//                         console.log(data["message"]);
//                     }
//                 },
//                 error: function(xhr, ajaxOptions, thrownError) {
//                     console.log(xhr);
//                 }
//             });
//         });
//     });
// });

// $(document).ready(function() {
//     var anchor = $(".thumbsdown");
//     // Add click listener to each thumbs up button
//     anchor.each(function likeDrink(index, element) {
//         $(this).on("click", function likeDrink() {
//             var user = $(this).attr("user");
//             var drink_id = $(this).attr("drinkid");
//             var url = APPURL + "/dislike_drink/";
//             var payload = {
//                 drink_id: drink_id,
//                 user: user
//             };
//             var csrftoken = getCookie("csrftoken");
//             var thumbsup = $("a[drinkid='" + drink_id + "']:first");
//             var thumbsdown = $("a[drinkid='" + drink_id + "']:last");
//             $.ajax({
//                 url: url,
//                 method: "POST",
//                 headers: { "X-CSRFToken": csrftoken },
//                 data: payload,
//                 dataType: "json",
//                 success: function(data) {
//                     if (data["status"] == 201) {
//                         console.log("Drink disliked!");
//                         dislikeDrinkAnimation(thumbsup, thumbsdown);
//                     } else if (data["status"] == 422) {
//                         console.log(
//                             "This is already in your disliked drinks"
//                         );
//                     } else {
//                         console.log("Error in disliking drink");
//                     }
//                 },
//                 error: function(xhr, ajaxOptions, thrownError) {
//                     console.log(xhr);
//                 }
//             });
//         });
//     });
// });

function likeDrinkFeedback(message) {
    document.getElementById("like-drink").innerHTML = message;
    $("#like-drink").show("slow");
    setTimeout(hideLikeDrinkFeedback, 5000);
}

function likeDrinkError(message) {
    document.getElementById("like-drink").innerHTML = message;
    $("#like-drink").show("slow");
    setTimeout(hideLikeDrinkError, 5000);
}

function hideLikeDrinkFeedback() {
    $("#like-drink").hide("slow");
}

function hideLikeDrinkError() {
    $("#dislike-drink").hide("slow");
}

function likeDrinkAnimation(thumbsup, thumbsdown){
    thumbsup.children("#blank_thumbsup").hide();
    thumbsup.children("#filled_thumbsup").show();
    thumbsdown.children("#blank_thumbsdown").show();
    thumbsdown.children("#filled_thumbsdown").hide();
}

function dislikeDrinkAnimation(thumbsup, thumbsdown){
    thumbsup.children("#blank_thumbsup").show();
    thumbsup.children("#filled_thumbsup").hide();
    thumbsdown.children("#blank_thumbsdown").hide();
    thumbsdown.children("#filled_thumbsdown").show();
}
