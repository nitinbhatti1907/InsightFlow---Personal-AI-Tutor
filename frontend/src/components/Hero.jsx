export default function Hero({ overview }) {
  const highlights = [
    'Personalized lesson flow',
    'Curated reading suggestions',
    'Quiz-driven practice',
  ];

  const fitCards = [
    {
      title: 'Focused learning experience',
      body: 'InsightFlow is purpose-built for Data Analysis with Python, so every session stays relevant, practical, and easy to navigate.',
      icon: '◎',
      tone: 'from-blue-50 to-cyan-50 border-blue-100',
    },
    {
      title: 'Fresh explanations on demand',
      body: 'Learners can open a topic, get a clear explanation, review trusted resources, and continue into guided practice without leaving the workspace.',
      icon: '✦',
      tone: 'from-emerald-50 to-teal-50 border-emerald-100',
    },
    {
      title: 'Built for progress tracking',
      body: 'Every learning session, quiz attempt, and follow-up action is stored in one place, helping learners and educators see momentum over time.',
      icon: '↗',
      tone: 'from-violet-50 to-fuchsia-50 border-violet-100',
    },
  ];

  return (
    <section className="relative overflow-hidden rounded-[2rem] border border-slate-200 bg-gradient-to-br from-slate-50 via-white to-indigo-50 p-8 shadow-soft lg:p-12">
      <div className="absolute -left-10 top-12 h-48 w-48 rounded-full bg-blue-100/70 blur-3xl" />
      <div className="absolute bottom-0 right-0 h-56 w-56 rounded-full bg-violet-100/70 blur-3xl" />
      <div className="absolute right-24 top-16 h-3 w-3 rounded-full bg-brand-500 shadow-[0_0_35px_rgba(37,99,235,0.6)]" />
      <div className="absolute left-1/2 top-10 h-2 w-2 rounded-full bg-emerald-400 shadow-[0_0_30px_rgba(16,185,129,0.55)]" />

      <div className="relative grid gap-8 lg:grid-cols-[1.5fr_0.8fr] lg:items-center">
        <div>
          <div className="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white/90 px-5 py-2 text-sm font-semibold text-slate-700 shadow-sm">
            <span className="text-brand-600">●</span>
            InsightFlow - Personal AI Tutor
          </div>

          <h1 className="mt-6 max-w-4xl text-4xl font-bold tracking-tight text-slate-900 lg:text-6xl">
            {overview?.title || 'Data Analysis with Python'}
          </h1>

          <p className="mt-5 max-w-4xl text-lg leading-8 text-slate-600">
            Learn faster with a guided workspace that turns one topic into a
            full learning session. InsightFlow delivers focused explanations,
            practical examples, curated resources, quiz practice, and progress
            tracking in one clean experience.
          </p>

          <div className="mt-8 flex flex-wrap gap-3">
            {highlights.map((item) => (
              <span
                key={item}
                className="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white/90 px-4 py-2 text-sm font-medium text-slate-700 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"
              >
                <span className="h-2 w-2 rounded-full bg-brand-500" />
                {item}
              </span>
            ))}
          </div>

          <div className="mt-8 grid gap-3 sm:grid-cols-3">
            <div className="rounded-3xl border border-slate-200 bg-white/80 p-4 shadow-sm">
              <p className="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">
                Active scope
              </p>
              <p className="mt-2 text-lg font-semibold text-slate-900">
                One course, zero noise
              </p>
            </div>

            <div className="rounded-3xl border border-slate-200 bg-white/80 p-4 shadow-sm">
              <p className="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">
                Resource flow
              </p>
              <p className="mt-2 text-lg font-semibold text-slate-900">
                Explain, explore, practice
              </p>
            </div>

            <div className="rounded-3xl border border-slate-200 bg-white/80 p-4 shadow-sm">
              <p className="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">
                Coverage
              </p>
              <p className="mt-2 text-lg font-semibold text-slate-900">
                {overview?.topic_count || 6} curated topic tracks
              </p>
            </div>
          </div>
        </div>

        <div className="rounded-[2rem] border border-slate-200 bg-white/85 p-6 shadow-xl backdrop-blur">
          <div className="flex items-center justify-between gap-3">
            <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">
              Why InsightFlow
            </p>
            <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-600">
              Launch-ready
            </span>
          </div>

          <div className="mt-5 space-y-4">
            {fitCards.map((item) => (
              <div
                key={item.title}
                className={`rounded-3xl border bg-gradient-to-br p-4 ${item.tone}`}
              >
                <div className="flex items-start gap-4">
                  <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-white/80 text-lg font-bold text-slate-800 shadow-sm">
                    {item.icon}
                  </div>
                  <div>
                    <p className="text-lg font-semibold text-slate-900">
                      {item.title}
                    </p>
                    <p className="mt-2 text-sm leading-7 text-slate-600">
                      {item.body}
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}