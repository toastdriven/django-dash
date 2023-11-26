import { Header } from '@/components/Header.jsx';
import { MainContent } from '@/components/MainContent';
import { Footer } from '@/components/Footer.jsx';

export function Sponsors() {
  return (
    <>
      <Header />

      <MainContent>
        <h1 class="text-5xl font-bold mb-8">Sponsors</h1>

        <p>
          None yet. If you'd like to sponsor this year's competition, please{' '}
          <a href="mailto:daniel@toastdriven.com">email me</a>!
        </p>
      </MainContent>

      <Footer />
    </>
  );
}
