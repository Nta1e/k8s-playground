export default {
	purge: ['./src/**/*.svelte', './src/**/*.css'],
	content: ['./src/routes/**/*.{svelte,js,ts}'],
	plugins: [require('daisyui')]
};
