export function Header({ ...props }) {
  return (
    <header class="w-full py-8 bg-cyan-700">
      <div
        class="center-column flex flex-row text-neutral-100"
      >
        <div class="shrink-0 grow w-64 mr-8">
          <a href="/">
            <img
              src="/img/stopwatch.png"
              alt="Django Dash"
              class="inline-block h-16 mr-2"
            />
          </a>
          <a href="/">
            <img
              src="/img/django_dash.png"
              alt="Django Dash"
              class="inline-block h-16"
            />
          </a>
        </div>

        <div
          class="text-right mt-6"
        >
          <span>
            <a href="/login/">Login</a>{' '}
            ...or...{' '}
            <a href="/signup/">Sign Up</a>
          </span>
        </div>
      </div>
    </header>
  );
}
