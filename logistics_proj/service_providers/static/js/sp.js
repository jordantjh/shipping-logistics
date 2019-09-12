function deleteButton() {
    window.location.replace("?delete=yes");
}

function filterChanged() {
    param = document.getElementById("filter-by").value;
    window.location.replace("/?filterby=" + param);
}

function updateFormChanged() {
    updateSelect = document.getElementById("update-select");
    let addDiv = document.getElementById("form-add-div");  // multi-declare so put outside
    let child, signed_by, condition_comment, br;
    switch (updateSelect.value) {
        case 'dock-confirmed':
            // clear div before adding
            child = addDiv.firstElementChild;
            while (child) {
                addDiv.removeChild(child);
                child = addDiv.firstElementChild;
            }

            // create signed_by
            signed_by = document.createElement("input");
            signed_by.setAttribute("type", "text");
            signed_by.setAttribute("name", "signed_by");
            signed_by.setAttribute("placeholder", "signed by ...");
            signed_by.setAttribute("style", "margin-right: 10px;");


            // create condition_comment
            condition_comment = document.createElement("input");
            condition_comment.setAttribute("type", "text");
            condition_comment.setAttribute("name", "condition_comment");
            condition_comment.setAttribute("placeholder", "comment on condition");

            // append to form
            addDiv.appendChild(signed_by);
            addDiv.appendChild(condition_comment);
            break;
        case 'appt-confirmed':
            // clear div before adding
            child = addDiv.firstElementChild;
            while (child) {
                addDiv.removeChild(child);
                child = addDiv.firstElementChild;
            }

            // create appt_by_user
            let appt_by_user = document.createElement("input");
            appt_by_user.setAttribute("type", "text");
            appt_by_user.setAttribute("name", "appt_by_user");
            appt_by_user.setAttribute("placeholder", "Made by ...");
            appt_by_user.setAttribute("style", "margin-right: 10px;");
            appt_by_user.setAttribute("style", "margin-bottom: 2px;");

            // create <br>
            br = document.createElement("br");

            // create appt_comment
            let appt_comment = document.createElement("textarea");
            appt_comment.setAttribute("name", "appt_comment");
            appt_comment.setAttribute("rows", "2");
            appt_comment.setAttribute("cols", "50");
            appt_comment.setAttribute("placeholder", "Appointment Comment");

            // append to form
            addDiv.appendChild(appt_by_user);
            addDiv.appendChild(br);
            addDiv.appendChild(appt_comment);
            break;
        case 'delivery-confirmed':
            // clear div before adding
            child = addDiv.firstElementChild;
            while (child) {
                addDiv.removeChild(child);
                child = addDiv.firstElementChild;
            }

            // create signed_by
            signed_by = document.createElement("input");
            signed_by.setAttribute("type", "text");
            signed_by.setAttribute("name", "signed_by");
            signed_by.setAttribute("placeholder", "signed by ...");
            signed_by.setAttribute("style", "margin-right: 10px;");

            // create condition_comment
            condition_comment = document.createElement("input");
            condition_comment.setAttribute("type", "text");
            condition_comment.setAttribute("name", "condition_comment");
            condition_comment.setAttribute("placeholder", "comment on condition");
            condition_comment.setAttribute("style", "margin-bottom:2px;");

            // create <br>
            br = document.createElement("br");

            // create file upload
            let pod_div = document.createElement("p");
            pod_div.innerText = "Proof of Delivery: ";
            let pod_upload = document.createElement("input");
            pod_upload.setAttribute("type", "file");
            pod_upload.setAttribute("name", "pod_upload");
            pod_div.appendChild(pod_upload);

            // append to form
            addDiv.appendChild(signed_by);
            addDiv.appendChild(condition_comment);
            addDiv.appendChild(br);
            addDiv.appendChild(pod_div);
            break;
        default:
            // clear div
            child = addDiv.firstElementChild;
            while (child) {
                addDiv.removeChild(child);
                child = addDiv.firstElementChild;
            }
            break;
    }
}