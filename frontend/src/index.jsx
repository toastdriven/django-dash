import { render } from 'preact';
import { LocationProvider, Router, Route } from 'preact-iso';

import { Home } from '@/pages/Home.jsx';
import { CodeOfConduct } from '@/pages/competitions/CodeOfConduct.jsx';
import { Faq } from '@/pages/competitions/Faq.jsx';
import { Rules } from '@/pages/competitions/Rules.jsx';
import { Sponsors } from '@/pages/competitions/Sponsors.jsx';
import { About } from '@/pages/competitions/About.jsx';
import { NotFound } from '@/pages/_404.jsx';

import './style.css';

export function App() {
  return (
    <LocationProvider>
      <main>
        <Router>
          <Route path="/" component={Home} />

          <Route path="/faq/" component={Faq} />
          <Route path="/code-of-conduct/" component={CodeOfConduct} />

          <Route path="/:year/rules/" component={Rules} />
          <Route path="/:year/sponsors/" component={Sponsors} />
          <Route path="/:year/about/" component={About} />

          {/* <Route path="/archive/:year/" component={Rules} /> */}

          <Route default component={NotFound} />
        </Router>
      </main>
    </LocationProvider>
  );
}

render(<App />, document.getElementById('app'));
