---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<h1 class="screen-reader-text">Bo Li 李波 — AI for Biology: from multimodal virtual cells to experimental decisions</h1>

<span class='anchor' id='about-me'></span>

<div class="hero-block">
  <div class="hero-kicker">{% include icon.html name="dna" %}<span>AI for Biology</span><span class="hero-topics">Multimodal Virtual Cells · Perturbation Modeling · Intervention Design</span></div>
  <div class="hero-title">From Multimodal Virtual Cells to Experimental Decisions</div>
  <p class="hero-copy">I build AI methods that turn multimodal perturbation data into better experimental decisions. My research connects reliable measurement, cellular response modeling, and intervention design to identify which biological effects we can predict and which interventions are worth testing.</p>
  <div class="hero-evidence">
    <span><strong>2 first-author papers</strong> in <em>Nature Communications</em></span>
    <span class="hero-evidence-links"><a href="#phenoprofiler">PhenoProfiler ↗</a><a href="#spaim">SpaIM ↗</a></span>
    {% include scholar-stats.html %}
  </div>
  <div class="hero-affiliations">
    <span>{% include icon.html name="university" %}<a href="https://www.um.edu.mo/"><strong>University of Macau</strong></a> (advisor <a href="https://fic.um.edu.mo/zh-hant/people/bobzhang/">Bob Zhang</a>; co-advisor <a href="https://polytechnic.purdue.edu/profile/song1081">Qianqian Song</a>, <a href="https://www.purdue.edu/">Purdue</a>)</span>
    <span>{% include icon.html name="globe-asia" %}Visiting <a href="https://www.nus.edu.sg/"><strong>NUS</strong></a> (host <a href="https://www.comp.nus.edu.sg/cs/people/zhangy/">Yang Zhang</a>)</span>
  </div>
</div>

<div class="avail">
  {% include icon.html name="search" %}
  <div class="avail-copy"><strong>Seeking Fall 2027 postdoctoral opportunities</strong> in AI for Biology, virtual cells, measurement-aware evaluation, and intervention design.</div>
  <div class="avail-actions">
    <a class="link-btn" href="{{ site.author.cv | relative_url }}">View CV <span aria-hidden="true">↗</span></a>
    <a class="link-btn ghost" href="mailto:{{ site.author.email }}">Email</a>
  </div>
</div>

## {% include icon.html name="bullhorn" class="h-icon" %}News {#news}

{% include news.html %}

## {% include icon.html name="flask" class="h-icon" %}Research {#research}

<div class="research-grid">
  <div class="research-card">
    <div class="research-card-head">
      <span class="research-icon">{% include icon.html name="microscope" %}</span>
      <div class="research-num">01 · MEASURE</div>
    </div>
    <h3>What biological distinctions and predictive capabilities can we reliably evaluate?</h3>
    <p>Determine what biological distinctions experiments can reproducibly resolve and what response structure predictive models actually recover. Separate measurement limits, aggregate performance, and context-specific recovery before interpreting benchmark results.</p>
    <div class="research-work">
      <a href="https://boom5426.github.io/PertResolve/">PertResolve</a>
      <a href="https://boom5426.github.io/DrugDis/">DrugDis</a>
      <a href="https://github.com/limengran98/MorphoSuff">MorphoSuff</a>
    </div>
  </div>

  <div class="research-card">
    <div class="research-card-head">
      <span class="research-icon">{% include icon.html name="project-diagram" %}</span>
      <div class="research-num">02 · MODEL</div>
    </div>
    <h3>What biological information transfers across modalities and contexts?</h3>
    <p>Learn and evaluate cellular representations across transcriptomic, morphological, spatial, and perturbational measurements, with an emphasis on what information remains useful under biological and experimental shifts.</p>
    <div class="research-work">
      <a href="https://qsong-github.github.io/MVCBench/">MVCBench</a>
      <a href="https://phenoprofiler.org/">PhenoProfiler</a>
      <a href="https://github.com/QSong-github/SpaIM">SpaIM</a>
    </div>
  </div>

  <div class="research-card research-card-current">
    <div class="research-card-head">
      <span class="research-icon">{% include icon.html name="bullseye" %}</span>
      <div class="research-num">03 · DESIGN</div>
      <span class="research-focus">Current focus</span>
    </div>
    <h3>Which experiments are worth performing next?</h3>
    <p>Formulate intervention design as a finite-budget decision problem: rank feasible interventions toward a biological objective and evaluate the selected experiments using independently measured outcomes.</p>
    <div class="research-direction">Toward adaptive intervention selection and prospective experimental feedback.</div>
    <div class="research-work">
      <a href="https://boom5426.github.io/VCDesign-CED/">VCDesign</a>
    </div>
  </div>
