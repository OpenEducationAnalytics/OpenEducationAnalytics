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

if (window.location.pathname.includes("partners")) {
    // get filter text
    var filter_text = document.getElementsByName('oeaRegions')[0];
    // console.log(filter_text.value);


    var all_list = document.getElementById('all_list');
    var asia_list = document.getElementById('asia_list');
    var africa_list = document.getElementById('africa_list');
    var north_america_list = document.getElementById('north_america_list');
    var south_america_list = document.getElementById('south_america_list');
    var middle_east_list = document.getElementById('middle_east_list');
    var australia_pacific_list = document.getElementById('australia_pacific_list');
    var europe_list = document.getElementById('europe_list');
    var antartica_list = document.getElementById('antartica_list');

    asia_list.style.display = 'none';
    africa_list.style.display = 'none';
    all_list.style.display = 'flex';
    europe_list.style.display = 'none';
    north_america_list.style.display = 'none';
    south_america_list.style.display = 'none';
    antartica_list.style.display = 'none';
    middle_east_list.style.display = 'none';
    australia_pacific_list.style.display = 'none';


    function filterByRegion() {
        switch (filter_text.value) {
            case 'Asia':
                asia_list.style.display = 'flex';
                africa_list.style.display = 'none';
                all_list.style.display = 'none';
                north_america_list.style.display = 'none';
                south_america_list.style.display = 'none';
                antartica_list.style.display = 'none';
                middle_east_list.style.display = 'none';
                australia_pacific_list.style.display = 'none';
                europe_list.style.display = 'none';
                break;
            case 'Australia / Pacific':
                asia_list.style.display = 'none';
                africa_list.style.display = 'none';
                all_list.style.display = 'none';
                north_america_list.style.display = 'none';
                south_america_list.style.display = 'none';
                antartica_list.style.display = 'none';
                middle_east_list.style.display = 'none';
                australia_pacific_list.style.display = 'flex';
                europe_list.style.display = 'none';
                break;
            case 'Africa':
                asia_list.style.display = 'none';
                africa_list.style.display = 'flex';
                all_list.style.display = 'none';
                north_america_list.style.display = 'none';
                south_america_list.style.display = 'none';
                antartica_list.style.display = 'none';
                middle_east_list.style.display = 'none';
                australia_pacific_list.style.display = 'none';
                europe_list.style.display = 'none';
                break;
            case 'North America / Central America /Caribbean':
                asia_list.style.display = 'none';
                africa_list.style.display = 'none';
                all_list.style.display = 'none';
                north_america_list.style.display = 'flex';
                south_america_list.style.display = 'none';
                antartica_list.style.display = 'none';
                middle_east_list.style.display = 'none';
                australia_pacific_list.style.display = 'none';
                europe_list.style.display = 'none';
                break;
            case 'Europe':
                asia_list.style.display = 'none';
                africa_list.style.display = 'none';
                all_list.style.display = 'none';
                north_america_list.style.display = 'none';
                south_america_list.style.display = 'none';
                antartica_list.style.display = 'none';
                middle_east_list.style.display = 'none';
                australia_pacific_list.style.display = 'none';
                europe_list.style.display = 'flex';
                break;
            case 'Antartica':
                asia_list.style.display = 'none';
                africa_list.style.display = 'none';
                all_list.style.display = 'none';
                north_america_list.style.display = 'none';
                south_america_list.style.display = 'none';
                antartica_list.style.display = 'flex';
                middle_east_list.style.display = 'none';
                australia_pacific_list.style.display = 'none';
                europe_list.style.display = 'none';
                break;
            case 'Middle East':
                asia_list.style.display = 'none';
                africa_list.style.display = 'none';
                all_list.style.display = 'none';
                north_america_list.style.display = 'none';
                south_america_list.style.display = 'none';
                antartica_list.style.display = 'none';
                middle_east_list.style.display = 'flex';
                australia_pacific_list.style.display = 'none';
                europe_list.style.display = 'none';
                break;
            case 'South America':
                asia_list.style.display = 'none';
                africa_list.style.display = 'none';
                all_list.style.display = 'none';
                north_america_list.style.display = 'none';
                south_america_list.style.display = 'flex';
                antartica_list.style.display = 'none';
                middle_east_list.style.display = 'none';
                australia_pacific_list.style.display = 'none';
                europe_list.style.display = 'none';
                break;
            default:
                asia_list.style.display = 'none';
                africa_list.style.display = 'none';
                all_list.style.display = 'flex';
                north_america_list.style.display = 'none';
                south_america_list.style.display = 'none';
                antartica_list.style.display = 'none';
                middle_east_list.style.display = 'none';
                australia_pacific_list.style.display = 'none';
                europe_list.style.display = 'none';
                break;
        }


    }
}
