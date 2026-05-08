# GetSheetFormatPath Method (ISwDMDocument13)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.html) on this topic. |
| GetSheetFormatPath Method (ISwDMDocument13) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md) : GetSheetFormatPath Method (ISwDMDocument13) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*SheetName*
:   Sheet name

*FormatPath*
:   Path and filename of the sheet format

Gets the path and filename of the sheet format used for the specified sheet.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetSheetFormatPath( _    ByVal SheetName As System.String, _    ByRef FormatPath As System.String _ ) As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument13 Dim SheetName As System.String Dim FormatPath As System.String Dim value As System.Integer   value = instance.GetSheetFormatPath(SheetName, FormatPath) ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetSheetFormatPath(     System.string SheetName,    out System.string FormatPath ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetSheetFormatPath(  &   System.String^ SheetName, &   [Out] System.String^ FormatPath ) ``` | |

#### Parameters

*SheetName*
:   Sheet name

*FormatPath*
:   Path and filename of the sheet format

#### Return Value

Result as defined in [swSheetFormatPathResult](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swSheetFormatPathResult.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument13::GetSheetFormatPath](swdocumentmgr~SwDMDocument13~GetSheetFormatPath.md).

# Example

[Get Drawing Sheets' Properties (C#)](Get_Drawing_Sheets_Properties_Example_CSharp.htm)
  
[Get Drawing Sheets' Properties (VB.NET)](Get_Drawing_Sheets_Properties_Example_vbnet.htm)

# Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later. An empty string is returned for documents saved in earlier versions of SOLIDWORKS.

Before calling this method, call [ISwDMDocument4::GetActiveSheetName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.md) or [ISwDMDocument6::GetSheetNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.md).

# See Also

#### 

[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md)
  
[ISwDMDocument13 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13_members.md)
  
[ISwDMDocument13::GetSheetProperties Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetProperties.md)

# Availability

SOLIDWORKS Document Manager 2009 SP0
