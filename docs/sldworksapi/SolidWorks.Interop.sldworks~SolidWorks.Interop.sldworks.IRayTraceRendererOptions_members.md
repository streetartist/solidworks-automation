# IRayTraceRendererOptions Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members`

Allows access to a ray-trace rendering engine's options.
The following tables list the members exposed by [IRayTraceRendererOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AlphaOutput](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~AlphaOutput.md) | Gets or sets whether to [render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md) the model as alpha or final color output. |
| Property | [BloomEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomEnabled.md) | Gets or sets whether to enable bloom effect. |
| Property | [BloomRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomRadius.md) | Gets or sets the the distance bloom radiates from source. |
| Property | [BloomThreshold](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomThreshold.md) | Gets or sets the level of brightness or emissiveness to which bloom effect is applied. |
| Property | [CausticAmount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticAmount.md) | Gets or sets the maximum number of photons fired, which controls the amount of visible caustics. |
| Property | [CausticQuality](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticQuality.md) | Gets or sets the number of photons sampled at each pixel, which controls the quality of the caustics. |
| Property | [ClientWorkload](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload.md) | Gets or sets how many buckets (sections of rendering) are sent to each client processor. |
| Property | [ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.md) | Gets or sets whether to enable contour/cartoon rendering. |
| Property | [ContourEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourEnabled.md) | Obsolete. Superseded by [IRayTraceRendererOptions::ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.md). |
| Property | [ContourLineColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineColor.md) | Gets or sets the color of the contour lines. |
| Property | [ContourLineThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineThickness.md) | Gets or sets the thickness of contour lines. |
| Property | [CustomRenderSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CustomRenderSettings.md) | Gets or sets whether to enable custom render settings. |
| Property | [DefaultImagePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DefaultImagePath.md) | Gets or sets the default path to which to save the image. |
| Property | [DirectCaustics](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DirectCaustics.md) | Gets or sets whether to enable direct caustics in the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md). |
| Property | [FinalRenderQuality](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~FinalRenderQuality.md) | Gets or sets quality of the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md). |
| Property | [Gamma](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~Gamma.md) | Gets or sets the value for midtones of the rendered image while preserving the extreme whites and blacks. |
| Property | [HasCartoonEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonEdges.md) | Gets or sets whether to render with cartoon edges. |
| Property | [HasCartoonShading](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonShading.md) | Gets or sets whether to render with cartoon shading. |
| Property | [ImageFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageFormat.md) | Gets or sets the format of the image. |
| Property | [ImageHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageHeight.md) | Gets or sets the height of the image. |
| Property | [ImageWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageWidth.md) | Gets or sets the width of the image. |
| Property | [IncludeAnnotationsInRendering](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~IncludeAnnotationsInRendering.md) | Gets or sets whether to include annotations and dimensions visible in the model when [rendering to a file](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile.md). |
| Property | [NetworkRendering](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.md) | Gets or sets whether to enable network rendering. |
| Property | [NetworkSharedDirectory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory.md) | Gets or sets the name of the shared network directory for [network renders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.md). |
| Property | [NumberOfReflections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NumberOfReflections.md) | Gets or sets the number of reflections in the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md). |
| Property | [NumberOfRefractions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NumberOfRefractions.md) | Gets or sets the number of refractions in the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.md). |
| Property | [OffloadedRendering](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering.md) | Gets or sets whether to offload rendering to other networked machines. |
| Property | [OutputAmbientOcclusion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OutputAmbientOcclusion.md) | Gets or sets whether to render with ambient occlusion. |
| Property | [PreviewRenderQuality](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~PreviewRenderQuality.md) | Gets or sets the quality of the rendering in the preview window. |
| Property | [RenderAnnotationsToSeparateImage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderAnnotationsToSeparateImage.md) | Gets or sets whether to render annotations and dimensions visible in the model to a separate image file. |
| Property | [RenderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderType.md) | Gets or sets whether to render with contour or cartoon lines. |
| Property | [SendDataForNetworkJob](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob.md) | Gets or sets whether to send rendering data over the network. |
| Property | [ShadedContour](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ShadedContour.md) | Gets or sets whether to shade the contours lines. |
| Property | [UseSceneBackgroundImageAspectRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UseSceneBackgroundImageAspectRatio.md) | Gets or sets whether to use the aspect ratio of the scene's background image for ray-trace rendering engine preview and final renders. |
| Property | [UseSolidWorksViewAspectRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UseSolidWorksViewAspectRatio.md) | Gets or sets whether to use the aspect ratio of the SOLIDWORKS view for ray-trace rendering engine preview and final renders. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [UpdateGraphics](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UpdateGraphics.md) | Updates the graphics area. |

[Top](#top)

 

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
