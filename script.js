<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <meta content="px-captcha" name="description"/>
    <title>Access to this page has been denied</title>
    <style>
        /* Modern CSS Reset & Base Styles */
        *, *::before, *::after {
            box-sizing: border-box;
        }
        
        body {
            margin: 0;
            padding: 0;
            font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4edf9 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #333;
            line-height: 1.6;
        }
        
        /* Container Styles */
        .px-captcha-error-container {
            background-color: #ffffff;
            border-radius: 16px;
            padding: 40px 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            max-width: 500px;
            width: 90%;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .px-captcha-error-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 6px;
            background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
        }
        
        /* Header Styles */
        .px-captcha-error-header {
            color: #2c3e50;
            font-size: 28px;
            margin: 20px 0 30px;
            font-weight: 700;
            line-height: 1.2;
            text-align: center;
        }
        
        /* Message Styles */
        .px-captcha-error-message {
            color: #7f8c8d;
            font-size: 18px;
            margin: 0 0 35px;
            line-height: 1.5;
            text-align: center;
        }
        
        /* Button Styles */
        .px-captcha-error-button {
            text-align: center;
            line-height: 56px;
            width: 260px;
            margin: 30px auto;
            border-radius: 50px;
            border: solid 2px #3498db;
            font-size: 20px;
            color: #3498db;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            background: transparent;
            display: block;
            position: relative;
            overflow: hidden;
        }
        
        .px-captcha-error-button:hover {
            background-color: #3498db;
            color: white;
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(52, 152, 219, 0.3);
        }
        
        .px-captcha-error-button:active {
            transform: translateY(0);
        }
        
        /* Error Wrapper */
        .px-captcha-error-wrapper {
            margin: 25px 0 0;
        }
        
        /* Error Message Box */
        div.px-captcha-error {
            margin: 0 auto;
            text-align: center;
            width: 100%;
            max-width: 400px;
            padding: 15px;
            font-size: 14px;
            background-color: #fff8f8;
            color: #e74c3c;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid #ffdddd;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
        }
        
        /* Error Icon */
        img.px-captcha-error {
            margin: 0 10px -3px 0;
            width: 20px;
            height: 20px;
        }
        
        /* Reference ID Box */
        .px-captcha-error-refid {
            border-top: solid 1px #eee;
            padding: 15px 0;
            margin: 25px 0 0;
            border-radius: 0 0 16px 16px;
            background-color: #f8f9fa;
            font-size: 13px;
            line-height: 1.5;
            text-align: center;
            color: #95a5a6;
            font-weight: 500;
        }
        
        /* Responsive Design */
        @media (min-width: 620px) {
            .px-captcha-error-container {
                width: 530px;
                top: 50%;
                left: 50%;
                margin-top: -170px;
                margin-left: -265px;
                border-radius: 16px;
                box-shadow: 0 15px 50px rgba(0, 0, 0, 0.1);
                padding: 50px 40px;
            }
            
            .px-captcha-error-header {
                font-size: 32px;
            }
            
            .px-captcha-error-message {
                font-size: 20px;
            }
            
            div.px-captcha-error {
                font-size: 15px;
            }
        }
        
        @media (max-width: 619px) {
            .px-captcha-error-container {
                width: 90%;
                padding: 35px 25px;
            }
            
            .px-captcha-error-header {
                font-size: 26px;
                margin: 15px 0 25px;
            }
            
            .px-captcha-error-message {
                font-size: 17px;
                margin: 0 0 30px;
            }
            
            .px-captcha-error-button {
                width: 230px;
                font-size: 18px;
                line-height: 50px;
            }
        }
        
        @media (max-width: 480px) {
            body {
                background-color: #fff;
                padding: 20px 15px;
            }
            
            .px-captcha-error-header {
                font-size: 24px;
                margin: 20px 0 20px;
            }
            
            .px-captcha-error-message {
                font-size: 16px;
                margin: 0 0 25px;
            }
            
            .px-captcha-error-button {
                width: 100%;
                max-width: 240px;
                font-size: 17px;
                line-height: 48px;
            }
            
            div.px-captcha-error {
                font-size: 13px;
                padding: 12px;
            }
            
            .px-captcha-error-refid {
                position: fixed;
                width: 100%;
                left: 0;
                bottom: 0;
                border-radius: 0;
                font-size: 12px;
                padding: 12px 0;
                background: white;
                border-top: 1px solid #eee;
            }
        }
        
        @media (max-width: 390px) {
            div.px-captcha-error {
                font-size: 12px;
                flex-direction: column;
                text-align: center;
                line-height: 1.4;
            }
            
            img.px-captcha-error {
                margin: 0 0 8px 0;
            }
            
            .px-captcha-error-refid {
                font-size: 11px;
            }
        }
        
        /* Animation Effects */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .px-captcha-error-container {
            animation: fadeIn 0.6s ease-out forwards;
        }
        
        /* Interactive States */
        .px-captcha-error-button:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.3);
        }
        
        /* Accessibility */
        @media (prefers-reduced-motion: reduce) {
            .px-captcha-error-container {
                animation: none;
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
</head>
<body>
    <script>
        /* PerimeterX assignments */
        window._pxVid = '';
        window._pxUuid = '6ccae952-7534-11f0-a8d8-af3e8a9a458f';
        window._pxAppId = 'PXhBU9onSl';
        window._pxHostUrl = '/hBU9onSl/xhr';
        window._pxCustomLogo = '';
        window._pxJsClientSrc = '/hBU9onSl/init.js';
        window._pxMobile = false;
        window._pxFirstPartyEnabled = true;
        var pxCaptchaSrc = '/hBU9onSl/captcha/captcha.js?a=c&u=6ccae952-7534-11f0-a8d8-af3e8a9a458f&v=&m=0&h=R0VU';
        var script = document.createElement('script');
        script.src = pxCaptchaSrc;
        script.onload = onScriptLoad;
        script.onerror = onScriptError;
        var onScriptErrorCalled;
        document.head.appendChild(script);
        var timeoutID = setTimeout(onScriptError, 5000);
        function onScriptLoad() {
            clearTimeout(timeoutID);
            setTimeout(function() {
                if (!isContentLoaded()) {
                    onScriptError();
                }
            }, 2500);
        }
        function onScriptError() {
            if (onScriptErrorCalled) {
                return;
            }
            onScriptErrorCalled = true;
            script = document.createElement('script');
            script.src = 'https://captcha.px-cloud.net/PXhBU9onSl/captcha.js?a=c&u=6ccae952-7534-11f0-a8d8-af3e8a9a458f&v=&m=0&h=R0VU';
            script.onload = function() {
                clearTimeout(timeoutID);
            };
            script.onerror = window._pxOnError;
            document.head.appendChild(script);
            timeoutID = setTimeout(function() {
                if (!isContentLoaded()) {
                    window._pxOnError();
                }
            }, 5000);
        }
        function isContentLoaded() {
            return !!document.querySelector('div,span');
        }
        window._pxOnError = function () {
            var div = document.createElement('div');
            div.className = 'px-captcha-error-container';
            div.innerHTML = '<div class="px-captcha-error-header">Before we continue...</div><div class="px-captcha-error-message">Press & Hold to confirm you are<br>a human (and not a bot).</div><div class="px-captcha-error-button">Press & Hold</div><div class="px-captcha-error-wrapper"><div class="px-captcha-error"><img class="px-captcha-error" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAQCAMAAADDGrRQAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAABFUExURUdwTNYELOEGONQILd0AONwALtwEL+AAL9MFLfkJSNQGLdMJLdQJLdQGLdQKLtYFLNcELdUGLdcBL9gFL88OLdUFLNEOLglBhT4AAAAXdFJOUwC8CqgNIRgRoAS1dWWuR4RTjzgryZpYblfkcAAAAI9JREFUGNNdj+sWhCAIhAdvqGVa1r7/oy6RZ7eaH3D4ZACBIed9wlOOMtUnSrEmZ6cHa9YAIfsbCkWrdpi/c50Bk2CO9mNLdMAu03wJA3HpEnfpxbyOg6ruyx8JJi6KNstnslp1dbPd9GnqmuYq7mmcv1zjnbQw8cV0xzkqo+fX1zkjUOO7wnrInUTxJiruC3vtBNRoQQn2AAAAAElFTkSuQmCC">Please check your internet connection' + (window._pxMobile ? '' : ' or disable your ad-blocker') + '.</div></div><div class="px-captcha-error-refid">Reference ID ' + window._pxUuid + '</div>';
            document.body.appendChild(div);
            if (window._pxMobile) {
                setTimeout(function() {
                    location.href = '/px/captcha_close?status=-1';
                }, 5000);
            }
        };
    </script>
</body>
</html>
