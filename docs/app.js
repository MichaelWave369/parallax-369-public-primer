(() => {
  const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
  const panels = Array.from(document.querySelectorAll('[role="tabpanel"]'));

  if (!tabs.length || !panels.length) return;

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
})();