function showResultConst() {
    const x = 10;
    document.getElementById("idConst").innerHTML = "x : "+ x;

    // const x = 6; -> Error: x has been defined
    // y = 7; -> Error: const cannot be Reassigned

    // Error: const Must be Assigned
    // const z;
    // z = 8;
}