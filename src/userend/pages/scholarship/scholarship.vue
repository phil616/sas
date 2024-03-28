<template>
	<!--
	本模块与材料相同
	-->
	<view>
		<uni-section title="所有奖助学金相关的内容如下:" type="line">
			<!-- 加载时渲染，按条件筛选 -->
			<uni-collapse accordion v-model="accordionVal">
				<uni-collapse-item
				 v-for="(item,index) in imageTaskActions" 
				 v-if="selected_type == 0 || item.activity_type == selected_type"
				 :index="index" 
				 :key="index" :title="item.act_title"
				 >
				 
					<view class="card-content">
						<text> 活动详情：{{item.act_desc}}</text><br>
						<text> 活动发起：{{item.act_grant}}</text><br>
						<text> 活动范围：{{item.act_range}}</text><br>
						<view class="comfirm-button">
							<button type="default" @click="goApplyAction(item.act_id)">上传该活动</button>
						</view>
					</view>
				</uni-collapse-item>
				
			</uni-collapse>
			
		</uni-section>
	</view>
</template>

<script>
	import utils from "@/utils.js";
	import config from "@/config.js"
	export default {
		data() {
			return {
				accordionVal:"",
				imageTaskActions:[],
			}
		},
		methods: {
			goApplyAction(actionId){
				uni.navigateTo({
						url:`/pages/uploader-item/uploader-item?id=${actionId}`,
						success: (res) => {
							console.log("success redirect",res)
						},
						fail: (res) => {
							console.log("fail redirect",res)
						}
				})
			},
		},
		created() {
			var _this = this
			uni.request({
				url:config.apiUrl+"/get/ImageActions",
				method:"GET",
				header:utils.getCommonOAuth2Header(),
				success: (res) => {
					_this.imageTaskActions = res.data
					console.log(_this.imageTaskActions)
				}				
			})
		}
	}
</script>

<style>
.card-content{
	padding: 10rpx;
}
.comfirm-button{
	padding: 10rpx;
}
</style>
