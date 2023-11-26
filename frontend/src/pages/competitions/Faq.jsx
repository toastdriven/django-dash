import { Header } from '@/components/Header.jsx';
import { MainContent } from '@/components/MainContent';
import { Footer } from '@/components/Footer.jsx';

function FIXME() {
  return (
    <span class="text-red-500">FIXME:</span>
  );
}

export function Faq({ year, ...props }) {
  return (
    <>
      <Header />

      <MainContent>
        <h1 class="text-3xl font-bold mb-8">(In)Frequently Asked Questions</h1>

        <h3 class="text-xl font-bold mb-4">What can I do ahead of time?</h3>

        <p class="mb-8">
          As stated in the rules, only generating ideas or paper mockups can be
          done before the official start of the competition.
        </p>

        <h3 class="text-xl font-bold mb-4">What happens if I&rsquo;m not going to finish in time?</h3>

        <p class="mb-4">
          Check in your code! Each team will have to provide a breakdown of what
          works/doesn&rsquo;t work at the end of the competition anyhow, so if
          anything works, we can judge based on that.
        </p>

        <p class="mb-4">
          &#8220;Better to have coded and lost than to have never coded at all&#8230;&#8221;
        </p>

        <p class="mb-8">
          (We apologize. The FAQ writer has been sacked and has being
          replaced with one who has experience with{' '}
          <a href="https://www.youtube.com/watch?v=djKPvXDwXcs">møøses</a>.)
        </p>

        <h3 class="text-xl font-bold mb-4">Can I outsource any part of this?</h3>

        <p class="mb-8">
          No. It has to be your own work.
        </p>

        <h3 class="text-xl font-bold mb-4">Who owns the code/media I produce?</h3>

        <p class="mb-8">
          You do, we don't. If you want keep it and turn it into a real, sale-able
          web app, go for it. If you want to package it up and share it,
          please, by all means. And if you just want to bury it out of
          embarrassment and shame, we'll be happy to console you, tell you you're a
          great person anyhow and help shovel.
        </p>

        <h3 class="text-xl font-bold mb-4">The rules suck!</h3>

        <p class="mb-8">
          Sorry. We're always up for future improvement, but generally the rules
          stay as the are for the current competition.
        </p>

        <h3 class="text-xl font-bold mb-4">
          Isn&rsquo;t this just like Rails Day/Rails Rumble/PyWeek/etc.?
          How freaking unoriginal can you get?
        </h3>

        <p class="mb-4">
          If you think this is as unoriginal as we can get, clearly you
          don&rsquo;t know us very well. :D
        </p>

        <p class="mb-8">
          In all seriousness, the point wasn&rsquo;t originality, it&rsquo;s to
          have fun, and put a great challenge out there for the Django community.
          The general formula has existed for a very long time, and it&rsquo;s
          proven to have been a great time in the past. Combine that with the
          awesomeness that is <a href="https://djangoproject.com/">Django</a>,
          and this should be no different.
        </p>

        <h3 class="text-xl font-bold mb-4">What&rsquo;s in it for me?</h3>

        <p class="mb-8">
          A chance to strut your stuff in front of others. If we manage to find
          sponsors, maybe there will be prizes. To push your skills and discover
          just exactly where your limits are. And maybe, just maybe, have a
          great time in the process.
        </p>

        <h3 class="text-xl font-bold mb-4">What&rsquo;s in it for you?</h3>

        <p class="mb-8">
          Nothing really. It's mostly a labor of love. It costs me money to
          host, time to build, time to organize, a big chunk of time for
          judging, and worst of all, I can't enter the competition myself.
          There's no profits, nothing from sponsors, etc.
        </p>

        <h3 class="text-xl font-bold mb-4">What is fun?</h3>

        <p class="mb-8">
          You&rsquo;re hopeless.
        </p>

        <h3 class="text-xl font-bold mb-4">
          I don&rsquo;t think anyone actually asked these questions.
          Are you just making this all up?
        </h3>

        <p class="mb-8">
          Maybe. See &#8220;What is fun&#8221; for details.
        </p>
      </MainContent>

      <Footer />
    </>
  );
}
