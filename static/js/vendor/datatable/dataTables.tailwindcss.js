/*! DataTables Tailwind CSS integration
 */

/*
 * This is a tech preview of Tailwind CSS integration with DataTables.
 */

// Set the defaults for DataTables initialisation
$.extend( true, DataTable.defaults, {
	renderer: 'tailwindcss'
} );


// Default class modification
$.extend( true, DataTable.ext.classes, {
	container: "dt-container dt-tailwindcss overflow-x-auto rounded-lg",
	search: {
		input: "w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
	},
	length: {
		select: "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
	},
	processing: {
		container: "dt-processing"
	},
	paging: {
		active: 'font-sm bg-gray-100 dark:bg-gray-700',		
		notActive: 'bg-white dark:bg-gray-800',
		//button: 'relative inline-flex justify-center items-center space-x-2 border px-4 py-1 leading-6 hover:z-10 focus:z-10 active:z-10 border-gray-200 hover:bg-primary-100 hover:text-primary-700 active:border-gray-200 active:shadow-none dark:border-gray-700 dark:active:border-gray-700',
		button: 'relative inline-flex items-center justify-center text-sm z-10 py-2 px-3 leading-tight text-primary-600 bg-primary-50 border border-primary-300 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white',
		first: 'rounded-l-lg',
		last: 'rounded-r-lg',
		enabled: 'text-gray-800 hover:text-gray-900 hover:border-gray-300 hover:shadow-sm focus:ring focus:ring-gray-300 focus:ring-opacity-25 dark:hover:bg-gray-700 dark:text-gray-300 dark:hover:border-gray-600 dark:hover:text-gray-200 dark:focus:ring-gray-600 dark:focus:ring-opacity-40',
		notEnabled: 'text-gray-300 dark:text-gray-600'
	},
	//table: 'min-w-full text-sm align-middle whitespace-nowrap',
	table: 'min-w-full divide-y',
	thead: {
		row: 'bg-gray-100 dark:bg-gray-700',
		cell: 'p-3 text-sm font-bold tracking-wider text-left text-gray-900 uppercase dark:text-white'
	},
	tbody: {
		row: 'even:bg-gray-100 dark:even:bg-gray-700',
		cell: 'p-3 text-sm font-normal text-gray-900 whitespace-nowrap dark:text-gray-200'
	},
	tfoot: {
		row: 'bg-gray-100 dark:bg-gray-700',
		cell: 'p-3 text-left'
	},
} );

DataTable.ext.renderer.pagingButton.tailwindcss = function (settings, buttonType, content, active, disabled) {
	var classes = settings.oClasses.paging;
	var btnClasses = [classes.button];

	btnClasses.push(active ? classes.active : classes.notActive);
	btnClasses.push(disabled ? classes.notEnabled : classes.enabled);

	var a = $('<a>', {
		'href': disabled ? null : '#',
		'class': btnClasses.join(' ')
	})
		.html(content);

	return {
		display: a,
		clicker: a
	};
};

DataTable.ext.renderer.pagingContainer.tailwindcss = function (settings, buttonEls) {
	var classes = settings.oClasses.paging;

	buttonEls[0].addClass(classes.first);
	buttonEls[buttonEls.length -1].addClass(classes.last);

	return $('<ul/>').addClass('pagination').append(buttonEls);
};

DataTable.ext.renderer.layout.tailwindcss = function ( settings, container, items ) {
	var row = $( '<div/>', {
			"class": items.full ?
				'grid grid-cols-1 gap-4 mb-4 inline-block min-w-full align-middle' :
				'grid grid-cols-2 gap-4 mb-4'
		} )
		.appendTo( container );

	$.each( items, function (key, val) {
		var klass;

		// Apply start / end (left / right when ltr) margins
		if (val.table) {
			klass = 'col-span-2 overflow-hidden shadow sm:rounded-lg';
		}
		else if (key === 'start') {
			klass = 'justify-self-start';
		}
		else if (key === 'end') {
			klass = 'col-start-2 justify-self-end';
		}
		else {
			klass = 'col-span-2 justify-self-center';
		}

		$( '<div/>', {
				id: val.id || null,
				"class": klass + ' ' + (val.className || '')
			} )
			.append( val.contents )
			.appendTo( row );
	} );
};
