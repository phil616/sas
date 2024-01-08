<!--德育分服务
根据原型，排版以此为：
当前德育分卡片
申请德育分跳转链接
德育分政策跳转链接
德育分历史详细列表
-->
<template>
	<view>
		<uni-section title="德育分服务" type="line">
		</uni-section>
		<view class="moral-status-card">
			<uni-card title="当前德育分" :extra="student_info.stu_name">
				<uni-section class="mb-10" title="当前分数">
					<template v-slot:right>
						{{current_score.total+80.0}}
					</template>
				</uni-section>
				 <uni-list>
					<uni-list-item title="基础分数" rightText="80"></uni-list-item>
					<uni-list-item title="额外加分" :rightText="current_score.checked"></uni-list-item>
					<uni-list-item title="扣除分数" :rightText="current_score.reduce"></uni-list-item>
					<uni-list-item title="尚未审核" :rightText="current_score.uncheck"></uni-list-item>
					<uni-list-item title="未成功加分" :rightText="current_score.reject"></uni-list-item>
				</uni-list>
			</uni-card>
		</view>
		<!-- CARD END -->
		
		
		<uni-list>
			<uni-list-item to="/pages/moral-action/moral-action" link="" title="申请德育分"></uni-list-item>
			<uni-list-item to="" link="" title="查看德育分相关政策"></uni-list-item>
		</uni-list>
		<view style="height: 20rpx;"></view>
		<uni-section title="德育分申请历史" type="line">
		</uni-section>
		<view class="moral-detail">
			<uni-table border stripe emptyText="暂无更多数据" >
				<uni-tr>
					<uni-th align="center">活动编号</uni-th>
					<uni-th align="center">活动分数</uni-th>
					<uni-th align="center">活动申请消息</uni-th>
					<uni-th align="center">审核状态</uni-th>
					<uni-th align="center">审核员</uni-th>
					<uni-th align="center">审核备注</uni-th>
				</uni-tr>
				
				<uni-tr v-for="(item, index) in score_list" :index="index" :key="index">
					<uni-td>{{item.action_id}}</uni-td>
					<uni-td>{{item.action_score}}</uni-td>
					<uni-td>{{item.rec_msg}}</uni-td>
					<uni-td>{{parseRecordStatus(item.rec_status)}}</uni-td>
					<uni-td>{{item.chk_username}}</uni-td>
					<uni-td>{{item.chk_commit}}</uni-td>
				</uni-tr>

			</uni-table>
			
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
				current_score:{},
				score_list:[]
			}
		},
		methods: {
			parseActionID(id){
				// 用于解析活动id，但Promise风格问题无法解析
				return id
			},
			parseRecordStatus(statusCode){
				// docs: https://www.yuque.com/cst3/orwkic/rff54tk13pdyi125
				switch (statusCode){
					case 1:
						return "未审核"
						break;
					case 2:
						return "正常通过"
						break;
					case 3:
						return "不通过"
						break;
					case 4:
						return "扣分项目"
						break;
					default:
						return "状态未知"
						break;
				}
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
			},
			getBasicMoralScore(){
				let username = uni.getStorageSync("usr_name")
				var _this = this
				uni.request({
					url:config.apiUrl+"/get/userMoralScore?username=" + username,
					method:"GET",
					header:utils.getCommonOAuth2Header(),
					success: (res) => {
						_this.current_score=res.data
					}
				})
			},
			getUserScoreIntelList(){
				let username = uni.getStorageSync("usr_name")
				var _this = this
				uni.request({
					url:config.apiUrl+"/get/UserMoralRecord?username=" + username,
					method:"GET",
					header:utils.getCommonOAuth2Header(),
					success: (res) => {
						_this.score_list=res.data.data
					}
				})
			}
		},
		created(){
			this.getInfo()
			this.getBasicMoralScore()
			this.getUserScoreIntelList()
		}
	}
</script>

<style>

</style>
