import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
	{
		path: '/',
		name: 'main',
		component: () => import('@/views/MainPage.vue'),
	},
	{
		path: '/location',
		name: 'location',
		component: () => import('@/views/LocationPage.vue'),
	},
	{
		path: '/profile',
		name: 'profile',
		component: () => import('@/views/accounts/ProfilePage.vue'),
	},
	{
		path: '/search',
		name: 'search',
		component: () => import('@/views/search/SearchPage.vue'),
		children: [
			{
				path: 'result',
				name: 'searchResult',
				component: () => import('@/components/SearchResult.vue'),
			},
		],
	},
	{
		path: '/course',
		name: 'course',
		component: () => import('@/views/course/CoursePage.vue'),
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
