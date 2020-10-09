<template>
  <div>
    <NewCard v-for="item in current_news_data" 
      :key=item.id      
      :title=item.title
      :date=item.date
      :image_url=item.cover
      :summary=item.summary
      :id=item.id
      :is_login=is_login
      style="margin: 5px;"
    >
    </NewCard>
    <el-pagination
      @current-change="handleCurrentChange"
      small
      layout="prev, pager, next"
      :total="news_total"
      :page-size="page_size"
    >
    </el-pagination>
  </div>
</template>
<script>
import NewCard from './NewCard';
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
      current_page:0, // init
      page_size:4,
    };
  },
  computed:{
    is_login:function(){
      return this.$store.state.isLogin && this.$route.path == "/admin";
    }
  },
  methods: {
    handleCurrentChange: function(cur_page){
      // el-pagination start from 1 not 0
      this.current_page = cur_page -1;
      if (!(this.current_page in this.news_data))
        this.get_data_from_api();
      this.current_news_data = this.news_data[this.current_page];
    },
    get_data_from_api:function(){
    var that = this;
    this.$axios
      .get('api/news_data/',{
          params:{
            limit: that.page_size,
            offset: that.current_page * that.page_size,
          }
        })
      .then(function (response) {
          //console.log("request!");
          that.news_data[that.current_page] = response.data.results;
          that.current_news_data = response.data.results;
          that.news_total = response.data.count;
      })
      .catch(function (error) { // 请求失败处理
        console.log(error);
        alert("get api data fail!")
      });
    }
  },
  mounted () {
    this.get_data_from_api();
  },
};
</script>

<style scoped>
</style>
