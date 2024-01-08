<!--

1. 公共竞赛类得分
2. 文体类得分
3. 卫生类得分
4. 表彰类得分
5. 院校活动得分
-->
<template>
	<view>
		<uni-title type="h1" align="center" title="德育分活动申请"></uni-title>
		<uni-section title="筛选" type="line">
			<uni-data-checkbox mode="button" v-model="value" :localdata="range" 
			></uni-data-checkbox>
		</uni-section>
		
		<uni-section title="所有活动列表" type="line">
			<!-- 加载时渲染，按条件筛选 -->
			<uni-collapse accordion v-model="accordionVal">
				<uni-collapse-item
				 v-for="(item,index) in activities" 
				 v-if="selected_type == 0 || item.activity_type == selected_type"
				 :index="index" 
				 :key="index" :title="item.action_title"
				 >
					<view class="card-content">
						<text> 活动详情：{{item.action_detail}}</text><br>
						<text> 活动时间：{{item.action_date}}</text><br>
						<text> 活动发起：{{item.action_grant}}</text><br>
						<text> 活动分值：{{item.action_score}}</text><br>
						<text> 活动类型：{{parseType(item.action_type)}}</text><br>
						<view class="comfirm-button">
							<button type="default" @click="goApplyAction(item.action_id)"> 申请该活动 </button>
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
				selected_type: 0,
				value: 0,
				range: [
					{"value": 0,"text": "所有类型"},
					{"value": 1,"text": "公共竞赛类"},
					{"value": 2,"text": "文艺体育类"},
					{"value": 3,"text": "寝室卫生类"},
					{"value": 4,"text": "个人表彰类"},
					{"value": 5,"text": "院校活动类"},
				],
				activities:[]
			}
		},
		methods: {
			goApplyAction:(id)=>{
				console.log(id)
				uni.navigateTo({
					url:`/pages/moral-item/moral-item?id=${id}`,
					success: (res) => {
						console.log("success redirect",res)
					},
					fail: (res) => {
						console.log("fail redirect",res)
					}
				})
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
			initGetActionOn(){
				var _this = this
				uni.request({
					url:config.apiUrl+"/get/MoralAction",
					method:"GET",
					header:utils.getCommonOAuth2Header(),
					success: (res) => {
						_this.activities = res.data.data
					}
				})
			},
			elected_class(e){this.selected_type = e['detail'].value;},
		},
		created() {
			this.initGetActionOn()
		}
	}
</script>

<style>
	.card-content{
		padding: 20rpx;
	}
	.comfirm-button{
		padding: 30rpx;
	}

</style>
