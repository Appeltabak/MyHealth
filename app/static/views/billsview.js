var BillsView = Backbone.View.extend({
	tagName: 'ul',

    initialize: function() {
        var that = this;
        this.collection = new Bills({reset: true});
        this.collection.fetch({success: function() {
            that.render();
        }})
    },

	render: function(){
		this.collection.each(function(bill){
			var billView = new BillView({ model: bill });
			this.$el.append(billView.render().el);
		}, this);
        $(document.body).append(this.el);
		return this;
	}
});