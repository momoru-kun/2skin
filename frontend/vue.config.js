module.exports = {
    // Paths
    outputDir: process.env.NODE_ENV === 'production' ? '../client/static' : 'dist/',
    indexPath: process.env.NODE_ENV === 'production' ? '../../templates/index.html' : 'index.html',
    assetsDir: '',
    publicPath: process.env.NODE_ENV === 'production' ? 'static' : '/',
    devServer: {
      proxy: {
        '^/api': {
          target: 'http://192.168.31.104:5000'
        },
        '^/static/img': {
          target: 'http://192.168.31.104:5001'
        }
      }
    }
  }