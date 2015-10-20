// Get and prepare data from database
var counter = 0;
var createdDates = [];
var slicedDates = [];
var uniqueDates = [];
var registeredPerDate = [];
var numberOfUniqueItems = 0;

$('.data').each(function () {

    //var name = $(this).attr('name');
    //var email = $(this).attr('email');
    var created = $(this).attr('created');
    if(created != undefined){

        createdDates.push(created);
        slicedDates.push(created.split(",").shift());
        counter += 1;
    }
});

// Figure how many unique items there are
for(var i = 0; i < slicedDates.length; i++){
    if(slicedDates[i] != slicedDates[i - 1]){
        // initialise the array with 0 for each Date
        registeredPerDate.push(0);
        // add unique items to list
        uniqueDates.push(slicedDates[i]);
    }
}

// figure out how many registrations for the same date and then increment the array index for each date.
for(var i = 0; i < slicedDates.length; i++) {
    if (registeredPerDate[numberOfUniqueItems] == 0) {
        registeredPerDate[numberOfUniqueItems] += 1;
    } else {
        if (slicedDates[i] == slicedDates[i - 1]) {
            registeredPerDate[numberOfUniqueItems] += 1;
        } else {
            numberOfUniqueItems += 1;
            registeredPerDate[numberOfUniqueItems] += 1;
        }
    }
}



// debug
console.log("counter = " + counter);
console.log("unique dates = " + uniqueDates);
console.log("Registrations per day = " + registeredPerDate);

var options = {
  //width: 500,
  //height: 300
};

var data = {
  labels: uniqueDates,
  series: [
    registeredPerDate
  ]
};


// Initialize a Line chart in the container with the ID chart1
  new Chartist.Line('#chart1', data, options);

  // Initialize a Line chart in the container with the ID chart2
  new Chartist.Bar('#chart2', data, options);