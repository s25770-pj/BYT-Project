const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  devServer: {
    port: 8081,
    host: "localhost",
    open: true,
  },
  pages: {
    index: {
      entry: "src/main.js",
      title: process.env.VUE_APP_SITE_TITLE,
    },
  },
  configureWebpack: {
    plugins: [
      new HtmlWebpackPlugin({
        title: process.env.VUE_APP_SITE_TITLE,
        filename: process.env.VUE_APP_SITE_TITLE + ".html",
      }),
    ],
  },
  transpileDependencies: true,
};
