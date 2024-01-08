<!-- 待完成 -->

<template>
	<view>
		<view style="padding-top: 50rpx;"></view>
		<view class="center-container">
			<uni-icons type="minus-filled" size="50"></uni-icons>
			<uni-title type="h1" title="当前学年尚未结束"></uni-title>
			<!-- 额外的注释信息 -->
		</view>
		
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
