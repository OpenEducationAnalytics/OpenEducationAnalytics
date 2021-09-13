if (window.location.pathname.includes("blog/") || window.location.pathname.includes("newsletter/")) {
    document.getElementById('insp').style.fontWeight = "bold";
}

var counter = (function () {
    var privateCounter = 1;

    function changeBy(val) {
        privateCounter += val;
    }

    return {
        increment: function () {
            changeBy(1);
        },
        decrement: function () {
            changeBy(-1);
        },
        value: function () {
            return privateCounter;
        }
    };
})();

//Right Scroll button
document.querySelector('.skip-right').addEventListener('click', function () {
    let cardSize = parseInt(document.querySelector("#customer_feedback_size").value)
    let leftSkipButton = document.querySelector(".skip-left")


    if (cardSize > counter.value()) {
        counter.increment()

        let element = document.querySelector(`.customer_${counter.value()}`)
        let previousElement = document.querySelector(`.customer_${counter.value() - 1}`)

        previousElement.classList.add('card-inactive')
        element.classList.remove('card-inactive')
        element.classList.add('card-active')

        leftSkipButton.classList.add('skip-btn__active')
        if (cardSize === counter.value()) {
            this.classList.remove('skip-btn__active')
        }
    } else {
        this.classList.remove('skip-btn__active')
    }
})


//Left Scroll button
document.querySelector('.skip-left').addEventListener('click', function () {
    let cardSize = parseInt(document.querySelector("#customer_feedback_size").value)
    let rightSkipButton = document.querySelector(".skip-right")


    if (cardSize >= counter.value() && counter.value() > 1) {
        counter.decrement()
        let element = document.querySelector(`.customer_${counter.value()}`)
        let previousElement = document.querySelector(`.customer_${counter.value() + 1}`)

        previousElement.classList.add('card-inactive')
        element.classList.remove('card-inactive')
        element.classList.add('card-active')

        rightSkipButton.classList.add('skip-btn__active')
        if (1 === counter.value()) {
            this.classList.remove('skip-btn__active')
        }

    } else {
        this.classList.remove('skip-btn__active')
    }

})

window.onscroll = function () {
    myFunction()
};

var navbar = document.getElementById("filtered-text");
var sticky = navbar.offsetTop;

function myFunction() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky");
    }
}
