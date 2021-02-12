


class Table {

    constructor(pythonTableStruct) {
        this.index = null;
        this.name = pythonTableStruct.table;
        this.rows = [];

        this.setRows(pythonTableStruct);

    }

    setRows(pythonTableStruct) {
        for (let count = 0; count < pythonTableStruct.data.length; count++) {
            const newRow = new Row(pythonTableStruct.data[count]);
            this.rows.push(newRow);
        }
    }


    getDropdownItemHtml() {
        let html = `<button class="dropdown-item dropdown-item-table" type="button" data-table-index="${this.index}">${this.name}</button>`;
        return html;
    }

    getTableHtml() {

        let html = '';
        for (let count = 0; count < this.rows.length; count++) {
            html += this.rows[count].getTableRowHtml();
        }

        return html;
    }


}


