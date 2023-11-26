export function Footer({ ...props }) {
  const today = new Date();
  const currentYear = today.getFullYear();

  return (
    <footer class="w-full py-8 bg-stone-600">
      <div
        class="center-column text-stone-200 text-sm"
      >
        <nav
          class="mb-4 grid grid-cols-4 gap-4"
        >
          <div>
            <dl>
              <dt class="font-bold text-base mb-2">Competition</dt>
              <dd>
                <a href="/">Home</a>
              </dd>
              <dd>
                <a href={`/${currentYear}/rules/`}>Rules</a>
              </dd>
              <dd>
                <a href={`/${currentYear}/sponsors/`}>Sponsors</a>
              </dd>
              <dd>
                <a href={`/${currentYear}/about/`}>About</a>
              </dd>
              <dd>
                <a href={`/faq/`}>FAQ</a>
              </dd>
              <dd>
                <a href="https://github.com/toastdriven/django-dash">Source on GitHub</a>
              </dd>
            </dl>
          </div>

          <div>
            <dl>
              <dt class="font-bold text-base mb-2">Archives</dt>
              <dd>
                2013
              </dd>
              <dd>
                2012
              </dd>
              <dd>
                2011
              </dd>
              <dd>
                2010
              </dd>
              <dd>
                2009
              </dd>
              <dd>
                2008
              </dd>
            </dl>
          </div>

          <div>

          </div>

          <div>
            <dl>
              <dt class="font-bold text-base mb-2">Social</dt>
              <dd>
                <a rel="me" href="https://hachyderm.io/@djangodash">Mastodon</a>
              </dd>
            </dl>
          </div>
        </nav>

        <div
          class="mb-4 flex flex-row gap-2"
        >
          {/* FIXME: Sponsor Logos! */}
        </div>

        <div
          class="text-center"
        >
          <div class="mb-2">
            Copyright 2008&mdash;{currentYear}
          </div>

          <div>
            A{' '}
            <a
              href="https://toastdriven.com/"
              class="toasty"
            >
              <img
                src="/img/tiny_toast.png"
                alt="Toast Driven"
                class="inline-block align-text-bottom mr-1"
              />
              Toast Driven
            </a>{' '}
            production
          </div>
        </div>
      </div>
    </footer>
  );
}
