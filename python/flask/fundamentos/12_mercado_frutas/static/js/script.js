document.addEventListener("DOMContentLoaded", () => {
    const frutaCards = document.querySelectorAll(".fruta-card");
    const totalItemsElem = document.getElementById("total-items");
    const totalPriceElem = document.getElementById("total-price");

    function updateTotals() {
        let totalItems = 0;
        let totalPrice = 0;

        frutaCards.forEach(card => {
            const input = card.querySelector(".counter-input");
            if (input) {
                const precio = parseFloat(input.getAttribute("data-precio")) || 0;
                let cantidad = parseInt(input.value) || 0;

                if (cantidad < 0) {
                    cantidad = 0;
                    input.value = 0;
                }

                totalItems += cantidad;
                totalPrice += cantidad * precio;
            }
        });

        if (totalItemsElem) totalItemsElem.innerText = totalItems;
        if (totalPriceElem) totalPriceElem.innerText = '$' + totalPrice.toFixed(2);
    }

    frutaCards.forEach(card => {
        const btnMinus = card.querySelector(".btn-minus");
        const btnPlus = card.querySelector(".btn-plus");
        const input = card.querySelector(".counter-input");

        if (btnPlus && input) {
            btnPlus.addEventListener("click", (e) => {
                e.preventDefault();
                input.value = (parseInt(input.value) || 0) + 1;
                updateTotals();
            });
        }

        if (btnMinus && input) {
            btnMinus.addEventListener("click", (e) => {
                e.preventDefault();
                const actual = parseInt(input.value) || 0;
                if (actual > 0) {
                    input.value = actual - 1;
                    updateTotals();
                }
            });
        }

        if (input) {
            input.addEventListener("input", () => {
                updateTotals();
            });
        }
    });
});
