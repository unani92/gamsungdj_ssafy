<template>
<g-signin-button
    v-if="isEmpty(user)"
    :params="googleSignInParams"
    @success="onGoogleSignInSuccess"
    @error="onGoogleSignInError"
>
    <div id="googleBtn">
        <div><img :src="require('@/assets/img/user/google_logo.png')" alt="google_logo_img" style="margin-left: -5px; width: 20px;"/></div>
        <div style="width:80%;">구글 로그인</div>
    </div>
</g-signin-button>
</template>

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
        ...mapActions(['setAuth', 'setUser']),
        // 구글 로그인
        onGoogleSignInSuccess (response) {
            const token = response.wc.access_token
            axios.post(baseURL+"accounts/google/", {
                access_token: token
            })
            .then(resp => {
                console.log(resp)
                this.setAuth("token " + resp.data.token)
                console.log(resp.data.user)
                this.setUser(resp.data.user)
                
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
    }
}
</script>

<style>
#googleBtn {
    
    border: none;
    border-radius: 6px;
    
    display: flex;
    justify-content: space-between;
    align-items: center;
}

</style>