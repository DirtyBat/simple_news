<template>
  <div>
    <NewCard v-for="(item, index) in news_data" :key=index
      :title=item.title
      :date=item.date
      :image_url=item.cover
      :summary=item.summary
      :id=item.id
      style="margin: 5px;"
    >
    </NewCard>
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
    };
  },
  methods: {},
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
