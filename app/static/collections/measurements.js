var Measurements = Backbone.Collection.extend({
    model: Measurement,
    url: '/api/measurements/bloodpressure/1'
});
