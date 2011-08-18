App.Routers.Main = Backbone.Router.extend({
  routes : {
    "": "index",
    "explore/:type/boxes_p:bpage/leaves_p:lpage": "explore"
  },

  index: function(){
    new App.Views.Index();
  },

  explore: function(type, bpage, lpage){
  var leaves = new App.Collections.Leaves();
  var boxes = new App.Collections.Boxes();

  boxes.fetch({
    error: function(){
      new Error({ message: "Error loading leaves." });
    }
  });

  leaves.fetch({
    success: function(){
      new App.Views.Explore({ leaves: leaves, boxes: boxes, bpage: bpage, lpage: lpage });
    },
    error: function(){
      new Error({ message: "Error loading leaves." });
    }
  });

  }
});

App.Routers.Boxes = Backbone.Router.extend({

});

App.Routers.Leaves = Backbone.Router.extend({

});

App.Routers.Persons = Backbone.Router.extend({

});

App.init = function(){
  new App.Routers.Main();
  Backbone.history.start();
};
