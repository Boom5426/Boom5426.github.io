---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<h1 class="screen-reader-text">Bo Li 李波: multimodal virtual cell modeling and agent systems</h1>

<span class='anchor' id='about-me'></span>

Hi, I'm **Bo Li (李波)**, a Ph.D. student in the Department of Artificial Intelligence, [University of Macau](https://www.um.edu.mo/), advised by [Prof. Bob Zhang](https://fic.um.edu.mo/zh-hant/people/bobzhang/) (University of Macau) and co-advised by [Prof. Qianqian Song](https://polytechnic.purdue.edu/profile/song1081) (Purdue University). Since June 2026 I have been a visiting student at the [School of Computing, National University of Singapore](https://www.comp.nus.edu.sg/), hosted by [Prof. Yang Zhang](https://www.comp.nus.edu.sg/cs/people/zhangy/).

I build **multimodal virtual cell models**: systems that learn how cells respond to drugs across morphology, transcriptomics, and molecular structure, together with the **agent systems** that turn such models into automated scientific discovery. My work has moved along one continuous line, from perceiving cell phenotypes in images, to aligning them with molecular readouts, to benchmarking and orchestrating virtual cell models end to end.

<div class="arc">
  <span class="step">Phenotype perception</span><span class="sep">→</span>
  <span class="step">Cross-modal understanding</span><span class="sep">→</span>
  <span class="step">Multimodal virtual cell modeling</span><span class="sep">→</span>
  <span class="step">Multi-agent scientific systems</span>
</div>

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
🔍 <b>I am seeking postdoctoral positions starting in Fall 2027</b>, in academia or industrial research, on multimodal virtual cell modeling, phenotypic drug discovery, and agentic systems for science. I am also always open to collaborations. Feel free to reach out.
</div>

