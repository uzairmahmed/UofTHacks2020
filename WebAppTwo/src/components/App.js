import React, { Component } from 'react';
import MarkdownRender from './MarkdownRender';
import DashBoard from './DashBoard';
import logo from '../images/thumb.png';
export default class App extends Component {
	render() {
		const eqn =
			'\begin{equation} \begin{smallmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \\ end{smallmatrix} end{equation}';
		return (
			<div className="body">
				<div className="header">
					<span>
						<img className="header-logo" src={logo} alt=""></img>S.T.E.M. Notes
					</span>
				</div>
				<div className="page">
					<MarkdownRender></MarkdownRender>
				</div>
				<DashBoard></DashBoard>
			</div>
		);
	}
}
