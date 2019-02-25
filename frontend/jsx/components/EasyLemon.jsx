import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'
import SearchComponent from './SearchComponent.jsx';

class EasyLemon extends React.Component {

  constructor(props) {
    super(props);
  
  // Bindings:
  this.updateResults = this.updateResults.bind(this);
  this.handleError = this.handleError.bind(this);
  this.handleJobSubmission = this.handleJobSubmission.bind(this);
  }

  /** 
  * Handles the submission for a job search. Creates the job_query for the backend.
  */
  handleJobSubmission() {
    let jobTitle = $('input[id=job-title]').val();
    let jobLocation = $('input[id=job-location]').val();
    let jobSalary = $('input[id=job-salary]').val();
    $('.submit-button').prop('disabled', true);
    $('.submit-button').val("Loading...");
    $.ajax({
        url: '/job_search',
        method: 'POST',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({jobTitle: jobTitle, jobLocation: jobLocation, jobSalary: jobSalary}),
        success: this.updateResults,
        error: this.handleError
    });
  }

  /**
   * Updates the page with results from the server. 
   */
  updateResults() {
    console.log("Success");
  }

  /**
   * Handles any server errors.
   */
  handleError() {
    console.log("Error");
  }


  render() {
    return <SearchComponent handleJobSubmission={this.handleJobSubmission} />
  }
}
// Props
EasyLemon.propTypes = {
};

export default EasyLemon;
