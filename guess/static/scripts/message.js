$(function(){
	var contaier = $('.message-box');
	var show_message = function(msg, msg_type) {
		if (typeof msg_type == 'undefined') msg_type = 'danger';

		msg = $('<div/>').text(msg).html();
		msg = msg.replace("\n", "<br />");
		
        var close_button = $('<button type="button" class="close" data-dismiss="alert"></button>')
            .append($('<span aria-hidden="true">&times;</span>'))
            .append($('<span class="sr-only">Close</span>'));

		var template = $('<div role="alert"><\/div>')
            .addClass('alert')
			.addClass('alert-' + msg_type)
			.addClass('alert-dismissible')
		contaier.prepend(template.html(msg).prepend(close_button));

        close_button.click(function(){
            template.fadeOut();
        });
	};
	var update = function() {
		$.ajax({
			url: '/guess',
			type: 'get',
			dataType: 'json',
			success: function(r) {
				try {
					show_message(r.msg, 'danger');
					update();
				} catch (e) {
					show_message('Server Error' + e, 'alert');
				}
			},
			error: function(jqxhr, status, thrown) {
				if (status == 'abort' || status == 'timeout' || jqxhr.status == 0 || status.toString() == 'parser') return;
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
			},
			error: function(jqxhr, status) {
				// if (status == 'abort') return;
				// if (status != 'timeout') {
				// 	show_message('向服务器发送消息时发生错误：' + status.toString(), 'error');
				// }
			}
		});
		$("#number").val("");
		return false;
	});
});
