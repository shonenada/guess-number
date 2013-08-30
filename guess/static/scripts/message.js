$(function(){
	var contaier = $('#message');
	var show_message = function(msg, msg_type) {
		if (typeof msg_type == 'undefined') msg_type = 'info';
		msg = $('<div/>').text(msg).html();
		msg = msg.replace("\n", "<br />");
		
		var template = $("<div><\/div>")
			.addClass('alert-message')
			.addClass('block-message')
			.addClass(msg_type);
		contaier.prepend(template.html(msg));
	};
	var update = function() {
		$.ajax({
			url: '/guess',
			type: 'get',
			dataType: 'json',
			success: function(r) {
				try {
					show_message(r.msg, 'info');
					update();
				} catch (e) {
					show_message('发生错误：' + e, 'alert');
				}
			},
			error: function(jqxhr, status, thrown) {
				if (status == 'abort' || status == 'timeout' || jqxhr.status == 0 || status.toString() == 'parser') return;
				// show_message('与服务器通讯发生错误：' + status.toString(), ' error');
			}
		});
	};
	update();
	$('#message-form').submit(function(){
		$.ajax({
			url: '/guess',
			type: 'post',
			dataType: 'json',
			data: $(this).serialize(),
			success: function() {
				update();
				$("#number").val("");
			},
			error: function(jqxhr, status) {
				// if (status == 'abort') return;
				// if (status != 'timeout') {
				// 	show_message('向服务器发送消息时发生错误：' + status.toString(), 'error');
				// }
			}
		});
		return false;
	});
});