<template>
  <!-- <img :src="require('@/assets/img/user/kakao_login_large_narrow.png')" alt="kakao_login_button" @click="kakaoLogin" style="width:190px !importnat;"/> -->
  <div @click="kakaoLogin">
      <b-icon icon="chat-fill" variant="warning" style="margin-left: -5px; width: 20px;"></b-icon>
      <span style="margin-left:5px;">카카오 로그인</span>
  </div>
</template>

<script src="https://developers.kakao.com/sdk/js/kakao.js"></script>
<script>
const baseURL = "http://localhost:8000/"
import axios from 'axios'
import { mapActions } from 'vuex'
export default {

    methods: {
        ...mapActions(['setAuth', 'setUser']),
        // 카카오 로그인
        kakaoLogin() {
            window.Kakao.Auth.login({
                scope: 'account_email',
                success: this.getKaKaoInfo,
                fail: function(error) {
                    console.log(error);
                },
            })  
        },
        getKaKaoInfo(authInfo) {
            axios.post(baseURL + "accounts/kakao/", { access_token: authInfo.access_token})
            .then(response => {
                console.log(response)
                this.setAuth("token " + response.data.token) 
                this.setUser(response.data.user)
            })
        },
    },
    created() {
        if (!window.Kakao.isInitialized()) {
            Kakao.init(process.env.VUE_APP_KAKAO_APP_KEY)
            console.log(window.Kakao.isInitialized())
        }
    }
}
</script>

<style>

</style>