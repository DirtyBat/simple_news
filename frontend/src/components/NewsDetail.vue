<template>
  <div>
    <Header></Header>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
      <el-breadcrumb-item>Detail</el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script>
import Header from "./Header";
export default {
  components: {
    Header
  },
  data() {
    return {};
  },
  methods: {},
  mounted() {}
};
</script>

<style scoped>
</style>