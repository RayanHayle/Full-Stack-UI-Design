function submitAnswer() {
    const form = document.getElementById('quiz-form');
    const selected = document.querySelector('input[name="answer"]:checked');

    if (!selected) {
        alert("Please choose an answer.");
        return;
    }

    const choice = selected.value;
    const correctAnswer = form.dataset.correct;
    const question = form.dataset.question;
    const next = form.dataset.next;
    const isCorrect = choice === correctAnswer ? 1 : 0;

    fetch('/submit/answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            correct: isCorrect,
            choice: choice,
            id: question,
        })
    })
    .then(response => {
        if (response.ok) {
            window.location.href = `/quiz/${next}`;
        } else {
            alert("Error submitting answer.");
        }
    })
    .catch(error => {
        console.error("Fetch error:", error);
    });
}

// submit button, move to next question 
document.addEventListener('DOMContentLoaded', function () {
    const submitButton = document.getElementById('submit-button');
    submitButton.addEventListener('click', submitAnswer);
});


