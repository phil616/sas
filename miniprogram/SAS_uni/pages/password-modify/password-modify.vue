<template>
	<view>
		<uni-section class="mb-10" title="修改密码" sub-title="默认密码为身份证号码后六位,如忘记密码,请联系管理员重置" padding>
		<uni-section class="modify-section" title="原密码" padding>
			<uni-easyinput  v-model="ori_password" placeholder="请输入原密码" />
		</uni-section>
		<divider/>
		<uni-section class="modify-section" title="新密码" padding> 
			<uni-easyinput  v-model="mod_password" placeholder="请输入新密码" />
		</uni-section>
		<uni-section class="modify-section" title="重复新密码" padding>
			<uni-easyinput  v-model="rpd_password" placeholder="请重复输入新密码" />
		</uni-section>
		<button @click="updatePassword" type="primary">修改密码</button>
		</uni-section>
		<uni-section title="关于修改面膜" padding>
		<text>
			根据学院相关保密条例，系统不会存储您的密码，
			而是通过B-Crypt加盐摘要算法存储摘要信息，因此无法获取原密码.
			若密码忘记，请联系管理员重置。
		</text>
		</uni-section>
	</view>
</template>

<script>
	import divider from "@/components/divider/divider.vue";
	import config from "@/config.js";
	import utils from "@/utils.js";
	export default {
		components:{divider},
		data() {
			return {
				ori_password:"",
				mod_password:"",
				rpd_password:"",
			}
		},
		methods: {
			updatePassword(){
				var _this = this
				let username = uni.getStorageSync("usr_name")
				uni.request({
					url:config.apiUrl+"/update/user/password",
					method:"POST",
					header:utils.getCommonOAuth2Header(),
					data:{
						username:username,
						oldPassword:_this.ori_password,
						newPassword:_this.rpd_password,
					},
					success: (res) => {
						// inner IF start
						if(res.statusCode==200){
							uni.showModal({
								title:"密码更改成功",
								content:"请重新登陆",
								showCancel: false,
								success: (res) => {
									if(res.confirm) {  
										uni.removeStorage({key:"usr_name"})
										uni.removeStorage({key:"token"})
										uni.removeStorage({key:"openid"})
										uni.navigateTo({
											url:"/pages/login/login"
										})
									}
								},
							})
						// inner IF end
						}else{
							uni.showModal({
								title:"密码修改失败",
								content:`原因为：${JSON.stringify(res.data)}`
							})
						}
					}
				})
			}
			//  Function updatePassword() END
			// here for new methods:
			
			
		}
	}
</script>

<style>

</style>
