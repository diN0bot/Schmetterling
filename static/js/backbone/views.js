App.Views.Index = Backbone.View.extend({
  initialize: function(){
  }
});

App.Views.Explore = Backbone.View.extend({
  initialize: function() {
    this.leaves = this.options.leaves;
    this.boxes = this.options.boxes;
    this.options.bpage ? this.bpage = this.options.bpage : this.bpage = 1
    this.options.lpage ? this.lpage = this.options.lpage : this.lpage = 1
    this.render();
  },

  render: function() {
    $("#leaves").html(ich.leavesTemplate());
    $("#boxes").html(ich.boxesTemplate());
    $("#boxes").append(ich.boxTemplate({"name":"New Box"}));
    if(this.leaves.length >0) {
      _(this.leaves.models.slice(this.lpage*9-8,this.lpage*9)).each(function(model) {
          $("#leaves #scrollBox").append(ich.leafTemplate({'source':model.attributes.type.substr(0,2) ,'name':model.attributes.name, 'id':model.attributes.id, 'uid':model.attributes.identifier, 'uri':model.attributes.resource_uri, 'type':model.attributes.type, 'data':model.attributes.data}));
      });
    }
    else{
      $("#leaves").append("<h3>Nothing to show</h3>");
    }
  }

});
