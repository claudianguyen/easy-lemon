function submitJobSearch() {
    let jobTitle = $('input[name=job-title]').val();
    let jobLocation = $('input[name=job-location]').val();
    let jobSalary = $('input[name=job-salary]').val();
    $.ajax({
        url: '/job_search',
        method: 'POST',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({jobTitle: jobTitle, jobLocation: jobLocation, jobSalary: jobSalary}),
        success: updateResults

    });


};

function updateResults(response) {
    $('#results').html(response);
}
