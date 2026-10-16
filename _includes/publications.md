{% comment %}Selected publications, shared by the English and Chinese pages. Pass lang="zh" for Chinese labels.{% endcomment %}
{% if include.lang == "zh" %}<p class="pub-legend"><sup>†</sup> 共同第一作者 &nbsp;·&nbsp; <sup>&#42;</sup> 通讯作者</p>{% else %}<p class="pub-legend"><sup>†</sup> Equal contribution &nbsp;·&nbsp; <sup>&#42;</sup> Corresponding author</p>{% endif %}

<h3 class="pub-group">{% if include.lang == "zh" %}已发表{% else %}Published{% endif %}</h3>

<div class='paper-box' id='phenoprofiler'><div class='paper-box-image'><div><div class="badge stage-a">(a) Cellular State · Image-based Profiling</div><a class="paper-figure-link" href="{{ '/images/PhenoProfiler.png' | relative_url }}" target="_blank" rel="noopener" title="View full-size figure"><picture><source srcset="{{ '/images/PhenoProfiler.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/PhenoProfiler.png' | relative_url }}" alt="PhenoProfiler: end-to-end phenotypic profiling of high-content cell images" width="800" height="372" loading="lazy" decoding="async"></picture></a></div></div>
<div class='paper-box-text' markdown="1">

