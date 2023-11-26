import * as path from 'path';
import { defineConfig } from 'vite';

import preact from '@preact/preset-vite';
import alias from '@rollup/plugin-alias';

const projectRootDir = path.resolve(__dirname);

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    preact(),
    alias({
      entries: [
        { find: '@', replacement: path.resolve(projectRootDir, 'src') },
      ]
    })
  ],
});
