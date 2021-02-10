

const m_TableData = G_TABLE_DATA;
const m_tables = [];
const m_tableNames = [];
const eTableDropdown = $('.dropdown-menu-tables');

// main logic
$(document).ready(function() {
    initTables();
    loadTableDropdownMenu();
    addListeners();
    
    // display the first table
    displayTableData(0);

    // set the first dropdown item to active
    let dropdownItems = $('.dropdown-item-table');
    toggleDropdownActiveClass(dropdownItems[0]);
});


// initialize all the table data into js objects
function initTables() {
    // convert all of the json data from python to js objects
    for (let count = 0; count < m_TableData.length; count++) {
        
        const newTable = new Table(m_TableData[count]);
        newTable.index = count;
        m_tables.push(newTable);
        
        m_tableNames.push(newTable.name);
    }

}


// display the tables in the dropdown
function loadTableDropdownMenu() {
    let html = '';

    for (let count = 0; count < m_tables.length; count++) {
        html += m_tables[count].getDropdownItemHtml();
    }

    $(eTableDropdown).html(html);
}


function addListeners() {
    listenerDropdownMenuItem();
}

function listenerDropdownMenuItem() {
    $(eTableDropdown).on('click', '.dropdown-item-table', function() {
        const index = $(this).attr('data-table-index');
        displayTableData(index);
        toggleDropdownActiveClass(this);
    });
}

function displayTableData(tableIndex) {
    const table = m_tables[tableIndex];
    const tableHtml = table.getTableHtml();

    $('#data-table tbody').html(tableHtml);
}


function toggleDropdownActiveClass(newActiveItem) {
    $('.dropdown-item-table').removeClass('active');
    $(newActiveItem).addClass('active');
}
