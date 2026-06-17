function checkQuiz(formId, resultId, answers) {
  const form = document.getElementById(formId);
  const result = document.getElementById(resultId);

  if (!form || !result) {
    return;
  }

  let score = 0;
  const total = Object.keys(answers).length;

  Object.entries(answers).forEach(([questionName, correctValue]) => {
    const selected = form.querySelector(`input[name="${questionName}"]:checked`);

    if (selected && selected.value === correctValue) {
      score += 1;
    }
  });

  result.textContent = `Bạn đúng ${score}/${total} câu.`;
  result.classList.add("alert", score === total ? "alert-success" : "alert-info");
}

function toggleSuggestedAnswer(answerId) {
  const answer = document.getElementById(answerId);

  if (!answer) {
    return;
  }

  answer.classList.toggle("show");
}
