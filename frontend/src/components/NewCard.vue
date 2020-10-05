<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>{{title}}</span>
        <span style="float: right; padding: 3px 0; color: gray; ">{{date}}</span>
      </div>
      <el-container>
        <el-aside>
          <!--<img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">-->
          <img v-bind:src="image_url" class="image">
        </el-aside>
        <el-main>
          <div class="text">
            {{summary}}
          </div>
      </el-main>
      </el-container>
    </el-card>
  </div>
</template>
<script>
import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from '../App.vue';
export default {
  name: "NewCard",
  props: ["title", "date", "image_url", "summary", "id"],
  data() {
    return {};
  },
  methods: {},
  mounted() {}
};
</script>

<style scoped>
  .text {
    font-size: 14px;
  }
  .image{
    width: 100%;
    max-height:270px;
    max-width:480px;
    display: block;
  }
  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }
  .box-card {
    width: 800px;
  }
  .el-aside {
    width: 480px;
  }
  /*
  .el-main {
    color: #333;
  }
  */
</style>