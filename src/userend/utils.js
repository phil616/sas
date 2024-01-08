
import {Base64} from '@/Base64.js';
export default{
	getLoginInfo(){
		var result = uni.getStorageSync("token")
		return result
	},
	getCommonOAuth2Header(){
		var result = uni.getStorageSync("token")
		if (result != "")
			return {"Authorization":"Bearer " + result}
		else
			return {}
	},
	removeLoginInfo(){
		// 删除token,openid,username,status等信息
	},
	verifyTokenExp(){
		var token = uni.getStorageSync("token")
		if (token=="" || token==undefined) {
			uni.removeStorage({
				key:"token"
			})
			return false
		}
		let strings = token.split("."); //截取token，获取载体
		var userinfo = JSON.parse(  // 按照jwt标准解析jwt头部信息
			Base64.decode(strings[1].replace(/-/g, "+").replace(/_/g, "/"))
		); 
		uni.setStorage({
			key:"usr_name",
			data:userinfo.usr,
		});
		var timestamp=new Date().getTime();
		let expTime = 0
		let curTime = 0
		expTime = userinfo.exp*1000
		curTime = timestamp
		if (curTime > expTime) return false;
		else return true
	},

}