/* ==========================================================================
   Nova Solar Solutions - site behaviour
   Vanilla JS, no dependencies.
   ========================================================================== */
(function () {
  'use strict';

  var onReady = function (fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  };

  /* ---------- Mobile navigation ---------- */
  function initNav() {
    var nav = document.querySelector('.nav');
    var toggle = document.querySelector('.nav__toggle');
    if (!nav || !toggle) return;

    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    // close when a link is tapped
    nav.addEventListener('click', function (e) {
      if (e.target.closest('.nav__link') && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    // close on outside click / Escape
    document.addEventListener('click', function (e) {
      if (!nav.classList.contains('is-open')) return;
      if (!nav.contains(e.target)) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* ---------- Header shadow on scroll ---------- */
  function initHeader() {
    var header = document.querySelector('.site-header');
    if (!header) return;
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Mark the active nav item ---------- */
  function initActiveLink() {
    var here = location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav__link').forEach(function (a) {
      var href = a.getAttribute('href');
      if (!href || href.charAt(0) === '#') return;
      if (href === here) {
        a.classList.add('is-active');
        a.setAttribute('aria-current', 'page');
      }
    });
  }

  /* ---------- Accordion (FAQ) ---------- */
  function initAccordion() {
    document.querySelectorAll('.acc').forEach(function (acc) {
      var btns = acc.querySelectorAll('.acc__btn');

      var close = function (btn) {
        var panel = document.getElementById(btn.getAttribute('aria-controls'));
        btn.setAttribute('aria-expanded', 'false');
        if (panel) panel.style.maxHeight = null;
      };
      var open = function (btn) {
        var panel = document.getElementById(btn.getAttribute('aria-controls'));
        btn.setAttribute('aria-expanded', 'true');
        if (panel) panel.style.maxHeight = panel.scrollHeight + 'px';
      };

      btns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          var isOpen = btn.getAttribute('aria-expanded') === 'true';
          btns.forEach(close);           // one panel at a time
          if (!isOpen) open(btn);
        });
      });

      // keep an open panel correctly sized after a resize
      window.addEventListener('resize', function () {
        btns.forEach(function (btn) {
          if (btn.getAttribute('aria-expanded') === 'true') {
            var panel = document.getElementById(btn.getAttribute('aria-controls'));
            if (panel) panel.style.maxHeight = panel.scrollHeight + 'px';
          }
        });
      });
    });
  }

  /* ---------- Reveal on scroll ---------- */
  function initReveal() {
    var items = document.querySelectorAll('.reveal');
    if (!items.length) return;

    if (!('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var delay = parseInt(el.getAttribute('data-delay') || '0', 10);
        setTimeout(function () { el.classList.add('is-in'); }, delay);
        io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Animated counters ---------- */
  function initCounters() {
    var nums = document.querySelectorAll('[data-count]');
    if (!nums.length) return;

    var run = function (el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var suffix = el.getAttribute('data-suffix') || '';
      var decimals = (el.getAttribute('data-decimals') || '0') | 0;
      var dur = 1500, start = null;

      var tick = function (ts) {
        if (start === null) start = ts;
        var p = Math.min((ts - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = (target * eased).toFixed(decimals) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };

    if (!('IntersectionObserver' in window)) {
      nums.forEach(run);
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { run(e.target); io.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    nums.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Form validation ---------- */
  function initForms() {
    var EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    // AU numbers: 04xx xxx xxx, 0x xxxx xxxx, 1300/1800 xxx xxx, +61...
    var PHONE = /^(\+?61|0)[\s-]?[2-478](?:[\s-]?\d){8}$|^1[38]00[\s-]?\d{3}[\s-]?\d{3}$/;

    document.querySelectorAll('form[data-validate]').forEach(function (form) {
      var msg = form.querySelector('.form-msg');

      var setError = function (field, text) {
        field.classList.add('has-error');
        var e = field.querySelector('.err-text');
        if (e && text) e.textContent = text;
      };
      var clearError = function (field) { field.classList.remove('has-error'); };

      var validate = function (input) {
        var field = input.closest('.field');
        if (!field) return true;
        var val = (input.value || '').trim();

        if (input.hasAttribute('required') && !val) {
          setError(field, 'This field is required.'); return false;
        }
        if (val && input.type === 'email' && !EMAIL.test(val)) {
          setError(field, 'Enter a valid email address.'); return false;
        }
        if (val && input.type === 'tel' && !PHONE.test(val.replace(/[()]/g, ''))) {
          setError(field, 'Enter a valid Australian phone number.'); return false;
        }
        // Victorian postcodes are 3xxx (and 8xxx for PO boxes)
        if (val && input.name === 'postcode' && !/^[38]\d{3}$/.test(val)) {
          setError(field, 'Enter a Victorian postcode (3000-3999).'); return false;
        }
        clearError(field);
        return true;
      };

      form.querySelectorAll('input,select,textarea').forEach(function (input) {
        input.addEventListener('blur', function () { validate(input); });
        input.addEventListener('input', function () {
          var f = input.closest('.field');
          if (f && f.classList.contains('has-error')) validate(input);
        });
      });

      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var ok = true, firstBad = null;
        form.querySelectorAll('input,select,textarea').forEach(function (input) {
          if (!validate(input)) { ok = false; if (!firstBad) firstBad = input; }
        });

        if (!ok) {
          if (msg) { msg.className = 'form-msg is-err'; msg.textContent = 'Please check the highlighted fields and try again.'; }
          if (firstBad) firstBad.focus();
          return;
        }

        // No backend is wired up yet - this is where the POST would go.
        var btn = form.querySelector('button[type="submit"]');
        var label = btn ? btn.textContent : '';
        if (btn) { btn.disabled = true; btn.textContent = 'Sending...'; }

        setTimeout(function () {
          if (msg) {
            msg.className = 'form-msg is-ok';
            msg.textContent = 'Thanks - your request has been received. A Nova Solar consultant will call you within one business day.';
          }
          form.reset();
          if (btn) { btn.disabled = false; btn.textContent = label; }
        }, 700);
      });
    });
  }

  /* ---------- Footer year ---------- */
  function initYear() {
    document.querySelectorAll('[data-year]').forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  }

  onReady(function () {
    initNav();
    initHeader();
    initActiveLink();
    initAccordion();
    initReveal();
    initCounters();
    initForms();
    initYear();
  });
})();
