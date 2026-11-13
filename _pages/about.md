---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<h1 class="screen-reader-text">Bo Li 李波 — Virtual Cells, Intervention Design & Self-Improving Models</h1>
<span class='anchor' id='about-me'></span>
<div class="hero-block">
  <div class="hero-kicker">{% include icon.html name="dna" %}<span>Scientific AI</span><span class="hero-topics">Virtual-Cell World Models · Closed-Loop Design · Self-Improving Models</span></div>
  <div class="hero-title">From Virtual Cells to Self-Improving Scientific AI</div>
  <p class="hero-copy">I study how AI systems learn from observations, guide scientific interventions, and improve through new evidence. My research spans multimodal cellular modeling, genetic and drug perturbation prediction, measurement-aware evaluation, and intervention design. In parallel, I investigate how pretrained models can acquire, retain, and accumulate new capabilities through weight-space programming. My long-term goal is to develop adaptive scientific AI systems that connect observation, experimentation, and continual learning to support better scientific decisions.</p>
  <div class="hero-affiliations">
    <span>{% include icon.html name="university" %}<a href="https://www.um.edu.mo/"><strong>University of Macau</strong></a> (advisor <a href="https://fic.um.edu.mo/zh-hant/people/bobzhang/">Bob Zhang</a>; co-advisor <a href="https://polytechnic.purdue.edu/profile/song1081">Qianqian Song</a>)</span>
    <span>{% include icon.html name="globe-asia" %}Visiting <a href="https://www.nus.edu.sg/"><strong>National University of Singapore</strong></a> (host <a href="https://www.comp.nus.edu.sg/cs/people/zhangy/">Yang Zhang</a>)</span>
  </div>
</div>
<div class="avail">
  {% include icon.html name="search" %}
  <div class="avail-copy"><strong>Open to postdoctoral and faculty opportunities starting in 2027</strong>, spanning virtual-cell world models, scientific intervention design, and adaptive AI.</div>
  <div class="avail-actions">
    <a class="link-btn" href="{{ site.author.cv | relative_url }}">View CV <span aria-hidden="true">↗</span></a>
    <a class="link-btn ghost" href="mailto:{{ site.author.email }}">Email</a>
  </div>
</div>

## {% include icon.html name="bullhorn" class="h-icon" %}News {#news}

{% include news.html %}

## {% include icon.html name="flask" class="h-icon" %}Research {#research}

<figure class="research-figure">
  <a href="{{ '/images/research_loop.webp' | relative_url }}" title="Open the full-resolution figure">
    <picture>
      <source media="(max-width: 40em)" srcset="{{ '/images/research_loop_vertical.webp' | relative_url }}" width="940" height="4413">
      <img src="{{ '/images/research_loop_1200.webp' | relative_url }}"
           srcset="{{ '/images/research_loop_1200.webp' | relative_url }} 1200w, {{ '/images/research_loop.webp' | relative_url }} 2400w"
           sizes="(max-width: 57.8em) 100vw, 900px"
           alt="Research loop in five parts: (a) cellular state learned from image, omics and spatial measurements; (b) a virtual cell predicts image and expression responses to drug and gene perturbations; (c) evaluation of which predicted differences measurements can resolve; (d) intervention design that ranks candidates by their predicted shift from a source state to a target state and tests the top-K within budget B; experiments on the selected candidates give measured outcomes, and (e) self-improving models (WeightCode, WeightLoop, CellScientist) turn them into lasting model updates that return to the virtual cell." width="1200" height="524" loading="lazy" decoding="async">
    </picture>
  </a>
  <figcaption><strong>From Multimodal Virtual Cells to Self-Improving Models.</strong> (a) Learn cellular state from multimodal measurements. (b) Predict responses to genetic and drug perturbations. (c) Assess which distinctions the measurements can reproducibly resolve. (d) Select interventions within a finite budget. (e) Turn measured outcomes into lasting model updates that feed the next round of prediction.</figcaption>
</figure>

