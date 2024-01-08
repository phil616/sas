<!--通过扣分列表，扣除-->
<template>
	<view class="container">
		<uni-card is-full :is-shadow="false">
			<text class="uni-h6">通过输入学号的方式快捷对某项活动扣分</text>
		</uni-card>
		<uni-section title="选择扣分项目" type="line" padding style="height: calc(100vh - 100px);">
			<uni-data-picker placeholder="选择扣分项目" popup-title="选择扣分项" :localdata="dataTree" v-model="classes"
				@change="onchange" @nodeclick="onnodeclick" @popupopened="onpopupopened" @popupclosed="onpopupclosed">
			</uni-data-picker>
			<uni-title type="h3" :title="getCurrentActionid()">
				
			</uni-title>
		</uni-section>
		<uni-section title="输入学号" subTitle="输入扣分的学号" type="line" padding>
			<uni-easyinput class="uni-mt-5" v-model="action_id" placeholder="活动编号"></uni-easyinput>
		</uni-section>
		<view style="padding: 20rpx;">
			<button type="primary" @click="submitReduce">提交扣分</button>
		</view>

	</view>
</template>
<script>
	export default {
		data() {
			return {
				classes: '无',
				dataTree: [{
					text: "测试活动扣分",
					value: "测试活动",
				},
				{
					text: "测试活动扣分2",
					value: "测试活动2",
				},
				{
					text: "测试活动扣分3",
					value: "测试3",
				}]
			}
		},
		methods: {
			getCurrentActionid(){
				return "选择的扣分项目是:" + this.classes
			},
			submitReduce(){
				
			},
			onnodeclick(e) {
				console.log(e);
			},
			onpopupopened(e) {
				console.log('popupopened');
			},
			onpopupclosed(e) {
				console.log('popupclosed');
			},
			onchange(e) {
				console.log('onchange:', e);
			}
		}
	}
</script>

<style>
	.title {
		font-size: 14px;
		font-weight: bold;
		margin: 20px 0 5px 0;
	}

	.data-pickerview {
		height: 400px;
		border: 1px #e5e5e5 solid;
	}

	 .popper__arrow {
    top: -6px;
    left: 50%;
    margin-right: 3px;
    border-top-width: 0;
    border-bottom-color: #EBEEF5;
}
 .popper__arrow {
    top: -6px;
    left: 50%;
    margin-right: 3px;
    border-top-width: 0;
    border-bottom-color: #EBEEF5;
}
</style>