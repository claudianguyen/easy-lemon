function submitJobSearch() {
    let jobTitle = $('input[name=job-title]').val();
    let jobLocation = $('input[name=job-location]').val();
    let jobSalary = $('input[name=job-salary]').val();
    let requestData = {jobTitle: jobTitle, jobLocation: jobLocation, jobSalary: jobSalary};
    $.ajax({
        url: '/job_search',
//        method: 'POST',
        contentType: 'application/json;charset=UTF-8',
        dataType: 'json',
        data: JSON.stringify(requestData, null, '\t'),
        success: updateResults

    });


};

function updateResults(response) {
    $('#results').html(response);
}
