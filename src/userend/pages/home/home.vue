<!--
开始页
文档序号：1
等级结构：1
-->
<template>
	<view>
		<view class="tempArea">

		</view>
		<uni-title type="h2" title="学生工作小程序" align="center"></uni-title>
		<uni-section title="小程序介绍" type="line" padding>
			<text class="uni-text">
				计算机科学技术学院学生工作小程序旨在为学生及学生骨干提供高效快捷的在线服务。包含了基本的查询功能和日常功能。
				
			</text>
		</uni-section>
		<view class="view-divider"></view>
		<uni-section title="快捷入口" type="line" padding>
			<uni-list>
				<uni-list-item to="/pages/uploader/uploader" link="" title="青年大学习"></uni-list-item>
				<uni-list-item to="/pages/moral/moral" link="" title="德育分管理"></uni-list-item>
				<uni-list-item to="/pages/richdoc/richdoc" link="" title="历史文档"></uni-list-item>
			</uni-list>
		</uni-section>
		<uni-section title="我的状态" type="line" padding>
			<uni-table border stripe emptyText="暂无更多数据" >
				<uni-tr>
					<uni-th align="center">名称</uni-th>
					<uni-th align="center">状态</uni-th>
				</uni-tr>
				<uni-tr>
					<uni-td>当前德育分</uni-td>
					<uni-td>{{current_score}}</uni-td>
				</uni-tr>
				<uni-tr>
					<uni-td>本学期成绩</uni-td>
					<uni-td>尚未获取</uni-td>
				</uni-tr>
			</uni-table>
		</uni-section>
	</view>
</template>

<script>
	import tool from "@/utils.js";
	import config from "@/config.js"
	export default {
		data() {
			return {
				current_score:"未登录",
				current_image_submit:"未登录",
				current_MIT_status:"未登录",
			}
		},
		methods: {
			
			
			getUserBasicStatusInfo(token){

			},
			getBasicMoralScore(){
				let username = uni.getStorageSync("usr_name")
				var _this = this
				uni.request({
					url:config.apiUrl+"/get/userMoralScore?username=" + username,
					method:"GET",
					header:tool.getCommonOAuth2Header(),
					success: (res) => {
						_this.current_score=res.data.total+80
					}
				})
			},
		},
		onLoad(){
			var loginToken = tool.getLoginInfo();
			if(loginToken != ""){
				this.getUserBasicStatusInfo(loginToken)
			}
		},
		created() {
			this.getBasicMoralScore()
		}
	}
</script>

<style>
.view-divider{
	height: 20rpx;
}
</style>
