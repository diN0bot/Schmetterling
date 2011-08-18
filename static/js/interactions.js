(function ($) {
   $.fn.liveDraggable = function (opts) {
      this.live("mouseover", function() {
         if (!$(this).data("init")) {
            $(this).data("init", true).draggable(opts);
         }
      });
   };
}(jQuery));

(function ($) {
   $.fn.liveDroppable = function (opts) {
      this.live("mouseover", function() {
         if (!$(this).data("init")) {
            $(this).data("init", true).droppable(opts);
         }
      });
   };
}(jQuery));

$(".draggable").liveDraggable({ revert: "invalid" });
$(".droppable").liveDroppable({ hoverClass: "boxHover" });
$("#leaves").liveDroppable({ hoverClass: "boxHover", accept: "#box .draggable" });
