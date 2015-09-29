var MeasurementView = Backbone.View.extend({
    tagName: 'tr',
    render: function() {
        this.$el.html("<td>" + this.model.get('systolic') + "</td>");
    }
});