import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'
import JobResultComponent from './JobResultComponent.jsx'

class JobResultListComponent extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const jobResults = this.props.jobResultList;
    return (
      <div className="job-results-container">
        {
          jobResults.map(function(jobResult, index) {
            return <JobResultComponent jobResult={jobResult} key={index}/>
          })
        }
      </div>
    );
  }
}

// Props
JobResultListComponent.propTypes = {
  jobResultList : PropTypes.array
};

export default JobResultListComponent;