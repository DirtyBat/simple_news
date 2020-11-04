<template>
  <div class="header">
    <img class="logo" src="@/assets/Logo.png" width="410px" />
    <!-- <span class="title">New Phase of EU-China relation for 2020-2030</span> -->
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {},
  mounted() {}
};
</script>

<style scoped>
.header {
  position: absolute; 
  line-height: 80px;
  top: 0px;
  left: 0px;
  right: 0px;
  background-color: #2d3a4b;
}

.logo {
  vertical-align: middle;
  padding: 0px 10px 0px 10px;
}

.title {
  position: absolute;
  color: white;
  font-weight: bold;
  font-size: 25px;
}
</style>