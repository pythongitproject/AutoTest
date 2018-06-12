var ms = $("#ms");
var ms_name = $("#ms_name");

ms.blur(function () {
    removestatus(ms);
});

ms_name.blur(function () {
    removestatus(ms_name);
});

$("#ms_sb").click(function () {
    if(ms_name.val().trim()==''){
        changestatus(ms_name);
    }else {
        if(ms.val().trim()==''){
            changestatus(ms);
        }else {
            $.ajax({
                type : "POST",
                url : "/env/add",
                data : {
                    "ms" : ms.val().trim(),
                    "ms_name" : ms_name.val().trim()
                },
                success : function (result) {
                    console.log(result);
                    if(result.success){
                        window.location.href = "/env/add";
                    }else {
                        alert('添加失败');
                    }
                },
                error : function (error) {
                    alert('添加异常')
                }
            });
        }
    }
});

function changestatus(obj) {
    obj.parent().parent().addClass("has-error");
}

function removestatus(obj) {
    obj.parent().parent().removeClass("has-error");
}

function remover_list(obj) {
    var ms_id = $(obj).attr("ms");
    $.ajax({
                type : "POST",
                url : "/env/del",
                data : {
                    "ms_id" : ms_id,
                },
                success : function (result) {
                    console.log(result);
                    if(result.success && result.sum >0){
                        $(obj).parent().hide();
                        return;
                    }else {
                        if(result.sum == 0){
                            window.location.href = "/env/add";
                        }else {
                            console.log('删除失败');
                        }

                    }
                },
                error : function (error) {
                    console.log('添加异常')
                }
            });

}