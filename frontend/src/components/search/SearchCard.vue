<template>
	<section>
		<!-- 클릭시 여행지 상세 페이지로 이동 -->
		<v-card v-ripple class="search-card">
			<v-img class="search-card-img" :src="searchImg" />

			<v-card-title class="search-card-title">
				{{ searchTitle }}
			</v-card-title>

			<v-card-text class="search-card-rating">
				<v-rating
					v-model="searchRating"
					background-color="grey"
					color="yellow accent-4"
					size="18"
					readonly
					dense
				/>
			</v-card-text>
		</v-card>

		<!-- <article>
      검색 결과가 없습니다.
    </article> -->
	</section>
</template>

<script>
export default {
	data() {
		return {
			searchTitle: '낙동강 체육공원', // 여행지 제목
			searchImg: 'https://picsum.photos/300', // 여행지 사진
			searchRating: 4, // 여행지 별점
		};
	},
};
</script>

<style lang="scss" scoped>
.search-card {
	margin: 0px auto;
	width: 98%;
	height: 260px;
	margin-top: 12px;

	.search-card-img {
		height: 180px;
		width: 100%;
	}
	.search-card-title {
		font-size: 17px;
		font-weight: bold;
		padding: 8px 15px 0px;
	}
	.search-card-rating {
		padding-bottom: 0px;
	}
}
</style>
