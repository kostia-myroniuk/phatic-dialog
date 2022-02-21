const path = require('path');

module.exports = {
  mode: 'development',
  entry: './public/script/index.js',
  devtool: "eval-source-map",
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'index.js',
  },
};