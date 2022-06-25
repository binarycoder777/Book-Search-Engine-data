<template>
  <el-container>
    <el-header class="header">
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
          style="width: 450px"
        ></el-autocomplete>
        <el-button @click="queryInfo" type="primary" icon="el-icon-search"
          >搜索</el-button
        >
      </div>

      <el-breadcrumb separator="|" class="login">
        <el-breadcrumb-item :to="{ path: '/' }">书架</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/' }">书城</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/' }">出版社</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/' }">登录</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/' }"></el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>
    <el-container>
      <el-aside width="400px">
        <sidebar :suggest_books="suggest_books" :suggest_source="suggest_source"></sidebar>
      </el-aside>
      <el-container>
        <el-main>
          <info :msg="msg"></info>
        </el-main>
        <el-footer>
          <el-pagination
            background
            layout="prev, pager, next"
            :total="total"
            :current-page.sync="current"
            :page-size.sync="size"
            :page-sizes="[5, 10, 50, 100]"
            @size-change="sizeList"
            @current-change="getTableList"
          >
          </el-pagination>
        </el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>




<script>
const axios = require("axios");
import sidebar from "../components/sidebar.vue";
import info from "../components/info.vue";

export default {
  components: { sidebar, info },
  data() {
    return {
      restaurants: [],
      state1: "",
      state2: "",
      msg: [],
      total: 100,
      size: 10,
      current: 1,
      suggest_books: [],
      suggest_source: [],
    };
  },
  methods: {
    sizeList() {
      this.current = 1;
      this.getTableList();
    },
    getTableList() {
      const { current, size } = this;
      const params = {
        current,
        size,
      };
      this.queryInfo();
    },
    async querySearch(queryString, cb) {
      let restaurants = await this.loadAll(queryString);
      // 调用 callback 返回建议列表的数据
      restaurants = restaurants.data;
      // 调用 callback 返回建议列表的数据
      cb(restaurants);
    },
    createFilter(queryString) {
      return (restaurant) => {
        return (
          restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) ===
          0
        );
      };
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
    queryInfo() {
      sessionStorage.setItem("key", this.state1);
      // 查询书籍
      this.axios
        .get("http://localhost:8081/book/search", {
          params: {
            keyword: this.state1,
            pageSize: this.size,
            pageIndex: this.current,
          },
        })
        .then((res) => {
          res = res.data;
          this.msg = res.content;
          this.total = res.totalElements;
          this.current = res.number + 1;
          this.size = res.size;
          // console.log(this.msg);
        });
      // 建议书籍
      this.axios
        .get("http://localhost:8081/book/suggest/doc", {
          params: {
            prefix: this.state1,
          },
        })
        .then((res) => {
          // res = res.data;
          this.suggest_books = res.data;
          // console.log("+++++++" + this.suggest_books);
        });
      // 建议资源
      this.axios
        .get("http://localhost:8081/book/suggest/source", {
          params: {
            prefix: this.state1,
          },
        })
        .then((res) => {
          // res = res.data;
          this.suggest_source = res.data;
          // console.log("+++++++" + this.suggest_books);
        });
    },
    handleSelect(item) {
      // console.log(item);
    },
    suggestPrefix(item) {
      // console.log(item);
    },
  },
  created() {
    this.state1 = sessionStorage.getItem("key");
    // console.log("=============="+this.state1);
    this.axios
      .get("http://localhost:8081/book/search", {
        params: {
          keyword: this.state1,
          pageSize: this.size,
          pageIndex: this.current,
        },
      })
      .then((res) => {
        res = res.data;
        this.msg = res.content;
        this.total = res.totalElements;
        this.current = res.number + 1;
        this.size = res.size;
      });
    // 建议书籍
    this.axios
      .get("http://localhost:8081/book/suggest/doc", {
        params: {
          prefix: this.state1,
        },
      })
      .then((res) => {
        // res = res.data;
        this.suggest_books = res.data;
        // console.log("+++++++" + this.suggest_books);
      });
    // 建议资源
    this.axios
      .get("http://localhost:8081/book/suggest/source", {
        params: {
          prefix: this.state1,
        },
      })
      .then((res) => {
        // res = res.data;
        this.suggest_source = res.data;
        console.log("===========" + this.suggest_source[0].title);
      });
  },
  // mounted() {
  //   this.msg = this.$route.query.keyworld;
  //   // console.log(this.msg)
  //   // console.log(this.state1)
  // },
};
</script>



<style scoped>
.logo {
  /* position: absolute; */
  float: left;
  margin-left: 5px;
  margin-top: 1px;
}
.logo img {
  width: 400px;
  height: 60px;
}

.search {
  float: left;
  margin-left: 50px;
}
.login {
  margin-top: 30px;
  float: right;
}
.el-pagination {
  margin-left: -400px;
  margin-top: 20px;
}
.el-input {
  margin-left: 100px;
  /* width: 400px; */
}
.el-header {
  background-color: #f9f9f9;
  text-align: center;
  line-height: 60px;
}
.el-footer {
  background-color: #fff;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #fff;
  color: #333;
  text-align: center;
  width: 800px;
}

.el-main {
  background-color: #fff;
  color: #333;
  height: 100%;
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
.el-container {
  height: 620px;
}
.el-button {
  height: 50px;
}
</style>