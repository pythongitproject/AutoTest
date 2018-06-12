var gp_name = $("#gp_name");


gp_name.blur(function () {
    removestatus(gp_name);
});

$("#ms_sb").click(function () {
    if(gp_name.val().trim()==''){
        changestatus(gp_name);
    }else {
            $.ajax({
                type : "POST",
                url : "/env/gp/add",
                data : {
                    "gp_name" : gp_name.val().trim()
                },
                success : function (result) {
                    console.log(result);
                    if(result.success){
                        window.location.href = "/env/gp/add";
                    }else {
                        alert('添加失败');
                    }
                },
                error : function (error) {
                    alert('添加异常')
                }
            });
    }
});

function changestatus(obj) {
    obj.parent().parent().addClass("has-error");
}

function removestatus(obj) {
    obj.parent().parent().removeClass("has-error");
}

function remover_list(obj) {
    var gp_id = $(obj).attr("gp");
    $.ajax({
                type : "POST",
                url : "/env/gp/del",
                data : {
                    "gp_id" : gp_id,
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