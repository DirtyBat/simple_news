<template>
  <div>
    <NewCard v-for="(item, index) in current_news_data" :key=index
      :title=item.title
      :date=item.date
      :image_url=item.cover
      :summary=item.summary
      :id=item.id
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
      current_news_data: [],
      news_total: 0,
      // page set
      current_page:0,
      page_size:3,
    };
  },
  methods: {
    handleCurrentChange: function(cur_page){
      // el-pagination start from 1 not 0
      this.current_page = cur_page -1;
      this.get_data_from_api();
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
          that.current_news_data = response.data.results;
          that.news_total = response.data.count;
      })
      .catch(function (error) { // 请求失败处理
        console.log(error);
        alert("get api data fail!")
      });
  }

  },
  computed:{},
  mounted () {
    this.get_data_from_api();
  },
};
</script>

<style scoped>
</style>
