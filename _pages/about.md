---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<style>
  .rucred {
    display: inline-block;
    background-color: rgb(174, 11, 42);
    color: white;
    font-size: 0.8em;
    padding: 2px 6px;
    border-radius: 3px;
    margin-left: 8px;
    font-weight: bold;
    vertical-align: middle;
  }
  .badge {
    font-weight: 600;
    margin-bottom: 5px;
  }
</style>

<style>
  .logo-row {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 2rem; 
  }
  .logo-row img {
    height: 60px;
    width: auto;
    /* 
       border-radius: 6px;
       box-shadow: 0 0 6px rgba(0,0,0,.15); */
  }
</style>

<style>
  .site-footer {
    text-align: center;
    font-size: 0.85em;
    color: rgb(128, 128, 128);
    margin: 2rem 0 1rem; 
  }
  .site-footer a {
    color: inherit;
    text-decoration: underline;
  }
</style>

<span class='anchor' id='about-me'></span>

Hi, I'm Bo Li, a Ph.D. student at the [University of Macau](https://www.um.edu.mo/), supervised by [Prof. Bob Zhang](https://www.fst.um.edu.mo/personal/bobzhang/). My research is co-supported by [Prof. Qianqian Song](https://hobi.med.ufl.edu/profile/song-qianqian/) from the [University of Florida](https://www.ufl.edu/), where I collaborate on interdisciplinary projects at the intersection of **AI Virtual Cell**.


My research interests focus on **AI Virtual Cell & Phenotypic Drug Discovery & Cell Painting**. Recently, I am focusing on:  

(1) Modeling virtual cells with generative models; 

(2) Evaluating large foundation models in virtual cell tasks. 


# 🔥 News
- *2025*: &nbsp;🎉🎉 happy everyday



# 📝 Selected Publications
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ArXiv 2025</div><img src='../images/PhenoProfiler.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PhenoProfiler : Advancing Morphology Representations for Image-based Drug Discovery](https://arxiv.org/abs/2502.19568)

[Code](https://github.com/QSong-github/PhenoProfiler), [WebServer](https://phenoprofiler.org/)

**Bo Li**, Bob Zhang, ..., Qianqian Song

Under review in Nature Communications (Major Revision)

**Abstract**: Achieving end-to-end cell image encoding for the first time in Image-based Phenotypic Drug Discovery tasks, with performance comparable to non-end-to-end encoding while reducing inference time by approximately 40 times.



</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ArXiv 2025</div><img src='../images/SpaIM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SpaIM: Single-cell Spatial Transcriptomics Imputation via Style Transfer](https://pmc.ncbi.nlm.nih.gov/articles/PMC11838188/) 

[Code](https://github.com/QSong-github/SpaIM)

**Bo Li**, Ziyang Tang, ..., Qianqian Song

Under review in Nature Communications (Minor Revision)

**Abstract**: Predicting unmeasured gene expression in spatial transcriptomics (ST) using single-cell RNA sequencing (scRNA-seq) and achieving state-of-the-art (SOTA) performance in cross-modal imputation based on style transfer concepts.


</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Briefings in Bioinformatics 2024</div><img src='../images/HGGEP.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Gene Expression Prediction from Histology Images via Hypergraph Neural Networks](https://academic.oup.com/bib/article/25/6/bbae500/7821151) 

[Code](https://github.com/QSong-github/HGGEP)

**Bo Li**, Yong Zhang, ..., Qianqian Song

Briefings in Bioinformatics 2024

**Abstract**: Constructing a hypergraph via Euclidean distance and adjacent position weighting to exploit local correlations in cell images, enabling gene expression prediction for cells in Whole Slide Image (WSI) pathology images.



</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pattern Recognition 2024</div><img src='../images/MHFAN.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Multi-scale hypergraph-based feature alignment network for cell localization](https://www.sciencedirect.com/science/article/pii/S0031320324000116) 

[Code](https://github.com/Boom5426/MHFAN)

**Bo Li**, Yong Zhang, ..., Baocai Yin

Pattern Recognition 2024

**Abstract**: Rethinking the cell localization task from the perspective of feature alignment for the first time and proposing a multi-scale hypergraph module that significantly improves accuracy by adaptively aggregating multi-level features.



</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EAAI 2024</div><img src='../images/EDT.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Exponential distance transform maps for cell localization](https://www.sciencedirect.com/science/article/pii/S0952197624001064?via%3Dihub) 

[Code](https://github.com/Boom5426/MHFAN)

**Bo Li**, Jie Chen, ..., and Hong Bu

Engineering Applications of Artificial Intelligence 2024

**Abstract**: To address the challenge of existing density maps losing cell location information in dense regions, a new exponential distance transform map is proposed to provide accurate cell location information with reasonable gradients.

</div></div>



# 📖 Educations
- *2024.08 – Present*: **University of Macau**
  
  *- Major: Computer Science, Full Scholarship, Supervisors: [Prof. Bob Zhang](https://www.fst.um.edu.mo/personal/bobzhang/), [Prof. Qianqian Song](https://hobi.med.ufl.edu/profile/song-qianqian/)*

- *2021.09 - 2024.07*: **Beijing University of Technology**
  
  *- Master of Electronic Information, Supervisors: [Prof. Yong Zhang](https://sist.bjut.edu.cn/info/1403/2489.htm), [Prof. Baocai Yin](https://sist.bjut.edu.cn/info/1403/2487.htm)*

- *2017.09 - 2021.07*: **Beijing Information Science & Technology University**
  
  *- Bachelor of Robotics Engineering, Supervisors: [Prof. Hongbo Huang](https://jsjxy.bistu.edu.cn/docs/2025-02/8d1313acd5814afd9f5d15f4b7b9403a.pdf)*



# 🎖 Honors and Awards
- *2024.07*: Top 100 Graduates of BJUT (Top 100/6331)
- *2024.07*: Excellent Graduate of Beijing
- *2023.10*: Xiaomi Scholarship
- *2023.10 & 2022.10*:The First Prize Scholarship
- *2022.10*: National Scholarship
- *2021.07*: Excellent Graduate of Beijing
- *2020.12*: The Second Prize of National Mathematics Competition



# 💻 Work Experiences
- *2022.05 – 2023.06*: *Algorithm Intern: Biomedical Image Analysis*, West China Hospital.


# 💼 Services
Reviewer: **Science Advances**, Briefings in Bioinformatics, BMC Biology, Engineering Applications of Artificial Intelligence, IET Image Processing.


# 🌍 Visitor Map

<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=1838a3&w=400&t=tt&d=opzTPaTNgNUrWvD_vjzXkFUMNo05ptM6XPnZfkpH53E&co=ffffff&cmo=af1616&cmn=1fba1f&ct=000000'></script>


<div class="logo-row">
  <img src="../images/Bistu-logo.png"      alt="">
  <img src="../images/Bjut-logo.png"  alt="">
  <img src="../images/UM_logo.png"      alt="">
  <img src="../images/huaxi-logo.png"      alt="">
</div>


<footer class="site-footer">
  <p>&copy; 2025 Bo Li. All rights reserved.</p>
  <p>
    Template adapted from
    <a href="https://github.com/RayeRen/acad-homepage.github.io"
       target="_blank" rel="noopener">Yi Ren</a>.
  </p>
</footer>
