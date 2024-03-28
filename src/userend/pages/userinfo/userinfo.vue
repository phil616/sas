<template>
	<view>
		<view class="title-container">
			<uni-section title="个人信息" sub-title="学生基本信息"></uni-section>
		</view>
		<view style="height: 20rpx;"></view>
		<uni-list>
			<uni-list-item title="学号" :rightText="student_info.stu_id" />
			<uni-list-item title="姓名" :rightText="student_info.stu_name" />
			<uni-list-item title="性别" :rightText="student_info.stu_sex" />
			<uni-list-item title="班级" :rightText="student_info.stu_clazz" />
			<uni-list-item title="身份证号" :rightText="student_info.stu_card" />
			<uni-list-item title="民族" :rightText="student_info.stu_nation" />
			<uni-list-item title="政治面貌" :rightText="student_info.stu_politics" />
			<uni-list-item title="籍贯" :rightText="student_info.stu_origin" />
			<uni-list-item title="家庭住址" :rightText="student_info.stu_home" />
			<uni-list-item title="联系电话" :rightText="student_info.stu_phone" />
			<uni-list-item title="电子邮箱" :rightText="student_info.stu_email" />
			<uni-list-item title="宿舍" :rightText="student_info.stu_location" />
			<uni-list-item title="学籍状态" :rightText="student_info.stu_status" />
			<uni-list-item title="毕业信息" :rightText="student_info.stu_graduate" />
		</uni-list>
		<view class="button-pad">
			<view style="height: 20rpx;"></view>
			<button @click="reloadPage" type="primary">刷新信息</button>
		</view>
		<view class="button-pad">
			<view style="height: 20rpx;"></view>
			<button @click="modifyInfo" type="primary">修改信息</button>
		</view>
				
	</view>
</template>

<script>
	import utils from "@/utils.js"
	import config from "@/config.js"
	export default {
		data() {
			return {
				student_info:{},
			}
		},
		methods: {
			modifyInfo(){
				uni.navigateTo({
					url:"/pages/info-modify/info-modify"
				})
			},
			reloadPage(){
				this.getInfo()
			},
			getInfo(){
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