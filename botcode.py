st.markdown(
    """<script type='text/javascript'>
	function initEmbeddedMessaging() {
		try {
			embeddedservice_bootstrap.settings.language = 'en_US'; // For example, enter 'en' or 'en-US'

			embeddedservice_bootstrap.init(
				'00D5w000004yOc7',
				'Rola',
				'https://casevault-dev-ed.my.site.com/ESWRola1712059238373',
				{
					scrt2URL: 'https://casevault-dev-ed.my.salesforce-scrt.com'
				}
			);
		} catch (err) {
			console.error('Error loading Embedded Messaging: ', err);
		}
	};
</script>
<script type='text/javascript' src='https://casevault-dev-ed.my.site.com/ESWRola1712059238373/assets/js/bootstrap.min.js' onload='initEmbeddedMessaging()'></script>
""",
    unsafe_allow_html=True,
)
