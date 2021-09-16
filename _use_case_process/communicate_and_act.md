---
title: Communicate and Act
subtitle: Use OEA Templates, Modules and Packages to quickly ingest and explore data and develop models that solve common education challenges like predicting at risk or vulnerable students
step: 4
---
Communicate analytics using Power BI data visualizations and reports; set up automated actions based on analytics using low code Power Apps, or trigger data-driven actions using Dynamics 365, Office 365, or Microsoft Teams. 

<div class="container-wrapper py-5 d-none">
   <div class="row justify-content-center text-center">
        <div class="col-sm-6 col-md-5 col-lg-6 col-xl-6 col-10">
            <h5>Some OEA Modules</h5>
        </div>
   </div>
   <div class="row justify-content-center my-4">
        {% for item in site.data.oea_modules %}
          <div class="col-md-3 text-center mt-5">
            <img src="{{ site.baseurl }}/assets/imgs/{{item.url}}" class="img-fluid {{item.style}}" />
          </div>
        {% endfor %}
   </div>
</div>

