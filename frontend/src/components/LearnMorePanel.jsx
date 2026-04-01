import SectionCard from './SectionCard';

export default function LearnMorePanel({ data, onOpen, loading }) {
  return (
    <section id="learn-more-panel" className="card-surface p-6">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">
            Deepen this lesson
          </p>
          <h3 className="mt-2 text-xl font-semibold text-slate-900">
            Continue in InsightFlow
          </h3>
          <p className="mt-2 text-sm leading-7 text-slate-600">
            Open the extended lesson to unlock advanced notes, a mini-project,
            and reflection prompts.
          </p>
        </div>

        <button
          type="button"
          onClick={onOpen}
          disabled={loading}
          className="rounded-2xl border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-900 shadow-sm transition hover:-translate-y-0.5 hover:border-brand-500 hover:text-brand-600 disabled:cursor-not-allowed disabled:opacity-70"
        >
          {loading ? 'Opening...' : 'Open Learn More'}
        </button>
      </div>

      {!data ? (
        <div className="mt-5 rounded-3xl border border-slate-200 bg-gradient-to-br from-slate-50 to-white p-5 text-sm leading-8 text-slate-600">
          InsightFlow keeps every lesson expandable. Once the first explanation
          is ready, learners can continue into deeper notes, a hands-on
          mini-project, and reflection-based review.
        </div>
      ) : (
        <div className="mt-6 space-y-5">
          <div className="grid gap-4 lg:grid-cols-2">
            {data.deeper_sections.map((section) => (
              <SectionCard key={section.title} section={section} />
            ))}
          </div>

          <div className="rounded-3xl border border-emerald-100 bg-gradient-to-br from-emerald-50 to-teal-50 p-5 shadow-sm">
            <div className="flex items-start gap-4">
              <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-white/80 text-xl shadow-sm">
                ⚙
              </div>
              <div>
                <p className="text-lg font-semibold text-slate-900">
                  Mini-project
                </p>
                <p className="mt-3 text-sm leading-8 text-slate-700">
                  {data.mini_project}
                </p>
              </div>
            </div>
          </div>

          <div className="rounded-3xl border border-violet-100 bg-gradient-to-br from-violet-50 to-fuchsia-50 p-5 shadow-sm">
            <div className="flex items-start gap-4">
              <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-white/80 text-xl shadow-sm">
                ?
              </div>
              <div className="min-w-0">
                <p className="text-lg font-semibold text-slate-900">
                  Reflection prompts
                </p>

                <ul className="mt-4 space-y-3 text-sm text-slate-700">
                  {data.reflection_questions.map((question) => (
                    <li key={question} className="flex items-start gap-3">
                      <span className="mt-2 h-2.5 w-2.5 rounded-full bg-violet-600" />
                      <span>{question}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}