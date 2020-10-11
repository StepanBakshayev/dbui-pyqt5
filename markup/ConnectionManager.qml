import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import QtQuick.Window 2.12


ColumnLayout {
    id: root

    property alias urlField: urlField
    signal connectDB(string url)

    RowLayout {
        Label {
            text: qsTr("URL")
        }
        TextField {
            id: urlField
            placeholderText: qsTr("Enter URL 1232")
        }
    }
    RowLayout {
        Button {
            text: qsTr("Connect")
            onClicked: root.connectDB(urlField.text)
        }
    }
}
