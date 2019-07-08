requirejs(['static/voila'], (voila) => {

    (async () => {
        const kernel = await voila.connectKernel();
        window.addEventListener('beforeunload', () => kernel.shutdown());

        const widgetManager = new voila.WidgetManager(kernel);

        const originalLoader = widgetManager.loader;
        widgetManager.loader = (moduleName, moduleVersion) => {
            if (moduleName === 'jupyter-vuetify') {
                moduleName = moduleName + '/nodeps'
            }
            return originalLoader(moduleName, moduleVersion);
        };

        await widgetManager.build_widgets();

        requirejs(['vue', 'app'], ({ provideWidget }, app) => {
            Object.values(widgetManager._models)
                .forEach(async (modelPromise) => {
                    const model = await modelPromise;
                    const meta = model.get('_metadata');
                    const mountId = meta && meta.mount_id;
                    if (mountId && model.get('_view_name')) {
                        const view = await widgetManager.create_view(model);
                        provideWidget(mountId, view);
                    }
                });

            app.$data.loading = false;
            removeInterferingStyleTags();
        });
    })();
});

function removeInterferingStyleTags() {
    document.querySelectorAll("style:not(#vuetify-theme-stylesheet)")
        .forEach((styleTag) => {
            if (styleTag.textContent.includes("/* Override Blueprint's _reset.scss styles */")) {
                document.head.removeChild(styleTag);
            }
        });
}

