import { withStyles } from '@ellucian/react-design-system/core/styles';
import { spacing40 } from '@ellucian/react-design-system/core/styles/tokens';
import { Typography, TextLink } from '@ellucian/react-design-system/core';
import React, { FC } from 'react';

interface TsDemoCardProps {
	classes: { [key: string]: string };
}

const TsDemoCard: FC<TsDemoCardProps> = ({ classes }) => {
	return (
		<div className={classes.card}>
			<Typography variant="h2">Aris TS demo extension</Typography>
			<Typography>
				<span>For sample extensions, visit the Ellucian Developer</span>
				<TextLink
					href="https://github.com/ellucian-developer/experience-extension-sdk-samples"
					target="_blank"
				>
					GitHub
				</TextLink>
			</Typography>
		</div>
	);
};

const styles = () => ({
	card: {
		marginTop: 0,
		marginRight: spacing40,
		marginBottom: 0,
		marginLeft: spacing40,
	},
});

export default withStyles(styles)(TsDemoCard);
