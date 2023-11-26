import { Header } from '@/components/Header.jsx';
import { MainContent } from '@/components/MainContent';
import { Footer } from '@/components/Footer.jsx';

function FIXME() {
  return (
    <span class="text-red-500">FIXME:</span>
  );
}

export function Rules({ year, ...props }) {
  return (
    <>
      <Header />

      <MainContent>
        <h1 class="text-5xl font-bold mb-8">Rules</h1>

        <div class="mb-4">
          <p>
            We want the Dash to be fun and for everyone to have a good time. To
            help this and to make the expectations clear, we&rsquo;ve got eight
            simple rules for the competition. Without further ado, they are:
          </p>

          <ol
            class="block list-decimal ml-8 mb-8"
          >
            <li>Majority in Django</li>
            <li>Nothing Gets Built Ahead Of Time</li>
            <li>48 Hours To Build</li>
            <li>Max Team Of 3</li>
            <li>Git for Version Control</li>
            <li>Your Entry Is Open Source</li>
            <li>Third Party Allowances</li>
            <li>Deployment</li>
          </ol>
        </div>

        <div class="mb-4">
          <dl>
            <dt class="font-bold text-lg">Majority in Django</dt>
            <dd class="mb-4">
              You can leverage other tools, but ~50% of your project ought to be
              in <a href="https://djangoproject.com/">Django</a>.
              We won't count the lines, but if you're not using
              Django, it's not really the <em>Django Dash</em> is it?
            </dd>

            <dt class="font-bold text-lg">Nothing Gets Built Ahead Of Time</dt>
            <dd class="mb-4">
              Ideas and/or pencil &amp; paper (not digital) mockups ONLY before
              the competition. <strong>NO CODE.</strong>
            </dd>

            <dt class="font-bold text-lg">48 Hours To Build</dt>
            <dd class="mb-4">
              Starts on <FIXME /> UTC
              and ends 48 hours later on <FIXME /> UTC.
              Anything submitted outside of that timeframe will be
              ignored during the judging.
            </dd>

            <dt class="font-bold text-lg">Max Team Of 3</dt>
            <dd class="mb-4">
              You and up to two other cohorts.
            </dd>

            <dt class="font-bold text-lg">Git for Version Control</dt>
            <dd class="mb-4">
              Please use <a href="https://git-scm.com/">Git</a> for version
              control. Ideally, you host your project on GitHub or GitLab, so
              your project is visible and you can easily setup the webhooks to
              talk to the Django Dash site. Instructions will
              be provided.
            </dd>

            <dt class="font-bold text-lg">Your Entry Is Open Source</dt>
            <dd class="mb-4">
              To help with the judging process, all entries must be open-source.
              This removes questions about judging code quality
              <strong>AND</strong> it's good for the community.
            </dd>

            <dt class="font-bold text-lg">Third Party Allowances</dt>
            <dd class="mb-4">
              You may use any third party sources (Python modules/Django apps/etc)
              you wish. But be warned that the less code you write, the worse your
              judging score will be. The point is that you should build an app/site,
              not just tie a couple things together.
            </dd>

            <dt class="font-bold text-lg"><FIXME /> Deployment</dt>
            <dd class="mb-4">
              ...
            </dd>
          </dl>
        </div>

        <div>
          <h3 class="text-xl font-bold">Other Questions?</h3>

          <p>
            Anything that's not strictly a rule of the competition can be found
            on our <a href="/faq/" title="FAQ">FAQ</a> page, so you may
            want to give that a glance.
          </p>
        </div>
      </MainContent>

      <Footer />
    </>
  );
}
