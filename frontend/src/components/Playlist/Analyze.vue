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