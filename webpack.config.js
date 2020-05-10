const path = require('path');

module.exports = {
    entry: './frontend/src/index.js', // relative path
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            // Load CSS
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            // Load SCSS
            {
                test: /\.scss$/,
                use: ['style-loader', 'css-loader', 'sass-loader']
            }
        ]
    },
    // resolve: {
    //     extensions: ['*', '.js', '.jsx']
    // },
    output: {
        path: path.join(__dirname, 'frontend/static/frontend/'), // Absolute path
        filename: 'app.js' // A name of compiled file
    }
};
