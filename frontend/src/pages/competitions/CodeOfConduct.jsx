import { Header } from '@/components/Header.jsx';
import { MainContent } from '@/components/MainContent';
import { Footer } from '@/components/Footer.jsx';

function FIXME() {
  return (
    <span class="text-red-500">FIXME:</span>
  );
}

export function CodeOfConduct({ ...props }) {
  return (
    <>
      <Header />

      <MainContent>
        <h1 class="text-5xl font-bold mb-8">Code of Conduct</h1>

        <div class="mb-4">
          <p>
            The Django Dash is a community event, and as such, our expectation
            is that anyone who wishes to participate in the Django Dash should
            be willing to engage with others in good faith & as a reasonable
            human being.
          </p>

          <p>
            To that end, we're adopting the same{' '}
            <a href="https://www.djangoproject.com/conduct/">
              Code of Conduct
            </a> as Django itself.
          </p>

          <p>
            These rules apply to <strong>ALL</strong> aspects of the Dash,
            including but <i>not limited to</i>: user profiles, team information, the
            entries themselves, and communications on Discord. For clarity, the
            basic rules are repeated here:
          </p>

          <ol
            class="block list-decimal ml-8 mb-8"
          >
            <li class="font-bold">Be friendly and patient.</li>
            <li class="font-bold">Be welcoming.</li>
            <li class="font-bold">Be considerate.</li>
            <li class="font-bold">Be respectful.</li>
            <li class="font-bold">Be careful in the words that you choose.</li>
            <li class="font-bold">When we disagree, try to understand why.</li>
          </ol>

          <p>
            Anyone are unable or unwilling to follow these rules may be
            subject to immediate removal from participation, and/or have their
            entries disqualified from judging. If you believe someone is
            violating the code of conduct, please contact{' '}
            <a href="mailto:info@djangodash.com">info@djangodash.com</a>.
          </p>
        </div>
      </MainContent>

      <Footer />
    </>
  );
}
