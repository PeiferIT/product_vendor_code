odoo.define('product_vendor_code.db', function (require) {
    "use strict";

	var rpc = require('web.rpc');
	var models = require('point_of_sale.models');
	var DB = require('point_of_sale.DB');

	models.load_fields('product.product',['vendor_code'])

	DB.include({

	    init: function(options){
	        this._super.apply(this, arguments);
	    },

	    _product_search_string: function(product){
	        var str = product.display_name;
	        if (product.barcode) {
	            str += '|' + product.barcode;
	        }
	        if (product.default_code) {
	            str += '|' + product.default_code;
	        }
	        if (product.description) {
	            str += '|' + product.description;
	        }
	        if (product.description_sale) {
	            str += '|' + product.description_sale;
	        }
	        if (product.vendor_code) {
	            str += '|' + product.vendor_code;
	        }

	        str  = product.id + ':' + str.replace(/:/g,'') + '\n';
	        return str;
	    },

    });
    
});