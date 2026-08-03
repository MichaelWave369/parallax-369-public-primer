(() => {
  const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
  const panels = Array.from(document.querySelectorAll('[role="tabpanel"]'));

  const activate = (tab) => {
    const stage = tab.dataset.stage;

    tabs.forEach((item) => {
      const selected = item === tab;
      item.classList.toggle('active', selected);
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
    });

    panels.forEach((panel) => {
      const selected = panel.id === `panel-${stage}`;
      panel.classList.toggle('active', selected);
      panel.hidden = !selected;
    });
  };

  if (tabs.length && panels.length) {
    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => activate(tab));

      tab.addEventListener('keydown', (event) => {
        if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;

        event.preventDefault();
        let nextIndex = index;

        if (event.key === 'ArrowRight') nextIndex = (index + 1) % tabs.length;
        if (event.key === 'ArrowLeft') nextIndex = (index - 1 + tabs.length) % tabs.length;
        if (event.key === 'Home') nextIndex = 0;
        if (event.key === 'End') nextIndex = tabs.length - 1;

        activate(tabs[nextIndex]);
        tabs[nextIndex].focus();
      });
    });
  }

  const versionLabel = document.querySelector('.hero .eyebrow');
  if (versionLabel) versionLabel.textContent = 'Public Candidate v0.4';

  const nav = document.querySelector('.site-header nav');
  if (nav) {
    const navItems = [
      { id: 'quickstart', href: 'quickstart.html', label: 'Quickstart' },
      { id: 'print-primer', href: 'primer.html', label: 'Print Primer' },
      { id: 'validation', href: 'validation.html', label: 'Validation' }
    ];

    navItems.forEach((item) => {
      if (nav.querySelector(`[data-nav-id="${item.id}"]`)) return;
      const link = document.createElement('a');
      link.href = item.href;
      link.textContent = item.label;
      link.dataset.navId = item.id;
      nav.append(link);
    });
  }

  const resourceGrid = document.querySelector('.resource-grid');
  if (resourceGrid) {
    const resources = [
      {
        id: 'quickstart',
        href: 'quickstart.html',
        label: 'v0.4 start',
        title: 'First project quickstart',
        detail: 'Create a local project scaffold, preserve human authority, and gather real usability observations.'
      },
      {
        id: 'print-primer',
        href: 'primer.html',
        label: 'One page',
        title: 'Printable public primer',
        detail: 'A concise screen-and-paper introduction to 3–6–9.'
      },
      {
        id: 'glossary',
        href: 'https://github.com/MichaelWave369/parallax-369-public-primer/blob/main/GLOSSARY.md',
        label: 'Reference',
        title: 'Public glossary',
        detail: 'Definitions for claims, receipts, evidence, authority, and status.'
      },
      {
        id: 'seed-swap',
        href: 'https://github.com/MichaelWave369/parallax-369-public-primer/blob/main/examples/seed-swap-station/README.md',
        label: 'Physical example',
        title: 'Seed-swap station',
        detail: 'A non-software walkthrough with a preserved human-factors failure.'
      },
      {
        id: 'decision-receipt',
        href: 'https://github.com/MichaelWave369/parallax-369-public-primer/blob/main/examples/decision-receipt-example.md',
        label: 'Receipt',
        title: 'Decision example',
        detail: 'See how options, assumptions, authority, dissent, and later evidence connect.'
      },
      {
        id: 'feedback',
        href: 'https://github.com/MichaelWave369/parallax-369-public-primer/blob/main/FEEDBACK.md',
        label: 'Review',
        title: 'Public feedback guide',
        detail: 'Report clarity, usability, accessibility, and compatibility observations.'
      },
      {
        id: 'compatibility',
        href: 'https://github.com/MichaelWave369/parallax-369-public-primer/blob/main/COMPATIBILITY_AND_VERSIONING.md',
        label: 'Adaptation',
        title: 'Compatibility rules',
        detail: 'Preserve the method contract while adapting format and tooling.'
      },
      {
        id: 'validation',
        href: 'validation.html',
        label: 'v0.3 helpers',
        title: 'Public validation',
        detail: 'Local receipt, template, link, static-site, and report checks with no release authority.'
      },
      {
        id: 'field-trial',
        href: 'https://github.com/MichaelWave369/parallax-369-public-primer/blob/main/FIELD_TRIAL.md',
        label: 'v0.4 evidence',
        title: 'Field-trial protocol',
        detail: 'Voluntary, minimal, non-sensitive observations that can inform a later human decision.'
      }
    ];

    resources.forEach((resource) => {
      if (resourceGrid.querySelector(`[data-resource-id="${resource.id}"]`)) return;

      const link = document.createElement('a');
      link.href = resource.href;
      link.dataset.resourceId = resource.id;

      const label = document.createElement('span');
      label.textContent = resource.label;

      const title = document.createElement('strong');
      title.textContent = resource.title;

      const detail = document.createElement('small');
      detail.textContent = resource.detail;

      link.append(label, title, detail);
      resourceGrid.append(link);
    });
  }
})();
