<template>
  <div class="edit-page">
    <el-breadcrumb separator-class="el-icon-arrow-right" style="margin-bottom:13px;margin-left:3px">
      <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
      <el-breadcrumb-item>Editor</el-breadcrumb-item>
    </el-breadcrumb>
    <el-input v-model="title" placeholder="请输入标题..." maxlength="50" show-word-limit>
      <template slot="prepend">标题</template>
    </el-input>
    <el-input v-model="summary" placeholder="请输入简介..." maxlength="300" show-word-limit>
      <template slot="prepend">简介</template>
    </el-input>
    <!-- 富文本编辑器 -->
    <Editor ref="editor"></Editor>
    <el-button type="primary" round style="float:right;margin-top:5px" @click="sumbmitNews">提交</el-button>
    <el-switch
      v-model="headline"
      active-text="头条"
      inactive-text="非头条"
      style="margin-top:18px;margin-right:15px;float:right"
    ></el-switch>
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
      id:"",
      title: "",
      summary: "",
      headline: false
    };
  },
  methods: {
    sumbmitNews: function() {
      let postData = {
        id:this.id,
        title: this.title,
        summary: this.summary,
        headline: this.headline,
        content: this.$refs.editor.editorData,
      };
      this.$axios.post("api/submit_news", postData);
    },
    getNewsData: function(id) {
      if (id <= 0) {
        return;
      }
      this.$axios
        .get("api/news_detail/", {
          params: { id: id }
        })
        .then(response => {
          this.title = response.data[0].title;
          this.summary = response.data[0].summary;
          this.headline = response.data[0].headline;
          this.$refs.editor.editorData = response.data[0].content;
        });
    }
  },
  mounted() {
    this.id = this.$route.params.id;
    this.getNewsData(this.id);
  }
};
</script>

<style scoped>
.el-input {
  padding-bottom: 10px;
}
</style>