module.exports = {
	name: 'TsDemo',
	publisher: 'Sample',
	cards: [
		{
			type: 'TsDemoCard',
			source: './src/cards/TsDemoCard',
			title: 'TsDemo Card',
			displayCardType: 'TsDemo Card',
			description:
				'This is an introductory card to the Ellucian Experience SDK',
			pageRoute: {
				route: '/',
				excludeClickSelectors: ['a'],
			},
		},
	],
	page: {
		source: './src/page/router.jsx',
	},
};
