<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">全部</el-breadcrumb-item>
      <el-breadcrumb-item>书名</el-breadcrumb-item>
      <el-breadcrumb-item>作者</el-breadcrumb-item>
      <el-breadcrumb-item>出版社</el-breadcrumb-item>
    </el-breadcrumb>
    <div v-for="item in msg" v-bind:key="item.id" class="info">
      <el-image
        style="width: 100px; height: 100px"
        :src="item.pic"
        :preview-src-list="srcList"
      >
      </el-image>
      <div class="info-content">
        <a class="info-content-title" :href="item.url">{{
          item.title | ellipsis
        }}</a>
        <span class="info-content-item info-content-author"
          >{{ item.author }}</span
        >
        <span class="info-content-item"
          >出版社:{{ item.site | ellipsis }}</span
        >
        <span v-html="item.summary" class="info-content-item"
          >简介：{{ item.summary }}</span
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "info",
  props: ["msg"],
  filters: {
    ellipsis(value) {
      if (!value) return "";
      if (value.length > 30) {
        return value.slice(0, 30) + "...";
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
      result: [
      ],
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

<style scoped>
.el-breadcrumb__item {
  padding: 25px;
}
.info {
  width: 700px;
  height: 150px;
  display: flex;
  flex-direction: row;
}

.info-content {
  width: 500px;
  height: 100%;
  display: flex;
  flex-direction: column;
  margin-left: 20px;
}

.info-content-item {
  font-size: 12px;
  color: grey;
}

.info-content-title {
  color: black;
  font-size: 22px;
}
.info-content-item{
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>
