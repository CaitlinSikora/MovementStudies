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
            console.log(e.keyCode);
            if (e.keyCode == 46) {
                console.log('Space pressed');
                time = int(vid.time()*100)*0.01;
                if (time-1 > 0){
                    prev_time = time-1;
                } else {
                    prev_time = 0;
                }
                segments.push(new Segment(time));
                segmentIndex+=1;
                segments.sort(function(a, b){
                    return a.end_time > b.end_time;
                });
                console.log("next index",segmentIndex);
                //markings.sort();
                console.log("Added");
                var target = $($this.find("button[data-toggle=fieldset-add-row]").data("target"));
                console.log("target",target);
                var oldrow = target.find("[data-toggle=fieldset-entry]:last");
                console.log("id",oldrow.find(":input")[0].id);
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
                if (first){
                    oldrow.remove();
                    first = false;
                }
            }
                // if (first){
                //     oldrow.attr('data-id', 0);
                //     oldrow.find(":input").each(function() {
                //         var id = $(this).attr('id').replace('-' + (elem_num - 1) + '-', '-' + (elem_num) + '-');
                //         //$(this).attr('name', id).attr('id', id).val('').removeAttr("checked");
                //         if ($(this).attr('name').includes('start_time')){
                //             $(this).val(prev_time);
                //             console.log($(this).attr('name'));
                //         } else if ($(this).attr('name').includes('end_time')){
                //             $(this).val(time);
                //             console.log($(this).attr('name'));
                //         } else {
                //             //$(this).attr('name', id).attr('id', id).val('').removeAttr("checked");
                //             console.log($(this).attr('name'));
                //         }
                //     });
                //     first = false;
                // } else {
                //     var row = oldrow.clone(true, true);
                //     console.log(row.find(":input")[0]);
                //     var elem_id = row.find(":input")[0].id;
                //     var elem_num = parseInt(elem_id.replace(/.*-(\d{1,4})-.*/m, '$1')) + 1;
                //     row.attr('data-id', elem_num);
                //     row.find(":input").each(function() {
                //         //console.log(this.id);
                //         var id = $(this).attr('id').replace('-' + (elem_num - 1) + '-', '-' + (elem_num) + '-');
                //         console.log(id);
                //         // YOU MIGHT NEED THIS LINE!
                //         //$(this).attr('name', id).attr('id', id).val('').removeAttr("checked");
                //         if ($(this).attr('name').includes('start_time')){
                //             $(this).attr('name', id).attr('id', id).val(prev_time).removeAttr("checked");
                //             console.log($(this).attr('name'));
                //         } else if ($(this).attr('name').includes('end_time')){
                //             $(this).attr('name', id).attr('id', id).val(time).removeAttr("checked");
                //             console.log($(this).attr('name'));
                //         } else {
                //             $(this).attr('name', id).attr('id', id).val('').removeAttr("checked");
                //             console.log($(this).attr('name'));
                //         }
                //     });
                // }
            //}
        });
        //End add new entry

        //Remove row
        $this.find("button[data-toggle=fieldset-remove-row]").click(function() {
            if($this.find("[data-toggle=fieldset-entry]").length > 1) {
                var thisRow = $(this).closest("[data-toggle=fieldset-entry]");
                console.log("removing");
                var removeTime = thisRow.find(':input').find('end_time').prevObject[1].value;
                //var index = segments.indexOf(Number(removeTime));
                var index = segments.map(function(e) { return e.index; }).indexOf(int(thisRow.attr('data-id')));
                console.log("index remove",index);
                //var index=int(thisRow.attr('data-id'));
                console.log(index);
                if(index!=-1){
                    segments.splice(index, 1);
                }
                thisRow.remove();
            }
        }); //End remove row
    });
});

var time=0;
var prev_time=0;
var first = true;


/* Need to change to just one time per movement on a separate branch.*/