[PhenoProfiler: Advancing Phenotypic Learning for Image-based Drug Discovery](https://www.nature.com/articles/s41467-025-67479-w)

**Bo Li**, Bob Zhang<sup>&#42;</sup>, Chengyang Zhang, Minghao Zhou, Weiliang Huang, Shihang Wang, Qing Wang, Mengran Li, Yong Zhang, Qianqian Song<sup>&#42;</sup>

<span class="venue venue-published">Nature Communications</span> **17**, 793 (2026) &nbsp;·&nbsp; [Paper](https://www.nature.com/articles/s41467-025-67479-w) &nbsp;·&nbsp; [Webserver](https://phenoprofiler.org/) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/PhenoProfiler) &nbsp;·&nbsp; [arXiv](https://arxiv.org/abs/2502.19568) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="phenoprofiler">BibTeX</button>

{% if include.lang == "zh" %}**简介**：直接从高内涵显微图像学习细胞表征，用于表型分析和药物发现，把图像特征与不同细胞扰动之间的生物学差异联系起来。{% else %}**TL;DR**: Learns cellular representations directly from high-content microscopy for phenotypic profiling and drug discovery, connecting image-derived features to biological differences between diverse cellular perturbations.{% endif %}

</div></div>

<div class='paper-box' id='spaim'><div class='paper-box-image'><div><div class="badge stage-a">(a) Cellular State · Spatial Omics</div><a class="paper-figure-link" href="{{ '/images/SpaIM.png' | relative_url }}" target="_blank" rel="noopener" title="View full-size figure"><picture><source srcset="{{ '/images/SpaIM.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/SpaIM.png' | relative_url }}" alt="SpaIM: style-transfer imputation for single-cell spatial transcriptomics" width="800" height="680" loading="lazy" decoding="async"></picture></a></div></div>
<div class='paper-box-text' markdown="1">

[SpaIM: Single-cell Spatial Transcriptomics Imputation via Style Transfer](https://www.nature.com/articles/s41467-025-63185-9)

**Bo Li**<sup>†</sup>, Ziyang Tang<sup>†</sup>, Aishwarya Budhkar, Xiang Liu, Tonglin Zhang, Baijian Yang<sup>&#42;</sup>, Jing Su<sup>&#42;</sup>, Qianqian Song<sup>&#42;</sup>

<span class="venue venue-published">Nature Communications</span> **16**, 7861 (2025) &nbsp;·&nbsp; [Paper](https://www.nature.com/articles/s41467-025-63185-9) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/SpaIM) &nbsp;·&nbsp; [Data](https://zenodo.org/records/14741028) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="spaim">BibTeX</button>

{% if include.lang == "zh" %}**简介**：通过风格迁移整合单细胞与空间转录组数据，预测空间基因表达，把刻画细胞身份和组织结构的两类互补测量联系起来。{% else %}**TL;DR**: Integrates single-cell and spatial transcriptomics through style-transfer imputation, predicting spatial gene-expression patterns to connect complementary measurements of cellular identity and tissue organization.{% endif %}

</div></div>

<h3 class="pub-group">{% if include.lang == "zh" %}在研工作 · 在审稿件与预印本{% else %}Current work · under review and preprints{% endif %}</h3>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge stage-d">(d) Experimental Choice · Intervention Design</div><a class="paper-figure-link" href="https://boom5426.github.io/VCDesign-CED/assets/vcdesign_overview.png" target="_blank" rel="noopener" title="View full-size figure"><img src="{{ '/images/publications/vcdesign.webp' | relative_url }}" alt="VCDesign: finite-budget intervention design for virtual cells" loading="lazy" decoding="async" width="800" height="498"></a></div></div>
<div class='paper-box-text' markdown="1">

[VCDesign: Finite-Budget Intervention Design for Virtual Cells](https://boom5426.github.io/VCDesign-CED/)

**Bo Li**<sup>†</sup>, Lin Wang<sup>†</sup>, Bob Zhang<sup>&#42;</sup>, Mengran Li, Zhenchao Tang, Chengyang Zhang, Minghao Sun, Chengliang Liu, Zhiyuan Liu, Yang Zhang<sup>&#42;</sup>

<span class="venue venue-manuscript">Under review</span> 2026 &nbsp;·&nbsp; [Project](https://boom5426.github.io/VCDesign-CED/) &nbsp;·&nbsp; [Manuscript](https://github.com/Boom5426/VCDesign-CED/blob/main/paper/VCDesign.pdf) &nbsp;·&nbsp; [Code](https://github.com/Boom5426/VCDesign-CED) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/VCDesign) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="vcdesign">BibTeX</button>

{% if include.lang == "zh" %}**简介**：在有限的实验预算下对可行干预进行排序，利用历史扰动数据和生物学知识，为尚未测得响应的候选干预确定优先级，并用独立测得的实验结果评估所选干预。{% else %}**TL;DR**: Ranks feasible interventions under a limited experimental budget, using historical perturbation data and biological knowledge to prioritize response-unseen candidates. Evaluates the selected experiments against independently measured outcomes.{% endif %}

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge stage-c">(c) Evaluation &amp; Resolution · Measurement Limits</div><a class="paper-figure-link" href="https://boom5426.github.io/PertResolve/assets/fig1_overview.png" target="_blank" rel="noopener" title="View full-size figure"><img src="{{ '/images/publications/pertresolve.webp' | relative_url }}" alt="PertResolve: measurement resolution for fine-grained perturbation prediction" loading="lazy" decoding="async" width="800" height="710"></a></div></div>
<div class='paper-box-text' markdown="1">

[Measurement resolution constrains fine-grained perturbation prediction](https://boom5426.github.io/PertResolve/)

**Bo Li**<sup>†</sup>, Chengyang Zhang<sup>†</sup>, Mengran Li<sup>†</sup>, Bob Zhang<sup>&#42;</sup>, Lin Wang, Zhenchao Tang, Jun Liu, Chengliang Liu, Chen Wei, Yuhao Yi<sup>&#42;</sup>, Jiancheng Lv, Yang Zhang<sup>&#42;</sup>

<span class="venue venue-manuscript">Under review</span> 2026 &nbsp;·&nbsp; [Project](https://boom5426.github.io/PertResolve/) &nbsp;·&nbsp; [Manuscript](https://github.com/Boom5426/PertResolve/blob/main/manuscript/PertResolve_manuscript.pdf) &nbsp;·&nbsp; [Code](https://github.com/Boom5426/PertResolve) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/PertResolve_Bench) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="pertresolve">BibTeX</button>

{% if include.lang == "zh" %}**简介**：把测量本身的局限和模型的局限分开：先检验实验能否可重复地区分细粒度的扰动效应，再检验预测模型能否恢复这些差异，而不只是学到共有的响应模式。{% else %}**TL;DR**: Separates measurement limits from modeling limits by testing whether experiments can reproducibly distinguish fine-grained perturbation effects, and whether predictive models recover those distinctions rather than only shared response patterns.{% endif %}

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge stage-c">(c) Evaluation &amp; Resolution · Drug-response Components</div><a class="paper-figure-link" href="https://boom5426.github.io/DrugDis/assets/fig1_overview.png" target="_blank" rel="noopener" title="View full-size figure"><img src="{{ '/images/publications/drugdis.webp' | relative_url }}" alt="DrugDis: disentangling general and context-specific effects in drug-response prediction" loading="lazy" decoding="async" width="800" height="516"></a></div></div>
<div class='paper-box-text' markdown="1">

[DrugDis: Disentangling general and context-specific effects in drug-response prediction](https://boom5426.github.io/DrugDis/)

**Bo Li**<sup>†</sup>, Chengliang Liu<sup>†</sup>, Yuzhong Peng<sup>†</sup>, Bob Zhang<sup>&#42;</sup>, Qing Wang, Pinxian Zeng, Mengran Li, Shenghui Huang, Chuxia Deng<sup>&#42;</sup>, Yang Zhang<sup>&#42;</sup>

<span class="venue venue-manuscript">Under review</span> 2026 &nbsp;·&nbsp; [Project](https://boom5426.github.io/DrugDis/) &nbsp;·&nbsp; [Manuscript](https://github.com/Boom5426/DrugDis/blob/main/manuscript/DrugDis_manuscript.pdf) &nbsp;·&nbsp; [Supplement](https://github.com/Boom5426/DrugDis/blob/main/manuscript/DrugDis_SI.pdf) &nbsp;·&nbsp; [Code](https://github.com/Boom5426/DrugDis) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/DrugDis) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="drugdis">BibTeX</button>

{% if include.lang == "zh" %}**简介**：把药物和样本的通用效应与情境特异的交互效应分开，揭示整体预测精度由什么驱动，以及模型改进是否真正恢复了生物学解释所需的响应成分。{% else %}**TL;DR**: Separates general drug and sample effects from context-specific interactions, revealing what drives aggregate prediction accuracy and whether model improvements recover the response components needed for biological interpretation.{% endif %}

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge stage-b">(b) Response Prediction · Multimodal Benchmark</div><a class="paper-figure-link" href="{{ '/images/MVCBench.png' | relative_url }}" target="_blank" rel="noopener" title="View full-size figure"><picture><source srcset="{{ '/images/MVCBench.webp' | relative_url }}" type="image/webp"><img src="{{ '/images/MVCBench.png' | relative_url }}" alt="MVCBench: benchmarking drug-molecular and gene representations for drug-induced virtual cell phenotypes" width="800" height="741" loading="lazy" decoding="async"></picture></a></div></div>
<div class='paper-box-text' markdown="1">

[MVCBench: A Multimodal Benchmark for Drug-induced Virtual Cell Phenotypes](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1)

**Bo Li**<sup>†</sup>, Qing Wang<sup>†</sup>, Shihang Wang<sup>†</sup>, Bob Zhang<sup>&#42;</sup>, Yuzhong Peng, Pinxian Zeng, Chengliang Liu, Mengran Li, Ziyang Tang, Xiaojun Yao, Chuxia Deng, Qianqian Song<sup>&#42;</sup>

<span class="venue venue-preprint">bioRxiv</span> 2026 &nbsp;·&nbsp; [Project](https://qsong-github.github.io/MVCBench/) &nbsp;·&nbsp; [Preprint](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1) &nbsp;·&nbsp; [Code](https://github.com/QSong-github/MVCBench) &nbsp;·&nbsp; [Data](https://huggingface.co/datasets/Boom5426/MVCBench) &nbsp;·&nbsp; <button type="button" class="bibtex-btn" data-key="mvcbench">BibTeX</button>

{% if include.lang == "zh" %}**简介**：对药物诱导的转录组与形态学响应，系统评测分子与细胞表征，检验哪些预测增益能跨化合物、细胞系、实验批次和数据集保持。{% else %}**TL;DR**: Benchmarks molecular and cellular representations for drug-induced transcriptomic and morphological responses, testing which predictive gains persist across compounds, cell lines, experimental batches, and datasets.{% endif %}

</div></div>

<div class="pub-record">{% if include.lang == "zh" %}完整论文列表见 {% else %}Full publication record on {% endif %}<a href="https://scholar.google.com/citations?hl=en&user=y1myk_IAAAAJ&view_op=list_works&sortby=pubdate"><strong>Google Scholar ↗</strong></a></div>

<script type="application/json" id="bibtex-data">{{ site.data.bibtex | jsonify }}</script>
