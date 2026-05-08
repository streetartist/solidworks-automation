# IMBD3DPdfData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members`

Gains access to the details for publishing a SOLIDWORKS MBD 3D PDF.
The following tables list the members exposed by [IMBD3DPdfData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Accuracy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~Accuracy.md) | Gets or sets the level of accuracy for lossy compression when publishing to SOLIDWORKS MBD 3D PDF. |
| Property | [CompressLossyTessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CompressLossyTessellation.md) | Gets or sets whether to apply lossy compression to polygons in the model when publishing to SOLIDWORKS MBD 3D PDF. |
| Property | [CreateAttachSTEP242](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CreateAttachSTEP242.md) | Gets or sets whether to export SOLIDWORKS parts and assemblies to STEP 242 format and attach the STEP 242 file to the SOLIDWORKS MBD 3D PDF. |
| Property | [ExcludeFromAnnotationView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ExcludeFromAnnotationView.md) | Gets or sets whether to exclude BOM tables from annotation views for this SOLIDWORKS MBD 3D PDF. |
| Property | [FilePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~FilePath.md) | Gets or sets the path and file name to which to save this SOLIDWORKS MBD 3D PDF. |
| Property | [STEP242Edition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~STEP242Edition.md) | Gets or sets the STEP 242 edition to use. |
| Property | [ThemeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.md) | Gets or sets the path and file name of the theme for this SOLIDWORKS MBD 3D PDF. |
| Property | [ViewPdfAfterSaving](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ViewPdfAfterSaving.md) | Gets or sets whether to display this SOLIDWORKS MBD 3D PDF after [publishing it](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.md). |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetAttachments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetAttachments.md) | Gets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF. |
| Method | [GetBomAreaCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetBomAreaCount.md) | Gets the number of BOM Table Areas defined in the [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.md) for this SOLIDWORKS MBD 3D PDF. |
| Method | [GetImportedNotes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetImportedNotes.md) | Gets the imported note names from the theme of this MBD3DPdfData. |
| Method | [GetMoreViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetMoreViews.md) | Gets the names of the custom views (i.e., [named views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.md) and [3D views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)) in the model for this SOLIDWORKS MBD 3D PDF. |
| Method | [GetStandardViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetStandardViews.md) | Gets the types of standard views in the model for this SOLIDWORKS MBD 3D PDF. |
| Method | [GetTextAndCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetTextAndCustomProperties.md) | Gets the text and custom properties in the [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.md) for this SOLIDWORKS MBD 3D PDF. |
| Method | [SetAttachments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetAttachments.md) | Sets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF. |
| Method | [SetBomTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetBomTable.md) | Maps a BOM Table Area in the [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.md) with a BOM table in the model and sets the columns in the BOM table to export to the BOM Table Area in a SOLIDWORKS MBD 3D PDF. |
| Method | [SetImportedNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetImportedNote.md) | Sets the specified imported note. |
| Method | [SetIndependentViewPort](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetIndependentViewPort.md) | Sets the specified view for an independent viewport for the SOLIDWORKS MBD 3D PDF. |
| Method | [SetMoreViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetMoreViews.md) | Sets the names of the custom views (i.e., [named views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.md) and [3D views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)) in the model for this SOLIDWORKS MBD 3D PDF. |
| Method | [SetStandardViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetStandardViews.md) | Sets the types of standard views in the model for this SOLIDWORKS MBD 3D PDF. |

[Top](#top)

 

See Also

#### Reference

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDocExtension::PublishTo3DPDF Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.md)  
[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)
