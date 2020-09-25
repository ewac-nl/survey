// Copyright 2020 Stefan Rijnhart <stefan@opener.amsterdam>
// License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
odoo.define('survey.upload_file', function (require) {
'use strict';

    require('survey.survey');
    var the_form = $('.js_surveyform');

    function prefill_binary(){
        /* Prefill the binary questions' filename placeholders, and when it is
           cleared, ensure that the proper widget becomes visible again.
        */
        var controller = the_form.attr("data-prefill-binary");
        if (! _.isUndefined(controller)) {
            $.ajax(controller, {dataType: "json"}).done(
                function(json_data){
                    _.each(json_data, function(value, key){
                        var input = the_form.find("input[name=review_" + key + "]");
                        input.val(value);
                        input.removeClass('hidden');
                        var file = the_form.find("input[name=" + key + "]");
                        file.addClass('hidden');
                        var del = the_form.find("a[name=delete_" + key + "]");
                        del.removeClass('hidden');
                        del.on('click', function(e) {
                            input.val('');
                            input.addClass('hidden');
                            del.addClass('hidden');
                            file.removeClass('hidden');
                        });
                    });
                });
        }
    }

    if(the_form.length) {
        prefill_binary();
    }
});
