<!--单一列表，设计数据结构-->

<template>
	<view>
		<uni-section title="值班表" type="line">
			<view style="padding-top: 50rpx;"></view>
			<view class="center-container">
				<uni-icons type="minus-filled" size="50"></uni-icons>
				<uni-title type="h1" title="暂无值班任务"></uni-title>
				<!-- 额外的注释信息 -->
			</view>
		</uni-section>
		<uni-section title="您下次值班时间:" type="line">
			<uni-title type="h3" title="本周没有值班任务"></uni-title>
		</uni-section>
		<uni-section title="学院值班表" type="line">
			<uni-table border stripe emptyText="暂无更多数据" >
				<uni-tr>
					<uni-th align="left"></uni-th>
					<uni-th align="center">周一</uni-th>
					<uni-th align="center">周二</uni-th>
					<uni-th align="center">周三</uni-th>
					<uni-th align="center">周四</uni-th>
					<uni-th align="center">周五</uni-th>
				</uni-tr>
				<uni-tr v-for="(item,index) in clazzList" :index="index" :key="index">
					<uni-td>{{item.username}}</uni-td>
					<uni-td>{{item.stu_name}}</uni-td>
					<uni-td>{{item.message}}</uni-td>
				</uni-tr>
			</uni-table>
		</uni-section>
		<uni-section title="学办值班表" type="line">
			<uni-table border stripe emptyText="暂无更多数据" >
				<!-- 表头行 -->
				<uni-tr>
					<uni-th align="left"></uni-th>
					<uni-th align="center">周一</uni-th>
					<uni-th align="center">周二</uni-th>
					<uni-th align="center">周三</uni-th>
					<uni-th align="center">周四</uni-th>
					<uni-th align="center">周五</uni-th>
				</uni-tr>
				<uni-tr v-for="(item,index) in clazzList" :index="index" :key="index">
					<uni-td>{{item.username}}</uni-td>
					<uni-td>{{item.stu_name}}</uni-td>
					<uni-td>{{item.message}}</uni-td>
				</uni-tr>
			</uni-table>
		</uni-section>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				clazzList:[],
			}
		},
		methods: {
			
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
