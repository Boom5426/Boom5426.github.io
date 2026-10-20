{% comment %}Selected publications, shared by the English and Chinese pages. Pass lang="zh" for Chinese labels.{% endcomment %}
{% if include.lang == "zh" %}<p class="pub-legend"><sup>†</sup> 共同第一作者 &nbsp;·&nbsp; <sup>&#42;</sup> 通讯作者</p>{% else %}<p class="pub-legend"><sup>†</sup> Equal contribution &nbsp;·&nbsp; <sup>&#42;</sup> Corresponding author</p>{% endif %}

<h3 class="pub-group">{% if include.lang == "zh" %}已发表{% else %}Published{% endif %}</h3>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge stage-b">(b) Response Prediction · Multimodal Benchmark</div><a class="paper-figure-link" href="{{ '/images/MVCBench.png' | relative_url }}" target="_blank" rel="noopener" title="View full-size figure"><picture><source srcset="{{ '/images/MVCBench.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/MVCBench.png' | relative_url }}" alt="MVCBench: benchmarking drug-molecular and gene representations for drug-induced virtual cell phenotypes" width="800" height="741" loading="lazy" decoding="async"></picture></a></div></div>
<div class='paper-box-text' markdown="1">

[MVCBench: A multimodal benchmark for drug-induced virtual cell phenotypes](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1)

**Bo Li**<sup>†</sup>, Qing Wang<sup>†</sup>, Shihang Wang<sup>†</sup>, Bob Zhang<sup>&#42;</sup>, Yuzhong Peng, Pinxian Zeng, Chengliang Liu, Mengran Li, Ziyang Tang, Xiaojun Yao, Chuxia Deng, Qianqian Song<sup>&#42;</sup>

