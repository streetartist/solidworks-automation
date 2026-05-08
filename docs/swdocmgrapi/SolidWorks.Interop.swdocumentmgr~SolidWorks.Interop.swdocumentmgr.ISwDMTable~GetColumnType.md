# GetColumnType Method (ISwDMTable)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnType.html) on this topic. |
| GetColumnType Method (ISwDMTable) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md) : GetColumnType Method (ISwDMTable) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*ColumnIndex*
:   Index of column

Gets the type of the specified column

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetColumnType( _    ByVal ColumnIndex As System.Integer _ ) As SwDmColumnType ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable Dim ColumnIndex As System.Integer Dim value As SwDmColumnType   value = instance.GetColumnType(ColumnIndex) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmColumnType GetColumnType(     System.int ColumnIndex ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmColumnType GetColumnType(  &   System.int ColumnIndex ) ``` | |

#### Parameters

*ColumnIndex*
:   Index of column

#### Return Value

Type of column as defined by [swDmColumnType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmColumnType.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable::GetColumnType](swdocumentmgr~SwDMTable~GetColumnType.md).

# Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

Before calling this method, call [ISwDMTable::GetColumnCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.md) to determine the index of the column.

# See Also

#### 

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md)
  
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.md)
  
[ISwDMTable::AddColumnLeft Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnLeft.md)
  
[ISwDMTable::AddColumnRight Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnRight.md)
  
[ISwDMTable::DeleteColumn Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteColumn.md)
  
[ISwDMTable2::GetColumnCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnCustomProperty.md)
  
[ISwDMTable2::GetColumnWidth Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnWidth.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
