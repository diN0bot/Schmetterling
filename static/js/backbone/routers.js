App.Routers.Main = Backbone.Router.extend({
  routes : {
    "": "index"
  },

  index: function(){
  var leaves = new App.Collections.Leaves();
  leaves.fetch({
    success: function(){
      new App.Views.Index({ collection: leaves });
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
