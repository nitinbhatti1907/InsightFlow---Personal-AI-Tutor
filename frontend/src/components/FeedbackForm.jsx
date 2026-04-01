export default function FeedbackForm({ feedback, onChange, onSubmit, loading, successMessage }) {
  return (
    <section className="card-surface p-6">
      <div>
        <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">Educator signal</p>
        <h3 className="mt-2 text-xl font-semibold text-slate-900">Save learner feedback</h3>
      </div>

      <div className="mt-5 grid gap-4 lg:grid-cols-2">
        <label className="block text-sm font-medium text-slate-700">
          Learner name
          <input
            value={feedback.learner_name}
            onChange={(event) => onChange('learner_name', event.target.value)}
            className="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none transition focus:border-brand-500"
          />
        </label>

        <label className="block text-sm font-medium text-slate-700">
          Rating (1 to 5)
          <input
            type="number"
            min="1"
            max="5"
            value={feedback.rating}
            onChange={(event) => onChange('rating', Number(event.target.value))}
            className="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none transition focus:border-brand-500"
          />
        </label>
      </div>

      <label className="mt-4 block text-sm font-medium text-slate-700">
        Comment
        <textarea
          rows="4"
          value={feedback.comment}
          onChange={(event) => onChange('comment', event.target.value)}
          placeholder="What was useful, where was the bottleneck, and what should improve?"
          className="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none transition focus:border-brand-500"
        />
      </label>

      <div className="mt-5 flex flex-wrap items-center gap-3">
        <button
          type="button"
          onClick={onSubmit}
          disabled={loading}
          className="rounded-2xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-accent-600 disabled:cursor-not-allowed disabled:opacity-70"
        >
          {loading ? 'Saving...' : 'Save feedback'}
        </button>
        {successMessage && <span className="text-sm text-emerald-700">{successMessage}</span>}
      </div>
    </section>
  );
}
