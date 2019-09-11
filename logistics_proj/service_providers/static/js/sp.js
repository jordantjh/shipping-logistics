function test() {
    param = document.getElementById("filter-by").value;
    window.location.replace("/?filterby=" + param);
}