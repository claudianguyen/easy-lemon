import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'
import JobSearchComponent from './JobSearchComponent.jsx';
import JobResultListComponent from './JobResultListComponent.jsx';
import Dialog from './Dialog.jsx';
import Header from './Header.jsx';

class EasyLemon extends React.Component {

  constructor(props) {
    super(props);

    // Initialize state.
    this.state = {
      jobTitle: "Software Engineer",
      jobLocation: "San Mateo",
      jobSalary: "120,000",
      jobExperience: "1",
      jobResults: [],
      showDialog: false,
      submissionDialogText:""
    }
  
    // Bind event handlers:
    this.handleCloseDialogButton = this.handleCloseDialogButton.bind(this);
    this.handleJobSubmission = this.handleJobSubmission.bind(this);
    this.handleJobQueryChange = this.handleJobQueryChange.bind(this);
    this.updateResults = this.updateResults.bind(this);
    this.handleError = this.handleError.bind(this);
    this.submitJobQuery = this.submitJobQuery.bind(this);
  }

  /**
   * Handles the close button for the dialog.
   */
  handleCloseDialogButton() {
    this.setState({ showDialog: false});
  }

  /** 
   * Handles the submission for a job search. Creates the job_query for the backend.
   */
  handleJobSubmission() {
    this.setState({ submissionDialogText: Dialog.LOADING, showDialog: true }, this.submitJobQuery);
  }

  /**
   * Handles the actual ajax request to submit the jobQuery to the backend.
   */
  submitJobQuery() {
    let jobTitle = this.state.jobTitle;
    let jobLocation = this.state.jobLocation;
    let jobExperience = this.state.jobExperience;
    let jobSalary = this.state.jobSalary;
    $.ajax({
      url: '/job_search',
      method: 'POST',
      contentType: 'application/json;charset=UTF-8',
      data: JSON.stringify({jobTitle: jobTitle, jobLocation: jobLocation, jobExperience: jobExperience, jobSalary: jobSalary}),
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
    this.setState({ jobResults: data, showDialog: false, submissionDialogText: ""});
  }

  /**
   * Handles any server errors.
   */
  handleError() {
    // alert("An error occurred. Please try again.");
    this.setState({ submissionDialogText: Dialog.ERROR });
  }

  /**
   * Handler for changes to the "Job Query" searchboxes.
   */
  handleJobQueryChange(e, jobParam) {
    switch(jobParam) {
      case JobSearchComponent.JOB_TITLE:
        this.setState({ jobTitle: e.target.value});
        break;
      case JobSearchComponent.JOB_LOCATION:
        this.setState({ jobLocation: e.target.value});
        break;
      case JobSearchComponent.JOB_SALARY:
        this.setState({ jobSalary: e.target.value});
        break;
      case JobSearchComponent.JOB_EXPERIENCE:
        this.setState({ jobExperience: e.target.value});
        break;
      default:
        return;
    }
  }

  render() {
    return (
      <div className="easy-lemon-container">
      <Header />
      <Dialog
        showDialog={this.state.showDialog}
        dialogText={this.state.submissionDialogText}
        handleCloseDialogButton={this.handleCloseDialogButton}
      />
        <JobSearchComponent 
          handleJobSubmission={this.handleJobSubmission}
          handleJobQueryChange={this.handleJobQueryChange}
        />
        <div />
        <JobResultListComponent jobResultList={this.state.jobResults} />
      </div>
    );
  }
}

// Props
EasyLemon.propTypes = {
};

export default EasyLemon;
