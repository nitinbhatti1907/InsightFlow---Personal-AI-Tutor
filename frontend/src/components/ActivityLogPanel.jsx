import { useMemo, useState } from 'react';

function getActivityTheme(activityType = '') {
  const value = activityType.toLowerCase();

  if (value.includes('quiz')) {
    return {
      badge: 'bg-emerald-100 text-emerald-700 border-emerald-200',
      iconWrap: 'bg-emerald-500/10 text-emerald-600',
      dot: 'bg-emerald-500',
      stripe: 'from-emerald-500 to-teal-500',
    };
  }

  if (value.includes('learn')) {
    return {
      badge: 'bg-violet-100 text-violet-700 border-violet-200',
      iconWrap: 'bg-violet-500/10 text-violet-600',
      dot: 'bg-violet-500',
      stripe: 'from-violet-500 to-fuchsia-500',
    };
  }

  if (value.includes('mark_read') || value.includes('read')) {
    return {
      badge: 'bg-amber-100 text-amber-700 border-amber-200',
      iconWrap: 'bg-amber-500/10 text-amber-600',
      dot: 'bg-amber-500',
      stripe: 'from-amber-500 to-yellow-500',
    };
  }

  return {
    badge: 'bg-blue-100 text-blue-700 border-blue-200',
    iconWrap: 'bg-blue-500/10 text-blue-600',
    dot: 'bg-blue-500',
    stripe: 'from-blue-500 to-cyan-500',
  };
}

function getActivityIcon(activityType = '') {
  const value = activityType.toLowerCase();

  if (value.includes('quiz')) return '✓';
  if (value.includes('learn')) return '↗';
  if (value.includes('mark_read') || value.includes('read')) return '✓';
  return '✦';
}

function getFriendlyTitle(activityType = '') {
  const value = activityType.toLowerCase();

  if (value.includes('quiz')) return 'Quiz completed';
  if (value.includes('learn')) return 'Learn More opened';
  if (value.includes('mark_read') || value.includes('read')) return 'Marked as read';
  return 'Generated content';
}

function getActivityDescription(activity) {
  if (activity?.description && activity.description.trim()) {
    return activity.description;
  }

  if (activity?.detail && activity.detail.trim()) {
    return activity.detail;
  }

  const topic = activity?.topic_title || 'this topic';
  const type = (activity?.activity_type || '').toLowerCase();

  if (type.includes('quiz')) {
    return `You completed a quiz for ${topic}.`;
  }

  if (type.includes('learn')) {
    return `You opened deeper learning content for ${topic}.`;
  }

  if (type.includes('mark_read') || type.includes('read')) {
    return `You marked ${topic} as read and added it to your progress.`;
  }

  return `You generated a new InsightFlow lesson for ${topic}.`;
}

export default function ActivityLogPanel({ learnerOverview }) {
  const [showAll, setShowAll] = useState(false);

  const activities = useMemo(() => {
    return learnerOverview?.recent_activity || [];
  }, [learnerOverview]);

  const visibleActivities = showAll ? activities : activities.slice(0, 2);

  return (
    <section className="card-surface p-6 lg:p-8">
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">
            InsightFlow timeline
          </p>
          <h2 className="mt-2 text-2xl font-semibold text-slate-900">
            Your recent learning activity
          </h2>
        </div>

        <div className="rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-600 shadow-sm">
          Saved per account
        </div>
      </div>

      {activities.length === 0 ? (
        <div className="mt-6 rounded-3xl border border-dashed border-slate-200 bg-gradient-to-br from-slate-50 to-white px-6 py-10 text-sm leading-7 text-slate-500">
          Start your first InsightFlow lesson to build a visible learning
          timeline here.
        </div>
      ) : (
        <>
          <div
            className={`mt-6 space-y-4 ${showAll ? 'max-h-[560px] overflow-y-auto pr-2' : ''
              }`}
          >
            {visibleActivities.map((activity, index) => {
              const theme = getActivityTheme(activity.activity_type);
              const icon = getActivityIcon(activity.activity_type);

              return (
                <article
                  key={`${activity.created_at}-${activity.topic_title}-${index}`}
                  className="group relative overflow-hidden rounded-3xl border border-slate-200 bg-white p-5 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-lg"
                >
                  <div
                    className={`absolute left-0 top-0 h-full w-1.5 bg-gradient-to-b ${theme.stripe}`}
                  />

                  <div className="flex items-start justify-between gap-4">
                    <div className="flex min-w-0 items-start gap-4">
                      <div
                        className={`flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl ${theme.iconWrap} text-lg font-bold shadow-sm`}
                      >
                        {icon}
                      </div>

                      <div className="min-w-0">
                        <p
                          className={`inline-flex rounded-full border px-3 py-1 text-xs font-semibold uppercase tracking-[0.18em] ${theme.badge}`}
                        >
                          {getFriendlyTitle(activity.activity_type)}
                        </p>

                        <h3 className="mt-3 line-clamp-2 text-xl font-semibold text-slate-900">
                          {activity.topic_title || 'Untitled topic'}
                        </h3>
                      </div>
                    </div>

                    <span
                      className={`mt-1 h-3 w-3 shrink-0 rounded-full ${theme.dot}`}
                    />
                  </div>

                  <p className="mt-4 line-clamp-2 text-sm leading-7 text-slate-600">
                    {getActivityDescription(activity)}
                  </p>

                  <div className="mt-5 flex items-center justify-between gap-4">
                    <p className="text-sm font-semibold tracking-[0.12em] text-slate-400">
                      {activity.created_at
                        ? new Date(activity.created_at).toLocaleString('en-CA', {
                          timeZone: 'America/Toronto',
                          year: 'numeric',
                          month: 'numeric',
                          day: 'numeric',
                          hour: 'numeric',
                          minute: '2-digit',
                          second: '2-digit',
                          hour12: true,
                        })
                        : 'Recently'}
                    </p>

                    <div className="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-500 transition group-hover:bg-slate-900 group-hover:text-white">
                      InsightFlow event
                    </div>
                  </div>
                </article>
              );
            })}
          </div>

          {activities.length > 2 && (
            <div className="mt-6 flex justify-center">
              <button
                type="button"
                onClick={() => setShowAll((current) => !current)}
                className="rounded-2xl border border-slate-200 bg-white px-6 py-3 text-sm font-semibold text-slate-700 shadow-sm transition hover:border-brand-200 hover:bg-brand-50 hover:text-brand-700"
              >
                {showAll ? 'Show less' : 'More'}
              </button>
            </div>
          )}
        </>
      )}
    </section>
  );
}