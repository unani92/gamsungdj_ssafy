<template>
<div>
<b-modal v-model="showJoin" id="modalbackdrop" ref="modalbackdrop" title="회원가입"
        :hide-header-close="true"
        :no-close-on-backdrop="selectedBackdrop=='false'"
        centered>
    <b-row>
        <b-form class="form-container">
            <div class="avatar-wrapper mb-3" @click="uploadImg">
                <b-avatar v-if="!avatar" size="150" class="profile-pic"></b-avatar>
                <b-avatar v-else size="150" class="profile-pic" id="changeImg" :src="avatarURL"></b-avatar>
                <b-form-file v-model="avatar" id="file-upload" accept="image/jpeg, image/png, image/gif" @change="onChangeImg"/>
            </div>
            <b-form-group label="닉네임" label-for="username-input"> 
                <b-form-input v-model="username" id="username-input"></b-form-input>
            </b-form-group>
            <b-form-group label="성별">
                <v-select v-model="gender" :options="genderData" :reduce="genderData=>genderData.value" />
            </b-form-group>
            <b-form-group label="나이">
                <v-select v-model="age" :options="ageData" :reduce="ageData=>ageData.value" />
            </b-form-group>
        </b-form>
    </b-row>
    <template slot="modal-footer">
        <b-button variant="primary" @click="submit('modalbackdrop')" class="mr-1">작성완료</b-button>
        <b-button variant="secondary" @click="hideModal('modalbackdrop')">취소</b-button>
    </template>
</b-modal>
</div>
</template>

<script>
import httpUser from'@/utils/http-user'
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import { mapActions } from 'vuex'
export default {
    components: {
        'v-select': vSelect
    },
    props: ['showJoin', 'username'],
    data() {
        return {
            selectedBackdrop: 'false',
            gender: '',
            age: '',
            avatar: null,
            avatarURL: '',
            genderData: [
                {
                    label: "남성",
                    value: "M"
                },
                {
                    label: "여성",
                    value: "F"
                },
            ],
            ageData: [
                {
                    label: "10세 이하",
                    value: "0"
                },
                {
                    label: "10대",
                    value: "1"
                },
                {
                    label: "20대",
                    value: "2"
                },
                {
                    label: "30대",
                    value: "3"
                },
                {
                    label: "40대",
                    value: "4"
                },
                {
                    label: "50세 이상",
                    value: "5"
                }
            ]
        }
    },
    methods: {
        ...mapActions(['setUser']),
        hideModal (refname) {
            this.showJoin = false   
            this.$emit("hideModal")      
        },
        uploadImg() {
            const fileUpload = document.getElementById('file-upload')
            fileUpload.click();
        },
        onChangeImg(e) {
            const file = e.target.files[0]; // Get first index in files
            this.avatarURL = URL.createObjectURL(file); // Create File URL
        },
        submit(refname) {
            if (this.avatar !== null) {
                const joinInfo = new FormData()
                joinInfo.append("avatar", this.avatar)
                joinInfo.append("gender",this.gender)
                joinInfo.append("age", this.age)
                joinInfo.append("is_signed_up", true)
                joinInfo.append("nickname", this.username)
                this.postData(joinInfo, refname)
            }
            else {
                const joinInfo = {
                    "nickname": this.username,
                    "gender": this.gender,
                    "age": this.age,
                    "is_signed_up":true
                }
                this.postData(joinInfo, refname)
            }
            
            
        },
        postData(joinInfo, refname) {
            if (this.gender != "" && this.age !="") {
                httpUser.post('', joinInfo, {
                    headers: {
                        Authorization: this.$store.state.authorization,
                    }
                })
                .then(res => {
                    this.setUser(res.data)
                    this.hideModal(refname)
                })
                .catch(res => {
                    console.log(res)
                })
            }
            else if (this.gender == "" && this.age != "") {
                alert("성별을 선택하세요.")
            }
            else if (this.gender != "" && this.age == "") {
                alert("나이를 선택하세요.")
            }
            else {
                alert("성별과 나이는 필수정보입니다. 정보를 입력해주세요")
            }
        }

    }

}
</script>

<style scoped>
.form-container {
    width: 100%;
}
.avatar-wrapper{
	position: relative;
	height: 150px;
	width: 150px;
	margin: auto;
	border-radius: 50%;
	overflow: hidden;
	box-shadow: 1px 1px 15px -5px black;
	transition: all .3s ease;
	cursor:pointer;
}
.avatar-wrapper:hover {
    opacity: 0.5;
}

</style>