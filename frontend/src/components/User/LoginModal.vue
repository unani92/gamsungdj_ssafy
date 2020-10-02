<template>
<div>
    <b-modal v-model="showLogin" id="modalbackdrop" ref="loginmodal" title="로그인"
            :no-close-on-backdrop="true"
            :hide-header-close="true"
            centered>
        <b-row style="justify-content: center;">
            <div>
            <g-signin-button
                v-if="isEmpty(user)"
                :params="googleSignInParams"
                @success="onGoogleSignInSuccess"
                @error="onGoogleSignInError"
            >
                <div id="googleBtn">
                    <div><img :src="require('@/assets/img/user/google_logo.png')" alt="google_logo_img" style="margin-left: 10px; width: 30px;"/></div>
                    <div id="googleBtnText">구글 로그인</div>
                </div>
            </g-signin-button>

            <img :src="require('@/assets/img/user/kakao_login_large_narrow.png')" alt="kakao_login_button" @click="kakaoLogin" style="width:200px; margin-top:10px; cursor: pointer;"/>
            </div>
        </b-row>
        <template slot="modal-footer">
            <b-button variant="secondary" @click="hideModal('loginmodal')">취소</b-button>
        </template>
    </b-modal>
    <JoinForm :showJoin="showJoin" :username="username" @hideModal="hideModal"/>
</div>
</template>

<script src="https://developers.kakao.com/sdk/js/kakao.js"></script>
<script>
import JoinForm from './JoinForm.vue'
import httpUser from'@/utils/http-user'
import axios from 'axios'
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
    components: {
        JoinForm
    },
    props: ['showLogin'],
    data() {
        return {
            showJoin: false,
            googleSignInParams: {
                client_id: process.env.VUE_APP_GOOGLE_CLIENT_ID
            },
            user: [],
            username: ''
        }
    },
    methods: {
        ...mapActions(['setAuth', 'setUser', 'setPlayList']),
        // 구글 로그인
        onGoogleSignInSuccess (response) {
            const token = response.wc.access_token
            console.log(response)
            httpUser.post("google/", {
                access_token: token
            })
            .then(resp => {
                console.log(resp)
                this.setAuth("JWT " + resp.data.token)
                this.createUserProfile(resp)

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
            httpUser.post("kakao/", { access_token: authInfo.access_token })
            .then(response => {
                console.log(response)
                this.setAuth("JWT " + response.data.token)
                this.createUserProfile(Response)
            })
        },
        // 회원가입시 프로필 생성
        createUserProfile(auth) {
            httpUser.get('', this.config)
            .then(res => {
                if (res.data.data.is_signed_up) {
                    this.setUser(res.data.data)
                    this.setPlayList(res.data.playlists)
                    this.hideModal('loginmodal')
                }
                else {
                    console.log(res.data)
                    this.joinForm(res.data.data.username)
                }
            })
        },
        joinForm(username) {
            this.username = username
            this.showJoin = true
            this.$emit("hideModal")
        },
        hideModal (refname) {
            this.showJoin = false
            this.showLogin = false
            this.$emit("hideModal")
        },

    },
    computed: {
        ...mapState(['authorization']),
        ...mapGetters({config: 'config'})
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
    height: 49px;
    border: none;
    border-radius: 6px;
    background-color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
}
#googleBtnText {
    margin-left: -10px;
    width:90%;
    text-align: center;
    font-size: 16.5px;
    color: rgb(29, 2, 2);
}

</style>
