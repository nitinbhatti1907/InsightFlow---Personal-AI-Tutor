export default function QuizPanel({ quiz, answers, onAnswerChange, onSubmit, result, loading }) {
  if (!quiz?.length) {
    return null;
  }

  return (
    <section className="card-surface p-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">Knowledge check</p>
          <h3 className="mt-2 text-xl font-semibold text-slate-900">Mini-quiz</h3>
        </div>
        <button
          type="button"
          onClick={onSubmit}
          disabled={loading}
          className="rounded-2xl bg-brand-600 px-5 py-3 text-sm font-semibold text-white transition hover:bg-brand-700 disabled:cursor-not-allowed disabled:opacity-70"
        >
          {loading ? 'Checking...' : 'Check answers'}
        </button>
      </div>

      <div className="mt-6 space-y-6">
        {quiz.map((item, index) => (
          <div key={item.question} className="rounded-3xl border border-slate-200 bg-slate-50 p-5">
            <p className="font-semibold text-slate-900">Q{index + 1}. {item.question}</p>
            <div className="mt-4 grid gap-3">
              {item.options.map((option, optionIndex) => {
                const isSelected = answers[index] === optionIndex;
                const review = result?.reviewed_questions?.[index];
                const showCorrect = review && review.correct_index === optionIndex;
                const showWrong = review && review.selected_index === optionIndex && !review.is_correct;

                return (
                  <button
                    key={option}
                    type="button"
                    onClick={() => onAnswerChange(index, optionIndex)}
                    className={[
                      'rounded-2xl border px-4 py-3 text-left text-sm transition',
                      isSelected ? 'border-brand-500 bg-brand-50 text-slate-900' : 'border-slate-200 bg-white text-slate-700 hover:border-brand-300',
                      showCorrect ? 'border-emerald-400 bg-emerald-50' : '',
                      showWrong ? 'border-rose-400 bg-rose-50' : '',
                    ].join(' ')}
                  >
                    {option}
                  </button>
                );
              })}
            </div>
            {result?.reviewed_questions?.[index] && (
              <p className="mt-4 text-sm leading-7 text-slate-600">
                <span className="font-semibold text-slate-900">Explanation:</span> {result.reviewed_questions[index].explanation}
              </p>
            )}
          </div>
        ))}
      </div>

      {result && (
        <div className="mt-6 rounded-3xl border border-emerald-200 bg-emerald-50 p-5">
          <p className="text-sm font-semibold uppercase tracking-[0.2em] text-emerald-700">Quiz result</p>
          <p className="mt-2 text-2xl font-bold text-slate-900">{result.score_percent}%</p>
          <p className="mt-1 text-sm text-slate-700">{result.correct_answers} out of {result.total_questions} correct</p>
          <p className="mt-3 text-sm leading-7 text-slate-700">{result.feedback}</p>
        </div>
      )}
    </section>
  );
}
