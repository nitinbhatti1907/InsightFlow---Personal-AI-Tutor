const learningStyles = [
  { value: 'visual', label: 'Visual learner' },
  { value: 'hands-on', label: 'Hands-on learner' },
  { value: 'reading', label: 'Reading-focused' },
  { value: 'exam-prep', label: 'Exam preparation' },
];

const levels = [
  { value: 'beginner', label: 'Beginner' },
  { value: 'intermediate', label: 'Intermediate' },
  { value: 'advanced', label: 'Advanced' },
];

const detailModes = [
  { value: 'quick', label: 'Quick' },
  { value: 'standard', label: 'Standard' },
  { value: 'deep', label: 'Deep dive' },
];

const OTHER_TOPIC_ID = 'others';

export default function TopicExplorer({
  topics,
  form,
  onChange,
  onGenerate,
  loading,
  error,
}) {
  const isOtherSelected = form.topic_id === OTHER_TOPIC_ID;

  return (
    <section className="card-surface relative overflow-hidden p-6 lg:p-8">
      <div className="absolute right-10 top-8 h-28 w-28 rounded-full bg-blue-100/40 blur-3xl" />
      <div className="absolute bottom-8 left-10 h-28 w-28 rounded-full bg-violet-100/40 blur-3xl" />

      <div className="relative flex items-start justify-between gap-4">
        <div>
          <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">
            Start a learning session
          </p>
          <h2 className="mt-2 text-2xl font-semibold text-slate-900">
            Build your next lesson in InsightFlow
          </h2>
          <p className="mt-2 max-w-3xl text-sm leading-7 text-slate-600">
            Choose a guided topic or switch to Others for a custom request
            related to Data Analysis with Python.
          </p>
        </div>

        <div className="hidden rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-600 shadow-sm lg:block">
          <span className="font-semibold text-slate-900">{topics.length}</span>{' '}
          curated topics
        </div>
      </div>

      <div className="relative mt-6 grid gap-6 lg:grid-cols-2">
        <div className="space-y-4">
          <label className="block text-sm font-medium text-slate-700">
            Topic
            <select
              value={form.topic_id}
              onChange={(event) => {
                const nextValue = event.target.value;
                onChange('topic_id', nextValue);
                if (nextValue !== OTHER_TOPIC_ID) {
                  onChange('topic_query', '');
                }
              }}
              className="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-4 text-sm shadow-sm outline-none ring-0 transition focus:border-brand-500"
            >
              {topics.map((topic) => (
                <option key={topic.id} value={topic.id}>
                  {topic.title}
                </option>
              ))}
              <option value={OTHER_TOPIC_ID}>Others</option>
            </select>
          </label>

          <label className="block text-sm font-medium text-slate-700">
            Search by your own words
            <input
              value={form.topic_query}
              onChange={(event) => onChange('topic_query', event.target.value)}
              disabled={!isOtherSelected}
              placeholder={
                isOtherSelected
                  ? 'Example: missing values, groupby, seaborn boxplot, pivot table'
                  : 'Select Others to type your own topic'
              }
              className="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-4 text-sm shadow-sm outline-none transition focus:border-brand-500 disabled:cursor-not-allowed disabled:bg-slate-100 disabled:text-slate-400"
            />
          </label>

          <div className="rounded-3xl border border-brand-100 bg-gradient-to-r from-brand-50 to-blue-50 px-5 py-4 text-sm leading-7 text-slate-700">
            <span className="font-semibold text-slate-900">InsightFlow tip:</span>{' '}
            the custom field activates only when you choose{' '}
            <span className="font-semibold text-slate-900">Others</span>. Keep
            requests focused on Data Analysis with Python topics.
          </div>
        </div>

        <div className="grid gap-4 sm:grid-cols-2">
          <label className="block text-sm font-medium text-slate-700">
            Level
            <select
              value={form.proficiency_level}
              onChange={(event) =>
                onChange('proficiency_level', event.target.value)
              }
              className="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-4 text-sm shadow-sm outline-none transition focus:border-brand-500"
            >
              {levels.map((level) => (
                <option key={level.value} value={level.value}>
                  {level.label}
                </option>
              ))}
            </select>
          </label>

          <label className="block text-sm font-medium text-slate-700">
            Detail depth
            <select
              value={form.detail_mode}
              onChange={(event) => onChange('detail_mode', event.target.value)}
              className="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-4 text-sm shadow-sm outline-none transition focus:border-brand-500"
            >
              {detailModes.map((mode) => (
                <option key={mode.value} value={mode.value}>
                  {mode.label}
                </option>
              ))}
            </select>
          </label>

          <label className="block text-sm font-medium text-slate-700 sm:col-span-2">
            Learning style
            <select
              value={form.learning_style}
              onChange={(event) => onChange('learning_style', event.target.value)}
              className="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-4 text-sm shadow-sm outline-none transition focus:border-brand-500"
            >
              {learningStyles.map((style) => (
                <option key={style.value} value={style.value}>
                  {style.label}
                </option>
              ))}
            </select>
          </label>
        </div>
      </div>

      {error && (
        <div className="relative mt-5 rounded-2xl border border-rose-200 bg-rose-50 px-4 py-3 text-sm text-rose-700">
          {error}
        </div>
      )}

      <div className="relative mt-6 flex flex-wrap items-center gap-4">
        <label className="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2 text-sm text-slate-600 shadow-sm">
          <input
            type="checkbox"
            checked={form.include_resources}
            onChange={(event) =>
              onChange('include_resources', event.target.checked)
            }
          />
          Include resource summaries
        </label>

        <label className="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2 text-sm text-slate-600 shadow-sm">
          <input
            type="checkbox"
            checked={form.include_quiz}
            onChange={(event) => onChange('include_quiz', event.target.checked)}
          />
          Include quiz
        </label>

        <button
          type="button"
          onClick={onGenerate}
          disabled={loading || (isOtherSelected && !form.topic_query.trim())}
          className="ml-auto rounded-2xl bg-slate-900 px-7 py-3.5 text-sm font-semibold text-white shadow-lg transition hover:-translate-y-0.5 hover:bg-brand-600 disabled:cursor-not-allowed disabled:opacity-70"
        >
          {loading ? 'Building lesson...' : 'Generate content'}
        </button>
      </div>
    </section>
  );
}