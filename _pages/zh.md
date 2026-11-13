---
permalink: /zh/
lang: zh
title: "中文主页"
description: "李波，澳门大学计算机科学博士生、新加坡国立大学访问博士生，研究多模态虚拟细胞、扰动建模、干预决策与权重空间编程。"
author_profile: true
---

<h1 class="screen-reader-text">李波 Bo Li — 虚拟细胞、干预设计与模型能力进化</h1>
<span class='anchor' id='about-me'></span>
<div class="hero-block">
  <div class="hero-kicker">{% include icon.html name="dna" %}<span>科学人工智能</span><span class="hero-topics">虚拟细胞世界模型 · 闭环干预设计 · 模型能力进化</span></div>
  <div class="hero-title">从虚拟细胞到持续进化的科学 AI</div>
  <p class="hero-copy">我研究 AI 系统如何从观测中学习、支持科学干预，并通过新证据持续改进。研究涵盖多模态细胞建模、基因与药物扰动预测、测量感知评估和干预设计。同时，我探索如何通过权重空间编程，使预训练模型获得、保留并积累新能力。长期目标是构建连接观测、实验与持续学习的自适应科学 AI 系统，支持更可靠的科学决策。</p>
  <div class="hero-affiliations">
    <span>{% include icon.html name="university" %}<a href="https://www.um.edu.mo/"><strong>澳门大学</strong></a> (导师 <a href="https://fic.um.edu.mo/zh-hant/people/bobzhang/">Bob Zhang</a>; 联合导师 <a href="https://polytechnic.purdue.edu/profile/song1081">Qianqian Song</a>)</span>
    <span>{% include icon.html name="globe-asia" %}访问 <a href="https://www.nus.edu.sg/"><strong>新加坡国立大学</strong></a> (合作导师 <a href="https://www.comp.nus.edu.sg/cs/people/zhangy/">Yang Zhang</a>)</span>
  </div>
</div>
<div class="avail">
  {% include icon.html name="search" %}
  <div class="avail-copy"><strong>开放 2027 年起的博士后与教职合作机会</strong>，方向包括虚拟细胞世界模型、科学干预设计和可持续更新的 AI 模型。</div>
  <div class="avail-actions">
    <a class="link-btn" href="{{ site.author.cv | relative_url }}">查看简历 <span aria-hidden="true">↗</span></a>
    <a class="link-btn ghost" href="mailto:{{ site.author.email }}">邮件联系</a>
  </div>
</div>

## {% include icon.html name="bullhorn" class="h-icon" %}近期动态 {#news}

{% include news.html lang="zh" %}

## {% include icon.html name="flask" class="h-icon" %}研究方向 {#research}

<figure class="research-figure">
  <a href="{{ '/images/research_loop.webp' | relative_url }}" title="查看高清原图">
    <picture>
      <source media="(max-width: 40em)" srcset="{{ '/images/research_loop_vertical.webp' | relative_url }}" width="940" height="4413">
      <img src="{{ '/images/research_loop_1200.webp' | relative_url }}"
           srcset="{{ '/images/research_loop_1200.webp' | relative_url }} 1200w, {{ '/images/research_loop.webp' | relative_url }} 2400w"
           sizes="(max-width: 57.8em) 100vw, 900px"
           alt="研究闭环示意图，共五部分：(a) 从图像、组学和空间测量中学习细胞状态；(b) 虚拟细胞预测药物和基因扰动下的图像与表达响应；(c) 评估测量能够分辨哪些预测差异；(d) 按从起始状态到目标状态的预测迁移对候选干预排序，并在预算 B 内测试前 K 个；所选干预的实验给出实测结果，(e) 自我改进模型（WeightCode、WeightLoop、CellScientist）把这些结果转化为持久的模型更新，回到虚拟细胞。" width="1200" height="524" loading="lazy" decoding="async">
    </picture>
  </a>
  <figcaption><strong>从多模态虚拟细胞到自我改进的模型。</strong> (a) 学习多模态细胞状态；(b) 预测基因与药物扰动响应；(c) 检验测量能够可重复分辨哪些差异；(d) 在有限预算下选择下一步干预；(e) 把实测结果转化为持久的模型更新，进入下一轮预测。</figcaption>
</figure>

<ol class="research-strands">
  <li class="strand stage-a">
    <div class="strand-label">{% include icon.html name="microscope" %}<span>(a) · 细胞状态</span></div>
    <div class="strand-body">
      <h3>从成像与组学测量中能学到怎样的细胞状态表征？</h3>
      <div class="research-work">
      <a href="https://phenoprofiler.org/">PhenoProfiler</a>
      <a href="https://github.com/QSong-github/SpaIM">SpaIM</a>
      <a href="https://doi.org/10.1093/bib/bbae500">HGGEP</a>
      </div>
    </div>
  </li>
  <li class="strand stage-b">
    <div class="strand-label">{% include icon.html name="project-diagram" %}<span>(b) · 响应预测</span></div>
    <div class="strand-body">
      <h3>学到的干预下细胞状态转变，能否跨模态、化合物与细胞情境泛化？</h3>
      <div class="research-work">
      <a href="https://qsong-github.github.io/MVCBench/">MVCBench</a>
      </div>
    </div>
  </li>
  <li class="strand stage-c">
    <div class="strand-label">{% include icon.html name="search" %}<span>(c) · 评估与分辨</span></div>
    <div class="strand-body">
      <h3>预测增益何时反映的是实验能够可重复分辨的生物学？</h3>
      <div class="research-work">
      <a href="https://boom5426.github.io/PertResolve/">PertResolve</a>
      <a href="https://boom5426.github.io/DrugDis/">DrugDis</a>
      <a href="https://www.biorxiv.org/content/10.64898/2026.09.22.753654v2">MorphoSuff</a>
      </div>
    </div>
  </li>
  <li class="strand stage-d">
    <div class="strand-label">{% include icon.html name="bullseye" %}<span>(d) · 实验选择</span><span class="research-focus">当前重点</span></div>
    <div class="strand-body">
      <h3>用模型做规划：给定目标细胞状态和有限预算，下一步最值得测试哪些干预？</h3>
      <div class="research-work">
      <a href="https://boom5426.github.io/VCDesign-CED/">VCDesign</a>
      </div>
    </div>
  </li>
  <li class="strand stage-e">
    <div class="strand-label">{% include icon.html name="code" %}<span>(e) · 模型能力进化</span></div>
    <div class="strand-body">
      <h3>闭合反馈环：实测结果能否持续为模型增加能力，这些增益又能否改进它的下一步决策？</h3>
      <div class="research-work">
      <a href="https://github.com/Gen-Verse/WeightCode">WeightCode</a>
      <a href="https://arxiv.org/abs/2611.07319">WeightLoop</a>
      <a href="https://arxiv.org/abs/2605.07335">CellScientist</a>
      </div>
    </div>
  </li>
