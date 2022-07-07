const path = require("path");
const PerspectivePlugin = require("@finos/perspective-webpack-plugin");
const HtmlWebPackPlugin = require("html-webpack-plugin");

const mode = process.argv.includes("--watch") ? "development" : "production";

module.exports = {
  mode,
  devtool: "source-map",
  output: {
    path: path.resolve(__dirname, "..", "perspective_workspace_react_tornado", "static"),
  },
  resolve: {
    extensions: [".js", ".jsx"],
    fallback: {
      fs: false,
      path: false,
    },
  },

  plugins: [
    new HtmlWebPackPlugin({
      title: "Perspective React Example",
      template: "./src/html/index.html",
    }),
    new PerspectivePlugin(),
  ],

  module: {
    rules: [
      {
        test: /\.js(x?)$/,
        enforce: "pre",
        loader: "babel-loader",
      },
      {
        test: /\.css$/,
        exclude: /node_modules\/monaco-editor/,
        use: [{loader: "style-loader"}, {loader: "css-loader"}],
      },
    ],
  },
};
