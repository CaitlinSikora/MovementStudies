$(function() {
    $("div[data-toggle=fieldset]").each(function() {
        var $this = $(this);
            
        //Add new entry
        $this.find("button[data-toggle=fieldset-add-row]").click(function() {
            //var fieldthis = $(this);
            var target = $($(this).data("target"));
            console.log(target);
            var oldrow = target.find("[data-toggle=fieldset-entry]:last");
            var row = oldrow.clone(true, true);
            console.log(row.find(":input")[0]);
            var elem_id = row.find(":input")[0].id;
            var elem_num = parseInt(elem_id.replace(/.*-(\d{1,4})-.*/m, '$1')) + 1;
            row.attr('data-id', elem_num);
            row.find(":input").each(function() {
                console.log(this);
                var id = $(this).attr('id').replace('-' + (elem_num - 1) + '-', '-' + (elem_num) + '-');
                $(this).attr('name', id).attr('id', id).val('').removeAttr("checked");
            });
            oldrow.after(row);
        }); 

        $(window).keypress(function(e) {
            if (e.keyCode == 0 || e.keyCode == 32) {
                console.log('Space pressed');
                prev_time = time;
                time = vid.time();
                markings.push(time);
                markings.sort();
                console.log("Added");
                console.log(markings);
                var target = $($this.find("button[data-toggle=fieldset-add-row]").data("target"));
                console.log(target);
                var oldrow = target.find("[data-toggle=fieldset-entry]:last");
                var row = oldrow.clone(true, true);
                console.log(row.find(":input")[0]);
                var elem_id = row.find(":input")[0].id;
                var elem_num = parseInt(elem_id.replace(/.*-(\d{1,4})-.*/m, '$1')) + 1;
                row.attr('data-id', elem_num);
                row.find(":input").each(function() {
                    //console.log(this.id);
                    var id = $(this).attr('id').replace('-' + (elem_num - 1) + '-', '-' + (elem_num) + '-');
                    console.log(id);
                    // YOU MIGHT NEED THIS LINE!
                    //$(this).attr('name', id).attr('id', id).val('').removeAttr("checked");
                    if ($(this).attr('name').includes('start_time')){
                        $(this).attr('name', id).attr('id', id).val(prev_time).removeAttr("checked");
                        console.log($(this).attr('name'));
                    } else if ($(this).attr('name').includes('end_time')){
                        $(this).attr('name', id).attr('id', id).val(time).removeAttr("checked");
                        console.log($(this).attr('name'));
                    } else {
                        $(this).attr('name', id).attr('id', id).val('').removeAttr("checked");
                        console.log($(this).attr('name'));
                    }
                });
                oldrow.after(row);
            }
        });
        //End add new entry

        //Remove row
        $this.find("button[data-toggle=fieldset-remove-row]").click(function() {
            if($this.find("[data-toggle=fieldset-entry]").length > 1) {
                var thisRow = $(this).closest("[data-toggle=fieldset-entry]");
                console.log("removing");
                var removeTime = thisRow.find(':input').find('end_time').prevObject[1].value;
                var index = markings.indexOf(Number(removeTime));
                if(index!=-1){
                    console.log(markings.indexOf(0));
                    console.log(markings);
                    console.log(removeTime);
                    console.log(index);
                    markings.splice(index, 1);
                }
                thisRow.remove();
            }
        }); //End remove row
    });
});

var time=0;
var prev_time;

$('#submit').mouseover(function(){
    console.log('hovering');
    var instruct = '  Wait! Are you finished adding movements?';
    $('#instruct').html(instruct);
});
$('#submit').mouseleave(function(){
    console.log('not hovering');
    var instruct = '';
    $('#instruct').html(instruct);
});