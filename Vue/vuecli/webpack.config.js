// webpack 설정
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')
module.exports = {
    // 여러개의 파일을 읽어오기
    mode: 'development', // vue 개발자 도구 사용
    entry: {
        app: path.join(__dirname, 'src', 'main.js')

    },
    // 관련된 모듈
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: 'vue-loader'
            },
            {
                test: /\.css$/,
                use: ['vue-style-loader', 'css-loader']
            }
        ]

    },
    plugins: [
        new VueLoaderPlugin()
    ],
    // 최종 결과
    output: {
        filename: 'app.js',
        path: path.join(__dirname, 'dist')
    }
}