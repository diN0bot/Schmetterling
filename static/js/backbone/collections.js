App.Collections.Boxes = Backbone.Collection.extend({
  url: BOX_API,
  parse: function(data){
      return data.objects;
  }
});

App.Collections.Leaves = Backbone.Collection.extend({
  url: LEAF_API,
  model: Leaf,
  parse: function(data){
      return data.objects;
  }
});

App.Collections.Persons = Backbone.Collection.extend({
  url: PERSON_API,
  parse: function(data){
      return data.objects;
  }
});
