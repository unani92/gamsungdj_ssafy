<template>
<div>
    Login
    <div>
        <br>
        <img :src="require('@/assets/img/user/kakao_login_large_narrow.png')" width="150" alt="kakao_login_button" @click="kakaoLogin"/>
        <g-signin-button
            v-if="isEmpty(user)"
            :params="googleSignInParams"
            @success="onGoogleSignInSuccess"
            @error="onGoogleSignInError"
          >
            <button id="googleBtn">
                <div width="20%"><img :src="require('@/assets/img/user/google_logo.png')" width="25px" alt="google_logo_img"/></div>
                <div style="width:80%;">구글 로그인</div>
            </button>
          </g-signin-button>
        
    </div>
   
</div>
</template>

<script src="https://developers.kakao.com/sdk/js/kakao.js"></script>
<script>
const baseURL = "http://localhost:8000/"
import axios from 'axios'
import { mapActions } from 'vuex'
export default {
    data() {
        return {
            googleSignInParams: {
                client_id: process.env.VUE_APP_GOOGLE_CLIENT_ID
            },
            googleForm: '',
            user: []

        }
    },
    methods: {
        ...mapActions(['setAuth']),
        // 구글 로그인
        onGoogleSignInSuccess (response) {
            const token = response.wc.access_token
            axios.post(baseURL+"accounts/google/", {
                access_token: token
            })
            .then(resp => {
                console.log(resp)
                this.setAuth("token " + resp.data.token)
                
            })
            .catch(err => {
                console.log(err.response)
            })
        },
        onGoogleSignInError (error) {
            console.log('OH NOES', error)
        },
        isEmpty (obj) {
            return Object.keys(obj).length === 0
        },
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
                this.setAuth("token " + response.data.token)  
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

<style scoped>
#googleBtn {
    
    
    border: none;
    border-radius: 6px;
    background-color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>