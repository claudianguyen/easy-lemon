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
    

    console.log("In JobResultsListComponent, JobResult is: ");
    console.log(jobResults);
    return (
      <div className="job-results-container">
        {jobResults.map(function(jobResult, index) {
          return <JobResultComponent jobResult={jobResult} />
        })}
      </div>
      
    );
  }
}

// Props
JobResultListComponent.propTypes = {
  jobResultList : PropTypes.array
};

export default JobResultListComponent;