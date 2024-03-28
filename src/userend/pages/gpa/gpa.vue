<template>
	<view>
		<view class="title-container">
			<uni-section title="成绩卡片" sub-title="本学生所有科目成绩如下"></uni-section>
		</view>
		<view style="height: 20rpx;"></view>

		<!-- 使用uni-list组件包含所有列表项 -->
		<uni-list>
		  <!-- 使用v-for遍历成绩列表 -->
		  <uni-list-item 
			v-for="(item, index) in scoreList" 
			:key="index" 
			:title="item.gpa_type"
			:note="item.gpa_time"
			:rightText="item.gpa_score"
			:showArrow="false"
		  >
		  </uni-list-item>
		</uni-list>

				
	</view>
</template>

<script>
	import utils from "@/utils.js"
	import config from "@/config.js"
	export default {
		data() {
			return {
				student_info:{},
				scoreList:[],
			}
		},
		methods: {
			getInfo(){
				//TODO 文档尚未完成，需要完成文档
				let username = uni.getStorageSync("usr_name")
				uni.request({
					url:config.apiUrl+"/gpa/get/user/scorelist?username=" + username,
					method:"GET",
					header:utils.getCommonOAuth2Header(),
					success: (res) => {
						this.scoreList=res.data
					}
				})
			}
		},
		created(){
			this.getInfo()
		}
	}
</script>

<style lang="scss">
	.title-container{
		padding: 0rpx;
	}
	.button-pad{
		padding: 20rpx;
	}
</style>