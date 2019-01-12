function submitJobSearch() {
    console.log("CLICK");
    $.ajax({
        url: '/job_search',
//        method: 'POST',
        success: helper_function
    });


};

function helper_function(response) {
    console.log(response)
    $('#results').html(response);
}
