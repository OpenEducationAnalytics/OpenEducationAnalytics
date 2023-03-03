function populate_asset_table(table, type) {
    table.style.visibility = "visible"
    while(table.rows.length > 1) {
        table.deleteRow(-1);
      }
    assets = get_json_data(type)
    for(var idx in assets) {
        tr = table.insertRow(-1);
        var asset_name = tr.insertCell(-1);
        asset_name.innerHTML = assets[idx]['Name']
        var version = tr.insertCell(-1);
        version.innerHTML = assets[idx]['Version']
        var lastUpdatedTime = tr.insertCell(-1);
        lastUpdatedTime.innerHTML = assets[idx]['LastUpdatedTime']
        var deleteBtn = document.createElement("button")
        deleteBtn.classList.add('btn')
        deleteBtn.classList.add('btn-primary')
        deleteBtn.innerHTML = 'delete';
        deleteBtnCell = tr.insertCell(-1);
        deleteBtnCell.appendChild(deleteBtn)
    }
}

function get_json_data(name) {
    var data_str = document.getElementById(name).textContent
    data_str = data_str.replace(/&quot;/ig,'"');
    data_str = data_str.replaceAll("'", "\"")
    var data = JSON.parse(data_str);
    return data
}

window.addEventListener("load", function(){
    var modulesBtn = document.getElementById("modulesBtn")
    var packagesBtn = document.getElementById("packagesBtn")
    var schemasBtn = document.getElementById("schemasBtn")
    var tbody = document.getElementById("installedAssetsTableBody")
    var table = document.getElementById("installedAssetsTable")
    table.style.visibility = "hidden"
    modulesBtn.addEventListener("click", e => {
        populate_asset_table(tbody, "modules")
    })
    packagesBtn.addEventListener("click", e => {
        populate_asset_table(tbody, "packages")
    })
    schemasBtn.addEventListener("click", e => {
        populate_asset_table(tbody, "schemas")
    })
})