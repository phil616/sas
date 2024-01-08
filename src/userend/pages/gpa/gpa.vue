<template>
	<view>
		<uni-section title="成绩卡片" type="line">
			<view style="padding-top: 50rpx;"></view>
			<view class="center-container">
				<uni-icons type="minus-filled" size="50"></uni-icons>
				<uni-title type="h1" title="本学期尚未结束"></uni-title>
				<!-- 额外的注释信息 -->
			</view>
		</uni-section>

	</view>
</template>

<script>
	export default {
		data() {
			return {
			
			}
		},
		methods: {
			
		}
	}
</script>

<style>
.center-container{
	height: 100%;
	flex: auto;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}
</style>
