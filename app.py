# shirt_company.py
from flask import Flask, render_template_string

app = Flask(__name__)

# Modern HTML template with responsive design
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <meta content="px-captcha" name="description"/>
    <title>Access to this page has been denied</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background-color: #fafbfc;
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 530px;
            width: 100%;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 40px 30px;
            text-align: center;
        }
        
        .header {
            color: #2d3748;
            font-size: 28px;
            font-weight: 500;
            margin-bottom: 25px;
            line-height: 1.2;
        }
        
        .message {
            color: #4a5568;
            font-size: 18px;
            margin-bottom: 30px;
            line-height: 1.5;
        }
        
        .button {
            display: inline-block;
            padding: 15px 40px;
            background-color: #4299e1;
            color: white;
            border-radius: 50px;
            font-size: 18px;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.3s;
            border: none;
            margin-bottom: 30px;
        }
        
        .button:hover {
            background-color: #3182ce;
        }
        
        .button:active {
            background-color: #2b6cb0;
        }
        
        .error-container {
            background-color: #fed7d7;
            border-radius: 6px;
            padding: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
        }
        
        .error-icon {
            margin-right: 10px;
            width: 24px;
            height: 24px;
        }
        
        .error-text {
            color: #c53030;
            font-size: 14px;
            text-align: left;
        }
        
        .ref-id {
            color: #a0aec0;
            font-size: 12px;
            padding-top: 15px;
            border-top: 1px solid #e2e8f0;
        }
        
        @media (max-width: 480px) {
            .container {
                padding: 30px 20px;
                box-shadow: none;
                border-radius: 0;
            }
            
            .header {
                font-size: 24px;
            }
            
            .message {
                font-size: 16px;
            }
            
            .button {
                padding: 12px 30px;
                font-size: 16px;
            }
            
            .ref-id {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #fafbfc;
                padding: 10px;
                font-size: 14px;
                border-top: 1px solid #e2e8f0;
                margin-bottom: 0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="header">Before we continue...</h1>
        <p class="message">Press & Hold to confirm you are<br>a human (and not a bot).</p>
        <button class="button" onmousedown="handlePress()" onmouseup="handleRelease()" ontouchstart="handlePress()" ontouchend="handleRelease()">Press & Hold</button>
        
        <div class="error-container">
            <img class="error-icon" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAQCAMAAADDGrRQAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAABFUExURUdwTNYELOEGONQILd0AONwALtwEL+AAL9MFLfkJSNQGLdMJLdQJLdQGLdQKLtYFLNcELdUGLdcBL9gFL88OLdUFLNEOLglBhT4AAAAXdFJOUwC8CqgNIRgRoAS1dWWuR4RTjzgryZpYblfkcAAAAI9JREFUGNNdj+sWhCAIhAdvqGVa1r7/oy6RZ7eaH3D4ZACBIed9wlOOMtUnSrEmZ6cHa9YAIfsbCkWrdpi/c50Bk2CO9mNLdMAu03wJA3HpEnfpxbyOg6ruyx8JJi6KNstnslp1dbPd9GnqmuYq7mmcv1zjnbQw8cV0xzkqo+fX1zkjUOO7wnrInUTxJiruC3vtBNRoQQn2AAAAAElFTkSuQmCC" alt="Error icon">
            <div class="error-text">Please check your internet connection{% if not mobile %} or disable your ad-blocker{% endif %}.</div>
        </div>
        
        <div class="ref-id">Reference ID {{ ref_id }}</div>
    </div>

    <script>
        // Preserve original PerimeterX variables
        window._pxVid = '';
        window._pxUuid = '{{ ref_id }}';
        window._pxAppId = 'PXhBU9onSl';
        window._pxHostUrl = '/hBU9onSl/xhr';
        window._pxCustomLogo = '';
        window._pxJsClientSrc = '/hBU9onSl/init.js';
        window._pxMobile = {{ mobile|tojson }};
        window._pxFirstPartyEnabled = true;
        
        var pxCaptchaSrc = '/hBU9onSl/captcha/captcha.js?a=c&u={{ ref_id }}&v=&m=0&h=R0VU';
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
            script.src = 'https://captcha.px-cloud.net/PXhBU9onSl/captcha.js?a=c&u={{ ref_id }}&v=&m=0&h=R0VU';
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
        
        // Modern button press handling
        function handlePress() {
            // Add visual feedback
            document.querySelector('.button').style.backgroundColor = '#2b6cb0';
            document.querySelector('.button').style.transform = 'scale(0.98)';
        }
        
        function handleRelease() {
            // Reset visual feedback
            document.querySelector('.button').style.backgroundColor = '#4299e1';
            document.querySelector('.button').style.transform = 'scale(1)';
        }
        
        // Preserve original error handler
        window._pxOnError = function () {
            var style = document.createElement('style');
            style.innerText = '@import url(https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap);body{background-color:#fafbfc}.px-captcha-error-container{position:fixed;height:340px;background-color:#fff;font-family:Roboto,sans-serif}.px-captcha-error-header{color:#f0f1f2;font-size:29px;margin:67px 0 33px;font-weight:500;line-height:.83;text-align:center}.px-captcha-error-message{color:#f0f1f2;font-size:18px;margin:0 0 29px;line-height:1.33;text-align:center}.px-captcha-error-button{text-align:center;line-height:48px;width:253px;margin:auto;border-radius:50px;border:solid 1px #f0f1f2;font-size:20px;color:#f0f1f2}.px-captcha-error-wrapper{margin:18px 0 0}div.px-captcha-error{margin:auto;text-align:center;width:400px;height:30px;font-size:12px;background-color:#fcf0f2;color:#ce0e2d}img.px-captcha-error{margin:6px 8px -2px 0}.px-captcha-error-refid{border-top:solid 1px #f0eeee;height:27px;margin:13px 0 0;border-radius:0 0 3px 3px;background-color:#fafbfc;font-size:10px;line-height:2.5;text-align:center;color:#b1b5b8}@media (min-width:620px){.px-captcha-error-container{width:530px;top:50%;left:50%;margin-top:-170px;margin-left:-265px;border-radius:3px;box-shadow:0 2px 9px -1px rgba(0,0,0,.13)}}@media (min-width:481px) and (max-width:620px){.px-captcha-error-container{width:85%;top:50%;left:50%;margin-top:-170px;margin-left:-42.5%;border-radius:3px;box-shadow:0 2px 9px -1px rgba(0,0,0,.13)}}@media (max-width:480px){body{background-color:#fff}.px-captcha-error-header{color:#f0f1f2;font-size:29px;margin:55px 0 33px}.px-captcha-error-container{width:530px;top:50%;left:50%;margin-top:-170px;margin-left:-265px}.px-captcha-error-refid{position:fixed;width:100%;left:0;bottom:0;border-radius:0;font-size:14px;line-height:2}}@media (max-width:390px){div.px-captcha-error{font-size:10px}.px-captcha-error-refid{font-size:11px;line-height:2.5}}';
            document.head.appendChild(style);
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
</html>'''

@app.route('/')
def home():
    # Sample reference ID - in real implementation this would be dynamic
    ref_id = '6e84cab4-7536-11f0-b63c-56d71461e29a'
    mobile = False  # Set to True for mobile version
    
    return render_template_string(HTML_TEMPLATE, ref_id=ref_id, mobile=mobile)

if __name__ == '__main__':
    app.run(debug=True)
