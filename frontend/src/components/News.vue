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
      news_data: null,
      // page set
      current_page:0,
      page_size:3,
    };
  },
  methods: {
    handleCurrentChange: function(cur_page){
      // el-pagination start from 1 not 0
      this.current_page = cur_page -1;
    }
  },
  computed:{
    current_news_data: function(){
      if (this.news_data)
        return this.news_data.slice(this.current_page * this.page_size,
        (this.current_page + 1) * this.page_size)
    },
    news_total: function(){
        return this.news_data?this.news_data.length:0;
    }
  },
  mounted () {
    this.$axios
      .get('api/news_data/')
      .then(response => (this.news_data = response.data))
      .catch(function (error) { // 请求失败处理
        console.log(error);
        alert("get api data fail!")
      });
  }
};
</script>

<style scoped>
</style>
