import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'
import JobSearchComponent from './JobSearchComponent.jsx';
import JobResultListComponent from './JobResultListComponent.jsx';

class EasyLemon extends React.Component {

  constructor(props) {
    super(props);

    // Initialize state.
    this.state = {
      jobTitle: "Software Engineer",
      jobLocation: "San Mateo",
      jobSalary: "120,000",
      jobResults: []
    }
  
    // Bind event handlers:
    this.handleJobSubmission = this.handleJobSubmission.bind(this);
    this.handleJobQueryChange = this.handleJobQueryChange.bind(this);
    this.updateResults = this.updateResults.bind(this);
  }

  /** 
   * Handles the submission for a job search. Creates the job_query for the backend.
   */
  handleJobSubmission() {
    let jobTitle = this.state.jobTitle;
    let jobLocation = this.state.jobLocation;
    let jobSalary = this.state.jobSalary;
    $('.job-search-submit-button').prop('disabled', true);
    $('.job-search-submit-button').val("Loading...");
    $.ajax({
        url: '/job_search',
        method: 'POST',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({jobTitle: jobTitle, jobLocation: jobLocation, jobSalary: jobSalary}),
        success: this.updateResults,
        error: this.handleError
    });
    // console.log(this.state);
  }

  /**
   * Updates the page with results from the server. 
   */
  updateResults(response) {
    let data = JSON.parse(response);
    this.setState({ jobResults: data});

    $('.job-search-submit-button').prop('disabled', false);
    $('.job-search-submit-button').val("Submit");
  }

  /**
   * Handles any server errors.
   */
  handleError() {
    $('.job-search-submit-button').prop('disabled', false);
    $('.job-search-submit-button').val("Submit");
    alert("An error occurred. Please try again.");
  }

  /**
   * Handler for changes to the "Job Query" searchboxes.
   */
  handleJobQueryChange(e, jobParam) {
    switch(jobParam) {
      case JobSearchComponent.JOB_TITLE:
        this.setState({ jobTitle: e.target.value});
      case JobSearchComponent.jobLocation:
        this.setState({ jobLocation: e.target.value});
      case JobSearchComponent.jobSalary:
        this.setState({ jobSalary: e.target.value});
      default:
        return;
    }
  }

  render() {
    return (
      <div className="easy-lemon-container">
        <h1 className="easy-lemon-header">Welcome to easy lemon!</h1>
        <JobSearchComponent 
          handleJobSubmission={this.handleJobSubmission}
          handleJobQueryChange={this.handleJobQueryChange}
        />
        <JobResultListComponent jobResultList={this.state.jobResults} />
      </div>
    );
  }
}
// Props
EasyLemon.propTypes = {
};

export default EasyLemon;
