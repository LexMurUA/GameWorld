document.addEventListener("DOMContentLoaded", function () {
   
    fetch("/cart/count/")
        .then(response => response.json())
        .then(data => {
            document.getElementById("cart-counter").textContent = data.cart_items_count;
        })
        .catch(error => console.error("Помилка при оновленні корзини:", error));

    
    document.addEventListener("click", function (event) {
        let button = event.target.closest(".add-to-cart");
        if (!button) return;  

        event.preventDefault();  

        let productId = button.dataset.productId;
        let url = `/cart/add/${productId}/`;

        fetch(url, { method: "GET" })
            .then(response => response.json())
            .then(data => {
                showNotification(data.message);
                updateCartCount(data.cart_items);
            })
            .catch(error => console.error("Помилка:", error));
    });
});


function showNotification(message) {
    let notification = document.createElement("div");
    notification.className = "cart-notification";
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.remove();  
    }, 3000);
}


function updateCartCount(count) {
    let cartCounter = document.getElementById("cart-counter");
    if (cartCounter) {
        cartCounter.textContent = count;
    }
}
