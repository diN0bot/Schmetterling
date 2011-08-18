var Box = Backbone.Model.extend({
  url: function(){
     return this.get('resource_uri') || this.collection.url;
  }
});

var Leaf = Backbone.Model.extend({
  url: function(){
     return this.get('resource_uri') || this.collection.url;
  }
});

var Person = Backbone.Model.extend({
  url: function(){
     return this.get('resource_uri') || this.collection.url;
  }
});
