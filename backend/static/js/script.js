// =============================
// HAMBURGER MENU
// =============================

function toggleMenu() {

    const menu = document.getElementById("mainMenu");

    menu.classList.toggle("active");

}



// =============================
// LANGUAGE TOGGLE
// =============================

let currentLanguage = "en";


function toggleLanguage() {

    const button = document.querySelector(".language-btn");


    if (currentLanguage === "en") {

        currentLanguage = "hi";

        button.innerText = "English";


        // Normal text

        document.querySelectorAll("[data-hi]").forEach(function(element) {

            element.innerText = element.getAttribute("data-hi");

        });


        // Input placeholders

        document.querySelectorAll("[data-placeholder-hi]").forEach(function(element) {

            element.placeholder =
                element.getAttribute("data-placeholder-hi");

        });


    }

    else {

        currentLanguage = "en";

        button.innerText = "हिंदी";


        // Normal text

        document.querySelectorAll("[data-en]").forEach(function(element) {

            element.innerText = element.getAttribute("data-en");

        });


        // Input placeholders

        document.querySelectorAll("[data-placeholder-en]").forEach(function(element) {

            element.placeholder =
                element.getAttribute("data-placeholder-en");

        });

    }

}
// =============================
// FAQ TOGGLE
// =============================

function toggleFAQ(button) {

    const faqItem = button.parentElement;
    const allItems = document.querySelectorAll(".faq-item");

    // Close other FAQs
    allItems.forEach(function(item) {

        if (item !== faqItem) {

            item.classList.remove("active");

            const icon = item.querySelector(".faq-icon");

            if (icon) {
                icon.innerText = "+";
            }
        }
    });

    // Open / Close clicked FAQ
    faqItem.classList.toggle("active");

    const icon = faqItem.querySelector(".faq-icon");

    if (faqItem.classList.contains("active")) {
        icon.innerText = "−";
    } else {
        icon.innerText = "+";
    }
}