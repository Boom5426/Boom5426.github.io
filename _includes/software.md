{% comment %}Software table, shared by the English and Chinese pages. Pass lang="zh" for Chinese labels.{% endcomment %}
{% if include.lang == "zh" %}代表性研究软件与社区资源。{% else %}Selected research software and community resources.{% endif %}

{% if include.lang == "zh" %}| 项目 | 简介 | Stars |{% else %}| Project | What it is | Stars |{% endif %}
| :--- | :--- | :--- |
| [VCDesign](https://github.com/Boom5426/VCDesign-CED) | {% if include.lang == "zh" %}面向虚拟细胞的有限预算干预排序与决策对齐评估{% else %}Finite-budget intervention ranking and decision-aligned evaluation for virtual cells{% endif %} | {% include github-stars.html repo="Boom5426/VCDesign-CED" %} |
| [MVCBench](https://github.com/QSong-github/MVCBench) | {% if include.lang == "zh" %}虚拟细胞表征与泛化能力的多模态基准{% else %}Multimodal benchmark for virtual-cell representation and generalization{% endif %} | {% include github-stars.html repo="QSong-github/MVCBench" %} |
| [PhenoProfiler](https://github.com/QSong-github/PhenoProfiler) | {% if include.lang == "zh" %}面向高内涵细胞成像的端到端表型表征学习{% else %}End-to-end phenotypic representation learning for high-content cell imaging{% endif %} | {% include github-stars.html repo="QSong-github/PhenoProfiler" %} |
| [Awesome-Virtual-Cell](https://github.com/Boom5426/Awesome-Virtual-Cell) | {% if include.lang == "zh" %}虚拟细胞研究的文献、数据集、基准与资源汇总{% else %}Curated literature, datasets, benchmarks, and resources for virtual-cell research{% endif %} | {% include github-stars.html repo="Boom5426/Awesome-Virtual-Cell" %} |
| [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills) | {% if include.lang == "zh" %}用于科研论文撰写、修改、审查与重投的 Agent 技能{% else %}Agent skills for scientific manuscript drafting, revision, auditing, and resubmission{% endif %} | {% include github-stars.html repo="Boom5426/Nature-Paper-Skills" %} |
| [SpaIM](https://github.com/QSong-github/SpaIM) | {% if include.lang == "zh" %}用于空间转录组插补的跨模态建模{% else %}Cross-modal modeling for spatial transcriptomics imputation{% endif %} | {% include github-stars.html repo="QSong-github/SpaIM" %} |
{: .software-table}

<p class="stats-note">{% if include.lang == "zh" %}Star 数截至 {{ site.data.github_stars.updated_at | date: "%Y-%m-%d" }} · 点击查看 GitHub 实时数据。{% else %}Stars as of {{ site.data.github_stars.updated_at | date: "%b %-d, %Y" }} · Links open current GitHub counts.{% endif %}</p>
