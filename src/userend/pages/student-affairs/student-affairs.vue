<template>
	<view>
		<uni-section title="学生组织服务中心" type="line">
			<view class="center-container">
				<uni-title type="h1" title="选择目前的学生工作"></uni-title>
				<!-- 额外的注释信息 -->
			</view>
			<view style="padding: 20rpx;">
			<text>未在列表中的学生工作，请在管理系统后台操作</text>
			</view>
		</uni-section>
		<view style="height: 30rpx;"></view>
		<view style="padding: 20rpx;">
			<uni-title v-show="!verifyGroup" type="h2" title="您不是学生骨干,无需处理学生工作"></uni-title>
		</view>
		
		<uni-list v-show="verifyGroup">
			<uni-list-item to="/pages/sa-duty/sa-duty" link="" title="查看本周值班表"></uni-list-item>
			<uni-list-item v-show="false" to="/pages/moral-reduce/moral-reduce" link="" title="德育分快捷扣分"></uni-list-item>
			<uni-list-item to="/pages/sa-database/sa-database" link="" title="访问学生数据库"></uni-list-item>
			<uni-list-item to="/pages/sa-process/sa-process" link="" title="查看材料提交进程"></uni-list-item>
		</uni-list>
	</view>
</template>

<script>
	import utils from "@/utils.js";
	import config from "@/config.js"
	export default {
		data() {
			return {
				verifyGroup:false
			}
		},
		methods: {
		},
		created() {
			var _this = this
			var token = uni.getStorageSync("token")
			uni.request({
				url:config.apiUrl + "/get/userManagerRole",
				header:utils.getCommonOAuth2Header(),
				method:"POST",
				data:{
					token:token
				},
				success: (res) => {
					if(res.statusCode == 200){
						res.data.map(function(val,idx){
							if(val== "group" || val=="staff" || val=="manager"){
								_this.verifyGroup = true
							}
						})
					}
				}
			})
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