## 🔥 News
- *2026.06*: &nbsp;🇸🇬 Started a one-year visit to the **School of Computing, National University of Singapore**, hosted by [Prof. Yang Zhang](https://www.comp.nus.edu.sg/cs/people/zhangy/).
- *2026.05*: &nbsp;📄 **CellScientist** preprint released on [arXiv](https://arxiv.org/abs/2605.07335) (co-author).
- *2026.04*: &nbsp;🧬 **MVCBench** preprint released on [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1).
- *2026.01*: &nbsp;🎉 One paper accepted at **ICLR 2026** (co-author).
- *2025.12*: &nbsp;🎉 **PhenoProfiler** published in [***Nature Communications***](https://www.nature.com/articles/s41467-025-67479-w).
- *2025.08*: &nbsp;🎉 **SpaIM** published in [***Nature Communications***](https://www.nature.com/articles/s41467-025-63185-9).

## 📝 Selected Publications

Five representative works below<span id="gs-cit-wrap" hidden>, cited <b><span id="total_cit"></span></b> times in total</span>. The complete list is one click below, and on [Google Scholar](https://scholar.google.com/citations?hl=en&user=y1myk_IAAAAJ&view_op=list_works&sortby=pubdate).

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint 2026</div><picture><source srcset="{{ '/images/MVCBench.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/MVCBench.png' | relative_url }}" alt="MVCBench: benchmarking drug-molecular and gene representations for drug-induced virtual cell phenotypes" width="800" height="741" loading="lazy" decoding="async"></picture></div></div>
<div class='paper-box-text' markdown="1">

[MVCBench: A Multimodal Benchmark for Drug-induced Virtual Cell Phenotypes](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1)

**Bo Li**, Qing Wang, Shihang Wang, Bob Zhang, Yuzhong Peng, Pinxian Zeng, Chengliang Liu, Mengran Li, Ziyang Tang, Xiaojun Yao, Chuxia Deng, Qianqian Song

<span class="venue">bioRxiv</span> 2026 &nbsp;·&nbsp; [Preprint](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1)

**TL;DR**: A systematic benchmark of 24 drug-molecular and gene representation methods across ~1.1M drug-induced profiles. It exposes a modality-dependent asymmetry: advanced molecular representations substantially help morphological phenotype prediction but barely beat classical fingerprints for transcriptomic response, where task-specific gene representations outperform general-purpose foundation models.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Nature Communications 2026</div><picture><source srcset="{{ '/images/PhenoProfiler.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/PhenoProfiler.png' | relative_url }}" alt="PhenoProfiler: end-to-end phenotypic profiling of high-content cell images" width="800" height="372" loading="lazy" decoding="async"></picture></div></div>
<div class='paper-box-text' markdown="1">

[PhenoProfiler: Advancing Phenotypic Learning for Image-based Drug Discovery](https://www.nature.com/articles/s41467-025-67479-w)

**Bo Li**, Bob Zhang, Chengyang Zhang, Minghao Zhou, Weiliang Huang, Shihang Wang, Qing Wang, Mengran Li, Yong Zhang, Qianqian Song

<span class="venue">Nature Communications</span> **17**, 793 (2026) &nbsp;·&nbsp; [Paper](https://www.nature.com/articles/s41467-025-67479-w) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/PhenoProfiler) &nbsp;·&nbsp; [arXiv](https://arxiv.org/abs/2502.19568)

**TL;DR**: The first end-to-end encoder for image-based phenotypic drug discovery. It replaces the conventional multi-step segmentation-and-feature-extraction pipeline with a single model, evaluated on ~400K high-content images and 8.42M single-cell images, improving accuracy and robustness by up to 20% over prior methods while cutting inference time by roughly 40×.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Nature Communications 2025</div><picture><source srcset="{{ '/images/SpaIM.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/SpaIM.png' | relative_url }}" alt="SpaIM: style-transfer imputation for single-cell spatial transcriptomics" width="800" height="680" loading="lazy" decoding="async"></picture></div></div>
<div class='paper-box-text' markdown="1">

[SpaIM: Single-cell Spatial Transcriptomics Imputation via Style Transfer](https://www.nature.com/articles/s41467-025-63185-9)

**Bo Li**, Ziyang Tang, Aishwarya Budhkar, Xiang Liu, Tonglin Zhang, Baijian Yang, Jing Su, Qianqian Song

<span class="venue">Nature Communications</span> **16**, 7861 (2025) &nbsp;·&nbsp; [Paper](https://www.nature.com/articles/s41467-025-63185-9) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/SpaIM)

**TL;DR**: Recasts cross-modal imputation as style transfer, separating data-agnostic gene-expression "content" from platform-specific "style" to predict unmeasured genes in spatial transcriptomics from scRNA-seq. Across 53 datasets spanning sequencing- and imaging-based platforms, it consistently outperforms 12 state-of-the-art methods in gene coverage and expression accuracy.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Briefings in Bioinformatics 2024</div><picture><source srcset="{{ '/images/HGGEP.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/HGGEP.png' | relative_url }}" alt="HGGEP: hypergraph neural network for gene expression prediction from histology" width="800" height="457" loading="lazy" decoding="async"></picture></div></div>
<div class='paper-box-text' markdown="1">

[Gene Expression Prediction from Histology Images via Hypergraph Neural Networks](https://academic.oup.com/bib/article/25/6/bbae500/7821151)

**Bo Li**, Yong Zhang, Qing Wang, Chengyang Zhang, Mengran Li, Guangyu Wang, Qianqian Song

<span class="venue">Briefings in Bioinformatics</span> **25**(6), bbae500 (2024) &nbsp;·&nbsp; [Paper](https://academic.oup.com/bib/article/25/6/bbae500/7821151) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/HGGEP)

**TL;DR**: Builds a hypergraph over image patches using Euclidean distance and adjacent-position weighting, so that higher-order local correlations in whole-slide images can be exploited to predict spot-level gene expression.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pattern Recognition 2024</div><picture><source srcset="{{ '/images/MHFAN.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/MHFAN.png' | relative_url }}" alt="MHFAN: multi-scale hypergraph feature alignment network for cell localization" width="800" height="828" loading="lazy" decoding="async"></picture></div></div>
<div class='paper-box-text' markdown="1">

[Multi-scale Hypergraph-based Feature Alignment Network for Cell Localization](https://www.sciencedirect.com/science/article/pii/S0031320324000116)

**Bo Li**, Yong Zhang, Chengyang Zhang, Xinglin Piao, Yongli Hu, Baocai Yin

<span class="venue">Pattern Recognition</span> **149**, 110260 (2024) &nbsp;·&nbsp; [Paper](https://www.sciencedirect.com/science/article/pii/S0031320324000116) &nbsp;·&nbsp; [Code](https://github.com/Boom5426/MHFAN)

**TL;DR**: Reframes cell localization as a feature-alignment problem and introduces a multi-scale hypergraph module that adaptively aggregates multi-level features, substantially improving localization accuracy in dense tissue.

</div></div>

<details class="pub-list">
<summary>Full publication list</summary>
<p class="pub-note">Every journal paper and preprint, newest first, 26 in total. <b>Bo Li</b> in bold; first-author work therefore opens the author line. Compiled from the ORCID and Crossref records.</p>
<p class="pub-year">2026</p>
<ul class="pub-items">
<li><a href="https://doi.org/10.1109/TNNLS.2026.3676197">Adaptive Prototype-Guided Personalized Propagation for Heterophilic Graphs With Missing Data</a><br><span class="pub-au">Mengran Li, Wenbin Xing, Zelin Zang, <b>Bo Li</b>, Chengyang Zhang, Yong Zhang, et al.</span><br><span class="pub-venue"><i>IEEE Transactions on Neural Networks and Learning Systems</i>, 1-16 (2026)</span></li>
<li><a href="https://arxiv.org/abs/2605.07335">CellScientist: Dual-Space Hierarchical Orchestration for Closed-Loop Refinement of Virtual Cell Models</a><br><span class="pub-au">Mengran Li, <b>Bo Li</b>, Jiaying Wang, Wenbin Xing, Yixuan Dong, Chengyang Zhang, et al.</span><br><span class="pub-venue"><i>arXiv</i> preprint (2026)</span></li>
<li><a href="https://doi.org/10.1109/TCSS.2026.3718932">DiffCTRG: A Diffusion Model for City-Level Traffic Report Generation</a><br><span class="pub-au">Chengyang Zhang, Yong Zhang, Qitan Shao, <b>Bo Li</b>, Yisheng Lv, Xinglin Piao, et al.</span><br><span class="pub-venue"><i>IEEE Transactions on Computational Social Systems</i>, 1-13 (2026)</span></li>
<li><a href="https://doi.org/10.1038/s42003-025-09312-0">Hypergraph-driven spatial multimodal fusion for precise domain delineation and tumor microenvironment decoding</a><br><span class="pub-au">Chengyang Zhang, Xulong Li, <b>Bo Li</b>, Chenxun Deng, Mengran Li, Shiqi Zhang, et al.</span><br><span class="pub-venue"><i>Communications Biology</i>, <b>9</b>, 45 (2026)</span></li>
<li><a href="https://doi.org/10.1016/j.cviu.2026.104878">LocSAM: Modular SAM enhancement for dense object localization in complex scenes</a><br><span class="pub-au">Jingjing Wang, Yong Zhang, <b>Bo Li</b>, Yongli Hu, Bob Zhang, Baocai Yin</span><br><span class="pub-venue"><i>Computer Vision and Image Understanding</i>, <b>271</b>, 104878 (2026)</span></li>
<li><a href="https://doi.org/10.2139/ssrn.6514587">Mitigating Feature Degradation in Deep Forward-Forward Networks</a><br><span class="pub-au">Weijing Zhao, Bob Zhang, Yuqi Wang, <b>Bo Li</b>, Kangdao Liu</span><br><span class="pub-venue"><i>SSRN</i> preprint (2026)</span></li>
<li><a href="https://doi.org/10.1016/j.patcog.2025.112975">MORSE: Molecular representation learning via structured semantic extraction across hierarchical and asymmetric biological modalities</a><br><span class="pub-au">Ronghui Zhang, Mengran Li, Wenbin Xing, <b>Bo Li</b>, Chengyang Zhang, Wenxuan Tu, et al.</span><br><span class="pub-venue"><i>Pattern Recognition</i>, <b>174</b>, 112975 (2026)</span></li>
<li><a href="https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1">MVCBench: A Multimodal Benchmark for Drug-induced Virtual Cell Phenotypes</a><br><span class="pub-au"><b>Bo Li</b>, Qing Wang, Shihang Wang, Bob Zhang, Yuzhong Peng, Pinxian Zeng, et al.</span><br><span class="pub-venue"><i>bioRxiv</i> preprint (2026)</span></li>
<li><a href="https://doi.org/10.1038/s41467-025-67479-w">PhenoProfiler: advancing phenotypic learning for image-based drug discovery</a><br><span class="pub-au"><b>Bo Li</b>, Bob Zhang, Chengyang Zhang, Minghao Zhou, Weiliang Huang, Shihang Wang, et al.</span><br><span class="pub-venue"><i>Nature Communications</i>, <b>17</b>, 793 (2026)</span></li>
<li><a href="https://doi.org/10.1093/bioinformatics/btag598">PSSD: Progressive Spatial-Semantic Decoupling for Flow-Based Gene Expression Prediction from Histology Images</a><br><span class="pub-au">Chengyang Zhang, <b>Bo Li</b>, Bob Zhang, Yuansong Zeng, Yuhao Yi, Jiancheng Lv</span><br><span class="pub-venue"><i>Bioinformatics</i>, btag598 (2026)</span></li>
</ul>
<p class="pub-year">2025</p>
<ul class="pub-items">
<li><a href="https://doi.org/10.1109/TITS.2024.3510402">ChatTraffic: Text-to-Traffic Generation via Diffusion Model</a><br><span class="pub-au">Chengyang Zhang, Yong Zhang, Qitan Shao, <b>Bo Li</b>, Yisheng Lv, Xinglin Piao, et al.</span><br><span class="pub-venue"><i>IEEE Transactions on Intelligent Transportation Systems</i>, <b>26</b>, 2656-2668 (2025)</span></li>
<li><a href="https://doi.org/10.1038/s41467-025-63185-9">SpaIM: single-cell spatial transcriptomics imputation via style transfer</a><br><span class="pub-au"><b>Bo Li</b>, Ziyang Tang, Aishwarya Budhkar, Xiang Liu, Tonglin Zhang, Baijian Yang, et al.</span><br><span class="pub-venue"><i>Nature Communications</i>, <b>16</b>, 7861 (2025)</span></li>
<li><a href="https://doi.org/10.1109/TCSS.2024.3509399">TDG-Mamba: Advanced Spatiotemporal Embedding for Temporal Dynamic Graph Learning via Bidirectional Information Propagation</a><br><span class="pub-au">Mengran Li, Junzhou Chen, <b>Bo Li</b>, Yong Zhang, Ronghui Zhang, Siyuan Gong, et al.</span><br><span class="pub-venue"><i>IEEE Transactions on Computational Social Systems</i>, <b>12</b>, 2014-2029 (2025)</span></li>
</ul>
<p class="pub-year">2024</p>
<ul class="pub-items">
<li><a href="https://doi.org/10.1093/bib/bbae403">AntiFormer: graph enhanced large language model for binding affinity prediction</a><br><span class="pub-au">Qing Wang, Yuzhou Feng, Yanfei Wang, <b>Bo Li</b>, Jianguo Wen, Xiaobo Zhou, et al.</span><br><span class="pub-venue"><i>Briefings in Bioinformatics</i>, <b>25</b>, bbae403 (2024)</span></li>
<li><a href="https://doi.org/10.1109/TITS.2024.3440650">BjTT: A Large-Scale Multimodal Dataset for Traffic Prediction</a><br><span class="pub-au">Chengyang Zhang, Yong Zhang, Qitan Shao, Jiangtao Feng, <b>Bo Li</b>, Yisheng Lv, et al.</span><br><span class="pub-venue"><i>IEEE Transactions on Intelligent Transportation Systems</i>, <b>25</b>, 18992-19003 (2024)</span></li>
<li><a href="https://doi.org/10.1145/3638774">CrowdGraph: Weakly supervised Crowd Counting via Pure Graph Neural Network</a><br><span class="pub-au">Chengyang Zhang, Yong Zhang, <b>Bo Li</b>, Xinglin Piao, Baocai Yin</span><br><span class="pub-venue"><i>ACM Transactions on Multimedia Computing, Communications, and Applications</i>, <b>20</b>, 1-23 (2024)</span></li>
<li><a href="https://doi.org/10.36227/techrxiv.172710195.56931827/v1">Deep learning in phenotypic drug discovery: a survey</a><br><span class="pub-au"><b>Bo Li</b>, Weiliang Huang, Weijing Zhao, Caijie Zhao, Jingtao Wang, Yuqi Wang</span><br><span class="pub-venue"><i>TechRxiv</i> preprint (2024)</span></li>
<li><a href="https://doi.org/10.1109/JBHI.2023.3329542">Difference-Deformable Convolution With Pseudo Scale Instance Map for Cell Localization</a><br><span class="pub-au">Chengyang Zhang, Jie Chen, <b>Bo Li</b>, Min Feng, Yongquan Yang, Qikui Zhu, et al.</span><br><span class="pub-venue"><i>IEEE Journal of Biomedical and Health Informatics</i>, <b>28</b>, 355-366 (2024)</span></li>
<li><a href="https://doi.org/10.1016/j.engappai.2024.107948">Exponential distance transform maps for cell localization</a><br><span class="pub-au"><b>Bo Li</b>, Jie Chen, Hang Yi, Min Feng, Yongquan Yang, Qikui Zhu, et al.</span><br><span class="pub-venue"><i>Engineering Applications of Artificial Intelligence</i>, <b>132</b>, 107948 (2024)</span></li>
<li><a href="https://doi.org/10.1093/bib/bbae500">Gene expression prediction from histology images via hypergraph neural networks</a><br><span class="pub-au"><b>Bo Li</b>, Yong Zhang, Qing Wang, Chengyang Zhang, Mengran Li, Guangyu Wang, et al.</span><br><span class="pub-venue"><i>Briefings in Bioinformatics</i>, <b>25</b>, bbae500 (2024)</span></li>
<li><a href="https://doi.org/10.1016/j.engappai.2023.107634">Lite-UNet: A lightweight and efficient network for cell localization</a><br><span class="pub-au"><b>Bo Li</b>, Yong Zhang, Yunhan Ren, Chengyang Zhang, Baocai Yin</span><br><span class="pub-venue"><i>Engineering Applications of Artificial Intelligence</i>, <b>129</b>, 107634 (2024)</span></li>
<li><a href="https://doi.org/10.1016/j.patcog.2024.110260">Multi-scale hypergraph-based feature alignment network for cell localization</a><br><span class="pub-au"><b>Bo Li</b>, Yong Zhang, Chengyang Zhang, Xinglin Piao, Yongli Hu, Baocai Yin</span><br><span class="pub-venue"><i>Pattern Recognition</i>, <b>149</b>, 110260 (2024)</span></li>
</ul>
<p class="pub-year">2023</p>
<ul class="pub-items">
<li><a href="https://doi.org/10.1007/s00371-022-02485-3">CCST: crowd counting with swin transformer</a><br><span class="pub-au"><b>Bo Li</b>, Yong Zhang, Haihui Xu, Baocai Yin</span><br><span class="pub-venue"><i>The Visual Computer</i>, <b>39</b>, 2671-2682 (2023)</span></li>
<li><a href="https://doi.org/10.1145/3594670">Hypergraph Association Weakly Supervised Crowd Counting</a><br><span class="pub-au"><b>Bo Li</b>, Yong Zhang, Chengyang Zhang, Xinglin Piao, Baocai Yin</span><br><span class="pub-venue"><i>ACM Transactions on Multimedia Computing, Communications, and Applications</i>, <b>19</b>, 1-20 (2023)</span></li>
</ul>
<p class="pub-year">2022</p>
<ul class="pub-items">
<li><a href="https://doi.org/10.1155/2022/5614974">Suitability Evaluation of Crop Variety via Graph Neural Network</a><br><span class="pub-au">Qiusi Zhang, <b>Bo Li</b>, Yong Zhang, Shufeng Wang</span><br><span class="pub-venue"><i>Computational Intelligence and Neuroscience</i>, <b>2022</b>, 1-10 (2022)</span></li>
</ul>
<p class="pub-year">2021</p>
<ul class="pub-items">
<li><a href="https://doi.org/10.1007/s10044-021-00959-z">Approaches on crowd counting and density estimation: a review</a><br><span class="pub-au"><b>Bo Li</b>, Hongbo Huang, Ang Zhang, Peiwen Liu, Cheng Liu</span><br><span class="pub-venue"><i>Pattern Analysis and Applications</i>, <b>24</b>, 853-874 (2021)</span></li>
</ul>
</details>

## 🛠 Open Source

Research code and community resources, **700+ GitHub stars** in total.

| Project | What it is | Stars |
| :--- | :--- | :--- |
| [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills) | Agent skills for drafting, revising, auditing, and resubmitting Nature-style manuscripts | [![GitHub stars](https://img.shields.io/github/stars/Boom5426/Nature-Paper-Skills?style=flat&label=%20&color=00369f)](https://github.com/Boom5426/Nature-Paper-Skills) |
| [Awesome-Virtual-Cell](https://github.com/Boom5426/Awesome-Virtual-Cell) | Papers, datasets, benchmarks, and community resources for AI virtual cells | [![GitHub stars](https://img.shields.io/github/stars/Boom5426/Awesome-Virtual-Cell?style=flat&label=%20&color=00369f)](https://github.com/Boom5426/Awesome-Virtual-Cell) |
| [Awesome-Phenotypic-Drug-Discovery](https://github.com/Boom5426/Awesome-Phenotypic-Drug-Discovery) | Curated resources for phenotypic drug discovery | [![GitHub stars](https://img.shields.io/github/stars/Boom5426/Awesome-Phenotypic-Drug-Discovery?style=flat&label=%20&color=00369f)](https://github.com/Boom5426/Awesome-Phenotypic-Drug-Discovery) |
| [PhenoProfiler](https://github.com/QSong-github/PhenoProfiler) | End-to-end phenotypic profiling for image-based drug discovery | [![GitHub stars](https://img.shields.io/github/stars/QSong-github/PhenoProfiler?style=flat&label=%20&color=00369f)](https://github.com/QSong-github/PhenoProfiler) |
| [SpaIM](https://github.com/QSong-github/SpaIM) | Style-transfer imputation for spatial transcriptomics | [![GitHub stars](https://img.shields.io/github/stars/QSong-github/SpaIM?style=flat&label=%20&color=00369f)](https://github.com/QSong-github/SpaIM) |
| [MHFAN](https://github.com/Boom5426/MHFAN) | Multi-scale hypergraph feature alignment for cell localization | [![GitHub stars](https://img.shields.io/github/stars/Boom5426/MHFAN?style=flat&label=%20&color=00369f)](https://github.com/Boom5426/MHFAN) |
| [UM_CS_QE](https://github.com/Boom5426/UM_CS_QE) | Study resources for the University of Macau CIS Ph.D. qualifying exam | [![GitHub stars](https://img.shields.io/github/stars/Boom5426/UM_CS_QE?style=flat&label=%20&color=00369f)](https://github.com/Boom5426/UM_CS_QE) |

## 📖 Education
- *2026.06 – 2027.06*: **National University of Singapore**

  *- Visiting Student, School of Computing. Host: [Prof. Yang Zhang](https://www.comp.nus.edu.sg/cs/people/zhangy/)*

- *2024.08 – Present*: **University of Macau**

  *- Ph.D. in Computer Science, Department of Artificial Intelligence, Full Scholarship. Advisors: [Prof. Bob Zhang](https://fic.um.edu.mo/zh-hant/people/bobzhang/), [Prof. Qianqian Song](https://polytechnic.purdue.edu/profile/song1081)*

- *2021.09 – 2024.07*: **Beijing University of Technology**

  *- M.Eng. in Electronic Information. Advisors: [Prof. Yong Zhang](https://yanzhao.bjut.edu.cn/info/1434/11510.htm), [Prof. Baocai Yin](https://www.bjut.edu.cn/info/1059/1568.htm)*

- *2017.09 – 2021.07*: **Beijing Information Science & Technology University**

  *- B.Eng. in Robotics Engineering. Advisor: [Prof. Hongbo Huang](https://jsjxy.bistu.edu.cn/docs/2025-02/8d1313acd5814afd9f5d15f4b7b9403a.pdf)*

## 🎖 Honors and Awards
- *2024*: Ph.D. Scholarship, University of Macau
- *2024.07*: Top 100 Graduates of BJUT (Top 100 / 6331)
- *2024.07 & 2021.07*: Beijing Outstanding Graduate
- *2023.10*: Xiaomi Scholarship
- *2023.10 & 2022.10*: First-Class Academic Scholarship, BJUT
- *2022.10*: National Scholarship
- *2021*: First Prize, Science & Technology Innovation Scholarship, BISTU
- *2020.12*: Second Prize, National Mathematics Competition

## 📜 Patents
Co-inventor of three Chinese invention patents on cell image density map generation and cell localization: **CN115457546A**, **CN115810046A**, **CN115457547A**.

## 💼 Academic Service

**Journal reviewer**: *Science Advances*, IEEE TIP, IEEE TNNLS, IEEE TCE, IEEE TSMCS, Medical Image Analysis, Bioinformatics, Briefings in Bioinformatics, BMC Biology, Engineering Applications of Artificial Intelligence, Expert Systems with Applications, Knowledge-Based Systems, CAAI Transactions on Intelligence Technology, and Artificial Intelligence Review.

**Collaborations**: Purdue University, Cornell University, University of Florida, National University of Singapore, Sun Yat-sen University, Sichuan University, Beijing University of Technology, and Macao Polytechnic University.

## 🧰 Skills
- **Research**: multimodal representation learning, medical image analysis, spatial omics modeling, phenotypic drug discovery, virtual cell modeling and benchmarking.
- **Agent systems**: multi-agent design, skill-based architectures, memory-augmented systems, reusable workflow design for scientific applications.
- **Engineering**: Python, PyTorch, CUDA, Linux.

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
