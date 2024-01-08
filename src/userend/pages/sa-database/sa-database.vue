<!--表单条件查询某个人-->

<template>
	<view>
		<uni-section title="学生信息查询" type="line">
			<view class="center-container">
				<uni-title type="h1" title="小程序端只支持学号查询"></uni-title>
			</view>
			<view style="padding: 20rpx;">
				<text>导出名单、结构化查询等操作请前往PC客户端。</text><hr>
				<text>为保障学生信息安全，您的每次查询将会被记录跟踪。</text><hr>
				<text>高频次查询会导致账号不可用</text>
			</view>
		</uni-section>
		<view style="height: 20rpx;"></view>
		<view class="input-box">
			<uni-section title="输入学生学号" subTitle="通过学号或用户名进行搜素,暂不支持模糊搜索" type="line" padding>
				<uni-easyinput class="uni-mt-5" suffixIcon="search" v-model="searchNumber" placeholder="右侧图标" @iconClick="iconClick"></uni-easyinput>
			</uni-section>
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
	</view>
</template>

<script>
	import utils from "@/utils.js";
	import config from "@/config.js"
	export default {
		data() {
			return {
				student_info:{},
				searchNumber:"",
			}
		},
		methods: {
			
			iconClick(){
				var _this = this
				uni.request({
					url:config.apiUrl + "/get/studentInfo?username="+_this.searchNumber,
					method:"GET",
					header:utils.getCommonOAuth2Header(),
					success: (res) => {
						if(res.statusCode == 200){
							this.student_info = res.data
						}else{
							uni.showToast({
								title:`查询失败${res.data}`,
								icon:"error",
								duration:2000
							})
						}
						
					}
				})
				
			}
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
