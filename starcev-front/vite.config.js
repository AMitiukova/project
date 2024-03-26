import { defineConfig } from 'vite';
import inject from '@rollup/plugin-inject'

export default defineConfig({
    plugins: [
        inject({
            jQuery: 'jquery',
        }),
    ],
    build: {
        rollupOptions: {
            external: ['jquery'],
            output: {
                jquery: "jquery",
                $: "jquery",
                'window.jQuery': 'jquery'
            }
        }
    }
});