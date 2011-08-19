App.Views.Index = Backbone.View.extend({
  initialize: function(){
  }
});

App.Views.Explore = Backbone.View.extend({
  initialize: function() {
    this.leaves = this.options.leaves;
    this.boxes = this.options.boxes;
    this.type = this.options.type;
    this.options.bpage ? this.bpage = this.options.bpage : this.bpage = 1
    this.options.lpage ? this.lpage = this.options.lpage : this.lpage = 1
    this.render();
  },

  render: function() {
    var prevLink = "#explore/" + this.type + "/boxes_p" + this.bpage.toString() + "/leaves_p" + (this.lpage-1)
    var nextLink = "#explore/" + this.type + "/boxes_p" + this.bpage.toString() + "/leaves_p" + (Number(this.lpage)+1)
    $("#leaves").html(ich.leavesTemplate({"prevLink":prevLink, "nextLink":nextLink}));
    $("#boxes").html(ich.boxesTemplate());
    newBox();
    if(this.leaves.length >0) {
      _(this.leaves.models.slice(this.lpage*9-8,this.lpage*9)).each(function(model) {
            opts = {'source':model.attributes.type.substr(0,2),
            'name':model.attributes.name,
            'id':model.attributes.id,
            'uid':model.attributes.identifier,
            'uri':model.attributes.resource_uri,
            'type':model.attributes.type,
            'data':model.attributes.data
          }
          $("#leaves #scrollBox").append(ich.leafTemplate(opts));
      });
    }
    else{
      $("#leaves").append("<h3>Nothing to show</h3>");
    }
  }

});
