<template>
  <el-carousel :interval="4000" type="card" height="330px">
    <el-carousel-item v-for="(item, index) in headlines" :key="index" @click='handleClick(index, item.id)'>
      <el-card class="card">
        <el-image
          v-bind:src="item.cover"
          class="image"
        >
        </el-image>
        {{item.title}}
      </el-card>
    </el-carousel-item>
  </el-carousel>
</template>
<script>
import Vue from "vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import App from "../App.vue";
export default {
  name: "Headline",
  components: {},
  data(){
      return{
          headlines:[]
      }
  },
  methods: {
    handleClick: function (index, new_id) {
      console.log(new_id);
      this.$router.push({
        path: `/news/${new_id}`,
      });
    },
  },
  mounted() {
    var that = this;
    this.$axios
      .get("api/news_data/", {
        params: {
          headline: "true",
        },
      })
      .then(function (response) {
        //console.log("request!");
        that.headlines = response.data;
      })
      .catch(function (error) {
        // 请求失败处理
        console.log(error);
        alert("get api data of headlines fail!");
      });
  },
};
</script>
<style>
.image {
  width: 100%;
  height: 250px;
  max-height: 250px;
}
.card {
  height: 325px;
  font-weight: bold;
  font-family: "PingFang SC";
  color: black;
}
</style>