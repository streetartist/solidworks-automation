# IInterferenceDetectionMgr Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members`

Allows you to run interference detection on an assembly to determine whether components interfere with each other.
The following tables list the members exposed by [IInterferenceDetectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CreateFastenersFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~CreateFastenersFolder.md) | Gets or sets whether to create the Fasteners folders to segregate interferences involving fasteners. |
| Property | [IgnoreHiddenBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IgnoreHiddenBodies.md) | Gets or sets whether to ignore hidden bodies during interference detection. |
| Property | [IncludeMultibodyPartInterferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IncludeMultibodyPartInterferences.md) | Gets or sets whether to report interferences between bodies within multibody parts. |
| Property | [MakeInterferingPartsTransparent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.md) | Gets or sets whether to display the components of the selected interference in transparent mode. |
| Property | [NonInterferingComponentDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.md) | Gets or sets the mode to display non-interfering components. |
| Property | [ShowIgnoredInterferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ShowIgnoredInterferences.md) | Gets or sets whether to show ignored interferences. |
| Property | [TreatCoincidenceAsInterference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatCoincidenceAsInterference.md) | Gets or sets whether to treat coincident entities as interference. |
| Property | [TreatSubAssembliesAsComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.md) | Gets or sets whether to treat subassemblies as single components so that interferences between a sub-assembly's components are not reported. |
| Property | [UseTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~UseTransform.md) | Gets or sets whether to use transforms in interference detection. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Done](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~Done.md) | Stops the interference detection. |
| Method | [ExportResults](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ExportResults.md) | Saves interference detection results to a file. |
| Method | [GetComponentsAndTransforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsAndTransforms.md) | Gets the interfering components and their transforms. |
| Method | [GetComponentsTransformInterference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterference.md) | Calculates and gets the interfering components for the specified components and math transform. |
| Method | [GetComponentsTransformInterferenceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterferenceCount.md) | Calculates and gets the number of interfering components for the specified components and math transform. |
| Method | [GetInterferenceComponentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponentCount.md) | Calculates and gets the number of interfering components. |
| Method | [GetInterferenceComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.md) | Calculates and gets the interfering components. |
| Method | [GetInterferenceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceCount.md) | Calculates and gets the number of interferences. |
| Method | [GetInterferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferences.md) | Calculates and gets the interferences. |
| Method | [IGetComponentsTransformInterference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetComponentsTransformInterference.md) | Calculates and gets the interfering components for the specified components and math transform. |
| Method | [IGetInterferenceComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.md) | Calculates and gets the interfering components. |
| Method | [IGetInterferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferences.md) | Calculates and gets the interferences. |
| Method | [SetComponentsAndTransforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~SetComponentsAndTransforms.md) | Sets the interfering components and their transforms. |

[Top](#top)

 

See Also

#### Reference

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.md)  
[IModeler::CheckInterferenceBetweenTwoBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterferenceBetweenTwoBodies.md)
