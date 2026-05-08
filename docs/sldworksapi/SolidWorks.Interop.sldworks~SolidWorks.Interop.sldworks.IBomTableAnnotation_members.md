# IBomTableAnnotation Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members`

Allows access to the IBomFeature object for this table annotation.
The following tables list the members exposed by [IBomTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [BomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~BomFeature.md) | Gets the BOM for this table annotation. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [ApplySavedSortScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~ApplySavedSortScheme.md) | Sorts this BOM table using the sort data that was previously saved in the table. |
| Method | [Collapse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Collapse.md) | Collapses the specified item. |
| Method | [Dissolve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Dissolve.md) | Dissolves into individual components the subassembly or weldment at the specified row index of this BOM table annotation. |
| Method | [Expand](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Expand.md) | Expands the specified item. |
| Method | [GetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomProperties.md) | Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation. |
| Method | [GetAllCustomPropertiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomPropertiesCount.md) | Gets the number of items in the list of available custom properties that can be used for a custom properties column in this BOM table annotation. |
| Method | [GetBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetBomTableSortData.md) | Gets an instance of [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md). |
| Method | [GetColumnCustomProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnCustomProperty.md) | Gets the custom property used to fill the values in a specified user-defined column. |
| Method | [GetColumnUseTitleAsPartNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnUseTitleAsPartNumber.md) | Gets whether the document title is being used for the specified part-number column. |
| Method | [GetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents.md) | Obsolete. Superseded by [IBomTableAnnotation::GetComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.md). |
| Method | [GetComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.md) | Gets the components in the specified row for the specified configuration in this BOM table annotation. |
| Method | [GetComponentsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount.md) | Obsolete. Superseded by [IBomTableAnnotation::GetComponentsCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.md). |
| Method | [GetComponentsCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.md) | Gets the number of components, the item number, and the part number in the specified row for the specified configuration in this BOM table annotation. |
| Method | [GetModelPathNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNames.md) | Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row. |
| Method | [GetModelPathNamesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNamesCount.md) | Gets the number of model pathnames in the specified row of this BOM table annotation. |
| Method | [IGetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetAllCustomProperties.md) | Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation. |
| Method | [IGetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents.md) | Obsolete. Superseded by [IBomTableAnnotation::IGetComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents2.md). |
| Method | [IGetComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents2.md) | Gets the components in the specified row for the specified configuration in this BOM table annotation. |
| Method | [IGetModelPathNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetModelPathNames.md) | Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row. |
| Method | [RestoreRestructuredComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~RestoreRestructuredComponents.md) | Restores the previously dissolved subassembly or weldment at the specified row index of this BOM table annotation. |
| Method | [SaveAsExcel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SaveAsExcel.md) | Saves this BOM table annotation as a Microsoft Excel document with the specified properties. |
| Method | [SetColumnCustomProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SetColumnCustomProperty.md) | Sets the custom property used to fill the values in a specified user-defined column. |
| Method | [SetColumnUseTitleAsPartNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SetColumnUseTitleAsPartNumber.md) | Sets whether to use the document title for the specified part-number column. |
| Method | [Sort](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Sort.md) | Sorts this BOM table using the specified sorting data. |

[Top](#top)

 

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md)
