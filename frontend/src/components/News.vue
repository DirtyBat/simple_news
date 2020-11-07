<template>
  <div>
    <el-tabs v-model="newsType" @tab-click="newsTypeChange">
      <el-tab-pane label="The project" name="The project"></el-tab-pane>
      <el-tab-pane label="Researchers" name="Researchers"></el-tab-pane>
      <el-tab-pane label="About China-EU relations" name="About China-EU relations"></el-tab-pane>
      <el-tab-pane label="Conferences and seminars" name="Conferences and seminars"></el-tab-pane>
      <el-tab-pane label="Results" name="Results"></el-tab-pane>
    </el-tabs>
    <NewCard
      v-for="item in current_news_data"
      :key="item.id"
      :title="item.title"
      :date="item.date"
      :image_url="item.cover"
      :summary="item.summary"
      :id="item.id"
      :is_login="is_login"
      style="margin-bottom: 5px;"
    ></NewCard>
    <el-pagination
      @current-change="handleCurrentChange"
      small
      layout="prev, pager, next"
      :total="news_total"
      :page-size="page_size"
    ></el-pagination>
  </div>
</template>
<script>
import NewCard from "./NewCard";
export default {
  name: "news",
  components: { NewCard },
  data() {
    return {
      // api get data
      news_data: new Array(),
      news_total: 0,
      current_news_data: [],
      // page set
      current_page: 0, // init
      page_size: 4,
      newsType: "The project"
    };
  },
  computed: {
    is_login: function() {
      return this.$store.state.isLogin && this.$route.path == "/admin";
    }
  },
  methods: {
    handleCurrentChange: function(cur_page) {
      // el-pagination start from 1 not 0
      this.current_page = cur_page - 1;
      if (!(this.current_page in this.news_data)) {
        this.get_data_from_api({
          types: this.newsType,
          limit: this.page_size,
          offset: this.current_page * this.page_size
        });
      }
      this.current_news_data = this.news_data[this.current_page];
    },
    get_data_from_api: function(params) {
      var that = this;
      this.$axios
        .get("api/news_data/", {
          params
        })
        .then(function(response) {
          //console.log("request!");
          that.news_data[that.current_page] = response.data.results;
          that.current_news_data = response.data.results;
          that.news_total = response.data.count;
        })
        .catch(function(error) {
          // 请求失败处理
          console.log(error);
          alert("get api data fail!");
        });
    },
    newsTypeChange: function(tag, event) {
      this.get_data_from_api({
        types: this.newsType,
        limit: this.page_size,
        offset: this.current_page * this.page_size
      });
    }
  },
  mounted() {
    this.get_data_from_api({
      types: this.newsType,
      limit: this.page_size,
      offset: this.current_page * this.page_size
    });
  }
};
</script>

<style scoped>
</style>
