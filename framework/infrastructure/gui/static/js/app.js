window.addEventListener("load", function(){
    let table = document.getElementById('metadata-table');
    let columnForm = document.querySelectorAll("tbody .column-form");
    let addButton = document.querySelector("#add-form")
    let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
    let formNum = columnForm.length-1

    addButton.addEventListener('click', addForm)

    function addForm(e){
        e.preventDefault()
        let newRow = columnForm[0].cloneNode(true);
        let formRegex = RegExp(`form-(\\d){1}-`,'g')
        formNum++
        newRow.innerHTML = newRow.innerHTML.replace(formRegex, `form-${formNum}-`)
        newRow.id = `form-${formNum}`
        table.children[0].appendChild(newRow);
        totalForms.setAttribute('value', `${formNum+1}`)
    }
})

