<template>
	<view>
		<web-view :src="docUrl"></web-view>
	</view>
</template>

<script>
	import utils from "@/utils.js";
	import config from "@/config.js"
	export default {
		data() {
			return {
				docUrl:"",
			}
		},
		methods: {
			
		},
		created() {
			var _this = this
			_this.docUrl = config.staticUrl+"/docUrl.html"
		}
	}
</script>

<style>

</style>
