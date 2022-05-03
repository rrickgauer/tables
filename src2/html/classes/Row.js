


class Row {

    constructor(pythonRowStruct) {
        this.field   = pythonRowStruct.field;
        this.type    = pythonRowStruct.type;
        this.null    = pythonRowStruct.null;
        this.key     = pythonRowStruct.key;
        this.default = pythonRowStruct.default;
        this.extra   = pythonRowStruct.extra;
    }

    getKeys() {
        const keys = Object.keys(this);
        return keys;
    }

    getTableRowHtml() {

        let html = `<tr class="table-row">`;

        const keys = this.getKeys();
        for (let count = 0; count < keys.length; count++) {
            const key = keys[count];
            html += this.getTableCellHtml(this[key]);
        }

        html += '</tr>';

        return html;

    }

    getTableCellHtml(cellData) {
        let html = `<td>${cellData}</td>`;
        return html;
    }



}