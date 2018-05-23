(function(window,$){
	navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;  
    window.URL = window.URL || window.webkitURL || window.mozURL || window.msURL; 
	class FaceAI{
		constructor(){
			this.video = document.createElement('video')
			this.video.width = 400
			this.video.height = 300
			this.video.style.display = 'none'
			this.dataUrl = ''
			this.base64Image = ''
			this.getFaceUrl = "http://127.0.0.1:7000/renlianshibie"
			this.audio =''
			this.audioType = '';
			document.body.appendChild(this.video)
			
			this.exArray = [];
			var that = this
//			MediaStreamTrack.getSources(function (sourceInfos) {  
//	            for (var i = 0; i != sourceInfos.length; ++i) {  
//	                var sourceInfo = sourceInfos[i];  
//	                //这里会遍历audio,video，所以要加以区分  
//	                if (sourceInfo.kind === 'video') {  
//	                    that.exArray.push(sourceInfo.id);  
//	                }  
//	            }  
//	        });
	        this.getMedia()
	        console.log(this)
		}
		getMedia(){
			var that = this
			if (navigator.getUserMedia) {  
                navigator.getUserMedia({  
                    'video': {  
                        'optional': [{  
                            'sourceId': that.exArray[1] //0为前置摄像头，1为后置  
                        }]  
                    },  
                    'audio':true  
                }, function(stream){
                	that.successFunc(stream)
                }, this.errorFunc);    //success是获取成功的回调函数
            }  
            else {  
                alert('Native device media streaming (getUserMedia) not supported in this browser.');  
            }  
		}
		successFunc(stream){
			
			//alert('Succeed to get media!');  
            if (this.video.mozSrcObject !== undefined) {  
                //Firefox中，video.mozSrcObject最初为null，而不是未定义的，我们可以靠这个来检测Firefox的支持  
                this.video.mozSrcObject = stream;  
            }  
            else {  
                this.video.src = window.URL && window.URL.createObjectURL(stream) || stream;  
//              this.vidio.src = HTMLMediaElement.srcObject(stream)
//				console.log(stream)
            }  
  
            this.video.play();  
  
            // 音频  
            this.audio = new Audio();  
            this.audioType = this.getAudioType(this.audio);  
            if (this.audioType) {  
                this.audio.src = 'polaroid.' + this.audioType;  
                this.audio.play();  
            }  
		}
		errorFunc(e) {  
            alert('Error！'+e);  
        }
		// 将视频帧绘制到Canvas对象上,Canvas每60ms切换帧，形成肉眼视频效果  
		drawVideoAtCanvas(Id) {
			var that = this
//			console.log(that)
			var canvas2 = document.getElementById(Id);  
        	var context2 = canvas2.getContext('2d');  
            window.setInterval(function () {  
                context2.drawImage(that.video, 0, 0,400,300);
//              console.log(that.resFaceInfo)
                if(that.resFaceInfo){
                	
                	var listFace = that.resFaceInfo.face_list
                	for(var i=0;i<listFace.length;i++){
                		
                		var item = listFace[i].location
                		context2.beginPath()
                		context2.lineWidth = 2
                		context2.strokeStyle = 'pink'
                		context2.strokeRect(item.left,item.top,item.width,item.height)
                		context2.closePath()
                	}
                	
                }
            }, 60);  
            
        }
		//获取音频格式  
        getAudioType(element) {  
            if (element.canPlayType) {  
                if (element.canPlayType('audio/mp4; codecs="mp4a.40.5"') !== '') {  
                    return ('aac');  
                } else if (element.canPlayType('audio/ogg; codecs="vorbis"') !== '') {  
                    return ("ogg");  
                }  
            }  
            return false;  
        }
        getPhoto(Id) {
        	var canvas1 = document.getElementById(Id);  
        	var context1 = canvas1.getContext('2d');
            context1.drawImage(this.video, 0, 0,400,300); //将video对象内指定的区域捕捉绘制到画布上指定的区域，实现拍照。  
            this.dataUrl = canvas1.toDataURL('image/png',0.6)
            this.base64Image = this.dataUrl.replace("data:image/png;base64,", "");
            
//          console.log(this.dataUrl)
            
        }
        getFaceInfo(){
        	
        	var that = this
            $.ajax({
            	type:"post",
            	url:that.getFaceUrl,
            	data:{
            		imgData:that.base64Image
            	},
            	async:true,
            	complete:function(res){
            		var result = JSON.parse(res.responseText)
//          		console.log(that)
            		if (result.error_msg=='SUCCESS'){
            			that.resFaceInfo = result.result
            			console.log(that)
            		}
            		
            		
            	}
            });
//          document.getElementById('img').src = dataUrl
        }
	}
	window.FaceAI = FaceAI
})(window,$)
