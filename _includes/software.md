{% comment %}Selected projects, shared by English and Chinese pages. Pass lang="zh" for Chinese labels.{% endcomment %}
{% if include.lang == "zh" %}代表性研究软件与开放科学资源。{% else %}Selected research software and open-science resources.{% endif %}

{% if include.lang == "zh" %}| 项目 | 简介 | Stars |{% else %}| Project | What it is | Stars |{% endif %}
| :--- | :--- | :--- |
| [WeightCode](https://github.com/Gen-Verse/WeightCode) | {% if include.lang == "zh" %}通过可执行权重程序安装、复用并积累模型新能力{% else %}Executable weight programs for capability installation, reuse and accumulation{% endif %} | {% include github-stars.html repo="Gen-Verse/WeightCode" %} |
| [VCDesign](https://github.com/Boom5426/VCDesign-CED) | {% if include.lang == "zh" %}面向虚拟细胞的有限预算干预设计与决策评估{% else %}Finite-budget intervention design and decision-aligned evaluation{% endif %} | {% include github-stars.html repo="Boom5426/VCDesign-CED" %} |
| [PertResolve](https://github.com/Boom5426/PertResolve) | {% if include.lang == "zh" %}区分扰动预测中的测量局限与模型局限{% else %}Disentangling measurement and model limits in perturbation prediction{% endif %} | {% include github-stars.html repo="Boom5426/PertResolve" %} |
| [DrugDis](https://github.com/Boom5426/DrugDis) | {% if include.lang == "zh" %}药物响应预测中的通用效应与情境特异交互评估{% else %}General and context-specific effects in drug-response prediction{% endif %} | {% include github-stars.html repo="Boom5426/DrugDis" %} |
| [MVCBench](https://github.com/QSong-github/MVCBench) | {% if include.lang == "zh" %}药物诱导虚拟细胞表型的多模态评估基准{% else %}Multimodal benchmark for drug-induced virtual-cell phenotypes{% endif %} | {% include github-stars.html repo="QSong-github/MVCBench" %} |
| [PhenoProfiler](https://github.com/QSong-github/PhenoProfiler) | {% if include.lang == "zh" %}从高内涵显微图像学习细胞表型特征{% else %}Cellular phenotypic learning from high-content microscopy{% endif %} | {% include github-stars.html repo="QSong-github/PhenoProfiler" %} |
| [SpaIM](https://github.com/QSong-github/SpaIM) | {% if include.lang == "zh" %}利用单细胞参考进行空间转录组基因插补{% else %}Spatial-transcriptomics imputation using single-cell references{% endif %} | {% include github-stars.html repo="QSong-github/SpaIM" %} |
| [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills) | {% if include.lang == "zh" %}科研论文写作、修改和审查的 Agent 技能{% else %}Agent skills for scientific writing, revision and review{% endif %} | {% include github-stars.html repo="Boom5426/Nature-Paper-Skills" %} |
| [Awesome Virtual Cell](https://github.com/Boom5426/Awesome-Virtual-Cell) | {% if include.lang == "zh" %}虚拟细胞论文、资源和交互研究地图{% else %}Virtual-cell literature, resources and interactive research map{% endif %} | {% include github-stars.html repo="Boom5426/Awesome-Virtual-Cell" %} |
| [Awesome Weight-Space Programming](https://github.com/Boom5426/Awesome-Weight-Space-Programming) | {% if include.lang == "zh" %}权重空间方法、可编程模型和相关研究图谱{% else %}Weight-space methods, programmable models and research landscape{% endif %} | {% include github-stars.html repo="Boom5426/Awesome-Weight-Space-Programming" %} |
{: .software-table}

<p class="stats-note">{% if include.lang == "zh" %}Star 数截至 {{ site.data.github_stars.updated_at | date: "%Y-%m-%d" }}；点击项目可查看最新数据。{% else %}Stars as of {{ site.data.github_stars.updated_at | date: "%b %-d, %Y" }}; open each project for current counts.{% endif %}</p>
