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


        let selectedRole = ""
        switch (value) {
            case "All":
                selectedRole = "All"
                break;
            case "PM":
                selectedRole = "Project Managers"
                break;
            case "DSDA":
                selectedRole = "Data Scientists and Data Analysts"
                break;
            case "DST":
                selectedRole = "Data Strategy Team"
                break;
            case "DAE":
                selectedRole = "Data Architects and Engineers"
                break;
            case "R":
                selectedRole = "Researchers"
                break;
        }
        element.innerText = selectedRole
        let filterTitle = document.getElementById('filter-title');
        filterTitle.innerText = selectedRole
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


    //Sticky Filter
    const nav = document.querySelector('#stickyFilterNav');
    let navTop = nav.offsetTop;

    function fixedNav() {

        // console.log(window.scrollY)
        // console.log(navTop)

        if (window.scrollY >= 720) {
            nav.classList.remove('d-none');
        } else {
            nav.classList.add('d-none');
        }
    }

    window.addEventListener('scroll', fixedNav);


    function scrollToPosition() {
        document.getElementById('filter-text-anchor').scrollIntoView();
    }


}


