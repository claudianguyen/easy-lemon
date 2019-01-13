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
    let data = JSON.parse(response);
    let jobResultsTable = $('#results tbody');
    jobResultsTable.empty();
    for (var jobResultIndex = 0; jobResultIndex < data.length; jobResultIndex++) {
        jobResult = data[jobResultIndex];
        let jobResultRow = "<tr>";
        jobResultRow += "<td>" + jobResult['job_title'] + "</td>";
        jobResultRow += "<td>" + jobResult['job_company'] + "</td>";
        jobResultRow += "<td>" + jobResult['job_exp'] + "</td>";
        jobResultRow += "<td>" + "<a target=\"_blank\"" + "href=\"" + jobResult['job_url'] + "\">click here</a>" + "</td>";
        jobResultRow += "</tr>";
        jobResultsTable.append(jobResultRow)
    }
}
