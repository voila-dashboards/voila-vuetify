var path = require('path');
var rules = [
    { test: /\.css$/, use: ['style-loader', 'css-loader']},
    {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        loader: 'file-loader',
    }
];

module.exports = [{
    entry: './src/index.js',
    output: {
        filename: 'index.js',
        path: path.resolve(__dirname, '..', 'share', 'jupyter', 'voila', 'templates', 'vuetify-base', 'static', 'deps'),
        publicPath: 'voila/static/deps/',
        libraryTarget: 'amd'
    },
    devtool: 'source-map',
    module: {
        rules: rules
    },
    externals: [],
    // vue met compiler
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        }
    },
    mode: 'production',
    performance: {
        maxEntrypointSize: 1400000,
        maxAssetSize: 1400000
    },
},];
