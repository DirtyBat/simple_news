<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
      <el-breadcrumb-item>Detail</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card style="margin-top:13px">
      <div slot="header">
        <span class="title">{{title}}</span>
      </div>
      <div v-html="content" class="content"></div>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "",
      content: "",
      date: ""
    };
  },
  methods: {},
  mounted() {
    let params = {
      id: this.$route.params.id
    };
    this.$axios
      .get("api/news_detail/", {
        params
      })
      .then(response => {
        this.title = response.data[0].title;
        this.content = response.data[0].content;
        this.date = response.data[0].date;
      });
  }
};
</script>

<style scoped>
.title {
  font-weight: bold;
  font-size: 26px;
}

.content{
    margin-left:12%; 
    margin-right:12%; 
}
</style>