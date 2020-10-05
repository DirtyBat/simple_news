<template>
  <div class="edit-page">
    <el-input v-model="title" placeholder="请输入标题..." maxlength="20" show-word-limit>
      <template slot="prepend">标题</template>
    </el-input>
    <el-input v-model="summary" placeholder="请输入简介..." maxlength="200" show-word-limit>
      <template slot="prepend">简介</template>
    </el-input>
    <!-- 富文本编辑器 -->
    <Editor ref="editor"></Editor>
    <el-button type="primary" round style="float:right;margin-top:5px" @click="sumbmitNews">提交</el-button>
    <el-switch v-model="headline" active-text="头条" inactive-text="非头条" style="margin-top:18px;margin-right:15px;float:right"></el-switch>
  </div>
</template>

<script>
import Editor from "./Editor";
export default {
  components: {
    Editor
  },
  data() {
    return {
      title: "",
      summary: "",
      headline:false,
    };
  },
  methods: {
    sumbmitNews: function(){
       let postData = {
          title:this.title,
          summary:this.summary,
          headline:this.headline,
          content:this.$refs.editor.getContent(),
        };
        console.log(this.$refs.editor.getContent())
        this.$axios.post("api/submit_news", postData);
    },
  },
  mounted() {
    let vm = this;
    // setInterval(function(){
    //   console.log(vm.title);
    // },2500);
  }
};
</script>

<style scoped>
.edit-page {
  margin-left: 15%;
  margin-right: 15%;
}

.el-input {
  padding-bottom: 10px;
}
</style>