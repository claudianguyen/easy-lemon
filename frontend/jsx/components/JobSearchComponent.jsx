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
        <label htmlFor="job-title">
          <span className="job-search-label">Job Title</span>
          <br/>
          <input type="text" 
            className="job-search-input-box" 
            id="job-title" 
            defaultValue="software engineer" 
            onChange={(e) => this.props.handleJobQueryChange(e, JobSearchComponent.jobTitle)}
          />
        </label>
        <br/>
        <label htmlFor="job-location">
          <span className="job-search-label">Location</span>
          <br/>
          <input type="text" 
            className="job-search-input-box" 
            id="job-location" 
            defaultValue="San Mateo"
            onChange={(e) => this.props.handleJobQueryChange(e, JobSearchComponent.jobLocation)}
          />
        </label>
        <br/>
        <label htmlFor="job-salary">
          <span className="job-search-label">Desired Salary</span>
          <br/>
          <input type="text" 
            className="job-search-input-box" 
            id="job-salary" 
            defaultValue="100000" 
            onChange={(e) => this.props.handleJobQueryChange(e, JobSearchComponent.jobSalary)}
          />
        </label>
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

JobSearchComponent.jobTitle = "jobTitle";
JobSearchComponent.jobSalary = "jobSalary";
JobSearchComponent.jobLocation = "jobLocation";


export default JobSearchComponent;
