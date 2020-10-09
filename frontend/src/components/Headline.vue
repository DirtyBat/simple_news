<template>
  <el-carousel :interval="4000" type="card" height="330px" @change="setCurIndex">
    <el-carousel-item v-for="(item, index) in headlines" :key="index">
      <el-card class="card" @click.native="handleClick(index, item.id)">
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
export default {
  name: "Headline",
  components: {},
  data(){
      return{
          headlines:[],
          cur_index:null,
      }
  },
  methods: {
    handleClick: function (index, new_id) {
      //console.log(index);
      if (index == this.cur_index)
        this.$router.push({
          path: `/news/${new_id}`,
        });
    },
    setCurIndex: function (cur) {
      this.cur_index = cur
    }
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
  height: 327px;
  font-weight: bold;
  font-family: "PingFang SC";
  color: black;
}
</style>