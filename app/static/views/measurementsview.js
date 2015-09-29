var MeasurementsView = Backbone.View.extend({
    tagName: 'table',

    initialize: function() {
        var that = this;
        this.collection = new Measurements({reset: true});
        this.collection.fetch({success: function() {
            console.log(that.collection)
        }})
    },

    render: function() {
        this.collection.each(function (measurement) {

        })
    }
});