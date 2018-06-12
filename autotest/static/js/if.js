//切换文本/参数
function changeBody(obj) {
    if($(obj).hasClass("active")){
        return;
    }else {
        if($(obj).hasClass("bd_text")){
            $(".bd_param").removeClass("active");
            $(obj).addClass("active");
            $(".request_param_body").hide();
            $(".request_text_body").show();

        }else {
            $(".bd_text").removeClass("active");
            $(obj).addClass("active");
            $(".request_text_body").hide();
            $(".request_param_body").show();

        }
    }
}


//删除行
function del_step(obj){
        var tr = obj.parentNode.parentNode;
        var tbody = tr.parentNode;
        tbody.removeChild(tr);
}
//添加request_header
$("#hd_btn").click(function () {
    var newRow = "<tr> <td name='var_key' contenteditable='true'></td><td name='var_value' contenteditable='true'></td> <td> " +
        "<button type=\"button\" class=\"close rm\" aria-label=\"Close\" onclick='del_step(this)'>\n" +
        "                                                        <span aria-hidden=\"true\">&times;</span>\n" +
        "                                                </button>" +
        "</td> </tr>";
    $("#request_header tr:last").after(newRow);
});

//添加request_body
$("#bd_btn").click(function () {
    var newRow = "<tr> <td name='var_key' contenteditable='true'></td><td name='var_value' contenteditable='true'></td> <td> " +
        "<button type=\"button\" class=\"close rm\" aria-label=\"Close\" onclick='del_step(this)'>\n" +
        "                                                        <span aria-hidden=\"true\">&times;</span>\n" +
        "                                                </button> " +
        "</td> </tr>";
    $(".request_param_body tr:last").after(newRow);
});


function getbodytype(){
    var type = "";
    $(".bodyparam li").each(function () {
        if($(this).hasClass("active")){
            type =  $(this).attr("class");
        }
    });
    if(type!=""){
        type = type.replace("active","").trim();
    }
    return type;
}

function isJOSN(str){
    if(str.trim()!="" && typeof str == "string"){
        try{
            var obj = JSON.parse(str);
            if(typeof obj == "object" && obj){
                return true;
            }else {
                return false;
            }
        }catch (e) {
            return false;
        }
        
    }else {
        return false;
    }

}

function sb(sb_type){
    var if_name = $("#if_name").val().trim();
    var group_id = $("#group_id option:selected").attr("gid");
    var if_url = $("#if_url").val().trim();
    var if_method = $("#if_method").val().trim();
    var if_type = $("#if_type").val().trim();
    var request_header_data;
    var request_body_data;
    var body_type;

    sb_type=="0"?body_type = "bd_param":body_type = "bd_text"

    var qq = new Object();
    $("#request_header tr").each(function (i) {
        if (i == 0) return true;
        var data = new Object();
        $(this).find("td[name]").each(function (k) {
            var name =  $(this).attr("name");
            data[k] = $(this).text().trim();
        });

        qq[data[0]] = data[1]
    });
    request_header_data = qq;
    if($.isEmptyObject(request_header_data)){
        request_header_data = "";
    }else {
        request_header_data = JSON.stringify(qq);
    }

    if(getbodytype() == "bd_param"){
        var bb = new Object();
        $(".request_param_body tr").each(function (i) {
            if (i == 0) return true;
            var data = new Object();
            $(this).find("td[name]").each(function (k) {
                var name =  $(this).attr("name");
                data[k] = $(this).text().trim();
            });

            bb[data[0]] = data[1]
        });
         request_body_data = bb;
        if($.isEmptyObject(request_body_data)){
            request_body_data = "";
        }else {
            request_body_data = JSON.stringify(bb);
        }

    }else {
        var request_text_body = $(".text_body").val();
        if(isJOSN(request_text_body)){
            request_body_data = request_text_body;
        }else {
            request_body_data = "";
        }
    }

    $.ajax({
        url : "/interface/add",
        type : "POST",
        data : {
            "sb_type": sb_type,
            "if_name" : if_name,
            "group_id" : group_id,
            "if_url" : if_url,
            "if_method" : if_method,
            "if_type" : if_type,
            "body_type": body_type,
            "request_header_data" : request_header_data,
            "request_body_data" : request_body_data
        },
        success : function (data) {
            // console.log(data);
            // var str = data.code +","+ data.msg +","+data.data;
            if(sb_type=="0"){
                window.location.href = "/interface/list";
            }else {
                var str = data.code + data.msg ;
                $("#rs_status").text(str);
                $("#result").text(data.data);
                $(".res_text").css("display",'block')
            }

        },
        error : function () {
            alert("网络开小差了，请刷新重试~");
        }
    });

}

//保存接口
$("#if_sb").click(function () {
    var sb_type = 0;
    sb(sb_type);
});

//测试接口
$("#ts_sb").click(function () {
    var sb_type = 1;
    sb(sb_type);
});



