<template>
  <el-dialog title="管理员登录" :visible="!this.$store.state.isLogin" width="30%">
    <el-input v-model="password">
      <template slot="prepend">密码</template>
    </el-input>
    <span slot="footer" class="dialog-footer">
      <el-button type="primary" @click="login">确认</el-button>
    </span>
  </el-dialog>
</template>

<script>
export default {
  data() {
    return {
      password: ""
    };
  },
  methods: {
    getNowDate: function() {
      let date = new Date();
      return date.getFullYear() + "-" + date.getMonth() + "-" + date.getDate();
    },
    login: function() {
      console.log(this.$store);
      let params = {
        password: this.password
      };
      this.$axios
        .get("api/get_token", {
          params
        })
        .then(response => {
          localStorage.setItem("token", response.data.token);
          localStorage.setItem("tokenDate", this.getNowDate());
          this.$store.commit("setLogin", response.data.token);
          this.$message({
            message: "登录成功",
            type: "success"
          });
        });
    },
    checkLoginState: function() {
      let token = localStorage.getItem("token");
      let tokenDate = localStorage.getItem("tokenDate");
      if (token == null) {
        return;
      }
      if (tokenDate == null || tokenDate !== this.getNowDate()) {
        return;
      }
      this.$store.commit("setLogin", token);
    }
  },
  created() {
    this.checkLoginState();
  }
};
</script>

<style scoped>
</style>