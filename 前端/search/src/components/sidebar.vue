<template>
  <div class="sidebar">
    <div class="book-title">
      <span class="label am-text-nowrap">书籍推荐</span>
    </div>
    <ul
      id="“suggest-book”"
      class="suggest"
      v-for="item in suggest_books"
      :key="item.id"
    >
      <a :href="item.url" style="font-size: 15px">{{
        item.title | ellipsis
      }}</a>
    </ul>
    <br />
    <div class="source-title">
      <span class="label am-text-nowrap">其它资源</span>
    </div>
    <ul
      id="“suggest-source"
      class="suggest"
      v-for="item in suggest_source"
      :key="item.id"
    >
      <a :href="item.url" style="font-size: 15px">{{
        item.title | ellipsis
      }}</a>
    </ul>
  </div>
</template>
<script>
export default {
  name: "sidebar",
  props: ["suggest_source", "suggest_books"],
  filters: {
    ellipsis(value) {
      if (!value) return "";
      if (value.length > 25) {
        return value.slice(0, 25) + "...";
      }
      return value;
    },
    ellipsisTitle(value) {
      if (!value) return "";
      if (value.length > 15) {
        // 截取长度
        return value.slice(0, 15) + "...";
      }
      return value;
    },
  },
  data: function () {
    return {
      result: [],
    };
  },
  methods: {
    //在当前组件内调用
  },

  computed: {
    //在在当前组件内调用
  },
};
</script>


<style>
a {
  color: #333;
  font-family: "Microsoft YaHei", sans-serif, "Lucida Grande", Helvetica, Arial,
    FreeSans, Arimo, "Droid Sans", "wenquanyi micro hei", "Hiragino Sans GB",
    "Hiragino Sans GB W3", FontAwesome, sans-serif;
}
/* .hh {
  margin-top: 40px;
} */
.suggest-book .suggest-source {
  /* margin-inline: -10px; */
  margin-bottom: -10px;
}
.sidebar {
  margin-top: 20px;
}
.suggest {
  height: 30px;
}
.label {
  background-color: #999;
  color: #fff !important;
  border-radius: 20 px;
  padding: 2 px 14 px;
  text-align: center;
}
.am-text-nowrap {
  white-space: nowrap;
}
</style>