window.addEventListener("load", function(){
    function populate_select_fields() {
        workspace_select = document.getElementById("workspace_select");
        for(var workspace in data) {
            var option = document.createElement("option");
            option.setAttribute('value', workspace);

            var optionText = document.createTextNode(workspace);
            option.appendChild(optionText);

            workspace_select.appendChild(option);
        }
    }
    var data_str = document.getElementById("mydata").textContent
    data_str = data_str.replace(/&quot;/ig,'"');
    data_str = data_str.replaceAll("'", "\"")
    var data = JSON.parse(data_str);
    var table = document.getElementById("tbody")
    var button = document.getElementById("button")
    populate_select_fields()
    button.addEventListener("click", e => {
        while(table.rows.length > 0) {
            table.deleteRow(0);
          }
        var workspace_name  = workspace_select.value
        var workspace_modules = data[workspace_name]['Installed_Modules']
        for(var m in workspace_modules) {
            tr = table.insertRow(0);
            var moduleName = tr.insertCell(-1);
            moduleName.innerHTML = workspace_modules[m]['Name']
            var moduleVersion = tr.insertCell(-1);
            moduleVersion.innerHTML = workspace_modules[m]['Version'];
            var lastUpdatedTime = tr.insertCell(-1);
            lastUpdatedTime.innerHTML = workspace_modules[m]['LastUpdatedTime'];
            var deleteBtn = document.createElement("button")
            deleteBtn.classList.add('btn')
            deleteBtn.classList.add('btn-primary')
            deleteBtn.innerHTML = 'delete';
            deleteBtn.addEventListener("click", function(){
                var index = (document.URL).lastIndexOf('/')
                var base_url = (document.URL).slice(0, index)
                $.ajax({
                    type: 'GET',
                    url: `${base_url}/delete_module`,
                    data : { 'workspace': workspace_name, 'module': workspace_modules[m]['Name']},
                })
            })
            deleteBtnCell = tr.insertCell(-1);
            deleteBtnCell.appendChild(deleteBtn)
        }
     })
})
