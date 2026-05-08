# GetTableNames Method (ISwDMDocument10)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetTableNames`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetTableNames.html) on this topic. |
| GetTableNames Method (ISwDMDocument10) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.md) : GetTableNames Method (ISwDMDocument10) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*TableType*
:   Type of table as defined by [swDMTableType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableType.md)

Gets the names of the tables in this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetTableNames( _    ByVal TableType As SwDmTableType _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument10 Dim TableType As SwDmTableType Dim value As System.Object   value = instance.GetTableNames(TableType) ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetTableNames(     SwDmTableType TableType ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetTableNames(  &   SwDmTableType TableType ) ``` | |

#### Parameters

*TableType*
:   Type of table as defined by [swDMTableType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableType.md)

#### Return Value

Array of table names

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument10::GetTableNames](swdocumentmgr~SwDMDocument10~GetTableNames.md).

# Example

[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)
  
[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)

# See Also

#### 

[ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.md)
  
[ISwDMDocument10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10_members.md)
  
[ISwDMDocument10::GetTable Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetTable.md)
  
[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md)
  
[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
