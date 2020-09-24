<template>
  <app-layout>
    <router-view :key="$route.fullPath" />
  </app-layout>
</template>

<script>
import AppLayout from "../../layouts/AppLayout";

export default {
  components: {
    "app-layout": AppLayout
  }
};
</script>
