<!--聚合后台-->

<template>
	<view>
		<uni-section title="通过活动编号和班级查询活动进度" type="line" padding>
		</uni-section>
		<uni-section title="输入活动编号" subTitle="在活动列表中查看具体活动编号" type="line" padding>
			<uni-easyinput class="uni-mt-5" v-model="action_id" placeholder="活动编号"></uni-easyinput>
		</uni-section>
		<uni-section title="输入班级" subTitle="要查询进程的班级" type="line" padding>
			<uni-easyinput class="uni-mt-5"  v-model="action_clazz" placeholder="班级"></uni-easyinput>
			<view class="center-container">
				<view style="height: 30rpx;"></view>
				<button @click="goQuery" type="primary">点击查询</button>
			</view>
		</uni-section>

		
		
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
</template>

<script>
	import utils from "@/utils.js";
	import config from "@/config.js"
	export default {
		data() {
			return {
				clazzList:[],
				action_id:"",
				action_clazz:"",
			}
		},
		methods: {
			goQuery(){
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
								url: config.apiUrl + `/get/userClazzImageTaskRecord?action_id=${_this.action_id}&clazz=${_this.action_clazz}`,
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
