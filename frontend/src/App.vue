<template>
  <div class="h-100">
    <router-view />
    <color-switcher style="display:none" />
  </div>
</template>

<script>
import ColorSwitcher from "./components/Common/ColorSwitcher";


export default {
  components: {
    "color-switcher": ColorSwitcher
  }
}
</script>
