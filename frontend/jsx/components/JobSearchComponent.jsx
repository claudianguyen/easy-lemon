import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'

class JobSearchComponent extends React.Component {

  constructor(props) {
    super(props);    
  }

  render() {
    return (
      <div>
        <h1>Welcome to easy lemon!</h1>
        <div>
          <label htmlFor="job-title" >
            <span className="job-search-label">Job Title</span>
            <br/>
            <input type="text" className="job-search-input-box" id="job-title" value="software engineer" />
          </label>
          <br/>
          <label htmlFor="job-location" >
            <span className="job-search-label">Location</span>
            <br/>
            <input type="text" className="job-search-input-box" id="job-location" value="San Mateo" />
          </label>
          <br/>
          <label htmlFor="job-salary" >
            <span className="job-search-label">Desired Salary</span>
            <br/>
            <input type="text" className="job-search-input-box" id="job-salary" value="100000" />
          </label>
          <br/>
          <input type="button" className="job-search-submit-button" value="Submit" onClick={this.props.handleJobSubmission} />
        </div>
      </div>      
    );
  }
}
// Props
JobSearchComponent.propTypes = {
  handleJobSubmission: PropTypes.func.isRequired
};

export default JobSearchComponent;
