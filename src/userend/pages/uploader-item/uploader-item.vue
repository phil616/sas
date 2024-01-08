<template>
	<view>
		<view class="detail-card">
			<uni-card title="活动详情" :extra="action_detail.action_title">
					<text> {{action_detail.act_desc}}</text>
			</uni-card>
			 <uni-list>
				<uni-list-item title="活动编号" :rightText="action_detail.act_id"></uni-list-item>
				<uni-list-item title="活动范围" :rightText="action_detail.act_range"></uni-list-item>
				<uni-list-item title="活动是否启用" :rightText="action_detail.act_on"></uni-list-item>
				<uni-list-item title="活动授权" :rightText="action_detail.act_grant"></uni-list-item>
			</uni-list>
			<view style="height: 20rpx;"></view>
			<uni-list>
				<uni-list-item title="我的状态" :rightText="myFile"></uni-list-item>
			</uni-list>
		</view>
		<view class="only-button"> 
			<button type="primary" @click="submitImage()">{{buttonName()}}</button>
		</view>
		<view class="my-file-picker">
			<uni-file-picker readonly
			:value="fileLists" :listStyles="listStyles">
			</uni-file-picker>
		</view>
		<view class="clazz-status">
			<uni-section title="班级提交情况" type="line">
				<view class="only-button">
					<button type="default" @click="showClazzStatus">查看班级提交情况</button>
				</view>
				<view v-show="clazzStatusFlag">
					<uni-table border stripe emptyText="暂无更多数据" >
						<!-- 表头行 -->
						<uni-tr>
							<uni-th align="center">学号</uni-th>
							<uni-th align="center">姓名</uni-th>
							<uni-th align="left">提交情况</uni-th>
						</uni-tr>
						<uni-tr v-for="(item,index) in clazzList" :index="index" :key="index">
							<uni-td>{{item.username}}</uni-td>
							<uni-td>{{item.stu_name}}</uni-td>
							<uni-td>{{item.message}}</uni-td>
						</uni-tr>
					
					</uni-table>
					
				</view>
			</uni-section>
		</view>
	</view>
</template>

<script>
	import utils from "@/utils.js";
	import config from "@/config.js"
	export default {
		data() {
			return {
				action_detail:{},
				myFile:"查询失败",
				fileLists: [],
				action_id:"",
				clazzList:[],
				clazzStatusFlag:false,
			}
		},
		methods: {
			showClazzStatus(){
				const demourl= "/get/userClazzImageTaskRecord?action_id=2&clazz=20403"
				var action_id= this.action_id
				var _this = this
				let username = uni.getStorageSync("usr_name")
				// 获取自己的班级
				uni.request({
					url:config.apiUrl+"/get/studentInfo?username=" + username,
					method:"GET",
					header:utils.getCommonOAuth2Header(),
					success: (res) => {
						// request function success callback start
						if (res.statusCode == 200){
							_this.clazz = res.data.stu_clazz;
							uni.request({
								url: config.apiUrl + `/get/userClazzImageTaskRecord?action_id=${_this.action_id}&clazz=${_this.clazz}`,
								method:"GET",
								header:utils.getCommonOAuth2Header(),
								success:(innerRes)=>{
									_this.clazzList = innerRes.data
									_this.clazzStatusFlag = true
								}
							})
						}
						// request function success callback end
					}
				})
			},
			getPosted(objList){
				
			},
			getNotPosted(objList){
				
			},
			buttonName(){
				if(this.myFile=="查询失败") return "";
				if(this.myFile=="未提交") return "上传图片";
				if(this.myFile=="已提交") return "修改图片";
			},
			submitImage(){
				// Vue Component methods Function (submitImage) Start
				let username = uni.getStorageSync("usr_name")
				var _this = this
				var _header = utils.getCommonOAuth2Header()
				_header['content-type'] = "multipart/form-data"
				// wx.chooseImage Start
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
						// upload file function start
					wx.uploadFile({
			            url: config.apiUrl+"/upload/file?filename="+fileDataPath.name,
						header:_header,
						name:'file',
			            filePath: fileDataPath.path,
			            success: (res) => {
							// upload file function start
							var res_data = JSON.parse(res.data)
							console.log(res_data)
							_this.fileLists.push({
								"name":res_data.file_name,
								"extname":"png",
								"url":res_data.file_uid,
								"uid":res_data.file_id				
							})
							// 在此阶段更新文件状态
							// inner request Function Start
							uni.request({
								url:config.apiUrl + "/update/userImageRecord",
								method:"POST",
								header:utils.getCommonOAuth2Header(),
								data:{
									act_id: _this.action_id,
									act_username: username,
									act_url: res_data.file_uid
								},
								success: (innerRes) => {
									if(innerRes.statusCode == 200){
										uni.showToast({
											title:"操作成功",
											icon:"success",
											duration:2000
										})
										setTimeout(uni.navigateBack, 2000);
										
									}
								}
							})
							// inner request Function end
							// upload file function end
				        },
				        fail: (err) => {
							console.log(err);
						}
				    });
				}
			});
			// wx.chooseImage end
			// Vue Component methods Function (submitImage) End
		}
		},
		onLoad(options) {
			let username = uni.getStorageSync("usr_name")
			var endpoint = "/get/ImageActionById?action_id=" + options.id
			this.action_id = options.id
			var _this = this
			uni.request({
				url:config.apiUrl + endpoint,
				method:"GET",
				header:utils.getCommonOAuth2Header(),
				success: (res) => {
					_this.action_detail = res.data
					uni.request({
						url:config.apiUrl + "/get/userImageRecord?"+`username=${username}&act_id=${res.data.act_id}`,
						method:"GET",
						header:utils.getCommonOAuth2Header(),
						success: (res) => {
							if(res.statusCode == 404){
								_this.myFile = "未提交"
							}else{
								_this.myFile = "已提交"
								_this.fileLists.push({
									url: config.apiUrl+"/download/uid?uid="+res.data.act_url,
									extname: 'png',
									name: 'logo.png'
								})
							}
						}
					})
					
				}
			})
		}
	}
</script>

<style>
.detail-card{
	padding: 10rpx;
	padding-right: 20rpx;
}
.only-button{
	padding: 20rpx;
	padding-right: 20rpx;
}
</style>
