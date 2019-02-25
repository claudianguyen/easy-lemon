import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'

class JobSearchComponent extends React.Component {

  constructor(props) {
    super(props);    
  }

  render() {
    return (
      <div className="job-search-div">
        <div className="job-search-param-div">
          <label htmlFor="job-title" className="job-search-label">Job Title</label>
          <br/>
          <input type="text" 
            className="job-search-input-box" 
            id="job-title" 
            defaultValue="software engineer" 
            onChange={(e) => this.props.handleJobQueryChange(e, JobSearchComponent.jobTitle)}
          />
        </div>
        <br/>
        <div className="job-search-param-div">
          <label htmlFor="job-location" className="job-search-label">Location</label>
          <br/>
          <input type="text" 
            className="job-search-input-box" 
            id="job-location" 
            defaultValue="San Mateo"
            onChange={(e) => this.props.handleJobQueryChange(e, JobSearchComponent.jobLocation)}
          />
        </div>
        <br/>
        <div className="job-search-param-div">
          <label htmlFor="job-salary" className="job-search-label">Desired Salary</label>
          <br/>
          <input type="number" 
            className="job-search-input-box" 
            id="job-salary" 
            defaultValue="100000" 
            onChange={(e) => this.props.handleJobQueryChange(e, JobSearchComponent.jobSalary)}
          />
        </div>
        <br/>
        <input type="button" className="job-search-submit-button" value="Submit" onClick={this.props.handleJobSubmission} />
      </div>
    );
  }
}

// Props
JobSearchComponent.propTypes = {
  handleJobSubmission: PropTypes.func.isRequired,
  handleJobQueryChange: PropTypes.func.isRequired
};

JobSearchComponent.JOB_TITLE = "jobTitle";
JobSearchComponent.JOB_LOCATION = "jobLocation";
JobSearchComponent.JOB_SALARY = "jobSalary";


export default JobSearchComponent;
