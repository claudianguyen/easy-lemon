import React from 'react';
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'


class Dialog extends React.Component {

  constructor(props) {
    super(props);
  }

  /**
   * Creates the dialog image based on the dialog text.
   */
  createDialogImage(dialogText) {
    let imgSrc = null;
    switch(dialogText) {
      case Dialog.LOADING:
        // Use string here instead of in object outside because object keys cannot contain periods unless the key is a string.
        // TODO: Find better way to track image sources.
        imgSrc = "https://media1.tenor.com/images/cee12cb41fd3c8917c38452590dae11e/tenor.gif?itemid=10875814";
        break;
    }
    return imgSrc === null ? null : <img src={imgSrc} className="dialog-image"/>
  }

  render() {
    let closeButton = null;
    let dialogImage = null
    if (!this.props.showDialog) {
      return null;
    }
    if (this.props.dialogText === Dialog.ERROR) {
      closeButton = <button onClick={this.props.handleCloseDialogButton}> Close </button>;
    }
    dialogImage = this.createDialogImage(this.props.dialogText);
    return (
      <div className="dialog-mask-backdrop">
        <div className="dialog-container">
          <div className="dialog-contents">
            {dialogImage}
            <div>{this.props.dialogText}</div>
            {closeButton}
          </div>
        </div>
      </div>
    );
  }
}

// Props
Dialog.propTypes = {
  // Whether to show the dialog or not.
  showDialog: PropTypes.bool.isRequired,
  // Text to be shown inside the dialog.
  dialogText: PropTypes.string,
  // Handler to close the dialog.
  handleCloseDialogButton: PropTypes.func
};

Dialog.LOADING = "Loading...";
Dialog.ERROR = "An error occured. Please try again.";

export default Dialog;