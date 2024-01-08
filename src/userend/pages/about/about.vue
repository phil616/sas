<template>
	<view>
		<web-view :src="aboutUrl"></web-view>
	</view>
</template>

<script>
	import utils from "@/utils.js";
	import config from "@/config.js"
	export default {
		data() {
			return {
				aboutUrl:"",
			}
		},
		methods: {
			
		},
		created() {
			var _this= this
			_this.aboutUrl = config.staticUrl+"/about.html"
		}
	}
</script>

<style>

</style>
