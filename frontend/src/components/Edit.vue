<template>
  <div class="edit-page">
    <Login></Login>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="margin-bottom:13px;margin-left:3px">
      <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
      <el-breadcrumb-item>Edit</el-breadcrumb-item>
    </el-breadcrumb>
    <el-input v-model="title" placeholder="请输入标题..." maxlength="50" show-word-limit>
      <template slot="prepend">标题</template>
    </el-input>
    <el-input v-model="summary" placeholder="请输入简介..." maxlength="300" show-word-limit>
      <template slot="prepend">简介</template>
    </el-input>
    <!-- 富文本编辑器 -->
    <Editor ref="editor"></Editor>
    <div class="option-bar">
      <el-switch v-model="headline" active-text="头条" inactive-text="非头条"></el-switch>
      <el-select v-model="selectedType" placeholder="请选择文章分类">
        <el-option v-for="(type,index) in types" :key="index" :label="type" :value="type"></el-option>
      </el-select>
      <el-button type="primary" :loading="uploading" round @click="sumbmitNews">提交</el-button>
    </div>
  </div>
</template>

<script>
import Editor from "./Editor";
import Login from "./Login";
export default {
  components: {
    Editor,
    Login
  },
  data() {
    return {
      id: "",
      title: "",
      summary: "",
      uploading: false,
      headline: false,
      selectedType: "The project",
      types: [
        "The project",
        "Researchers",
        "About China-EU relations",
        "Project conferences and seminars",
        "Results"
      ]
    };
  },
  methods: {
    sumbmitNews: function() {
      this.uploading = true;
      let postData = {
        token: this.$store.state.token,
        id: this.id,
        title: this.title,
        summary: this.summary,
        headline: this.headline,
        content: this.$refs.editor.editorData,
        types: this.selectedType
      };
      this.$axios.post("api/submit_news", postData).then(response => {
        window.location = process.env.API_ROOT + "news/" + this.id;
      });
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

.option-bar {
  line-height: 40px;
  height: 40px;
  float: right;
  word-spacing: 10px;
}
</style>