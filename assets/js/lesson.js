function saveEssayDraft(textareaId, storageKey) {
  const textarea = document.getElementById(textareaId);

  if (!textarea) {
    return;
  }

  localStorage.setItem(storageKey, textarea.value);
}

function loadEssayDraft(textareaId, storageKey) {
  const textarea = document.getElementById(textareaId);

  if (!textarea) {
    return;
  }

  const saved = localStorage.getItem(storageKey);

  if (saved) {
    textarea.value = saved;
  }
}
