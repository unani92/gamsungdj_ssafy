<template>
<div>
<b-modal v-model="showJoin" id="modalbackdrop" ref="modalbackdrop" :title="$t('회원가입')"
        :hide-backdrop="selectedBackdrop=='false'"
        :no-close-on-backdrop="selectedBackdrop=='false'">
    <b-row>
    <b-form class="form-container">
            <b-form-file v-model="avatar" accept="image/jpeg, image/png, image/gif" class="mb-3"></b-form-file>
            <b-form-group :label="$t('성별')">
                <v-select v-model="gender" :options="genderData" :reduce="genderData=>genderData.value" />
            </b-form-group>
            <b-form-group :label="$t('나이')">
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
const baseURL = "http://localhost:8000/api/"
import axios from 'axios'
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import { mapActions } from 'vuex'
export default {
    components: {
        'v-select': vSelect
    },
    props: ['showJoin'],
    data() {
        return {
            selectedBackdrop: 'false',
            gender: '',
            age: '',
            avatar: '',
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
        
        submit(refname) {
            this.hideModal(refname)
            const joinInfo = {
                "avatar": this.avatar,
                "gender": this.gender,
                "age": this.age,
            }
            axios.post(baseURL + "accounts/", joinInfo, {
                    headers: {
                        Authorization: this.$store.state.authorization,
                    }
                })
                .then(res => {
                    this.setUser(res.data)
                })
                .catch(res => {

                })
        },

    }

}
</script>

<style scoped>
.form-container {
    width: 100%;
}

</style>