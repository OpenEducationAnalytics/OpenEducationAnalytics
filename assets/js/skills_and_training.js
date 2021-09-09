$(document).ready(function () {
    $('[data-toggle="popover"]').popover();
});

if ((window.location.pathname.includes("skills-and-training"))) {
    function setFilter(action) {
        let allElements = document.getElementsByClassName("skill-card")
        let allFilteredElements = document.getElementsByClassName(action)

        //Get all Title labels
        let titles = document.getElementsByClassName('course-title')
        let filteredTextElement = document.getElementById('filtered-text')


        if (action.toLowerCase() === "all") {
            sectionTitles(titles, 'show')
            addCard(allElements)
        } else {
            sectionTitles(titles, 'hide')
            removeCard(allElements)
            addCard(allFilteredElements)
        }
        showSelectedFilterText(filteredTextElement, action)

    }

    function showSelectedFilterText(element, value) {
        let q = ""
        switch (value) {
            case "All":
                q = "All"
                break;
            case "PM":
                q = "Project Manager"
                break;
            case "LF":
                q = "Learners & Family"
                break;
            case "DAE":
                q = "Data Architects Engineer"
                break;
            case "DA":
                q = "Data Analysts"
                break;
            case "DTL":
                q = "Data Team + Learners"
                break;
            case "S":
                q = "Data Scientists"
                break;
            case "ED":
                q = "Educators"
                break;
            case "R":
                q = "Data Researchers"
                break;
        }
        element.innerText = q
    }

    function sectionTitles(elements, action) {
        if (action === 'show') {
            addCard(elements)
        } else if (action === 'hide') {
            removeCard(elements)
        }

    }

    function removeCard(elements) {
        for (let a = 0; a < elements.length; a++) {
            elements[a].classList.remove('d-block')
            elements[a].classList.add('d-none')
        }
    }

    function addCard(elements) {
        for (let b = 0; b < elements.length; b++) {
            elements[b].classList.remove('d-none')
            elements[b].classList.add('d-block')
        }
    }

}


