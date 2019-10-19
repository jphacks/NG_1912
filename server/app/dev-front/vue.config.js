const path = require('path');

module.exports = {


    publicPath: '/',
    outputDir: path.resolve(__dirname, '../app/templates'),
    assetsDir: '../static',
    indexPath: 'index.html',
    filenameHashing: true,

};