</div>

<div class="research-next" id="vision">
  <span class="research-next-label">Next direction</span>
  <p>Adaptive intervention design: connect virtual-cell models and scientific agents with independent experimental feedback, so each round of experiments informs the next.</p>
</div>

## {% include icon.html name="file-alt" class="h-icon" %}Selected Publications {#publications}

{% include publications.md %}

## {% include icon.html name="code" class="h-icon" %}Software & Resources {#software}

{% include software.md %}

## {% include icon.html name="graduation-cap" class="h-icon" %}Education {#education}
- *2026.06 – 2027.06*: **National University of Singapore**

  *- Visiting Student. Host: [Prof. Yang Zhang](https://www.comp.nus.edu.sg/cs/people/zhangy/)*

- *2024.08 – Present*: **University of Macau**

  *- Ph.D. in Computer Science, Department of Artificial Intelligence, Full Scholarship. Advisor: [Prof. Bob Zhang](https://fic.um.edu.mo/zh-hant/people/bobzhang/); Co-advisor: [Prof. Qianqian Song](https://polytechnic.purdue.edu/profile/song1081), Purdue University*

- *2021.09 – 2024.07*: **Beijing University of Technology**

  *- M.Eng. in Electronic Information. Advisors: [Prof. Yong Zhang](https://yanzhao.bjut.edu.cn/info/1434/11510.htm), [Prof. Baocai Yin](https://www.bjut.edu.cn/info/1059/1568.htm)*

- *2017.09 – 2021.07*: **Beijing Information Science & Technology University**

  *- B.Eng. in Robotics Engineering. Advisor: [Prof. Hongbo Huang](https://jsjxy.bistu.edu.cn/docs/2025-02/8d1313acd5814afd9f5d15f4b7b9403a.pdf)*

## {% include icon.html name="award" class="h-icon" %}Selected Honors & Awards {#honors}
- *2024*: Ph.D. Scholarship, University of Macau
- *2024.07*: Top 100 Graduates of BJUT (Top 100 / 6331)
- *2024.07 & 2021.07*: Beijing Outstanding Graduate
- *2023.10*: Xiaomi Scholarship
- *2022.10*: National Scholarship
- *2021*: First Prize, Science & Technology Innovation Scholarship, BISTU

## {% include icon.html name="lightbulb" class="h-icon" %}Patents {#patents}
Co-inventor of three Chinese invention patents on cell image density map generation and cell localization: **CN115457546A**, **CN115810046A**, **CN115457547A**.

## {% include icon.html name="hands-helping" class="h-icon" %}Academic Service {#service}

**Journal reviewer**: *Science Advances*, **IEEE TPAMI**, IEEE TIP, IEEE TNNLS, Medical Image Analysis, Bioinformatics, Briefings in Bioinformatics, Pattern Recognition, BMC Biology, Engineering Applications of Artificial Intelligence, and Expert Systems with Applications.

**Collaborations**: Purdue University, Cornell University, University of Florida, National University of Singapore, Sun Yat-sen University, Sichuan University, Beijing University of Technology, and Macao Polytechnic University.

<div class="logo-row">
  <img src="{{ '/images/Bistu-logo.png' | relative_url }}" alt="Beijing Information Science &amp; Technology University" width="121" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/Bjut-logo.png' | relative_url }}" alt="Beijing University of Technology" width="132" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/UM_logo.png' | relative_url }}" alt="University of Macau" width="120" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/huaxi-logo.png' | relative_url }}" alt="West China Hospital, Sichuan University" width="572" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/NUS_logo.jpg' | relative_url }}" alt="National University of Singapore" width="241" height="120" loading="lazy" decoding="async">
</div>

<footer class="site-footer">
  <p>&copy; 2026 Bo Li. All rights reserved.</p>
  <p>
    Template adapted from
    <a href="https://github.com/RayeRen/acad-homepage.github.io"
       target="_blank" rel="noopener">Yi Ren</a>.
  </p>
</footer>
