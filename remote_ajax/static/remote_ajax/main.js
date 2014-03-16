function DjangoRemoteAjax(){
    function ajax(url, success, data, type) {
        if (data == undefined) data = "";
        if (type == undefined) type = "GET";

        if( typeof FormData!='undefined'){
           $.ajax({
               headers: {'Cookie' : document.cookie },
               url: url,
               data: data,
               type: type,
               cache: false,
               contentType: false,
               processData: false,
               xhrFields: {withCredentials: true},
               success: success,
               error: function (data){
                   success(data.responseText);
               }
           });
        } else {
           $.ajax({
               headers: {'Cookie' : document.cookie },
               url: url,
               data: data,
               type: type,
               xhrFields: {withCredentials: true},
               success: success,
               error: function (data){
                   success(data.responseText);
               }
           });
        };
    }

    this.get = function (url, success, data) {
        ajax(url, success, data, "GET");
    }

    this.post = function (url, success, data) {
        ajax(url, success, data, "POST");
    }
}

django_remote_ajax = new DjangoRemoteAjax();
