<template>
	<view>
		<web-view :src="accordsUrl"></web-view>
	</view>
</template>

<script>
	import utils from "@/utils.js";
	import config from "@/config.js"
	export default {
		data() {
			return {
				accordsUrl:"",
			}
		},
		methods: {
			
		},
		created() {
			var _this= this
			_this.accordsUrl = config.staticUrl+"/accords.html"
		}
	}
</script>

<style>

</style>
