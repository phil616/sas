<!--

1. 公共竞赛类得分
2. 文体类得分
3. 卫生类得分
4. 表彰类得分
5. 院校活动得分
-->
<template>
	<view>	
		<view class="detail-card">
			<uni-card title="申请的活动详情" :extra="action_detail.action_title">
					<text> {{action_detail.action_detail}}</text>
			</uni-card>
			 <uni-list>
				<uni-list-item title="活动编号" :rightText="action_detail.action_id"></uni-list-item>
				<uni-list-item title="活动是否启用" :rightText="action_detail.action_on"></uni-list-item>
				<uni-list-item title="活动授权" :rightText="action_detail.action_grant"></uni-list-item>
				<uni-list-item title="活动日期" :rightText="action_detail.action_date"></uni-list-item>
				<uni-list-item title="活动分值" :rightText="action_detail.action_score"></uni-list-item>
				<uni-list-item title="活动类型" :rightText="parseType(action_detail.action_type)"></uni-list-item>
			</uni-list>
		</view>
		<view style="height: 20rpx;"></view>
		<view class="post-message-input">
			
			<uni-section title="活动描述" subTitle="请输入活动描述，用于简要描述附件，以便审核顺利通过"
			 type="line" padding>
			<uni-easyinput type="textarea" autoHeight
			v-model="apply_message" placeholder="请输入内容"></uni-easyinput>
			</uni-section>
		</view>
		<view style="height: 20rpx;"></view>
		<view class="post-filelist">
			<text>上传附件</text>
			<uni-section title="上传附件" subTitle="上传申请该活动所需附件/支撑材料或证明"
			 type="line" padding>
			 <uni-file-picker readonly 
			 :value="fileLists" :listStyles="listStyles" file-mediatype="all">
			 	</uni-file-picker>
				<view style="padding: 20rpx;"><button @click="addFileItem">添加一个新附件</button></view>
				<view style="padding: 20rpx;"><button @click="clearAllItem" type="warn">清空当前附件</button></view>
			</uni-section>
		</view>
		<view style="height: 20rpx;"></view>
		<view class="submit-button"> 
			<button @click="applyAction" type="primary">申请该活动</button>
		</view>

	</view>
</template>

<script>
	import utils from "@/utils.js"
	import config from "@/config.js"
	export default {
		data() {
			return {
				url:"",
				listStyles: {
					border: true, // 边框
					dividline: true,//分隔线
					borderStyle: {width: 1,color: 'blue',style: 'dashed',radius: 2,}// 线条样式
				},
				fileLists: [],
				optionId:0,
				action_detail:{},
				apply_message:"",
			}
		},
		methods: {
			applyAction(){
				var _this = this
				var url_list = ""
				console.log(_this.fileLists)
				if (this.fileLists.length == 0){
					uni.showToast({
						title:"无附件无法上传"
					})
					return
				}
				_this.fileLists.map(function (val,idx){
					url_list = url_list + val.url + ","
				})
				let username = uni.getStorageSync("usr_name")
				uni.request({
					url:config.apiUrl+"/add/ApplyMoralRecord",
					method:"POST",
					header:utils.getCommonOAuth2Header(),
					data:{
						action_id:_this.action_id,
						rec_username:username,
						rec_urls:url_list,
						rec_msg:_this.apply_message
					},
					success: (res) => {
						if(res.statusCode == 200){
							uni.showToast({
								title:"申请成功",
								icon:"success",
								duration:2000
							})
							setTimeout(uni.navigateBack, 2000);
							
						}
					}
				})
				
			},
			clearAllItem(){
				this.fileLists = []
			},
			parseType(typeCode){
				switch (typeCode){
					case 1: return "公共竞赛类";
					case 2: return "文艺体育类";
					case 3: return "寝室卫生类";
					case 4: return "个人表彰类";
					case 5: return "院校活动类";
					default: return "未知类型"
				}
			},
			addFileItem(){
				var _this = this
				var _header = utils.getCommonOAuth2Header()
				_header['content-type'] = "multipart/form-data"
				wx.chooseImage({
				    count: 1,
				    success: (res) => {
				        const fileDataPath = res.tempFiles[0];
						if(fileDataPath.size == 0){
							uni.showToast({
								title:"空文件无法上传",
								icon:"error"
							})
							return
						}
				        wx.uploadFile({
				            url: config.apiUrl+"/upload/file?filename="+fileDataPath.name,
							header:_header,
							name:'file',
				            filePath: fileDataPath.path,
							
				            success: (res) => {
								var res_data = JSON.parse(res.data)
								console.log(res_data)
								_this.fileLists.push({
									"name":res_data.file_name,
									"extname":"txt",
									"url":res_data.file_uid,
									"uid":res_data.file_id				
								})
				            },
				            fail: (err) => {
				                console.log(err);
				            }
				        });
				    }
				});
			}
			// function end
		},
		onLoad(options) {
			var endpoint = "/get/MoralActionInfoById?action_id=" + options.id
			this.action_id = options.id
			uni.request({
				url:config.apiUrl + endpoint,
				method:"GET",
				header:utils.getCommonOAuth2Header(),
				success: (res) => {
					this.action_detail = res.data
				}
			})
		},
		created() {

		}
	}
</script>

<style>
.post-message-input
{
	padding: 20rpx;
}
.post-filelist{
	padding: 20rpx;
}
.submit-button{
	padding: 20rpx;
	padding-left: 20rpx;
}
</style>
