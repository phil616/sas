<template>
	<view>
		<uni-section title="学生服务" type="line" padding>
			<uni-grid :column="2" :square="false" :highlight="false" @change="change">
				<uni-grid-item v-for="(item, index) in list" :index="index" :key="index">
					<view class="grid-item-box">
						<image :src="item.url" class="image" mode="aspectFill" />
						<text class="text">{{ item.text }}</text>
					</view>
				</uni-grid-item>
			</uni-grid>
		</uni-section>
		<uni-section title="其它服务" type="line" padding>
			<text>其他功能正在持续上线中</text>
		</uni-section>
	</view>
</template>

<script>
	import utils from "@/utils.js"
	export default {
		components: {},
		data() {
			return {
				list: [{
						url: '/static/images/gpa.png',
						text: '成绩卡片',
						page: '/pages/gpa/gpa',
					},
					{
						url: '/static/images/uploader.png',
						text: '材料上传',
						page: '/pages/uploader/uploader',
					},
					{
						url: '/static/images/moral.png',
						text: '德育分服务',
						page: '/pages/moral/moral',
					},
					{
						url: '/static/images/scholar.png',
						text: '奖助学金申请',
						page: '/pages/scholarship/scholarship',
					},
					{
						url: '/static/images/insurance.png',
						text: '医保登记',
						page: '/pages/insurance/insurance',						
					},
					{
						url: '/static/images/student-affairs.png',
						text: '学生工作',
						page: '/pages/student-affairs/student-affairs',
					},
					{
						url: '/static/images/richdoc.png',
						text: '学院文件',
						page: '/pages/richdoc/richdoc',
					},
					{
						url: '/static/images/userinfo.png',
						text: '个人信息',
						page: '/pages/userinfo/userinfo',
					},
					{
						url: '/static/images/about.png',
						text: '关于小程序',
						page: '/pages/about/about',
					},
					{
						url: '/static/images/accords.png',
						text: '服务条款',
						page: '/pages/accords/accords',
					}
				]
			}
		},
		methods: {
			change(e) {
				let {
					index
				} = e.detail
				uni.navigateTo({
					url:this.list[index].page
				})
			}
		},
		onLoad() {

		}
	}
</script>


<style lang="scss">
	.image {
		width: 25px;
		height: 25px;
	}

	.text {
		font-size: 14px;
		margin-top: 5px;
	}

	.example-body {
		/* #ifndef APP-NVUE */
		// display: block;
		/* #endif */
	}

	.grid-dynamic-box {
		margin-bottom: 15px;
	}

	.grid-item-box {
		flex: 1;
		// position: relative;
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 15px 0;
	}

	.grid-item-box-row {
		flex: 1;
		// position: relative;
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: row;
		align-items: center;
		justify-content: center;
		padding: 15px 0;
	}

	.grid-dot {
		position: absolute;
		top: 5px;
		right: 15px;
	}

	.swiper {
		height: 420px;
	}

	/* #ifdef H5 */
	@media screen and (min-width: 768px) and (max-width: 1425px) {
		.swiper {
			height: 630px;
		}
	}

	@media screen and (min-width: 1425px) {
		.swiper {
			height: 830px;
		}
	}

	/* #endif */
</style>

