import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import QtQuick.Window 2.12


Window {
    title: "UI for DB"

    id: window
    width: 400
    height: 500
    visible: true

    ConnectionManager {
        onConnectDB: application_state.connectDB(url)
        Component.onCompleted: urlField.text = application_state.url
    }
}
