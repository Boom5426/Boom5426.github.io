/* Homepage behaviour without jQuery: priority-plus navigation, image lightbox,
   off-site links in new tabs, collapsible author lists on phones, BibTeX copy. */
(function () {
  'use strict';

  // --- Priority-plus navigation: move masthead links that do not fit into the
  // dropdown behind the menu button (port of the old greedy-navigation plugin).
  var nav = document.getElementById('site-nav');
  if (nav) {
    var button = nav.querySelector('button');
    var visible = nav.querySelector('.visible-links');
    var hidden = nav.querySelector('.hidden-links');
    var breaks = [];

    var updateNav = function () {
      var buttonShown = !button.classList.contains('hidden');
      var available = buttonShown ? nav.clientWidth - button.offsetWidth - 30 : nav.clientWidth;
      if (visible.offsetWidth > available && visible.children.length) {
        breaks.push(visible.offsetWidth);
        hidden.insertBefore(visible.lastElementChild, hidden.firstChild);
        button.classList.remove('hidden');
        updateNav();
        return;
      }
      if (breaks.length && available > breaks[breaks.length - 1]) {
        visible.appendChild(hidden.firstElementChild);
        breaks.pop();
        updateNav();
        return;
      }
      if (!breaks.length) {
        button.classList.add('hidden');
        hidden.classList.add('hidden');
        button.classList.remove('close');
        button.setAttribute('aria-expanded', 'false');
      }
      button.setAttribute('count', breaks.length);
    };

    button.setAttribute('aria-expanded', 'false');
    button.addEventListener('click', function () {
      var open = hidden.classList.toggle('hidden') === false;
      button.classList.toggle('close', open);
      button.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', function (event) {
      if (!nav.contains(event.target) && !hidden.classList.contains('hidden')) {
        hidden.classList.add('hidden');
        button.classList.remove('close');
        button.setAttribute('aria-expanded', 'false');
      }
    });
    window.addEventListener('resize', updateNav);
    if (document.fonts && document.fonts.ready) { document.fonts.ready.then(updateNav); }
    updateNav();
  }

  // --- Off-site links and PDFs open in a new tab; in-page anchors stay put.
  var links = document.querySelectorAll('a[href]');
  for (var i = 0; i < links.length; i++) {
    var a = links[i];
    if (a.hasAttribute('target')) { continue; }
    var offsite = a.hostname && a.hostname !== window.location.hostname;
    var isPdf = /\.pdf$/i.test(a.pathname || '');
    if (offsite || isPdf) {
      a.setAttribute('target', '_blank');
      a.setAttribute('rel', (a.getAttribute('rel') ? a.getAttribute('rel') + ' ' : '') + 'noopener');
    }
  }

  // --- Lightbox: links to images (publication figures, WeChat QR) open in a dialog.
  var imageLinks = document.querySelectorAll('a[href$=".png"], a[href$=".jpg"], a[href$=".jpeg"], a[href$=".webp"], a[href$=".gif"]');
  if (imageLinks.length && typeof HTMLDialogElement === 'function') {
    var dialog = document.createElement('dialog');
    dialog.className = 'lightbox';
    dialog.innerHTML = '<button type="button" class="lightbox-close" aria-label="Close">×</button><img alt="">' +
      '<a class="lightbox-open" target="_blank" rel="noopener">Open full size ↗</a>';
    document.body.appendChild(dialog);
    var dialogImg = dialog.querySelector('img');
    var dialogLink = dialog.querySelector('.lightbox-open');
    dialog.addEventListener('click', function (event) {
      if (event.target === dialog || event.target.classList.contains('lightbox-close') || event.target === dialogImg) {
        dialog.close();
      }
    });
    dialog.addEventListener('close', function () { dialogImg.removeAttribute('src'); });
    Array.prototype.forEach.call(imageLinks, function (link) {
      link.addEventListener('click', function (event) {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.button !== 0) { return; }
        event.preventDefault();
        var inner = link.querySelector('img');
        dialogImg.src = link.href;
        dialogImg.alt = inner ? inner.alt : (link.getAttribute('aria-label') || link.textContent.trim());
        dialogLink.href = link.href;
        dialog.showModal();
      });
    });
  }

  // --- Phones: clamp long author lists to two lines with a toggle.
  var narrow = window.matchMedia('(max-width: 48em)');
  var authorLines = document.querySelectorAll('.paper-box-text > p:nth-of-type(2)');
  var lang = document.documentElement.lang === 'zh-CN' ? 'zh' : 'en';
  var labels = lang === 'zh' ? { more: '展开全部作者', less: '收起' } : { more: 'All authors', less: 'Fewer authors' };
  var applyClamp = function () {
    Array.prototype.forEach.call(authorLines, function (p) {
      var toggle = p.nextElementSibling && p.nextElementSibling.classList.contains('authors-toggle') ? p.nextElementSibling : null;
      if (!narrow.matches) {
        p.classList.remove('authors-clamped');
        if (toggle) { toggle.remove(); }
        return;
      }
      if (toggle) { return; }
      p.classList.add('authors-clamped');
      if (p.scrollHeight <= p.clientHeight + 2) {
        p.classList.remove('authors-clamped');
        return;
      }
      toggle = document.createElement('button');
      toggle.type = 'button';
      toggle.className = 'authors-toggle';
      toggle.setAttribute('aria-expanded', 'false');
      toggle.textContent = labels.more;
      toggle.addEventListener('click', function () {
        var clamped = p.classList.toggle('authors-clamped');
        toggle.textContent = clamped ? labels.more : labels.less;
        toggle.setAttribute('aria-expanded', String(!clamped));
      });
      p.parentNode.insertBefore(toggle, p.nextSibling);
    });
  };
  if (narrow.addEventListener) { narrow.addEventListener('change', applyClamp); }
  applyClamp();

  // --- BibTeX: copy the entry from _data/bibtex.yml; show it if the clipboard is unavailable.
  var bibData = document.getElementById('bibtex-data');
  if (bibData) {
    var entries = JSON.parse(bibData.textContent);
    var copied = lang === 'zh' ? '已复制 ✓' : 'Copied ✓';
    Array.prototype.forEach.call(document.querySelectorAll('.bibtex-btn'), function (btn) {
      var text = entries[btn.getAttribute('data-key')];
      if (!text) { btn.remove(); return; }
      var label = btn.textContent;
      var showFallback = function () {
        var pre = btn.closest('.paper-box-text').querySelector('.bibtex-fallback');
        if (!pre) {
          pre = document.createElement('pre');
          pre.className = 'bibtex-fallback';
          pre.textContent = text;
          btn.closest('p').insertAdjacentElement('afterend', pre);
          return;
        }
        pre.hidden = !pre.hidden;
      };
      btn.addEventListener('click', function () {
        if (!navigator.clipboard || !window.isSecureContext) { showFallback(); return; }
        navigator.clipboard.writeText(text).then(function () {
          btn.textContent = copied;
          btn.classList.add('is-copied');
          setTimeout(function () { btn.textContent = label; btn.classList.remove('is-copied'); }, 1600);
        }, showFallback);
      });
    });
  }
})();
