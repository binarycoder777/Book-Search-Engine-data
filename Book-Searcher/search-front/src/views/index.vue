<template>
  <el-container>
    <el-header>
      <div class="logo-header">
        <a>
          <img src="../img/2.jpg" />
        </a>
      </div>
      <el-breadcrumb separator="|" class="login">
        <el-breadcrumb-item :to="{ path: '/' }">书架</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/' }">书城</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/' }">出版社</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/' }">APP</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/' }"></el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>
    <el-main>
      <div class="logo">
        <a>
          <img src="../img/1.jpg" />
        </a>
      </div>
      <div class="search">
        <el-autocomplete
          class="inline-input"
          v-model="state1"
          :fetch-suggestions="querySearch"
          placeholder="请输入内容"
          @select="handleSelect"
          @input="suggestPrefix"
          style="width: 660px"
        ></el-autocomplete>
        <el-button type="primary" icon="el-icon-search" @click="searchInfo"
          >搜索</el-button
        >
      </div>
    </el-main>
    <el-footer>
      <div class="home-foot" style="height: 60px">
        <!-- <div> -->
        Copyright ©2021&nbsp;&nbsp;<a href="">BookAsk 书问</a>
        &nbsp;&nbsp;|&nbsp;&nbsp;<a
          href="javascript:void(0)"
          onclick="AddFavorite(window.location,document.title)"
          >收藏书问</a
        >
        &nbsp;&nbsp;|&nbsp;&nbsp;<a href="/sitemap.html">网站地图</a>
        &nbsp;&nbsp;|&nbsp;&nbsp;<a href="/about/us.html">关于我们</a>
        &nbsp;&nbsp;|&nbsp;&nbsp;<a href="/about/friend.html">合作伙伴</a>
        &nbsp;&nbsp;|&nbsp;&nbsp;<a href="/about/cooperation.html">商务合作</a>
        &nbsp;&nbsp;|&nbsp;&nbsp;<a href="/about/link.html">友情链接</a>
        &nbsp;&nbsp;|&nbsp;&nbsp;<a href="/about/recruit.html">书问招聘</a>
        <!-- </div> -->
      </div>
    </el-footer>
  </el-container>
</template>



<script>
const axios = require("axios");

export default {
  data() {
    return {
      restaurants: [],
      state1: "",
      state2: "",
    };
  },
  methods: {
    async querySearch(queryString, cb) {
      // let restaurants = []
       this.restaurants = await this.loadAll(queryString);
      // 调用 callback 返回建议列表的数据
      this.restaurants = this.restaurants.data;
      // console.log(restaurants);
      cb(this.restaurants);
    },
    createFilter(queryString) {
      return (restaurant) => {
        return (
          restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) ===
          0
        );
      };
    },
    loadInfo(item) {
      return axios({
        // 默认请求方式为get
        method: "get",
        url: "http://localhost:8081/book/search",
        // 传递参数
        params: {
          keyword: item,
        },
        responseType: "json",
      });
    },
    async queryInfo() {
      var a = await this.loadInfo(this.state1);
      this.msg = a.data;
    },
    async searchInfo() {
      await this.queryInfo();
      sessionStorage.setItem("key", this.state1);
      // console.log(ans)
      // var res = await this.loadInfo()
      this.$router.push({
        //核心语句
        path: "/display", //跳转的路径
        // query: {
        //   //路由传参时push和query搭配使用 ，作用时传递参数
        //   keyworld: this.msg,
        //   k: this.state1,
        // },
      });
    },
    loadAll(item) {
      return axios({
        // 默认请求方式为get
        method: "get",
        url: "http://localhost:8081/book/suggest",
        // 传递参数
        params: {
          prefix: item,
        },
        responseType: "json",
      });
    },
    handleSelect(item) {
      // console.log(item);
    },
    suggestPrefix(item) {
      // console.log(item);
    },
  },
};
</script>




<style>
.inline-input .el-input__inner {
  height: 50px;
  line-height: 50px;
}
</style>


<style scoped>
a {
  color: #ffffff;
  font-size: 15px;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.home-foot {
  height: 40px;
  width: 1520px;
  margin-left: -100px;
  margin-top: 10px;
  background: #666666;
  color: #ffffff;
  font-size: 18px;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.el-input {
  width: 50px;
}

.el-button {
  height: 50px;
}

.el-input__inner {
  height: 50px;
  line-height: 50px;
}

.logo {
  height: 30px;
}
.logo img {
  width: 400px;
  height: 70px;
}

/* .search .el-input__inner .el-button{
  float: left;
  margin-left: 25%;
} */

.login {
  margin-top: 20px;
  margin-left: 100px;
  float: left;
}
.el-breadcrumb__item {
  width: 100px;
}
.el-breadcrumb__separator {
  font-size: 20px;
}

.logo-header {
  /* margin-top: 30px; */
  float: left;
}
.logo-header img {
  width: 60px;
  height: 60px;
}

.el-header,
.el-footer {
  background-color: #fff;
  color: #333;
  text-align: center;
  line-height: 80px;
}

.el-main {
  background-color: #f9f9f9;
  color: #333;
  text-align: center;
  line-height: 500px;
  height: 565px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>