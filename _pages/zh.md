---
permalink: /zh/
lang: zh
title: "中文主页"
description: "李波，澳门大学博士生、新加坡国立大学访问学生，研究 AI for Biology：多模态虚拟细胞、扰动建模与干预设计。"
author_profile: true
---

<h1 class="screen-reader-text">李波 Bo Li — AI for Biology：从多模态虚拟细胞到实验决策</h1>

<span class='anchor' id='about-me'></span>

<div class="hero-block">
  <div class="hero-kicker">{% include icon.html name="dna" %}<span>AI for Biology</span><span class="hero-topics">多模态虚拟细胞 · 扰动建模 · 干预设计</span></div>
  <div class="hero-title">从多模态虚拟细胞到实验决策</div>
  <p class="hero-copy">我研究如何用 AI 把多模态细胞测量转化为实验决策。我的研究围绕一个闭环：从多模态数据中学习细胞状态，预测细胞对扰动的响应，检验实验能分辨哪些预测差异，再在有限预算下选择下一步最值得做的干预。</p>
  <div class="hero-affiliations">
    <span>{% include icon.html name="university" %}<a href="https://www.um.edu.mo/"><strong>澳门大学</strong></a>（导师 <a href="https://fic.um.edu.mo/zh-hant/people/bobzhang/">Bob Zhang</a>；联合导师 <a href="https://polytechnic.purdue.edu/profile/song1081">Qianqian Song</a>，<a href="https://www.purdue.edu/">普渡大学</a>）</span>
    <span>{% include icon.html name="globe-asia" %}访问 <a href="https://www.nus.edu.sg/"><strong>新加坡国立大学</strong></a>（合作导师 <a href="https://www.comp.nus.edu.sg/cs/people/zhangy/">Yang Zhang</a>）</span>
  </div>
</div>

<div class="avail">
  {% include icon.html name="search" %}
  <div class="avail-copy"><strong>正在寻找 2027 年秋季开始的博士后职位</strong>，方向包括 AI for Biology、虚拟细胞、测量感知的模型评估与干预设计。</div>
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
      <source media="(max-width: 40em)" srcset="{{ '/images/research_loop_vertical.webp' | relative_url }}" width="940" height="3924">
      <img src="{{ '/images/research_loop_1200.webp' | relative_url }}"
           srcset="{{ '/images/research_loop_1200.webp' | relative_url }} 1200w, {{ '/images/research_loop.webp' | relative_url }} 2400w"
           sizes="(max-width: 57.8em) 100vw, 900px"
           alt="研究闭环示意图，共四个面板：(a) 从图像、组学和空间测量中学习细胞状态；(b) 虚拟细胞预测药物和基因扰动下的图像与表达响应；(c) 评估测量能够分辨哪些预测差异；(d) 按从起始状态到目标状态的预测迁移对候选干预排序，并在预算 B 内测试前 K 个。所选干预的实验产生新的测量，形成闭环。" width="1200" height="385" loading="lazy" decoding="async">
    </picture>
  </a>
  <figcaption><strong>从多模态虚拟细胞到实验决策。</strong>(a) 从多模态测量中学习细胞状态。(b) 预测细胞对药物和基因扰动的响应。(c) 检验实验真正能分辨哪些预测差异。(d) 针对从起始状态到目标状态的迁移对干预排序，在有限预算内测试排名最前的候选。这些实验得到的新测量再回到起点，形成闭环。</figcaption>
</figure>

