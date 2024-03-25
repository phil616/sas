<template>
	<view>
		<!-- 头部标题 -->
		<view class="login-header">
			<uni-title type="h1" title="登录" color="#1aad19"></uni-title>
			<text>使用学号姓名登录</text>
		</view>
		
		<view class="login-body">
			<uni-forms :modelValue="formData">
				<uni-forms-item label="学号" name="username">
					<uni-easyinput type="text" v-model="formData.username" placeholder="请输入姓名" />
				</uni-forms-item>
				<uni-forms-item label="密码" name="password">
					<uni-easyinput type="password" v-model="formData.password" placeholder="请输入密码" />
				</uni-forms-item>
			</uni-forms>
			<button @click="userLogin" type="primary">登录</button>
			<view style="height: 20rpx;"></view>
			<button @click="wechatLogin" type="primary">微信登录</button>
		</view>
		<view class="login-footer">
			<uni-section class="mb-10" title="登录提示">
				<view class="text-padding">
					<text>1.若从未更改密码，则默认密码为身份证号码后六位，X为大写</text><hr>
					<text>2.第一次使用无法进行微信登陆，需要通过学号密码登录一次后，才能使用微信自动登录</text><hr>
					<text>3.登录即代表您同意</text><uni-tag text="服务条款" :inverted="true" @click="navToAccord()" type="primary" />
				</view>
			</uni-section>
		</view>
	</view>
</template>

<script>
	import utils from "@/utils.js"
	import config from "@/config.js"
	export default {
		data() {
			return {
				formData:{
					username:"",
					password:""
				},
				isBinded:false,
			}
		},
		methods: {
			navToAccord(){uni.navigateTo({
				url:"/pages/accords/accords"
			})},
			userLogin(){
				// 点击登录之后触发的函数
				var _this = this
				uni.request({
					url:config.apiUrl+"/token",
					method:"POST",
					header:{'content-type': "application/x-www-form-urlencoded"},
					data:
					{username:_this.formData.username,password:_this.formData.password},
					success: (res) => {
						if(res.statusCode == 200){
							uni.setStorage({
								key:"token",
								data:res.data.access_token
							})
							utils.verifyTokenExp()
							uni.reLaunch({
								url:"/pages/home/home"
							})
						}else{
							uni.showModal({
								title:"登录失败",
								content:`${JSON.stringify(res.data)}`
							})
						}
					}
				})
			
			// 用户名登录逻辑，通过code登录一次，
		},
			wechatLogin(){
				console.log("deprated")
				// 微信登陆逻辑，通过code登录获取token，如果失败，则未绑定，弹出提示。
				if(this.isBinded == true){
					uni.reLaunch({
						url:"/pages/home/home"
				})
				}else{
					uni.showModal({
						title:'尚未绑定',
						content:'首次登录后即可自动绑定微信账号',
					})
				}
				
			},
			userBindWechat(code,username,password){
				console.log("bind function called")
				uni.request({
					url:config.apiUrl+"/wechat_bind",
					method:'POST',
					data:{
						code:code,
						username:username,
						password:password,
						
					},
					success: (res) => {
						if(res.data.code == 200){
							uni.login({
								success:res=>{
									uni.request({
										url:config.apiUrl+"/wechat_token",
										method:"POST",
										data:{
											code:res.code
										},
										success: (resp) => {
											uni.setStorage({
												key:"token",
												data:resp.data.access_token
											})
										}
									})
								}
							})
							uni.reLaunch({
								url:"/pages/home/home"
							})
						}
					}
				})
			},
			bindStatusCheck(){
				// onLoad 阶段进行的函数，通过code请求一次token，如果出错，则从未绑定过。
				// 若未绑定，则isBinded为false，微信登陆弹出未绑定，若绑定，则直接通过code可登录。
				var _this = this
				// -- FUNCION_START wechat login
				uni.login({
					success:res=>{
						uni.request({
							url:config.apiUrl+"/wechat_token",
							method:'POST',
							data:{
								code:res.code
							},
							success: (res) => {
								if(res.statusCode == 401){
									// 401说明未绑定
									_this.isBinded = false
								}
								if(res.statusCode == 200){
									_this.isBinded = true
									uni.setStorage({
										key:"token",
										data:res.data.access_token
									})
								}
							}
						})
					}
				})
				// -- FUNCTION_END wechat login
			}
		},
		onLoad() {
			this.bindStatusCheck()
			if(utils.verifyTokenExp()){uni.navigateTo({
				url:"/pages/home/home"
			})}
			else{
				// token未颁发、过期、解析错误
			}
		}
	}
</script>

<style>
.login-body{
	padding: 30rpx;
}
.login-header{
	padding: 30rpx;
}
.text-padding{
	padding: 30rpx;
}
</style>
