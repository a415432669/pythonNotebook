(function(window,$){
	class SoundAI{
		constructor(){
			this.audio = document.createElement('audio')
			document.body.appendChild(this.audio)
		}
		getSound(content){
			var that = this;
			$.ajax({
				type:"get",
				url:"http://127.0.0.1:7000/soundai",
				data:{
					content:content
				},
				async:true,
				complete:function(res){
					console.log(res)
					that.audio.src = 'http://127.0.0.1:7000/static/audio/audio.mp3'
					that.audio.play()
				}
			});
		}
		
	}
	window.SoundAI = SoundAI
})(window,$)