<div class="research-grid">

  <div class="research-card stage-a">
    <div class="research-card-head">
      <span class="research-icon">{% include icon.html name="microscope" %}</span>
      <div class="research-num">(a) · 细胞状态</div>
    </div>
    <h3>从成像与组学测量中能学到怎样的细胞状态表征？</h3>
    <p>从显微图像、单细胞与空间组学以及病理切片中学习细胞表征，让不同的测量描述同一个细胞状态。</p>
    <div class="research-work">
      <a href="https://phenoprofiler.org/">PhenoProfiler</a>
      <a href="https://github.com/QSong-github/SpaIM">SpaIM</a>
      <a href="https://doi.org/10.1093/bib/bbae500">HGGEP</a>
    </div>
  </div>

  <div class="research-card stage-b">
    <div class="research-card-head">
      <span class="research-icon">{% include icon.html name="project-diagram" %}</span>
      <div class="research-num">(b) · 响应预测</div>
    </div>
    <h3>预测的扰动响应在模态、化合物与细胞情境之间迁移得如何？</h3>
    <p>预测细胞在药物和基因扰动下的图像与表达响应，并检验模型在化合物、细胞系、实验板和数据集变化下能否泛化。</p>
    <div class="research-work">
      <a href="https://qsong-github.github.io/MVCBench/">MVCBench</a>
    </div>
  </div>

  <div class="research-card stage-c">
    <div class="research-card-head">
      <span class="research-icon">{% include icon.html name="search" %}</span>
      <div class="research-num">(c) · 评估与分辨</div>
    </div>
    <h3>预测增益何时反映的是实验能够可重复分辨的生物学？</h3>
    <p>弄清实验能够可重复地分辨哪些生物学差异、模型真正恢复了哪些响应结构，在解读基准结果之前先把测量局限和模型局限区分开。</p>
    <div class="research-work">
      <a href="https://boom5426.github.io/PertResolve/">PertResolve</a>
      <a href="https://boom5426.github.io/DrugDis/">DrugDis</a>
      <a href="https://github.com/limengran98/MorphoSuff">MorphoSuff</a>
    </div>
  </div>

  <div class="research-card stage-d">
    <div class="research-card-head">
      <span class="research-icon">{% include icon.html name="bullseye" %}</span>
      <div class="research-num">(d) · 实验选择</div>
      <span class="research-focus">当前重点</span>
    </div>
    <h3>给定目标细胞状态和有限预算，下一步最值得测试哪些干预？</h3>
    <p>按从起始状态到目标状态的预测迁移对候选干预排序，在预算 B 内测试排名前 K 的候选，并用独立测得的结果评估这些选择。</p>
    <div class="research-work">
      <a href="https://boom5426.github.io/VCDesign-CED/">VCDesign</a>
    </div>
  </div>
</div>

<div class="research-next" id="vision">
  <span class="research-next-label">下一步方向</span>
  <p>自适应干预设计：把虚拟细胞模型、科研智能体和独立的实验反馈连接起来，让每一轮实验都为下一轮提供信息。</p>
</div>

## {% include icon.html name="file-alt" class="h-icon" %}代表性论文 {#publications}

{% include publications.md lang="zh" %}

## {% include icon.html name="code" class="h-icon" %}软件与资源 {#software}

{% include software.md lang="zh" %}

## {% include icon.html name="graduation-cap" class="h-icon" %}教育经历 {#education}
- *2026.06 – 2027.06*：**新加坡国立大学**

  *- 访问学生，合作导师：[Prof. Yang Zhang](https://www.comp.nus.edu.sg/cs/people/zhangy/)*

- *2024.08 – 至今（预计 2027.06 毕业）*：**澳门大学**

  *- 计算机科学博士（人工智能系），全额奖学金。导师：[Prof. Bob Zhang](https://fic.um.edu.mo/zh-hant/people/bobzhang/)；联合导师：[Prof. Qianqian Song](https://polytechnic.purdue.edu/profile/song1081)（普渡大学）*

- *2021.09 – 2024.07*：**北京工业大学**

  *- 电子信息硕士。导师：[Prof. Yong Zhang](https://yanzhao.bjut.edu.cn/info/1434/11510.htm)、[Prof. Baocai Yin](https://www.bjut.edu.cn/info/1059/1568.htm)*

- *2017.09 – 2021.07*：**北京信息科技大学**

  *- 机器人工程学士。导师：[Prof. Hongbo Huang](https://jsjxy.bistu.edu.cn/docs/2025-02/8d1313acd5814afd9f5d15f4b7b9403a.pdf)*

## {% include icon.html name="award" class="h-icon" %}荣誉奖励 {#honors}
- *2024*：澳门大学博士奖学金
- *2024.07*：北京工业大学 Top 100 毕业生（前 100 / 6331）
- *2024.07 & 2021.07*：北京市优秀毕业生
- *2023.10*：小米奖学金
- *2022.10*：国家奖学金
- *2021*：北京信息科技大学科技创新奖学金一等奖

## {% include icon.html name="lightbulb" class="h-icon" %}专利 {#patents}
两项已授权中国发明专利的共同发明人，内容涉及细胞定位：[**CN115457547B**](https://patents.google.com/patent/CN115457547B/en)（2026）、[**CN115810046B**](https://patents.google.com/patent/CN115810046B/en)（2026）。

## {% include icon.html name="hands-helping" class="h-icon" %}学术服务 {#service}

**会议审稿人**：ICLR 2027。

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
