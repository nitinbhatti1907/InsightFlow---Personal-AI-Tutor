function StatCard({ label, value, icon, tone }) {
  return (
    <div
      className={`rounded-3xl border p-5 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-lg ${tone}`}
    >
      <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-white/80 text-lg shadow-sm">
        {icon}
      </div>
      <p className="mt-4 text-sm font-medium text-slate-500">{label}</p>
      <p className="mt-3 text-4xl font-bold text-slate-900">{value}</p>
    </div>
  );
}

export default function DashboardPanel({ dashboard, topicsMap }) {
  const stats = [
    {
      label: 'Feedback entries',
      value: dashboard?.total_feedback_entries ?? 0,
      icon: '✦',
      tone: 'border-blue-100 bg-gradient-to-br from-blue-50 to-cyan-50',
    },
    {
      label: 'Average rating',
      value: dashboard?.average_rating ?? 0,
      icon: '★',
      tone: 'border-amber-100 bg-gradient-to-br from-amber-50 to-yellow-50',
    },
    {
      label: 'Average quiz score',
      value: `${dashboard?.average_quiz_score ?? 0}%`,
      icon: '✓',
      tone: 'border-emerald-100 bg-gradient-to-br from-emerald-50 to-teal-50',
    },
  ];

  return (
    <section className="card-surface p-6 lg:p-8">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">
            InsightFlow educator view
          </p>
          <h2 className="mt-2 text-2xl font-semibold text-slate-900">
            Teaching insights at a glance
          </h2>
          <p className="mt-2 text-sm leading-7 text-slate-600">
            Track learner feedback, see which topics attract the most attention,
            and monitor quiz outcomes from one dashboard.
          </p>
        </div>

        <span className="rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-600 shadow-sm">
          Live workspace insights
        </span>
      </div>

      <div className="mt-6 grid gap-4 md:grid-cols-3">
        {stats.map((item) => (
          <StatCard key={item.label} {...item} />
        ))}
      </div>

      <div className="mt-6 grid gap-6 lg:grid-cols-[0.95fr_1.05fr]">
        <div className="rounded-3xl border border-slate-200 bg-gradient-to-br from-white to-slate-50 p-5 shadow-sm">
          <div className="flex items-center justify-between gap-3">
            <h3 className="text-xl font-semibold text-slate-900">
              Most requested topics
            </h3>
            <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-600">
              Demand view
            </span>
          </div>

          <div className="mt-4 space-y-3">
            {dashboard?.most_requested_topics?.length ? (
              dashboard.most_requested_topics.map((item, index) => (
                <div
                  key={item.topic_id}
                  className="flex items-center justify-between rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm shadow-sm"
                >
                  <div className="flex items-center gap-3">
                    <div className="flex h-8 w-8 items-center justify-center rounded-full bg-brand-50 text-sm font-semibold text-brand-700">
                      {index + 1}
                    </div>
                    <span className="font-medium text-slate-800">
                      {topicsMap[item.topic_id] || item.topic_id}
                    </span>
                  </div>

                  <span className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-xs font-semibold text-slate-600">
                    {item.requests} request(s)
                  </span>
                </div>
              ))
            ) : (
              <div className="rounded-2xl border border-dashed border-slate-200 bg-slate-50 px-4 py-5 text-sm leading-7 text-slate-600">
                Topic demand will appear here once learners begin saving
                feedback and exploring more lessons.
              </div>
            )}
          </div>
        </div>

        <div className="rounded-3xl border border-slate-200 bg-gradient-to-br from-white to-slate-50 p-5 shadow-sm">
          <div className="flex items-center justify-between gap-3">
            <h3 className="text-xl font-semibold text-slate-900">
              Recent learner notes
            </h3>
            <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-600">
              Latest feedback
            </span>
          </div>

          <div className="mt-4 space-y-3">
            {dashboard?.recent_feedback?.length ? (
              dashboard.recent_feedback.map((item, index) => (
                <div
                  key={`${item.learner_name}-${index}`}
                  className="rounded-2xl border border-slate-200 bg-white p-4 shadow-sm"
                >
                  <div className="flex flex-wrap items-center justify-between gap-3">
                    <span className="font-semibold text-slate-900">
                      {item.learner_name}
                    </span>
                    <span className="rounded-full border border-amber-100 bg-amber-50 px-3 py-1 text-xs font-semibold text-amber-700">
                      {item.rating}/5
                    </span>
                  </div>

                  <p className="mt-2 text-sm font-medium text-brand-700">
                    {topicsMap[item.topic_id] || item.topic_id}
                  </p>

                  <p className="mt-3 text-sm leading-7 text-slate-600">
                    {item.comment || 'Learner submitted a rating without a written note.'}
                  </p>
                </div>
              ))
            ) : (
              <div className="rounded-2xl border border-dashed border-slate-200 bg-slate-50 px-4 py-5 text-sm leading-7 text-slate-600">
                Learner notes will appear here as soon as feedback starts coming
                into InsightFlow.
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}