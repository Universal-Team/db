$.expr[':'].external = function(obj){
	return !obj.href.match(/^\/\//)
		   && (obj.hostname != location.hostname);
};

$("a:external").prop("target", "_blank");
