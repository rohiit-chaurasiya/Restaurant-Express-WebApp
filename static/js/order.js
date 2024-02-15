document.addEventListener("DOMContentLoaded", function() {
    var upcomingOrders = document.getElementById("upcoming-orders");
    var pastOrders = document.getElementById("past-orders");
    var upcomingOrdersLink = document.querySelector(".upcoming-orders-link");
    var pastOrdersLink = document.querySelector(".past-orders-link");

    upcomingOrders.addEventListener("click", function() {
        upcomingOrders.classList.add("active");
        pastOrders.classList.remove("active");

        upcomingOrders.style.backgroundColor = "#fff";
        pastOrders.style.backgroundColor = "#F6F7F8";
        upcomingOrdersLink.style.color = "#4466F2";
        pastOrdersLink.style.color = "#0D0D0D";

        document.getElementById("upcoming-orders-hr").style.display = "block";
        document.getElementById("past-orders-hr").style.display = "none";
    });

    pastOrders.addEventListener("click", function() {
        pastOrders.classList.add("active");
        upcomingOrders.classList.remove("active");

        upcomingOrders.style.backgroundColor = "#F6F7F8";
        pastOrders.style.backgroundColor = "#fff";
        pastOrdersLink.style.color = "#4466F2";
        upcomingOrdersLink.style.color = "#0D0D0D";

        document.getElementById("past-orders-hr").style.display = "block";
        document.getElementById("upcoming-orders-hr").style.display = "none";
    });
});