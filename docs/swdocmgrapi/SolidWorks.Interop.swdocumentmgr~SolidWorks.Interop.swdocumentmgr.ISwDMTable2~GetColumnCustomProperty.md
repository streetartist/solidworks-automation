# GetColumnCustomProperty Method (ISwDMTable2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnCustomProperty`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnCustomProperty.html) on this topic. |
| GetColumnCustomProperty Method (ISwDMTable2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.md) : GetColumnCustomProperty Method (ISwDMTable2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*ColumnIndex*
:   Index of the column

*Error*
:   Error as defined by [swDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

Gets the custom property for the specified column in this table.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetColumnCustomProperty( _    ByVal ColumnIndex As System.Integer, _    ByRef Error As SwDmTableError _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable2 Dim ColumnIndex As System.Integer Dim Error As SwDmTableError Dim value As System.String   value = instance.GetColumnCustomProperty(ColumnIndex, Error) ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetColumnCustomProperty(     System.int ColumnIndex,    out SwDmTableError Error ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetColumnCustomProperty(  &   System.int ColumnIndex, &   [Out] SwDmTableError Error ) ``` | |

#### Parameters

*ColumnIndex*
:   Index of the column

*Error*
:   Error as defined by [swDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

#### Return Value

Column custom property, which is in the form of "$PRP:..."

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable2::GetColumnCustomProperty](swdocumentmgr~SwDMTable2~GetColumnCustomProperty.md).

# Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

Before calling this method, call [ISwDMTable::GetColumnCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.md) to determine the index of the column to whose custom property you want.

# See Also

#### 

[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.md)
  
[ISwDMTable2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2_members.md)
  
[ISwDMTable::AddColumnLeft Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnLeft.md)
  
[ISwDMTable::AddColumnRight Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnRight.md)
  
[ISwDMTable::DeleteColumn Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteColumn.md)
  
[ISwDMTable::GetColumnCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.md)
  
[ISwDMTable::GetColumnType Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnType.md)
  
[ISwDMTable2::GetColumnWidth Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnWidth.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
