<!--
个人页面，初始化请求：个人信息

-->
<template>
	<view class="container">
		<!-- 登录卡片 -->
		<view v-show="isLogin">
			<!-- 个人卡片头部 -->
			<uni-card :title="studentName" :sub-title="studentNumber" :extra="studentClazz">
				<text>{{studentInfo}}</text>
			</uni-card>
		</view>
		
		<!-- 未登录卡片 -->
		<view v-show="!isLogin" class="login-button">
			<view class="view-divider"></view>
				<button type="primary" @click="loginPage">点此登录</button>
			<view class="view-divider"></view>
		</view>

		<!-- 个人信息列表 -->
		<uni-list v-show="isLogin">
			<uni-list-item to="/pages/userinfo/userinfo" link="" title="基本信息"></uni-list-item>
			<uni-list-item to="/pages/password-modify/password-modify" link="" title="修改密码"></uni-list-item>
			<uni-list-item to="/pages/settings/settings" link="" title="系统推送管理"></uni-list-item>
		</uni-list>
		<!-- 关于信息列表 -->
		<view class="view-divider"></view>
		<uni-list>
			<uni-list-item to="/pages/about/about" link="" title="关于系统"></uni-list-item>
			<uni-list-item v-show="isLogin" link="" title="退出登录" @click="logout"></uni-list-item>
		</uni-list>
  </view>
</template>

<script>
	import utils from "@/utils.js"
	import config from "@/config.js"
	export default {
		data() {
			return {
				isLogin: false,
				studentName:  '未登录',
				studentNumber:'未登录',
				studentClazz: '未登录',
				studentInfo:  '未登录',
			}
		},
		methods: {
			loginPage(){
				uni.navigateTo({
					url:"/pages/login/login"
				})
			},
			logout(){
				uni.removeStorage({key:"usr_name"})
				uni.removeStorage({key:"token"})
				uni.removeStorage({key:"openid"})
				uni.navigateTo({
					url:"/pages/login/login"
				})
			}
		},
		onLoad() {
			console.log(utils.getCommonOAuth2Header())
			var _this = this
			if(utils.verifyTokenExp()){
				this.isLogin = true;
				// 加载初始人员信息
				var username = uni.getStorageSync("usr_name")
				uni.request({
					url:config.apiUrl + "/get/studentInfo?username="+username,
					method:"GET",
					header:utils.getCommonOAuth2Header(),
					success: (res) => {
						console.log(res.data)
						_this.studentName = res.data.stu_name
						_this.studentNumber = res.data.stu_id
						_this.studentClazz = res.data.stu_clazz
						_this.studentInfo = res.data.stu_status
					}
				})
			}
			
		}
	}
</script>

<style>
.view-divider{
	height: 20rpx;
}
.login-button
{
	padding: 20rpx;
}
</style>
