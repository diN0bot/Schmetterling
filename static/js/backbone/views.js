App.Views.Index = Backbone.View.extend({
  initialize: function() {
    this.leaves = this.options.collection;
    this.render();
  },

  render: function() {
    $("#container").html("");
    if(this.leaves.length >0) {
      _(this.leaves.models).each(function(model) {
          $("#container").append(ich.leafTemplate({'name':model.attributes.name, 'id':model.attributes.id, 'uid':model.attributes.identifier, 'uri':model.attributes.resource_uri, 'type':model.attributes.type, 'data':model.attributes.data}));
      });
    }
    else{
      $("#container").html("<h3>Nothing to show</h3>");
    }
  }

});
