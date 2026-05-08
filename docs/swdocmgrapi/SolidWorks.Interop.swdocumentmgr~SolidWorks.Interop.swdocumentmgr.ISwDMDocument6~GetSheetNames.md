# GetSheetNames Method (ISwDMDocument6)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.html) on this topic. |
| GetSheetNames Method (ISwDMDocument6) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6.md) : GetSheetNames Method (ISwDMDocument6) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the names of the sheets in the drawing document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetSheetNames() As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument6 Dim value As System.Object   value = instance.GetSheetNames() ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetSheetNames() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetSheetNames(); ``` | |

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument6::GetSheetNames](swdocumentmgr~SwDMDocument6~GetSheetNames.md).

# Example

[Get Drawing Sheets' Properties (C#)](Get_Drawing_Sheets_Properties_Example_CSharp.htm)
  
[Get Drawing Sheets' Properties (VB.NET)](Get_Drawing_Sheets_Properties_Example_vbnet.htm)

# Remarks

This method only supports drawing documents saved in SOLIDWORKS 2005 SP02 and later. An empty array is returned if the names of the sheets are not found.

# See Also

#### 

[ISwDMDocument6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6.md)
  
[ISwDMDocument6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6_members.md)
  
[ISwDMDocument4::GetActiveSheetName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.md)
  
[ISwDMDocument4::GetSheetCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetSheetCount.md)
  
[ISwDMDocument13::GetSheetFormatPath Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.md)

# Availability

SOLIDWORKS Document Manager API 2005 SP2
