function DataArray() {
    const influenzer = ["Veren", "Thea", "Kezia"];
    document.getElementById('array1').innerHTML = influenzer[0];
    document.getElementById('array2').innerHTML = influenzer[1];
    document.getElementById('array3').innerHTML = influenzer[2];
}
function DataObject() {
    const food = {
        "object1": "noodles",
        "object2": "fried chicken",
        "object3": "meatball"
    };
    document.getElementById('object1').innerHTML = food.object1;
    document.getElementById('object2').innerHTML = food.object2;
    document.getElementById('object3').innerHTML = food.object3;
}