export default function ResourceList({ resources }) {
  if (!resources?.length) {
    return null;
  }

  return (
    <section className="card-surface p-6 lg:p-8">
      <div className="flex items-center justify-between gap-4">
        <div>
          <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">
            Recommended reads
          </p>
          <h3 className="mt-2 text-2xl font-semibold text-slate-900">
            Curated resources for this lesson
          </h3>
        </div>
        <span className="rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-600 shadow-sm">
          {resources.length} resources
        </span>
      </div>

      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        {resources.map((resource, index) => (
          <a
            key={resource.url}
            href={resource.url}
            target="_blank"
            rel="noreferrer"
            className="group rounded-3xl border border-slate-200 bg-gradient-to-br from-white to-slate-50 p-5 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-lg"
          >
            <div className="flex items-start justify-between gap-4">
              <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-brand-50 text-brand-600 shadow-sm">
                {index + 1}
              </div>
              <span className="rounded-full border border-slate-200 bg-white px-3 py-1 text-xs font-semibold text-slate-600">
                {resource.type}
              </span>
            </div>

            <p className="mt-4 text-lg font-semibold text-slate-900 group-hover:text-brand-700">
              {resource.title}
            </p>

            <p className="mt-3 text-sm leading-7 text-slate-600">
              {resource.summary}
            </p>

            <div className="mt-5 inline-flex items-center gap-2 text-sm font-semibold text-brand-600">
              Open resource
              <span>↗</span>
            </div>
          </a>
        ))}
      </div>
    </section>
  );
}