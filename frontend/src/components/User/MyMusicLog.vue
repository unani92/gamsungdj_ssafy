<template>
<div>
    페이지 준비중입니다.
</div>
  
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import http from '@/utils/http-common'
export default {
    data() {
        return {
            logs: []

        }
    },

    computed: {
        ...mapState(['user']),
        ...mapGetters(['config'])
    },
    created() {
        http.get('log/',{}, this.config)
        .then((res) => {
            this.logs = res.data
        })
    }

}
</script>

<style>

</style>