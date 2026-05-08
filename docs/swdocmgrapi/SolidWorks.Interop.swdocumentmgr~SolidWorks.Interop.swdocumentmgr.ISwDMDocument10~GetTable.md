# GetTable Method (ISwDMDocument10)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetTable`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetTable.html) on this topic. |
| GetTable Method (ISwDMDocument10) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.md) : GetTable Method (ISwDMDocument10) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*NameIn*
:   Name of table

Gets the specified table.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetTable( _    ByVal NameIn As System.String _ ) As SwDMTable ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument10 Dim NameIn As System.String Dim value As SwDMTable   value = instance.GetTable(NameIn) ``` | |

| C# |  |
| --- | --- |
| ``` SwDMTable GetTable(     System.string NameIn ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMTable^ GetTable(  &   System.String^ NameIn ) ``` | |

#### Parameters

*NameIn*
:   Name of table

#### Return Value

[Table](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument10::GetTable](swdocumentmgr~SwDMDocument10~GetTable.md).

# Example

[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)
  
[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)

# Remarks

Only revision and bill of materials (BOM) tables are supported.

Before calling this method, call [ISwDMDocument10::GetTableNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetTableNames.md) to get the names of the tables in this document.

# See Also

#### 

[ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.md)
  
[ISwDMDocument10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10_members.md)
  
[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md)
  
[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
