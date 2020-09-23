<template>
    <div>
        <wordcloud
        :data="defaultWords"
        nameKey="name"
        valueKey="value"
        :color="myColors"
        :showTooltip="true"
        :wordClick="wordClickHandler">
        </wordcloud>
    </div>
</template>

<script>
import wordcloud from 'vue-wordcloud'
export default {
    components: {
        wordcloud
    },
    data() {
        return {
            myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
            defaultWords: [
                {
                    "name": "가나다라",
                    "value": 150
                },
                {
                    "name": "마바사",
                    "value": 120
                },
                {
                    "name": "아자차카",
                    "value": 98
                },
                {
                    "name": "타파하",
                    "value": 86
                },
                {
                    "name": "ABCD",
                    "value": 65
                },
                {
                    "name": "EFGH",
                    "value": 49
                },
                {
                    "name": "IJKL",
                    "value": 44
                },
                {
                    "name": "MNOP",
                    "value": 31
                },
                {
                    "name": "QRST",
                    "value": 35
                },
                {
                    "name": "UVWX",
                    "value": 215
                },
                {
                    "name": "YZ",
                    "value": 313
                },
                {
                    "name": "단어1",
                    "value": 515
                },
                {
                    "name": "단어1",
                    "value": 311
                },
                {
                    "name": "단어1",
                    "value": 152
                },
                {
                    "name": "단어2",
                    "value": 1229
                },
                {
                    "name": "단어3",
                    "value": 18
                },
                {
                    "name": "단어4",
                    "value": 16
                },
                {
                    "name": "단어5",
                    "value": 15
                },
                {
                    "name": "단어6",
                    "value": 9
                },
                {
                    "name": "단어7",
                    "value": 9
                },
                {
                    "name": "단어8",
                    "value": 9
                },
                {
                    "name": "단어9",
                    "value": 6
                }
            ]
        } 
    },
    methods: {
        wordClickHandler(name, value, vm) {
            console.log('wordClickHandler', name, value, vm);
        }
    },
}
</script>

<style>

</style>