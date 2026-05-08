# IDesignTable Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members`

Allows access to design table information and values.
The following tables list the members exposed by [IDesignTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AutoAddNewConfigs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AutoAddNewConfigs.md) | Gets or sets whether to automatically add rows or columns to the design table when new configurations are added to the model. |
| Property | [AutoAddNewParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AutoAddNewParams.md) | Gets or sets whether or not to automatically add rows or columns to the design table when new parameters are added to the model. |
| Property | [ColumnHidden](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.md) | Gets the visibility state of the specified column. |
| Property | [EnableCellDropdownLists](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EnableCellDropdownLists.md) | Gets or sets whether to enable cell drop-down lists in the design table. |
| Property | [FileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName.md) | Gets or sets the Microsoft Excel file for this design table. |
| Property | [LastError](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~LastError.md) | Gets or sets the last error that occurred in this design table. |
| Property | [LinkToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~LinkToFile.md) | Gets or sets whether to link the design table to the model. |
| Property | [RowHidden](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.md) | Gets the visibility state of the specified row. |
| Property | [SourceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType.md) | Gets or sets the type of source file for this design table. |
| Property | [Updatable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Updatable.md) | Gets or sets whether edits to the model update the design table. |
| Property | [Warn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Warn.md) | Gets or sets whether to display a warning when invalid information is encountered in the design table when updating the design table. |
| Property | [Worksheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Worksheet.md) | Gets the Microsoft Excel worksheet for this design table. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddRow](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.md) | Adds a row to the design table. |
| Method | [Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md) | Activates the design table within the part or assembly document. |
| Method | [Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.md) | Detaches the design table from the Microsoft Excel sheet. |
| Method | [EditFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.md) | Lets you change the characteristics of the design table. |
| Method | [EditTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable.md) | Obsolete. Superseded by [IDesignTable::EditTable2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2.md). |
| Method | [EditTable2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2.md) | Lets you edit the design table. |
| Method | [GetColumnCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount.md) | Gets the number of columns in the design table that are currently visible in the model view. |
| Method | [GetEntryText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryText.md) | Gets the contents of the specified cell as a string regardless of the cell's data type. |
| Method | [GetEntryValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryValue.md) | Gets the contents of the specified cell. |
| Method | [GetHeaderText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetHeaderText.md) | Gets the header text for the specified column. |
| Method | [GetRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.md) | Gets the number of rows in the design table that are currently visible in the model view. |
| Method | [GetStartColumnNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.md) | Gets the number of the first column in which a dimension is displayed. |
| Method | [GetStartRowNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.md) | Gets the number of the first row in which dimensions are displayed. |
| Method | [GetTitle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTitle.md) | Gets the design table title. |
| Method | [GetTotalColumnCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalColumnCount.md) | Gets the number of columns in the design table. |
| Method | [GetTotalRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalRowCount.md) | Gets the number of rows in the design table. |
| Method | [GetVisibleColumnCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleColumnCount.md) | Gets the number of columns visible in this design table. |
| Method | [GetVisibleLeftColumnNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.md) | Gets the number of the leftmost visible column. |
| Method | [GetVisibleRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.md) | Gets the number of rows visible in the design table. |
| Method | [GetVisibleTopRowNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.md) | Gets the number of the topmost visible row. |
| Method | [IsActive](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~IsActive.md) | Gets whether the design table is currently being edited. |
| Method | [SaveAsExcelFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SaveAsExcelFile.md) | Saves the design table to a Microsoft Excel file. |
| Method | [SetEntryText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryText.md) | Sets the text value of the specified entry. |
| Method | [SetEntryValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryValue.md) | Sets the data type and value in the specified cell. |
| Method | [SetRowChanged](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetRowChanged.md) | Sets the number of the row that was changed. |
| Method | [UpdateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.md) | Updates the characteristics of the design table. |
| Method | [UpdateModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.md) | Applies the edits to the design table to the model. |
| Method | [UpdateTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateTable.md) | Applies the changes made to the design table to the model. |

[Top](#top)

 

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
