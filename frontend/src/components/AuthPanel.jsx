export default function AuthPanel({ mode, form, onChange, onSubmit, onModeChange, loading, error }) {
  return (
    <section className="card-surface mx-auto max-w-5xl overflow-hidden">
      <div className="grid lg:grid-cols-[1.1fr_0.9fr]">
        <div className="bg-slate-900 px-8 py-10 text-white lg:px-10">
          <div className="badge border-white/20 bg-white/10 text-white">Personal learning assistant</div>
          <h1 className="mt-5 text-3xl font-bold tracking-tight lg:text-4xl">Learn Data Analysis with Python with a personal history and progress view</h1>
          <p className="mt-4 max-w-xl text-sm leading-7 text-slate-200">
            Create an account to save your generated topics, quiz completions, activity logs, and learning progress in one place.
          </p>
          <div className="mt-8 space-y-4 text-sm text-slate-200">
            <div className="rounded-2xl border border-white/10 bg-white/5 p-4">Track what you learned topic by topic</div>
            <div className="rounded-2xl border border-white/10 bg-white/5 p-4">See completed quizzes and your average score</div>
            <div className="rounded-2xl border border-white/10 bg-white/5 p-4">Measure progress toward the full course coverage</div>
          </div>
        </div>

        <div className="px-8 py-10 lg:px-10">
          <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">{mode === 'login' ? 'Welcome back' : 'Create account'}</p>
          <h2 className="mt-2 text-2xl font-semibold text-slate-900">
            {mode === 'login' ? 'Log in to continue learning' : 'Register your learner account'}
          </h2>

          {error ? (
            <div className="mt-4 rounded-2xl border border-rose-200 bg-rose-50 px-4 py-3 text-sm text-rose-700">{error}</div>
          ) : null}

          <div className="mt-6 space-y-4">
            {mode === 'register' ? (
              <label className="block text-sm font-medium text-slate-700">
                Full name
                <input
                  type="text"
                  value={form.full_name}
                  onChange={(event) => onChange('full_name', event.target.value)}
                  className="mt-2 w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm outline-none transition focus:border-brand-500"
                  placeholder="Enter your full name"
                />
              </label>
            ) : null}

            <label className="block text-sm font-medium text-slate-700">
              Email
              <input
                type="email"
                value={form.email}
                onChange={(event) => onChange('email', event.target.value)}
                className="mt-2 w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm outline-none transition focus:border-brand-500"
                placeholder="Enter your email"
              />
            </label>

            <label className="block text-sm font-medium text-slate-700">
              Password
              <input
                type="password"
                value={form.password}
                onChange={(event) => onChange('password', event.target.value)}
                className="mt-2 w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm outline-none transition focus:border-brand-500"
                placeholder="Minimum 6 characters"
              />
            </label>
          </div>

          <button
            type="button"
            onClick={onSubmit}
            disabled={loading}
            className="mt-6 w-full rounded-2xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-brand-600 disabled:cursor-not-allowed disabled:opacity-70"
          >
            {loading ? 'Please wait...' : mode === 'login' ? 'Log in' : 'Create account'}
          </button>

          <button
            type="button"
            onClick={() => onModeChange(mode === 'login' ? 'register' : 'login')}
            className="mt-4 text-sm font-medium text-brand-700 transition hover:text-brand-800"
          >
            {mode === 'login' ? 'Need an account? Register now' : 'Already have an account? Log in'}
          </button>
        </div>
      </div>
    </section>
  );
}
