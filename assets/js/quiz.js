function checkQuiz(formId, resultId, answers) {
  const form = document.getElementById(formId);
  const result = document.getElementById(resultId);

  if (!form || !result) {
    return;
  }

  let score = 0;
  const total = Object.keys(answers).length;

  form.querySelectorAll('.form-check').forEach((item) => {
    item.classList.remove('border', 'border-success', 'border-danger', 'bg-success-subtle', 'bg-danger-subtle');
  });

  Object.entries(answers).forEach(([questionName, correctValue]) => {
    const selected = form.querySelector(`input[name="${questionName}"]:checked`);
    const correctInput = form.querySelector(`input[name="${questionName}"][value="${correctValue}"]`);

    if (selected && selected.value === correctValue) {
      score += 1;
    }

    if (correctInput) {
      const correctWrapper = correctInput.closest('.form-check');

      if (correctWrapper) {
        correctWrapper.classList.add('border', 'border-success', 'bg-success-subtle');
      }
    }

    if (selected && selected.value !== correctValue) {
      const selectedWrapper = selected.closest('.form-check');

      if (selectedWrapper) {
        selectedWrapper.classList.add('border', 'border-danger', 'bg-danger-subtle');
      }
    }
  });

  result.textContent = `Bạn đúng ${score}/${total} câu.`;
  result.className = `quiz-result alert ${score === total ? 'alert-success' : 'alert-info'}`;
}

function toggleSuggestedAnswer(answerId) {
  const answer = document.getElementById(answerId);

  if (!answer) {
    return;
  }

  answer.classList.toggle("show");
}
