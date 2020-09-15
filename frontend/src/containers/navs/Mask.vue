<template>
    <div class="row aligner">
        <div class="col-sm-6 aligner">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/vDODJCJFRSo" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen></iframe>
        </div>
        <div class="col-sm-6 aligner">
            <h1>Play List</h1>
        </div>
    </div>
</template>

<script>
export default {
    mounted(){
        this.wrapWindowByMask()
    },
    methods:{
        wrapWindowByMask(){
        }
    }
}
</script>
<style>
.aligner {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0px;
}
</style>