</ol>

<div class="research-next" id="vision">
  <span class="research-next-label">下一步方向</span>
  <ul>
    <li><strong>可更新的细胞世界模型。</strong> 把新的实验结果转化为持久、可迁移的模型更新，而不是重新训练。</li>
    <li><strong>能力增长是否带来回报？</strong> 检验每次更新能否在留出实验上改进干预选择。</li>
    <li><strong>能力积累。</strong> 用可复用的模型编辑加入扰动与细胞情境相关能力，同时不遗忘已有能力。</li>
  </ul>
</div>

## {% include icon.html name="file-alt" class="h-icon" %}代表性论文 {#publications}

{% include publications.md lang="zh" %}

## {% include icon.html name="code" class="h-icon" %}软件与资源 {#software}

{% include software.md lang="zh" %}

## {% include icon.html name="graduation-cap" class="h-icon" %}教育经历 {#education}
- *2026.06 – 2027.06*：**新加坡国立大学**

  *- 访问博士生，合作导师：[Prof. Yang Zhang](https://www.comp.nus.edu.sg/cs/people/zhangy/)*

- *2024.08 – 至今（预计 2027.06 毕业）*：**澳门大学**

  *- 计算机科学博士（人工智能系），全额奖学金。导师：[Prof. Bob Zhang](https://fic.um.edu.mo/zh-hant/people/bobzhang/)；联合导师：[Prof. Qianqian Song](https://polytechnic.purdue.edu/profile/song1081)（普渡大学）*

- *2021.09 – 2024.07*：**北京工业大学**

  *- 电子信息硕士。导师：[Prof. Yong Zhang](https://znxy.bjut.edu.cn/info/1599/1256.htm)、[Prof. Baocai Yin](https://www.bjut.edu.cn/info/1059/1568.htm)*

- *2017.09 – 2021.07*：**北京信息科技大学**

  *- 机器人工程学士。导师：[Prof. Hongbo Huang](https://jsjxy.bistu.edu.cn/docs/2025-02/8d1313acd5814afd9f5d15f4b7b9403a.pdf)*

## {% include icon.html name="award" class="h-icon" %}荣誉奖励 {#honors}
- *2024*：澳门大学博士全额奖学金
- *2024.07*：北京工业大学 Top 100 毕业生（前 100 / 6331）
- *2024.07 & 2021.07*：北京市优秀毕业生
- *2023.10*：小米奖学金
- *2022.10*：国家奖学金（教育部）
- *2022、2023*：北京工业大学学业一等奖学金
- *2021*：北京信息科技大学科技创新奖学金一等奖

## {% include icon.html name="lightbulb" class="h-icon" %}专利 {#patents}
两项已授权中国发明专利的共同发明人，内容涉及细胞定位：[**CN115457547B**](https://patents.google.com/patent/CN115457547B/en)（2026）、[**CN115810046B**](https://patents.google.com/patent/CN115810046B/en)（2026）。

## {% include icon.html name="hands-helping" class="h-icon" %}学术服务 {#service}

**期刊审稿人**：*Science Advances*、**IEEE TPAMI**、IEEE TIP、IEEE TNNLS、Medical Image Analysis、Bioinformatics、Briefings in Bioinformatics、Pattern Recognition、BMC Biology、Engineering Applications of Artificial Intelligence、Expert Systems with Applications。

**合作单位**：普渡大学、康奈尔大学、佛罗里达大学、新加坡国立大学、中山大学、四川大学、北京工业大学、澳门理工大学。

<div class="logo-row">
  <img src="{{ '/images/Bistu-logo.png' | relative_url }}" alt="北京信息科技大学" width="121" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/Bjut-logo.png' | relative_url }}" alt="北京工业大学" width="132" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/UM_logo.png' | relative_url }}" alt="澳门大学" width="120" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/huaxi-logo.png' | relative_url }}" alt="四川大学华西医院" width="572" height="120" loading="lazy" decoding="async">
  <img src="{{ '/images/NUS_logo.jpg' | relative_url }}" alt="新加坡国立大学" width="241" height="120" loading="lazy" decoding="async">
</div>

<footer class="site-footer">
  <p>&copy; 2026 李波 Bo Li. 保留所有权利。</p>
  <p>
    模板改编自
    <a href="https://github.com/RayeRen/acad-homepage.github.io"
       target="_blank" rel="noopener">Yi Ren</a>。
  </p>
</footer>
