
// Tables-DataTables.js
// ====================================================================
// This file should not be included in your project.
// This is just a sample how to initialize plugins or components.
//
// - ThemeOn.net -



$(window).on('load', function() {


    // DATA TABLES
    // =================================================================
    // Require Data Tables
    // -----------------------------------------------------------------
    // http://www.datatables.net/
    // =================================================================

    $.fn.DataTable.ext.pager.numbers_length = 5;


    // Basic Data Tables with responsive plugin
    // -----------------------------------------------------------------
    $('#demo-dt-basic').dataTable( {
        "responsive": true,
        "sPaginationType" : "full_numbers",
         "bScrollCollapse" : true,
         "columnDefs": [{ "bSortable": false, "aTargets": [2, 3, 4, 5, 6] }],
         // "sDom": 'T<"clear">lfrtip',
        // "tableTools": {
        //         "sSwfPath": "../statics/plugins/datatables/extensions/TableTools/swfcopy_csv_xls_pdf.swf",
        //
        //         "sRowSelect": "multi",
        //         "aButtons": [
        //                //{ "sExtends": "new_record", "sButtonText": "Add" },
        //                {
        //                    "sExtends": "select", "sButtonText": "Delete Recods",
        //                    "fnClick": function (nButton, oConfig, oFlash) {
        //                        //delete stuff comes here
        //                        alert('test');
        //                    }
        //
        //                }
        //         ]
        //     },
        "bStateSave" : true,
        "oLanguage": {
            "sProcessing": "<img src='/images/datatable_loading.gif'>  努力加载数据中.",
            "sLengthMenu": "每页显示 _MENU_ 条记录",
            "sZeroRecords": "抱歉， 没有找到",
            "sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
            "sInfoEmpty": "没有数据，请刷新页面 或请查看Redis是否存活",
            "sInfoFiltered": "(从 _MAX_ 条数据中检索)",

            "sSearch": "模糊查询:  ",
            "oPaginate": {

                "sFirst" : "第一页",
                "sPrevious": "前一页",
                "sNext": "后一页",
                "sLast": "尾页"
            }
        },
        "language": {
            sZeroRecords : "没有您要搜索的内容",
            "paginate": {
              "previous": '<span aria-hidden="true">&laquo;</span>',
              "next": '<span aria-hidden="true">&raquo;</span>'
            }
        }
    } );


    $('#demo-dt-basic').on( 'click', function (){

    });


    // Row selection (single row)
    // -----------------------------------------------------------------
    var rowSelection = $('#demo-dt-selection').DataTable({
        "responsive": true,
        "language": {
            "paginate": {
              "previous": '<span aria-hidden="true">&laquo;</span>',
              "next": '<span aria-hidden="true">&raquo;</span>'
            }
        }
    });

    $('#demo-dt-selection').on( 'click', 'tr', function () {
        if ( $(this).hasClass('selected') ) {
            $(this).removeClass('selected');
        }
        else {
            rowSelection.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
        }
    } );






    // Row selection and deletion (multiple rows)
    // -----------------------------------------------------------------
    var rowDeletion = $('#demo-dt-delete').DataTable({
        "responsive": true,
        "language": {
            "paginate": {
              "previous": '<i class="demo-psi-arrow-left"></i>',
              "next": '<i class="demo-psi-arrow-right"></i>'
            }
        },
        "dom": '<"toolbar">frtip'
    });
    $('#demo-custom-toolbar').appendTo($("div.toolbar"));

    $('#demo-dt-delete tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
    } );

    $('#demo-dt-delete-btn').click( function () {
        rowDeletion.row('.selected').remove().draw( false );
    } );






    // Add Row
    // -----------------------------------------------------------------
    var t = $('#demo-dt-addrow').DataTable({
        "responsive": true,
        "language": {
            "paginate": {
              "previous": '<i class="demo-psi-arrow-left"></i>',
              "next": '<i class="demo-psi-arrow-right"></i>'
            }
        },
        "dom": '<"newtoolbar">frtip'
    });
    $('#demo-custom-toolbar2').appendTo($("div.newtoolbar"));

    $('#demo-dt-addrow-btn').on( 'click', function () {
        t.row.add( [
            'Adam Doe',
            'New Row',
            'New Row',
            nifty.randomInt(1,100),
            '2015/10/15',
            '$' + nifty.randomInt(1,100) +',000'
        ] ).draw();
    } );


});
