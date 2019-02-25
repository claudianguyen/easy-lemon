import React, { Component } from 'react';
import ReactDOM from 'react-dom'
import EasyLemon from './components/EasyLemon.jsx';

$(document).ready(function() {
	let easyLemonApp = document.querySelector("#easy-lemon-app");
	ReactDOM.render(<EasyLemon />, easyLemonApp);
});
