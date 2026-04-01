const accentClasses = {
  primary:
    'border-blue-100 bg-gradient-to-br from-blue-50 to-cyan-50 text-blue-700',
  secondary:
    'border-violet-100 bg-gradient-to-br from-violet-50 to-fuchsia-50 text-violet-700',
  success:
    'border-emerald-100 bg-gradient-to-br from-emerald-50 to-teal-50 text-emerald-700',
  warning:
    'border-amber-100 bg-gradient-to-br from-amber-50 to-yellow-50 text-amber-700',
  danger:
    'border-rose-100 bg-gradient-to-br from-rose-50 to-pink-50 text-rose-700',
  info: 'border-slate-200 bg-gradient-to-br from-slate-50 to-white text-slate-700',
};

const iconMap = {
  primary: '◈',
  secondary: '✦',
  success: '✓',
  warning: '⚑',
  danger: '!',
  info: '•',
};

export default function SectionCard({ section }) {
  const accent = section.accent || 'info';
  const theme = accentClasses[accent] || accentClasses.info;
  const icon = iconMap[accent] || iconMap.info;

  return (
    <article
      className={`group overflow-hidden rounded-3xl border p-6 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-lg ${theme}`}
    >
      <div className="flex items-start gap-4">
        <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-white/80 text-lg font-bold shadow-sm">
          {icon}
        </div>

        <div className="min-w-0">
          <h3 className="text-xl font-semibold text-slate-900">{section.title}</h3>
          <p className="mt-4 text-sm leading-8 text-slate-700">{section.body}</p>

          {section.bullets?.length > 0 && (
            <ul className="mt-5 space-y-3 text-sm text-slate-700">
              {section.bullets.map((bullet) => (
                <li key={bullet} className="flex items-start gap-3">
                  <span className="mt-2 h-2.5 w-2.5 rounded-full bg-slate-900" />
                  <span>{bullet}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </article>
  );
}