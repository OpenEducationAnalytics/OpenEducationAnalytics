// ---
// ---

// function filter_by_location(){
//     var location = document.getElementById("location");

//     filter_value = location.value;
//     console.log(filter_value);
//     document.getElementById("partner_list").innerHTML = 
//     '{% for partner in site.data.oea_partners | where_exp: "item", "item.location == ${filter_value}" %}<div class="col-11 col-md-5 col-sm-8 col-lg-3 col-xl-3 g-lg-0 g-xl-3 my-lg-3 my-2 my-xl-4 mx-xl-3 mx-lg-3 mx-1 my-2"><div class="card h-100"><div class="card-body"><ul class="list-unstyled"><li class="mb-3"><img src="{{site.baseurl}}/assets/imgs/partners/{{ partner.logo }}" alt="" height="50" class="img-fluid w-25"/></li><li style="color: #055BFA;"><h6>{{ partner.name }}</h6></li><li><h6 class="mb-0">{{ partner.contact_person }}</h6></li><li><p class="mb-0">{{ partner.email }}</p></li><li class="grey-text"><p class="mb-0">{{ partner.location }}</p></li></ul></div></div></div>{% endfor %}'
    
// }
// ;

var all = document.getElementById('all');
var all_list = document.getElementById('all_list');

var asia = document.getElementById('asia');
var asia_list = document.getElementById('asia_list');

var africa = document.getElementById('africa');
var africa_list = document.getElementById('africa_list');

var america_list = document.getElementById('america_list');
var europe_list = document.getElementById('europe_list');


asia_list.style.display = 'none';
africa_list.style.display = 'none';
all_list.style.display = 'flex';
america_list.style.display = 'none';
europe_list.style.display = 'none';





function addCheckedAttr(id){
    // console.log("flexxxxxxxxxx");
    // document.getElementById('asia').setAttribute('checked', true);
    // asia.checked = true;
    switch (id) {
        case 'asia':
            asia_list.style.display = 'flex';
            africa_list.style.display = 'none';
            all_list.style.display = 'none';
            america_list.style.display = 'none';
            europe_list.style.display = 'none';
            break;
        case 'all':
            asia_list.style.display = 'none';
            africa_list.style.display = 'none';
            all_list.style.display = 'flex';
            america_list.style.display = 'none';
            europe_list.style.display = 'none';
            break;
        case 'africa':
            asia_list.style.display = 'none';
            africa_list.style.display = 'flex';
            all_list.style.display = 'none';
            america_list.style.display = 'none';
            europe_list.style.display = 'none';
            break;
        case 'america':
            asia_list.style.display = 'none';
            africa_list.style.display = 'none';
            all_list.style.display = 'none';
            america_list.style.display = 'flex';
            europe_list.style.display = 'none';
            break;
        case 'europe':
            asia_list.style.display = 'none';
            africa_list.style.display = 'none';
            all_list.style.display = 'none';
            america_list.style.display = 'none';
            europe_list.style.display = 'flex';
            break;
        default:
            break;
    }

    
}