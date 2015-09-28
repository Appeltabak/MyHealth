var Bills = Backbone.Collection.extend({
    model: Bill,
    url: '/api/bills'
});