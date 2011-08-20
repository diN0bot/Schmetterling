(function ($) {
   $.fn.liveDraggable = function (opts) {
      this.live("mouseover", function() {
         if (!$(this).data("init")) {
            $(this).data("init", true).draggable(opts);
         }
      });
   };
}(jQuery));

$(".text").live("keyup", function(e){
  alert("name");
  if (e.keyCode == 13) {
    e.preventDefault();
    $(':button:contains("OK")').click();
  }
});

$(".draggable").liveDraggable({ revert: "invalid" });

$("#leaves").droppable({ hoverClass: "boxHover", accept: ".box .dropLeaf" });

$(".box h4").live("click", function(){
  var input, title, form;
  title = $(this);
  form = ich.boxNameFromTemplate();
  input = $(form).find("input");
  input.val(title.text());
  $(form).dialog({
      modal:true,
      buttons:{
        "OK": function(){
          title.text(input.val());
          $(this).dialog("close");
        }
      }
    });
});

function addToBox($box, $item){
  var name, title, source;
  name = $item.find(".leafName").text();
  title = $($box).find("h4");
  if(name != ""){
    source = $item.attr("class").substr(0,2);
    $item.remove();
    $($box).append(ich.droppedLeafTemplate({"name":name.substr(0,9), "source":source}).draggable({ revert: "invalid" }));
  } else {
    name = $item.text()
    $item.remove();
    $item.css("top", "0px");
    $item.css("left", "0px");
    $($box).append($item.draggable({ revert: "invalid" }));
    $("#boxes").children().each(function(i){
      if(this.children.length == 1 & $(this).find("h4").text() != "New Box"){
        $(this).remove();
       }
    });
  }
  if(title.text()=="New Box"){
    var form, input, title;
    form = ich.boxNameFromTemplate();
    input = $(form).find("input");

    title.text(name);
    input.val(name);
    $(form).dialog({
      modal:true,
      buttons:{
        "OK": function(){
          title.text(input.val());
          $(this).dialog("close");
        }
      }
    });
    newBox();
  }
};

function newBox(){
  var box_num;
  box_num = $("#boxes").children().length;
  $("#boxes").append(ich.boxTemplate({ "name":"New Box", "id":box_num }).droppable({
    hoverClass: "boxHover",
    drop: function( event, ui){
      addToBox( this, ui.draggable);
    }
  }));
}

function removeFromBox($box, $item){
};
