import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'

class JobResultComponent extends React.Component {

	constructor(props) {
		super(props);
	}

  render() {
    const jobResult = this.props.jobResult;
    return (
      <div>
        <div className="job-result">
          <h4>
            <a className="job-title-text" target="_blank" href={jobResult.jobUrl}>{jobResult.jobTitle}</a>
          </h4>
          <div>
            <p>
              <span className="job-company-text">{jobResult.jobCompany} </span>
              <span className="job-experience-text">{jobResult.jobExperience}</span>
              <span className="job-salary-text">{jobResult.jobSalary}</span>
            </p>
          </div>
        </div>
      </div>
    );
  }
}

// Props
JobResultComponent.propTypes = {
  jobResult : PropTypes.shape({
    jobTitle: PropTypes.string,
    jobUrl: PropTypes.string,
    jobCompany: PropTypes.string,
    jobExperience: PropTypes.string,
    jobSalary: PropTypes.string
  })
};

export default JobResultComponent;