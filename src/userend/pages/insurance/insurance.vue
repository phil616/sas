
<!-- 医保信息 -->
<template>
	<view>
		<view class="detail-card">
			<uni-card title="本年度在校参保情况" :extra="action_detail.action_title">
					<text> {{userMITStatus.username}}</text>
			</uni-card>
			 <uni-list>
				<uni-list-item title="是否参保" :rightText="parseMITChoice(userMITStatus.mit_choice)"></uni-list-item>
				<uni-list-item title="信息情况" :rightText="parseMITStatusCode(userMITStatus.mit_status)"></uni-list-item>
				<uni-list-item title="附件情况" :rightText="parseMITAttachment(userMITStatus.mit_attachments)"></uni-list-item>
			</uni-list>
		</view>
		<view class="reserved-option-list" v-show="false">
			
		</view>
	</view>
</template>

<script>
	import utils from "@/utils.js"
	import config from "@/config.js"
	export default {
		data() {
			return {
				userMITStatus:{},
				mapping:{},
				action_detail:{}
			}
		},
		methods: {
			parseMITChoice(choiceCode){
				if(choiceCode){
					return "参加学校医保"
				}else{return "未在校参保"}
			},
			parseMITStatusCode(statusCode){
				return this.mapping[String(statusCode)]
			},
			parseMITAttachment(attach){
				if (attach == "" || attach == null || attach == undefined ) {return "无附件或未上传"}
				else {return "已上传"}
			},
			initLoadData(){
				var _this = this
				let username = uni.getStorageSync("usr_name")

				uni.request({
					url:config.apiUrl + "/get/mit/static/mapping",
					method:"GET",
					header:utils.getCommonOAuth2Header(),
					success: (res) => {
						if(res.statusCode == 200){
							_this.mapping = res.data.data
							uni.request({
								url:config.apiUrl + "/get/mit/userStatus?username=" + username,
								method:"GET",
								header:utils.getCommonOAuth2Header(),
								success: (res) => {
									if(res.statusCode == 404){
										// not register
									}else if(res.statusCode == 200){
										_this.userMITStatus = res.data
									}
								}
							})
						}
					}
				})
			},
		},
		created() {
			this.initLoadData()
		}
	}
</script>

<style>
.detail-card{
	padding-right: 20rpx;

}
</style>
