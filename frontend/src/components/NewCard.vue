<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <el-link :underline="false" class="title" @click="ClickToDetail">{{
          title
        }}</el-link>
        <span class="date"
          ><i class="el-icon-time">{{ " " + date }}</i></span
        >
      </div>
      <el-container>
        <el-main>
          <div class="summary">
            {{ summary }}
          </div>
        </el-main>
        <el-aside>
          <!--<img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">-->
          <a href="">
            <el-image
              v-bind:src="image_url"
              class="image"
              @click="ClickToDetail"
            ></el-image>
          </a>
        </el-aside>
      </el-container>
      <div v-if="is_login" class="login">
        <el-link :underline="false" @click="Modify">编辑</el-link>
        <el-link :underline="false" @click="Delete(id)">删除</el-link>
      </div>
    </el-card>
  </div>
</template>
<script>
export default {
  name: "NewCard",
  props: ["title", "date", "image_url", "summary", "id", "is_login"],
  data() {
    return {};
  },
  methods: {
    ClickToDetail: function () {
      this.$router.push({
        path: `/news/${this.id}`,
      });
    },
    Modify: function () {
      this.$router.push({
        path: `/edit/${this.id}`,
      });
    },
    Delete: function (new_id) {
      this.$confirm("确认删除？")
        .then((_) => {
          let postData = {
            token: this.$store.state.token,
            id: new_id,
          };
          this.$axios.post("api/delete_news", postData);
        })
        .catch((_) => {});
    },
  },
  mounted() {},
};
</script>

<style scoped>
.title {
  font-size: 18px;
  font-weight: bold;
  font-family: "PingFang SC";
}
.summary {
  font-size: 16px;
}
.date {
  float: right;
  padding: 3px 0;
  color: gray;
  font-size: 12px;
}
.image {
  width: 100%;
  height: 150px;
  max-height: 150px;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}
.box-card {
  border-radius: 8px;
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