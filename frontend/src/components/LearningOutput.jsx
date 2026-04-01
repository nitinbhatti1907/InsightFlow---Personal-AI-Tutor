import SectionCard from './SectionCard';
import ResourceList from './ResourceList';

export default function LearningOutput({
  content,
  onContinue,
  onMarkRead,
  continueLoading,
  markReadLoading,
  isTopicRead,
  actionMessage,
}) {
  if (!content) {
    return (
      <section className="card-surface overflow-hidden p-8">
        <div className="rounded-[1.75rem] border border-slate-200 bg-gradient-to-r from-slate-50 via-white to-blue-50 p-6">
          <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">
            InsightFlow lesson space
          </p>
          <h2 className="mt-2 text-2xl font-semibold text-slate-900">
            Your lesson will appear here
          </h2>
          <p className="mt-4 max-w-3xl text-sm leading-8 text-slate-600">
            Start a topic to unlock a guided explanation, key concepts,
            examples, recommended resources, and a built-in quiz session.
          </p>
        </div>
      </section>
    );
  }

  return (
    <div className="space-y-6">
      <section className="card-surface p-6 lg:p-8">
        <div className="flex flex-wrap items-start justify-between gap-4">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">
              InsightFlow lesson
            </p>
            <h2 className="mt-2 text-3xl font-semibold text-slate-900">
              {content.topic_title}
            </h2>
          </div>

          <div className="flex flex-wrap gap-2">
            <span className="rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-600 shadow-sm">
              Live lesson
            </span>
            {content.matched_from_query ? (
              <span className="rounded-full border border-brand-100 bg-brand-50 px-4 py-2 text-sm font-medium text-brand-700 shadow-sm">
                Matched from: {content.matched_from_query}
              </span>
            ) : null}
          </div>
        </div>

        <div className="mt-5 rounded-3xl border border-brand-100 bg-gradient-to-r from-brand-50 to-blue-50 p-5 text-sm leading-8 text-slate-700">
          {content.focus_message}
        </div>

        <div className="mt-6 grid gap-4 lg:grid-cols-2">
          {content.sections.map((section) => (
            <SectionCard key={section.title} section={section} />
          ))}
        </div>

        <div className="mt-6 rounded-3xl border border-slate-200 bg-gradient-to-r from-slate-50 to-white p-5 shadow-sm">
          <div className="flex flex-col gap-5 lg:flex-row lg:items-center lg:justify-between">
            <div className="flex items-start gap-4">
              <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-900 text-xl text-white shadow-sm">
                →
              </div>

              <div>
                <p className="text-sm font-semibold uppercase tracking-[0.18em] text-slate-500">
                  Continue with InsightFlow
                </p>
                <p className="mt-3 text-sm leading-8 text-slate-700">
                  {content.next_step_prompt}
                </p>

                {actionMessage && (
                  <div className="mt-4 rounded-2xl border border-emerald-100 bg-emerald-50 px-4 py-3 text-sm text-emerald-700">
                    {actionMessage}
                  </div>
                )}
              </div>
            </div>

            <div className="flex flex-wrap gap-3">
              <button
                type="button"
                onClick={onContinue}
                disabled={continueLoading}
                className="rounded-2xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white shadow-sm transition hover:-translate-y-0.5 hover:bg-brand-600 disabled:cursor-not-allowed disabled:opacity-70"
              >
                {continueLoading ? 'Opening...' : 'Open Learn More'}
              </button>

              <button
                type="button"
                onClick={onMarkRead}
                disabled={markReadLoading || isTopicRead}
                className="rounded-2xl border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 shadow-sm transition hover:-translate-y-0.5 hover:border-emerald-300 hover:bg-emerald-50 hover:text-emerald-700 disabled:cursor-not-allowed disabled:opacity-70"
              >
                {isTopicRead
                  ? 'Marked as Read'
                  : markReadLoading
                  ? 'Saving...'
                  : 'Mark as Read'}
              </button>
            </div>
          </div>
        </div>
      </section>

      <ResourceList resources={content.resource_summaries} />
    </div>
  );
}