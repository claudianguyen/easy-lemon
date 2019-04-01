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
            <a className="job-title-text" target="_blank" href={jobResult.job_url}>{jobResult.job_title}</a>
          </h4>
          <div>
            <p>
              <span className="job-company-text">{jobResult.job_company} </span>
              <span className="job-experience-text">{jobResult.job_exp}</span>
              <span className="job-salary-text">{jobResult.job_salary}</span>
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
    job_title: PropTypes.string,
    job_url: PropTypes.string,
    job_company: PropTypes.string,
    job_exp: PropTypes.string,
    job_salary: PropTypes.string
  })
};

export default JobResultComponent;