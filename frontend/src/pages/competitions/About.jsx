import { Header } from '@/components/Header.jsx';
import { MainContent } from '@/components/MainContent';
import { Footer } from '@/components/Footer.jsx';

export function About() {
  return (
    <>
      <Header />

      <MainContent>
        <h1 class="text-5xl font-bold mb-8">About</h1>

        <section>
          <p>
            The Django Dash is
          </p>
        </section>
      </MainContent>

      <Footer />
    </>
  );
}
