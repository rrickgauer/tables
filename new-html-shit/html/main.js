/***************************************************
module variables
****************************************************/
const m_TableData           = G_TABLE_DATA;
let m_DatabaseName          = null;
const m_tables              = [];
const m_tableNames          = [];
const eTableDropdown        = $('.dropdown-menu-tables');
const eNumRows              = $('#num-rows');
const eColumnToggleDropdown = $('.dropdown-toggle-columns');
const eTable                = $('#data-table');
const eToggleActiveRows     = $('#toggle-active-rows');

/***************************************************
main logic
****************************************************/
$(document).ready(function() {
    initTables();
    displayDatabaseName();
    loadTableDropdownMenu();
    addListeners();
    
    // display the first table
    displayTableData(0);

    // set the first dropdown item to active
    let dropdownItems = $('.dropdown-item-table');
    toggleDropdownActiveClass(dropdownItems[0]);


});


function displayDatabaseName() {
    $('#db-name').text(m_DatabaseName);
}

/***************************************************
initialize all the table data into js objects
****************************************************/
function initTables() {
    m_DatabaseName = m_TableData.database;

    // convert all of the json data from python to js objects
    for (let count = 0; count < m_TableData.tables.length; count++) {
        
        const newTable = new Table(m_TableData.tables[count]);
        newTable.index = count;
        m_tables.push(newTable);
        
        m_tableNames.push(newTable.name);
    }

}


/***************************************************
display the tables in the dropdown
****************************************************/
function loadTableDropdownMenu() {
    let html = '';

    for (let count = 0; count < m_tables.length; count++) {
        html += m_tables[count].getDropdownItemHtml();
    }

    $(eTableDropdown).html(html);
}


/***************************************************
add all the event listeners
****************************************************/
function addListeners() {
    listenerDropdownMenuItem();
    listenerColumnToggleDropdown();
    listenerActivateTableRows();
    listenerToggleActiveRows();
}

/***************************************************
add all the event listeners
****************************************************/
function listenerDropdownMenuItem() {
    $(eTableDropdown).on('click', '.dropdown-item-table', function() {
        const index = $(this).attr('data-table-index');
        displayTableData(index);
        toggleDropdownActiveClass(this);
    });
}

/***************************************************
display a new table after selecting it from the 
dropdown
****************************************************/
function displayTableData(tableIndex) {
    const table = m_tables[tableIndex];
    const tableHtml = table.getTableHtml();

    $('#data-table tbody').html(tableHtml);

    addTableRowNumbers();
    loadAllTableText();
    displayNumberOfRows(tableIndex);
    displayTableName(table.name);
}


/***************************************************
Add row numbers to the table
****************************************************/
function addTableRowNumbers() {
    let rows = $('.table-row');

    for (let count = 0; count < rows.length; count++) {
        let row = $(rows[count]);
        $(row).prepend(`<td>${count + 1}</td>`);        
    }
}

/***************************************************
Displays the number of rows
****************************************************/
function displayNumberOfRows(tableIndex) {
    const numRows = m_tables[tableIndex].rows.length;
    $(eNumRows).text(numRows);
}

/***************************************************
Displays the table name in the tables dropdown menu
****************************************************/
function displayTableName(tableName) {
    $('.table-selector .dropdown-toggle').text(tableName);
}


/***************************************************
When a user selects a new table from the dropdown,
set it to active.
****************************************************/
function toggleDropdownActiveClass(newActiveItem) {
    $('.dropdown-item-table').removeClass('active');
    $(newActiveItem).addClass('active');
}



/***************************************************
Listens for users to toggle a column in the table
****************************************************/
function listenerColumnToggleDropdown() {
    $(eColumnToggleDropdown).find('.dropdown-item').on('click', function() {
        toggleColumn(this);
    });
}


/***************************************************
Show/hide a column in the table
****************************************************/
function toggleColumn(eDropdownItem) {
    // make sure at least one column is always visi
    if ($(eDropdownItem).hasClass('active') && !validateColumnToggle()) {
        return;
    }


    $(eDropdownItem).toggleClass('active');
    let columnIndex = $(eDropdownItem).attr('data-column-index');

    // hide the header
    const theaders = $(eTable).find('thead th');
    $(theaders[columnIndex]).toggleClass('column-hidden');

    columnIndex++;
    // hide the column in the body
    $(`.table-row td:nth-child(${columnIndex})`).toggleClass('column-hidden');
}

/***************************************************
Check if there is at least one active column
****************************************************/
function validateColumnToggle() {
    const numActiveColumns = $(eColumnToggleDropdown).find('.dropdown-item.active').length;

    if (numActiveColumns >= 2) {
        return true;
    } else {
        return false;
    }

}


/***************************************************
Listens for user to click on a row to toggle its
active status
****************************************************/
function listenerActivateTableRows() {
    $(eTable).on('click', '.table-row', function() {
        activateTableRow(this);
    });
}

/***************************************************
Toggles a table row's active status
****************************************************/
function activateTableRow(eTableRow) {
    $(eTableRow).toggleClass('active');
}





/***************************************************
Listens for user to toggle the checkbox that shows/hides
the active rows
****************************************************/
function listenerToggleActiveRows() {
    $(eToggleActiveRows).on('change', function() {
        toggleActiveRows();
    });
}


function toggleActiveRows() {

    $('.table-row').hide();

    const onlyShowActive = $(eToggleActiveRows).is(':checked');

    if (onlyShowActive) {
        $('.table-row.active').show();
    } else {
        $('.table-row').show();
    }
}