<span class="venue venue-manuscript">Nature Communications</span> {% if include.lang == "zh" %}**原则性接收**{% else %}**Accepted in Principle**{% endif %} (2026) &nbsp;·&nbsp; [Project](https://qsong-github.github.io/MVCBench/) &nbsp;·&nbsp; [Preprint](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/MVCBench) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/MVCBench) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="mvcbench">BibTeX</button>

{% if include.lang == "zh" %}**简介**：在化合物、细胞系、实验板和数据集四种分布偏移下，评测基于图像与基于表达的扰动预测。{% else %}**TL;DR**: Benchmarks image- and expression-based perturbation prediction under compound, cell-line, plate and dataset shifts.{% endif %}

</div></div>

<div class='paper-box' id='phenoprofiler'><div class='paper-box-image'><div><div class="badge stage-a">(a) Cellular State · Image-based Profiling</div><a class="paper-figure-link" href="{{ '/images/PhenoProfiler.png' | relative_url }}" target="_blank" rel="noopener" title="View full-size figure"><picture><source srcset="{{ '/images/PhenoProfiler.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/PhenoProfiler.png' | relative_url }}" alt="PhenoProfiler: end-to-end phenotypic profiling of high-content cell images" width="800" height="372" loading="lazy" decoding="async"></picture></a></div></div>
<div class='paper-box-text' markdown="1">

[PhenoProfiler: Advancing phenotypic learning for image-based drug discovery](https://www.nature.com/articles/s41467-025-67479-w)

**Bo Li**, Bob Zhang<sup>&#42;</sup>, Chengyang Zhang, Minghao Zhou, Weiliang Huang, Shihang Wang, Qing Wang, Mengran Li, Yong Zhang, Qianqian Song<sup>&#42;</sup>

<span class="venue venue-published">Nature Communications</span> **17**, 793 (2026) &nbsp;·&nbsp; [Paper](https://www.nature.com/articles/s41467-025-67479-w) &nbsp;·&nbsp; [Webserver](https://phenoprofiler.org/) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/PhenoProfiler) &nbsp;·&nbsp; [arXiv](https://arxiv.org/abs/2502.19568) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="phenoprofiler">BibTeX</button>

{% if include.lang == "zh" %}**简介**：直接从高内涵显微图像学习表型特征，不依赖人工设计的特征提取流程，用于化合物表型分析。{% else %}**TL;DR**: Learns phenotypic profiles directly from high-content microscopy images, without hand-crafted feature-extraction pipelines, for compound profiling.{% endif %}

</div></div>

<div class='paper-box' id='spaim'><div class='paper-box-image'><div><div class="badge stage-a">(a) Cellular State · Spatial Omics</div><a class="paper-figure-link" href="{{ '/images/SpaIM.png' | relative_url }}" target="_blank" rel="noopener" title="View full-size figure"><picture><source srcset="{{ '/images/SpaIM.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/SpaIM.png' | relative_url }}" alt="SpaIM: style-transfer imputation for single-cell spatial transcriptomics" width="800" height="680" loading="lazy" decoding="async"></picture></a></div></div>
<div class='paper-box-text' markdown="1">

[SpaIM: Single-cell spatial transcriptomics imputation via style transfer](https://www.nature.com/articles/s41467-025-63185-9)

**Bo Li**<sup>†</sup>, Ziyang Tang<sup>†</sup>, Aishwarya Budhkar, Xiang Liu, Tonglin Zhang, Baijian Yang<sup>&#42;</sup>, Jing Su<sup>&#42;</sup>, Qianqian Song<sup>&#42;</sup>

<span class="venue venue-published">Nature Communications</span> **16**, 7861 (2025) &nbsp;·&nbsp; [Paper](https://www.nature.com/articles/s41467-025-63185-9) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/SpaIM) &nbsp;·&nbsp; [Data](https://zenodo.org/records/14741028) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="spaim">BibTeX</button>

{% if include.lang == "zh" %}**简介**：把空间转录组中未测基因的插补视为从单细胞参考到空间数据的风格迁移。{% else %}**TL;DR**: Treats imputation of unmeasured genes in spatial transcriptomics as style transfer from single-cell references.{% endif %}

</div></div>

<h3 class="pub-group">{% if include.lang == "zh" %}在研工作 · 在审稿件与预印本{% else %}Current work · under review and preprints{% endif %}</h3>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge stage-c">(c) Evaluation &amp; Resolution · Measurement Limits</div><a class="paper-figure-link" href="https://boom5426.github.io/PertResolve/assets/fig1_overview.png" target="_blank" rel="noopener" title="View full-size figure"><img src="{{ '/images/publications/pertresolve.webp' | relative_url }}" alt="PertResolve: measurement resolution for fine-grained perturbation prediction" loading="lazy" decoding="async" width="800" height="710"></a></div></div>
<div class='paper-box-text' markdown="1">

[Measurement resolution constrains fine-grained perturbation prediction](https://boom5426.github.io/PertResolve/)

**Bo Li**<sup>†</sup>, Chengyang Zhang<sup>†</sup>, Mengran Li<sup>†</sup>, Bob Zhang<sup>&#42;</sup>, Lin Wang, Zhenchao Tang, Jun Liu, Chengliang Liu, Chen Wei, Yuhao Yi<sup>&#42;</sup>, Jiancheng Lv, Yang Zhang<sup>&#42;</sup>

<span class="venue venue-manuscript">Under review</span> 2026 &nbsp;·&nbsp; [Project](https://boom5426.github.io/PertResolve/) &nbsp;·&nbsp; [Manuscript](https://github.com/Boom5426/PertResolve/blob/main/manuscript/PertResolve_manuscript.pdf) &nbsp;·&nbsp; [Code](https://github.com/Boom5426/PertResolve) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/PertResolve_Bench) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="pertresolve">BibTeX</button>

{% if include.lang == "zh" %}**简介**：追问实验能够可重复分辨哪些细粒度的扰动差异，从而把模型的局限和测量的局限分开。{% else %}**TL;DR**: Asks which fine-grained perturbation distinctions an assay can reproducibly resolve, separating model limits from measurement limits.{% endif %}

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge stage-c">(c) Evaluation &amp; Resolution · Drug-response Components</div><a class="paper-figure-link" href="https://boom5426.github.io/DrugDis/assets/fig1_overview.png" target="_blank" rel="noopener" title="View full-size figure"><img src="{{ '/images/publications/drugdis.webp' | relative_url }}" alt="DrugDis: disentangling general and context-specific effects in drug-response prediction" loading="lazy" decoding="async" width="800" height="516"></a></div></div>
<div class='paper-box-text' markdown="1">

[DrugDis: Disentangling general and context-specific effects in drug-response prediction](https://boom5426.github.io/DrugDis/)

**Bo Li**<sup>†</sup>, Chengliang Liu<sup>†</sup>, Yuzhong Peng<sup>†</sup>, Bob Zhang<sup>&#42;</sup>, Qing Wang, Pinxian Zeng, Mengran Li, Shenghui Huang, Chuxia Deng<sup>&#42;</sup>, Yang Zhang<sup>&#42;</sup>

<span class="venue venue-manuscript">Under review</span> 2026 &nbsp;·&nbsp; [Project](https://boom5426.github.io/DrugDis/) &nbsp;·&nbsp; [Manuscript](https://github.com/Boom5426/DrugDis/blob/main/manuscript/DrugDis_manuscript.pdf) &nbsp;·&nbsp; [Supplement](https://github.com/Boom5426/DrugDis/blob/main/manuscript/DrugDis_SI.pdf) &nbsp;·&nbsp; [Code](https://github.com/Boom5426/DrugDis) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/DrugDis) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="drugdis">BibTeX</button>

{% if include.lang == "zh" %}**简介**：把药物响应预测拆成药物通用效应、样本通用效应和药物–样本交互效应三部分，说明整体精度可能掩盖情境特异部分的弱恢复。{% else %}**TL;DR**: Decomposes drug-response prediction into general drug, general sample and drug–sample interaction effects, showing that aggregate accuracy can hide weak recovery of the context-specific part.{% endif %}

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge stage-d">(d) Experimental Choice · Intervention Design</div><a class="paper-figure-link" href="https://boom5426.github.io/VCDesign-CED/assets/vcdesign_overview.png" target="_blank" rel="noopener" title="View full-size figure"><img src="{{ '/images/publications/vcdesign.webp' | relative_url }}" alt="VCDesign: finite-budget intervention design for virtual cells" loading="lazy" decoding="async" width="800" height="498"></a></div></div>
<div class='paper-box-text' markdown="1">

[VCDesign: Finite-budget intervention design for virtual cells](https://boom5426.github.io/VCDesign-CED/)

**Bo Li**<sup>†</sup>, Lin Wang<sup>†</sup>, Bob Zhang<sup>&#42;</sup>, Mengran Li, Zhenchao Tang, Chengyang Zhang, Minghao Sun, Chengliang Liu, Zhiyuan Liu, Yang Zhang<sup>&#42;</sup>

<span class="venue venue-manuscript">Under review</span> 2026 &nbsp;·&nbsp; [Project](https://boom5426.github.io/VCDesign-CED/) &nbsp;·&nbsp; [Manuscript](https://github.com/Boom5426/VCDesign-CED/blob/main/paper/VCDesign.pdf) &nbsp;·&nbsp; [Code](https://github.com/Boom5426/VCDesign-CED) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/VCDesign) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="vcdesign">BibTeX</button>

{% if include.lang == "zh" %}**简介**：在固定预算下，按朝向目标状态的预测迁移对候选干预排序；用独立测得的留出结果给所选集合打分，并把证据迁移到尚无测量响应的候选上。{% else %}**TL;DR**: Ranks candidate interventions toward a target state under a fixed budget, scores the selected set against independently measured held-out outcomes, and transfers evidence to candidates with no measured response.{% endif %}

</div></div>

<div class="pub-record">{% if include.lang == "zh" %}完整论文列表见 {% else %}Full publication record on {% endif %}<a href="https://scholar.google.com/citations?hl=en&user=y1myk_IAAAAJ&view_op=list_works&sortby=pubdate"><strong>Google Scholar ↗</strong></a></div>

<script type="application/json" id="bibtex-data">{{ site.data.bibtex | jsonify }}</script>
