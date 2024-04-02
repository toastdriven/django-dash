import { Header } from '@/components/Header.jsx';
import { MainContent } from '@/components/MainContent';
import { Footer } from '@/components/Footer.jsx';

export function About() {
  return (
    <>
      <Header />

      <MainContent>
        <section class="mb-8">
          <h1 class="text-5xl font-bold mb-8">About</h1>

          <p>
            The Django Dash is a chance for Django enthusiasts to flex their
            coding skills a little, and put a fine point on
            <i>“perfectionists with deadlines”</i>
            by giving you a <strong>REAL</strong> deadline. 48 hours from start
            to stop to produce the best app you can and have a little fun in
            the process.
          </p>
        </section>

        <section class="mb-8">
          <h2 class="text-3xl font-bold mb-8">History</h2>

          <p>
            The Django Dash originally started in late 2007. At the time,
            interest in <a href="https://djangoproject.com/">Django</a>{' '}
            was taking off, with the (somewhat) recently
            released{' '}
            <a href="https://www.djangoproject.com/weblog/2007/mar/23/096/">0.96</a>{' '}
            version headlining some great new features.
          </p>

          <p>
            At the same time, <a href="https://rubyonrails.org/">Ruby on Rails</a>{' '}
            was exploding, & there were several competitions devoted to it. But
            nothing in the Django sphere.
          </p>

          <p>
            Fresh off of competing in a <a href="https://pyweek.org/">PyWeek</a>{' '}
            game programming compeition & hyped by everything happening in the
            Django community, <a href="https://toastdriven.com/">Daniel</a>{' '}
            created a competition called the "Django Dash".
          </p>

          <p>
            It was hosted yearly for several years (2008-2013), then life
            happened. As the Dash is an unpaid labor of love & judging is
            especially painful, it was backburned for many years.
          </p>

          <p>
            And now it returns for 2024! <code>:tada:</code>
          </p>
        </section>

        <section class="mb-8">
          <h2 class="text-3xl font-bold mb-8">Past Projects</h2>

          <p>
            Some notable projects found their beginnings as part of
            previously held Django Dashes, including:
          </p>

          <ul>
            <li>
              <a href="https://readthedocs.org/">Read The Docs</a>
            </li>
            <li>
              <a href="https://djangopackages.org/">Django Packages</a>
            </li>
            <li>
              <i>
                Missing your project? Please open a{' '}
                <a href="https://github.com/toastdriven/django-dash/pulls">Pull Request</a>!
              </i>
            </li>
          </ul>
        </section>
      </MainContent>

      <Footer />
    </>
  );
}
