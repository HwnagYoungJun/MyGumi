<template>
	<header class="header-box">
		<img class="header-img" src="@/assets/images/tempLogo.png" alt="logo" />
		<i class="icon ion-md-notifications"></i>
	</header>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.header-box {
	display: flex;
	position: relative;
	margin-top: 16px;
	margin-bottom: 32px;
	justify-content: center;
	.header-img {
		width: 30%;
	}
	.ion-md-notifications {
		position: absolute;
		right: 10px;
		font-size: 26px;
	}
}
</style>
