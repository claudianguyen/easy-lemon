function submitJobSearch() {
    let jobTitle = $('input[name=job-title]').val();
    let jobLocation = $('input[name=job-location]').val();
    let jobSalary = $('input[name=job-salary]').val();
    $('.submit-button').prop('disabled', true);
    $('.submit-button').val("Loading...");
    $.ajax({
        url: '/job_search',
        method: 'POST',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({jobTitle: jobTitle, jobLocation: jobLocation, jobSalary: jobSalary}),
        success: updateResults

    });


};

function updateResults(response) {
    let data = JSON.parse(response);
    let jobResultsTable = $('#results tbody');
    jobResultsTable.empty();
    for (var jobResultIndex = 0; jobResultIndex < data.length; jobResultIndex++) {
        jobResult = data[jobResultIndex];
        let jobResultRow = "<tr>";
        jobResultRow += "<td>" + "<a target=\"_blank\"" + "href=\""
            + jobResult['job_url'] + "\">" + jobResult['job_title'] + "</a></td>";
        jobResultRow += "<td>" + jobResult['job_company'] + "</td>";
        jobResultRow += "<td>" + jobResult['job_exp'] + "</td>";
        jobResultRow += "<td>" + jobResult['job_salary'] + "</td>";
        jobResultRow += "</tr>";
        jobResultsTable.append(jobResultRow)
    }
    $('.submit-button').prop('disabled', false);
    $('.submit-button').val("Submit");


}
