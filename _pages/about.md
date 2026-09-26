---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<h1 class="screen-reader-text">Bo Li 李波 — AI for Biology: measuring, modeling, and designing cellular perturbations</h1>

<span class='anchor' id='about-me'></span>

<div class="hero-block">
  <div class="hero-kicker">AI FOR BIOLOGY</div>
  <div class="hero-title">Measuring, modeling, and designing cellular perturbations</div>
  <p class="hero-meta"><strong>Bo Li (李波)</strong> · Ph.D. Student, University of Macau · Visiting Student, NUS Computing</p>
  <p class="hero-copy">I develop computational methods for understanding and controlling cellular responses. My research asks what biological distinctions experiments can reliably resolve, how multimodal virtual-cell models can predict perturbation responses, and how desired cellular states can be translated into effective interventions.</p>
  <div class="hero-keywords">
    <span>Single-cell perturbations</span>
    <span>Multimodal virtual cells</span>
    <span>Measurement-aware evaluation</span>
    <span>Intervention design</span>
  </div>
</div>

I am a Ph.D. student in the Department of Artificial Intelligence, [University of Macau](https://www.um.edu.mo/), advised by [Prof. Bob Zhang](https://fic.um.edu.mo/zh-hant/people/bobzhang/) and co-advised by [Prof. Qianqian Song](https://polytechnic.purdue.edu/profile/song1081) at [Purdue University](https://www.purdue.edu/). Since June 2026, I have been a visiting student at the [National University of Singapore](https://www.nus.edu.sg/), hosted by [Prof. Yang Zhang](https://www.comp.nus.edu.sg/cs/people/zhangy/).

<div class="link-row">
  <a class="link-btn" href="mailto:Boom985426@gmail.com">Email</a>
  <a class="link-btn ghost" href="https://scholar.google.com/citations?hl=en&user=y1myk_IAAAAJ">Google Scholar</a>
  <a class="link-btn ghost" href="https://github.com/Boom5426">GitHub</a>
  <a class="link-btn ghost" href="https://orcid.org/0000-0003-0608-1502">ORCID</a>
  <a class="link-btn ghost" href="{{ '/files/CV_Bo_Li.pdf' | relative_url }}">CV (PDF)</a>
  <a class="link-btn ghost" href="{{ '/images/WeChat_QR.png' | relative_url }}" title="WeChat ID: BoomLi5426">WeChat</a>
</div>

📫 **Contact**: Boom985426@gmail.com &nbsp;·&nbsp; WeChat: BoomLi5426

<div class="avail">
🔍 <b>I am seeking postdoctoral positions starting in Fall 2027</b>, in academia or industrial research, on AI for Biology, virtual cells, perturbation modeling, and intervention design. I am also always open to collaborations.
</div>

<span class='anchor' id='research'></span>

## 🔬 Research

<div class="research-grid">
  <div class="research-card">
    <div class="research-num">01 · MEASURE</div>
    <h3>What can an experiment actually resolve?</h3>
    <p>Quantify perturbation detectability, identifiability, reproducibility, and the measurement resolution available to downstream predictive models.</p>
    <div class="research-work"><a href="https://boom5426.github.io/PertResolve/">PertResolve</a></div>
  </div>
  <div class="research-arrow">→</div>
  <div class="research-card">
    <div class="research-num">02 · MODEL</div>
    <h3>How do cells respond across perturbations and modalities?</h3>
    <p>Learn and evaluate cellular representations across transcriptomics, morphology, molecular structure, and biological context.</p>
    <div class="research-work"><a href="https://qsong-github.github.io/MVCBench/">MVCBench</a> · <a href="https://phenoprofiler.org/">PhenoProfiler</a> · <a href="https://github.com/QSong-github/SpaIM">SpaIM</a></div>
  </div>
  <div class="research-arrow">→</div>
  <div class="research-card">
    <div class="research-num">03 · DESIGN</div>
    <h3>Which intervention can move a cell toward a desired state?</h3>
    <p>Move beyond forward prediction toward inverse intervention design: given an initial and desired cellular state, identify effective perturbations.</p>
    <div class="research-work"><a href="https://boom5426.github.io/VCDesign-CED/">VCDesign</a></div>
  </div>
</div>

<span class='anchor' id='publications'></span>

## 📝 Selected Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">DESIGN · Intervention Design</div><img src="https://boom5426.github.io/VCDesign-CED/assets/vcdesign_overview.png" alt="VCDesign: candidate-conditioned inverse modeling for cellular intervention design" width="960" loading="lazy" decoding="async"></div></div>
<div class='paper-box-text' markdown="1">

[VCDesign: Candidate-Conditioned Inverse Modeling for Cellular Intervention Design](https://boom5426.github.io/VCDesign-CED/)

**Bo Li**, Lin Wang, Bob Zhang, Mengran Li, Zhenchao Tang, Chengyang Zhang, Minghao Sun, Chengliang Liu, Zhiyuan Liu, Yang Zhang

<span class="venue">Manuscript</span> 2026 &nbsp;·&nbsp; [Project](https://boom5426.github.io/VCDesign-CED/) &nbsp;·&nbsp; [Manuscript](https://github.com/Boom5426/VCDesign-CED/blob/main/paper/VCDesign.pdf) &nbsp;·&nbsp; [Code](https://github.com/Boom5426/VCDesign-CED) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/VCDesign)

**TL;DR**: Formulates cellular intervention design as finite-budget ranking over variable candidate sets and evaluates selected interventions by held-out outcomes, with Candidate Effect Distillation supporting response-unseen candidates.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MEASURE · Perturbation Evaluation</div><img src="https://boom5426.github.io/PertResolve/assets/fig1_overview.png" alt="PertResolve: measurement resolution for fine-grained perturbation prediction" width="920" loading="lazy" decoding="async"></div></div>
<div class='paper-box-text' markdown="1">

[Measurement resolution constrains fine-grained perturbation prediction](https://boom5426.github.io/PertResolve/)

**Bo Li**, Chengyang Zhang, Mengran Li, Bob Zhang, Lin Wang, Zhenchao Tang, Jun Liu, Chengliang Liu, Chen Wei, Yuhao Yi, Jiancheng Lv, Yang Zhang

<span class="venue">Manuscript</span> 2026 &nbsp;·&nbsp; [Project](https://boom5426.github.io/PertResolve/) &nbsp;·&nbsp; [Manuscript](https://github.com/Boom5426/PertResolve/blob/main/manuscript/PertResolve_manuscript.pdf) &nbsp;·&nbsp; [Code](https://github.com/Boom5426/PertResolve) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/PertResolve_Bench)

**TL;DR**: Separates what biological distinctions experiments can reproducibly resolve from what perturbation-prediction models can learn.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MODEL · Virtual Cell Benchmark</div><picture><source srcset="{{ '/images/MVCBench.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/MVCBench.png' | relative_url }}" alt="MVCBench: benchmarking drug-molecular and gene representations for drug-induced virtual cell phenotypes" width="800" height="741" loading="lazy" decoding="async"></picture></div></div>
<div class='paper-box-text' markdown="1">

[MVCBench: A Multimodal Benchmark for Drug-induced Virtual Cell Phenotypes](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1)

**Bo Li**, Qing Wang, Shihang Wang, Bob Zhang, Yuzhong Peng, Pinxian Zeng, Chengliang Liu, Mengran Li, Ziyang Tang, Xiaojun Yao, Chuxia Deng, Qianqian Song

<span class="venue">bioRxiv</span> 2026 &nbsp;·&nbsp; [Project](https://qsong-github.github.io/MVCBench/) &nbsp;·&nbsp; [Preprint](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/MVCBench) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/MVCBench)

**TL;DR**: Benchmarks molecular and gene representations for multimodal prediction of drug-induced cellular phenotypes at scale.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MODEL · Phenotypic Representation</div><picture><source srcset="{{ '/images/PhenoProfiler.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/PhenoProfiler.png' | relative_url }}" alt="PhenoProfiler: end-to-end phenotypic profiling of high-content cell images" width="800" height="372" loading="lazy" decoding="async"></picture></div></div>
<div class='paper-box-text' markdown="1">

[PhenoProfiler: Advancing Phenotypic Learning for Image-based Drug Discovery](https://www.nature.com/articles/s41467-025-67479-w)

**Bo Li**, Bob Zhang, Chengyang Zhang, Minghao Zhou, Weiliang Huang, Shihang Wang, Qing Wang, Mengran Li, Yong Zhang, Qianqian Song

<span class="venue">Nature Communications</span> **17**, 793 (2026) &nbsp;·&nbsp; [Paper](https://www.nature.com/articles/s41467-025-67479-w) &nbsp;·&nbsp; [Webserver](https://phenoprofiler.org/) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/PhenoProfiler) &nbsp;·&nbsp; [arXiv](https://arxiv.org/abs/2502.19568)

**TL;DR**: Learns cellular representations directly from high-content microscopy for image-based phenotypic drug discovery.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MODEL · Cross-modal Biology</div><picture><source srcset="{{ '/images/SpaIM.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/SpaIM.png' | relative_url }}" alt="SpaIM: style-transfer imputation for single-cell spatial transcriptomics" width="800" height="680" loading="lazy" decoding="async"></picture></div></div>
<div class='paper-box-text' markdown="1">

[SpaIM: Single-cell Spatial Transcriptomics Imputation via Style Transfer](https://www.nature.com/articles/s41467-025-63185-9)

**Bo Li**, Ziyang Tang, Aishwarya Budhkar, Xiang Liu, Tonglin Zhang, Baijian Yang, Jing Su, Qianqian Song

<span class="venue">Nature Communications</span> **16**, 7861 (2025) &nbsp;·&nbsp; [Paper](https://www.nature.com/articles/s41467-025-63185-9) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/SpaIM) &nbsp;·&nbsp; [Data](https://zenodo.org/records/14741028)

**TL;DR**: Connects single-cell and spatial transcriptomics through a style-transfer formulation for cross-modal gene-expression inference.

</div></div>

<div class="pub-record">Full publication record on <a href="https://scholar.google.com/citations?hl=en&user=y1myk_IAAAAJ&view_op=list_works&sortby=pubdate"><strong>Google Scholar ↗</strong></a></div>

<span class='anchor' id='news'></span>

## 🔥 News
- *2026.09*: &nbsp;🎯 Released **VCDesign**, a framework for finite-budget cellular intervention design and response-unseen candidate ranking. [Project](https://boom5426.github.io/VCDesign-CED/) · [Code](https://github.com/Boom5426/VCDesign-CED)
- *2026.09*: &nbsp;🧬 Released **PertResolve**, a measurement-resolution framework for fine-grained perturbation prediction. [Project](https://boom5426.github.io/PertResolve/) · [Code](https://github.com/Boom5426/PertResolve)
- *2026.06*: &nbsp;🇸🇬 Started a one-year visit to the **School of Computing, National University of Singapore**, hosted by [Prof. Yang Zhang](https://www.comp.nus.edu.sg/cs/people/zhangy/).
- *2026.05*: &nbsp;📄 **CellScientist** preprint released on [arXiv](https://arxiv.org/abs/2605.07335) (co-author).
- *2026.04*: &nbsp;🧬 **MVCBench** preprint released on [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1).
- *2026.01*: &nbsp;🎉 One paper accepted at **ICLR 2026** (co-author).
- *2025.12*: &nbsp;🎉 **PhenoProfiler** published in [***Nature Communications***](https://www.nature.com/articles/s41467-025-67479-w).



<span class='anchor' id='software'></span>

## 🛠 Software & Resources

Selected research software and community resources.

| Project | What it is | Stars |
| :--- | :--- | :--- |
| [VCDesign](https://github.com/Boom5426/VCDesign-CED) | Finite-budget cellular intervention design with support for response-unseen candidates | [![GitHub stars](https://img.shields.io/github/stars/Boom5426/VCDesign-CED?style=flat&label=%20&color=00369f)](https://github.com/Boom5426/VCDesign-CED) |
| [PertResolve](https://github.com/Boom5426/PertResolve) | Measurement-resolution framework and benchmark for perturbation prediction | [![GitHub stars](https://img.shields.io/github/stars/Boom5426/PertResolve?style=flat&label=%20&color=00369f)](https://github.com/Boom5426/PertResolve) |
| [MVCBench](https://github.com/QSong-github/MVCBench) | Multimodal benchmark for drug-induced virtual cell phenotypes | [![GitHub stars](https://img.shields.io/github/stars/QSong-github/MVCBench?style=flat&label=%20&color=00369f)](https://github.com/QSong-github/MVCBench) |
| [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills) | Agent skills for drafting, revising, auditing, and resubmitting scientific manuscripts | [![GitHub stars](https://img.shields.io/github/stars/Boom5426/Nature-Paper-Skills?style=flat&label=%20&color=00369f)](https://github.com/Boom5426/Nature-Paper-Skills) |
| [Awesome-Virtual-Cell](https://github.com/Boom5426/Awesome-Virtual-Cell) | Curated papers, datasets, benchmarks, and resources for AI virtual cells | [![GitHub stars](https://img.shields.io/github/stars/Boom5426/Awesome-Virtual-Cell?style=flat&label=%20&color=00369f)](https://github.com/Boom5426/Awesome-Virtual-Cell) |
| [PhenoProfiler](https://github.com/QSong-github/PhenoProfiler) | End-to-end phenotypic profiling for image-based drug discovery | [![GitHub stars](https://img.shields.io/github/stars/QSong-github/PhenoProfiler?style=flat&label=%20&color=00369f)](https://github.com/QSong-github/PhenoProfiler) |
| [SpaIM](https://github.com/QSong-github/SpaIM) | Cross-modal imputation for spatial transcriptomics | [![GitHub stars](https://img.shields.io/github/stars/QSong-github/SpaIM?style=flat&label=%20&color=00369f)](https://github.com/QSong-github/SpaIM) |

<span class='anchor' id='education'></span>

## 📖 Education
- *2026.06 – 2027.06*: **National University of Singapore**

  *- Visiting Student, School of Computing. Host: [Prof. Yang Zhang](https://www.comp.nus.edu.sg/cs/people/zhangy/)*

- *2024.08 – Present*: **University of Macau**

  *- Ph.D. in Computer Science, Department of Artificial Intelligence, Full Scholarship. Advisors: [Prof. Bob Zhang](https://fic.um.edu.mo/zh-hant/people/bobzhang/), [Prof. Qianqian Song](https://polytechnic.purdue.edu/profile/song1081)*

- *2021.09 – 2024.07*: **Beijing University of Technology**

  *- M.Eng. in Electronic Information. Advisors: [Prof. Yong Zhang](https://yanzhao.bjut.edu.cn/info/1434/11510.htm), [Prof. Baocai Yin](https://www.bjut.edu.cn/info/1059/1568.htm)*

- *2017.09 – 2021.07*: **Beijing Information Science & Technology University**

  *- B.Eng. in Robotics Engineering. Advisor: [Prof. Hongbo Huang](https://jsjxy.bistu.edu.cn/docs/2025-02/8d1313acd5814afd9f5d15f4b7b9403a.pdf)*

## 🎖 Selected Honors & Awards
- *2024*: Ph.D. Scholarship, University of Macau
- *2024.07*: Top 100 Graduates of BJUT (Top 100 / 6331)
- *2024.07 & 2021.07*: Beijing Outstanding Graduate
- *2023.10*: Xiaomi Scholarship
- *2022.10*: National Scholarship
- *2021*: First Prize, Science & Technology Innovation Scholarship, BISTU

## 📜 Patents
Co-inventor of three Chinese invention patents on cell image density map generation and cell localization: **CN115457546A**, **CN115810046A**, **CN115457547A**.

<span class='anchor' id='service'></span>

## 💼 Academic Service

**Journal reviewer**: *Science Advances*, **IEEE TPAMI**, IEEE TIP, IEEE TNNLS, Medical Image Analysis, Bioinformatics, Briefings in Bioinformatics, BMC Biology, Engineering Applications of Artificial Intelligence, and Expert Systems with Applications.

**Collaborations**: Purdue University, Cornell University, University of Florida, National University of Singapore, Sun Yat-sen University, Sichuan University, Beijing University of Technology, and Macao Polytechnic University.

## 🧭 Research Interests & Technical Stack

**Research**: AI for Biology · virtual cells · single-cell perturbation modeling · multimodal learning · phenotypic drug discovery · spatial omics · intervention design · scientific agents  
**Technical**: Python · PyTorch · CUDA · Linux

<div class="logo-row">
  <img src="{{ '/images/Bistu-logo.png' | relative_url }}" alt="Beijing Information Science &amp; Technology University" width="121" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/Bjut-logo.png' | relative_url }}" alt="Beijing University of Technology" width="132" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/UM_logo.png' | relative_url }}" alt="University of Macau" width="120" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/huaxi-logo.png' | relative_url }}" alt="West China Hospital, Sichuan University" width="572" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/NUS_logo.jpg' | relative_url }}" alt="National University of Singapore" width="241" height="120" loading="lazy" decoding="async">
</div>

<div class="globe-row">
  <script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=0zou2ciiYKWjym8xX1rNTExGh6V2Wkf-pe87Y6eESIE&w=100&h=100"></script>
</div>

<footer class="site-footer">
  <p>&copy; 2026 Bo Li. All rights reserved.</p>
  <p>
    Template adapted from
    <a href="https://github.com/RayeRen/acad-homepage.github.io"
       target="_blank" rel="noopener">Yi Ren</a>.
  </p>
</footer>
