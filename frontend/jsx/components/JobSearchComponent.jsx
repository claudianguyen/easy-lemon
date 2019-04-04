import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'

class JobSearchComponent extends React.Component {

  constructor(props) {
    super(props);    
  }

  /**
   * Only allow numbers and the comma.
   * TODO: More robust handling.
   */
   allowOnlySalaryValues(e) {
    let charCode = e.keyCode || e.which;
    if ((charCode < 48 || e.charCode > 57) && charCode != 188) {
      e.preventDefault();
    }
  }

  render() {
    const years = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10+"]
    return (
      <div className="job-search-div">
        <div className="job-search-param-div">
          <label htmlFor="job-title" className="job-search-label">Job Title</label>
          <br/>
          <input type="text" 
            className="job-search-input-box" 
            id="job-title" 
            defaultValue="software engineer" 
            onChange={(e) => this.props.handleJobQueryChange(e, JobSearchComponent.JOB_TITLE)}
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
            onChange={(e) => this.props.handleJobQueryChange(e, JobSearchComponent.JOB_LOCATION)}
          />
        </div>
        <br/>
        <div className="job-search-param-div">
          <label htmlFor="job-salary" className="job-search-label">Desired Salary</label>
          <br/>
          <input type="text" 
            className="job-search-input-box" 
            id="job-salary" 
            defaultValue="100000" 
            onChange={(e) => this.props.handleJobQueryChange(e, JobSearchComponent.JOB_SALARY)}
            onKeyPress={this.allowOnlySalaryValues}
          />
        </div>
        <br/>
        <div className="job-search-param-div">
          <label htmlFor="job-experience" className="job-search-label">Years of Experience</label>
          <br/>
          <select 
            className="job-search-select"
            id="job-experience"
            onChange={(e) => this.props.handleJobQueryChange(e, JobSearchComponent.JOB_EXPERIENCE)}>
              {years.map(year =>
                <option key={year} value={year}>{year}</option>)
              };
          </select>
          <br/>
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
JobSearchComponent.JOB_EXPERIENCE = "jobExperience";


export default JobSearchComponent;
