{% comment %}Research software and open-source community resources, shared by English and Chinese pages.{% endcomment %}
<h3 class="pub-group">{% if include.lang == "zh" %}研究软件与数据资源{% else %}Research software & datasets{% endif %}</h3>

{% if include.lang == "zh" %}| 项目 | 简介 | Stars |{% else %}| Project | What it is | Stars |{% endif %}
| :--- | :--- | :--- |
| [WeightCode](https://github.com/Gen-Verse/WeightCode) | {% if include.lang == "zh" %}用可执行权重程序为模型安装、复用和叠加新能力{% else %}Install, reuse and accumulate capabilities with executable weight programs{% endif %} | {% include github-stars.html repo="Gen-Verse/WeightCode" %} |
| [VCDesign](https://github.com/Boom5426/VCDesign-CED) | {% if include.lang == "zh" %}面向目标状态的有限预算干预排序与决策评估{% else %}Target-directed intervention ranking and decision-aligned evaluation{% endif %} | {% include github-stars.html repo="Boom5426/VCDesign-CED" %} |
| [PertResolve](https://github.com/Boom5426/PertResolve) | {% if include.lang == "zh" %}区分扰动预测中的测量分辨率与模型能力局限{% else %}Distinguish measurement-resolution and model limitations{% endif %} | {% include github-stars.html repo="Boom5426/PertResolve" %} |
| [DrugDis](https://github.com/Boom5426/DrugDis) | {% if include.lang == "zh" %}拆解药物响应预测中的通用效应与交互效应{% else %}Disentangle general and interaction effects in drug-response prediction{% endif %} | {% include github-stars.html repo="Boom5426/DrugDis" %} |
| [MVCBench](https://github.com/QSong-github/MVCBench) | {% if include.lang == "zh" %}药物诱导多模态虚拟细胞表型的泛化基准{% else %}Multimodal virtual-cell response benchmark{% endif %} | {% include github-stars.html repo="QSong-github/MVCBench" %} |
| [PhenoProfiler](https://github.com/QSong-github/PhenoProfiler) | {% if include.lang == "zh" %}高内涵显微图像表型特征学习{% else %}Phenotypic profiling from high-content microscopy{% endif %} | {% include github-stars.html repo="QSong-github/PhenoProfiler" %} |
| [SpaIM](https://github.com/QSong-github/SpaIM) | {% if include.lang == "zh" %}空间转录组跨模态基因插补{% else %}Cross-modal spatial-transcriptomics imputation{% endif %} | {% include github-stars.html repo="QSong-github/SpaIM" %} |
{: .software-table}

<h3 class="pub-group">{% if include.lang == "zh" %}开放科学与社区资源{% else %}Open-science & community resources{% endif %}</h3>

{% if include.lang == "zh" %}| 项目 | 简介 | Stars |{% else %}| Project | What it is | Stars |{% endif %}
| :--- | :--- | :--- |
| [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills) | {% if include.lang == "zh" %}科研论文撰写、修改、审查与投稿的 Agent 技能{% else %}Agent skills for scientific writing, revision and review{% endif %} | {% include github-stars.html repo="Boom5426/Nature-Paper-Skills" %} |
| [Awesome Virtual Cell](https://github.com/Boom5426/Awesome-Virtual-Cell) | {% if include.lang == "zh" %}虚拟细胞领域论文、基准与交互研究地图{% else %}Virtual-cell literature, benchmarks and interactive research map{% endif %} | {% include github-stars.html repo="Boom5426/Awesome-Virtual-Cell" %} |
| [Awesome Weight-Space Programming](https://github.com/Boom5426/Awesome-Weight-Space-Programming) | {% if include.lang == "zh" %}权重空间方法与可编程模型的研究图谱{% else %}Research landscape for weight-space methods and programmable models{% endif %} | {% include github-stars.html repo="Boom5426/Awesome-Weight-Space-Programming" %} |
| [DrugClaw](https://github.com/Boom5426/DrugClaw) | {% if include.lang == "zh" %}面向药物研究的智能体检索与科研技能库{% else %}Agentic drug-research retrieval and skill library{% endif %} | {% include github-stars.html repo="Boom5426/DrugClaw" %} |
{: .software-table}

<p class="stats-note">{% if include.lang == "zh" %}Star 快照截至 {{ site.data.github_stars.updated_at | date: "%Y-%m-%d" }}；无快照项目可直接打开 GitHub 查看。{% else %}Star snapshot as of {{ site.data.github_stars.updated_at | date: "%b %-d, %Y" }}; open GitHub to see projects without a snapshot.{% endif %}</p>
