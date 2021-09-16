---
title: Explore and Model Data
subtitle: Build off the work of the Open Education Analytics Community
step: 3
---
**Build off the work of the Open Education Analytics Community**

OEA GitHub includes open-source data <a href="https://github.com/microsoft/OpenEduAnalytics/tree/main/modules" target="_blank">modules</a> for common education datasets. You can connect many of your datasets quickly, combine them with other data, and move to data visualisation and insights quickly.

Use OEA <a href="https://github.com/microsoft/OpenEduAnalytics/tree/main/packages" target="_blank">packages</a> to develop models that solve common education challenges like predicting at risk or vulnerable students.

<div class="container-wrapper-blue py-5 my-4">
  <div class="row justify-content-center text-center">
        <div class="col-sm-6 col-md-5 col-lg-6 col-xl-6 col-10">
            <h5>Some OEA Packages Coming Soon</h5>
        </div>
   </div>
 <div class="row justify-content-center my-4 m d-none">
        {% for item in site.data.oea_packages %}
         <div class="col-11 col-md-5 col-sm-8 col-lg-3 col-xl-3 g-lg-0 g-xl-3 mt-3 mx-3">
             <a href="{{item.url}}" target="_blank">
             <div class="card card-with-hover h-100">
                              <div class="card-body text-center my-auto">
                                  <ul class="list-unstyled m-0">
                                      <li>
                                          <p class="m-0">{{item.name}}</p>
                                      </li>
                                  </ul>
                              </div>
                          </div>
             </a>
         </div>
        {% endfor %}
   </div>
   <div class="row justify-content-center my-4 m">
           {% for item in site.data.oea_packages %}
            <div class="col-11 col-md-5 col-sm-8 col-lg-3 col-xl-3 g-lg-0 g-xl-3 mt-3 mx-3">
                <div class="card h-100">
                                 <div class="card-body text-center my-auto">
                                     <ul class="list-unstyled m-0">
                                         <li>
                                             <p class="m-0">{{item.name}}</p>
                                         </li>
                                     </ul>
                                 </div>
                </div>
            </div>
           {% endfor %}
      </div>
</div>


OEA is developed as a community so that education systems and OEA partners can contribute back to OEA as they develop modules and packages for use cases that may be relevant to other education systems. Learn how to contribute <a href="https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md" target="_blank">here.</a>