<ol class="research-strands">
  <li class="strand stage-a">
    <div class="strand-label">{% include icon.html name="microscope" %}<span>(a) · CELLULAR STATE</span></div>
    <div class="strand-body">
      <h3>What representations of cellular state can be learned from imaging and omics measurements?</h3>
      <div class="research-work">
      <a href="https://phenoprofiler.org/">PhenoProfiler</a>
      <a href="https://github.com/QSong-github/SpaIM">SpaIM</a>
      <a href="https://doi.org/10.1093/bib/bbae500">HGGEP</a>
      </div>
    </div>
  </li>
  <li class="strand stage-b">
    <div class="strand-label">{% include icon.html name="project-diagram" %}<span>(b) · RESPONSE PREDICTION</span></div>
    <div class="strand-body">
      <h3>Do learned cell-state transitions under intervention generalize across modalities, compounds and contexts?</h3>
      <div class="research-work">
      <a href="https://qsong-github.github.io/MVCBench/">MVCBench</a>
      </div>
    </div>
  </li>
  <li class="strand stage-c">
    <div class="strand-label">{% include icon.html name="search" %}<span>(c) · EVALUATION &amp; RESOLUTION</span></div>
    <div class="strand-body">
      <h3>When does a predicted gain reflect biology that the assay can reproducibly resolve?</h3>
      <div class="research-work">
      <a href="https://boom5426.github.io/PertResolve/">PertResolve</a>
      <a href="https://boom5426.github.io/DrugDis/">DrugDis</a>
      <a href="https://www.biorxiv.org/content/10.64898/2026.09.22.753654v2">MorphoSuff</a>
      </div>
    </div>
  </li>
  <li class="strand stage-d">
    <div class="strand-label">{% include icon.html name="bullseye" %}<span>(d) · EXPERIMENTAL CHOICE</span><span class="research-focus">Current focus</span></div>
    <div class="strand-body">
      <h3>Planning with the model: given a target cellular state and a finite budget, which interventions are worth testing next?</h3>
      <div class="research-work">
      <a href="https://boom5426.github.io/VCDesign-CED/">VCDesign</a>
      </div>
    </div>
  </li>
  <li class="strand stage-e">
    <div class="strand-label">{% include icon.html name="code" %}<span>(e) · SELF-IMPROVING MODELS</span></div>
    <div class="strand-body">
      <h3>Closing the loop: can measured outcomes keep adding capabilities to a model, and do the gains improve its next decisions?</h3>
      <div class="research-work">
      <a href="https://github.com/Gen-Verse/WeightCode">WeightCode</a>
      <a href="https://arxiv.org/abs/2611.07319">WeightLoop</a>
      <a href="https://arxiv.org/abs/2605.07335">CellScientist</a>
      </div>
    </div>
  </li>
</ol>

<div class="research-next" id="vision">
  <span class="research-next-label">Next directions</span>
  <ul>
    <li><strong>Updatable cell world models.</strong> Turn new assay results into persistent, transferable model updates, not retraining.</li>
    <li><strong>Does capability growth pay off?</strong> Test whether each update improves intervention choices on held-out experiments.</li>
    <li><strong>Accumulating capabilities.</strong> Reusable model edits that add perturbation and cell-context skills without forgetting.</li>
  </ul>
</div>

## {% include icon.html name="file-alt" class="h-icon" %}Selected Publications {#publications}

{% include publications.md %}

## {% include icon.html name="code" class="h-icon" %}Software & Resources {#software}

{% include software.md %}

## {% include icon.html name="graduation-cap" class="h-icon" %}Education {#education}
- *2026.06 – 2027.06*: **National University of Singapore**

  *- Visiting Ph.D. Student. Host: [Prof. Yang Zhang](https://www.comp.nus.edu.sg/cs/people/zhangy/)*

- *2024.08 – Present (expected 2027.06)*: **University of Macau**

  *- Ph.D. in Computer Science, Department of Artificial Intelligence, Full Scholarship. Advisor: [Prof. Bob Zhang](https://fic.um.edu.mo/zh-hant/people/bobzhang/); Co-advisor: [Prof. Qianqian Song](https://polytechnic.purdue.edu/profile/song1081), Purdue University*

- *2021.09 – 2024.07*: **Beijing University of Technology**

  *- M.Eng. in Electronic Information. Advisors: [Prof. Yong Zhang](https://znxy.bjut.edu.cn/info/1599/1256.htm), [Prof. Baocai Yin](https://www.bjut.edu.cn/info/1059/1568.htm)*

- *2017.09 – 2021.07*: **Beijing Information Science & Technology University**

  *- B.Eng. in Robotics Engineering. Advisor: [Prof. Hongbo Huang](https://jsjxy.bistu.edu.cn/docs/2025-02/8d1313acd5814afd9f5d15f4b7b9403a.pdf)*

## {% include icon.html name="award" class="h-icon" %}Selected Honors & Awards {#honors}
- *2024*: Ph.D. Full Scholarship, University of Macau
- *2024.07*: Top 100 Graduates, Beijing University of Technology (top 100 of 6,331)
- *2024.07 & 2021.07*: Beijing Outstanding Graduate
- *2023.10*: Xiaomi Scholarship
- *2022.10*: National Scholarship, Ministry of Education of China
- *2022, 2023*: First-Class Academic Scholarship, Beijing University of Technology
- *2021*: First Prize, Science & Technology Innovation Scholarship, Beijing Information Science & Technology University

## {% include icon.html name="lightbulb" class="h-icon" %}Patents {#patents}
Co-inventor of two granted Chinese invention patents on cell localization: [**CN115457547B**](https://patents.google.com/patent/CN115457547B/en) (2026) and [**CN115810046B**](https://patents.google.com/patent/CN115810046B/en) (2026).

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
