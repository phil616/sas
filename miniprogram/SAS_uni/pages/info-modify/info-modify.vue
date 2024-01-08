<!--
Demo response data:
{
  "username": "042040314",
  "stu_id": "042040314",
  "stu_name": "dcp",
  "stu_clazz": "20403",
  "stu_sex": "男",
  "stu_card": "220181201111111111",
  "stu_nation": "北京",
  "stu_politics": "党员",
  "stu_origin": "吉林",
  "stu_home": "吉林省",
  "stu_phone": "13756610000",
  "stu_email": "12@126.com",
  "stu_location": "五号楼",
  "stu_status": "在籍",
  "stu_graduate": "毕业"
}
-->

<template>
	<view>
		<uni-section title="修改信息" sub-title="部分信息请联系管理员修改"></uni-section>
		<view style="height: 20rpx;>"></view>
		<divider />
		<view class="show-field"><text>姓名</text></view>
		<view class="show-input"><uni-easyinput disabled style v-model="student_info.stu_name" placeholder="姓名"></uni-easyinput></view>
		
		<divider />
		<view class="show-field"><text>学号</text></view>
		<view class="show-input"><uni-easyinput disabled  style v-model="student_info.stu_id" placeholder="学号"></uni-easyinput></view>
		
		<divider />
		<view class="show-field"><text>班级</text></view>
		<view class="show-input"><uni-easyinput disabled  style v-model="student_info.stu_clazz" placeholder="班级"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>性别</text></view>
		<view class="show-input"><uni-easyinput style v-model="student_info.stu_sex" placeholder="性别"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>身份证号</text></view>
		<view class="show-input"><uni-easyinput disabled  style v-model="student_info.stu_card" placeholder="身份证号"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>民族</text></view>
		<view class="show-input"><uni-easyinput style v-model="student_info.stu_nation" placeholder="民族"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>政治面貌</text></view>
		<view class="show-input"><uni-easyinput disabled  style v-model="student_info.stu_politics" placeholder="政治面貌"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>籍贯</text></view>
		<view class="show-input"><uni-easyinput  style v-model="student_info.stu_origin" placeholder="籍贯"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>家庭住址</text></view>
		<view class="show-input"><uni-easyinput style v-model="student_info.stu_home" placeholder="家庭住址"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>联系电话</text></view>
		<view class="show-input"><uni-easyinput style v-model="student_info.stu_phone" placeholder="联系电话"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>电子邮箱</text></view>
		<view class="show-input"><uni-easyinput style v-model="student_info.stu_email" placeholder="电子邮箱"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>宿舍地址</text></view>
		<view class="show-input"><uni-easyinput style v-model="student_info.stu_location" placeholder="宿舍地址"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>学籍状态</text></view>
		<view class="show-input"><uni-easyinput disabled  style v-model="student_info.stu_status" placeholder="学籍状态"></uni-easyinput></view>

		<divider />
		<view class="show-field"><text>毕业情况</text></view>
		<view class="show-input"><uni-easyinput disabled  style v-model="student_info.stu_graduate" placeholder="毕业情况"></uni-easyinput></view>
		<view style="height: 20rpx;"></view>
		<view class="button-pad">
			<view style="height: 20rpx;"></view>
			<button @click="updateInfo" type="primary">提交更新</button>
		</view>

	</view>
</template>

<script>
	import utils from "@/utils.js"
	import config from "@/config.js"
	import divider from "@/components/divider/divider.vue"
	export default {
		components:{divider},
		data() {
			return {
				student_info:{},
			}
		},
		methods: {
			updateInfo(){
				var _this = this
				uni.request({
					url:config.apiUrl + "/update/studentInfo",
					method:"POST",
					header:utils.getCommonOAuth2Header(),
					data:_this.student_info,
					success: (res) => {
						if(res.statusCode==200){
							uni.showModal({
								title:"更新成功",
								content:"刷新界面或重新进入应用以获得最新信息"
							})
						}
					}
				})
			}
		},
		created(){
			let username = uni.getStorageSync("usr_name")
			uni.request({
				url:config.apiUrl+"/get/studentInfo?username=" + username,
				method:"GET",
				header:utils.getCommonOAuth2Header(),
				success: (res) => {
					this.student_info=res.data
					
				}
			})
		}
	}
</script>

<style>
.show-field{
	width: 30%;  
	margin-left: auto; 
	display: inline-block;
	height: 30rpx;
}
.show-input{
	width: 70%;
	margin-right: auto; 
	display: inline-block;
	height: 30rpx;
}
.button-pad{
	padding: 20rpx;
}
</style>
