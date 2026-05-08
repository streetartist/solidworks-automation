# GetSheetProperties Method (ISwDMDocument13)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetProperties`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetProperties.html) on this topic. |
| GetSheetProperties Method (ISwDMDocument13) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md) : GetSheetProperties Method (ISwDMDocument13) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*SheetName*
:   Sheet name

*Properties*
:   Array of 8 doubles (see **Remarks**)

Gets the specified sheet's properties.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetSheetProperties( _    ByVal SheetName As System.String, _    ByRef Properties As System.Object _ ) As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument13 Dim SheetName As System.String Dim Properties As System.Object Dim value As System.Integer   value = instance.GetSheetProperties(SheetName, Properties) ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetSheetProperties(     System.string SheetName,    out System.object Properties ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetSheetProperties(  &   System.String^ SheetName, &   [Out] System.Object^ Properties ) ``` | |

#### Parameters

*SheetName*
:   Sheet name

*Properties*
:   Array of 8 doubles (see **Remarks**)

#### Return Value

Result as defined in [swsSheetPropertiesResult](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swSheetPropertiesResult.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument13::GetSheetProperties](swdocumentmgr~SwDMDocument13~GetSheetProperties.md).

# Example

[Get Drawing Sheets' Properties (C#)](Get_Drawing_Sheets_Properties_Example_CSharp.htm)
  
[Get Drawing Sheets' Properties (VB.NET)](Get_Drawing_Sheets_Properties_Example_vbnet.htm)

# Remarks

Before calling this method, call [ISwDMDocument4::GetActiveSheetName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.md) or [ISwDMDocument6::GetSheetNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.md).

The return value is an array of 8 doubles:

**[***sheetPaperSize, sheetWidth, sheetHeight, sheetScale1, sheetScale2, firstAngle, templateSize, templateVisible***]**

where:

1. *sheetPaperSize*: long packed into a double represented by [swDwgPaperSizes\_e](SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.md)
2. *sheetWidth*: sheet width
3. *sheetHeight*: sheet height
4. *sheetScale1*: sheet scale1
5. *sheetScale2*: sheet scale2
6. *firstAngle*: Boolean packed into a double; true if sheet is using first angle project, false if not
7. *templateSize*: long packed into a double represented by [swDwgTemplates\_e](SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.md)
8. *templateVisible*: Boolean packed into a double; true if template is visible, false if not

# See Also

#### 

[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md)
  
[ISwDMDocument13 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13_members.md)
  
[ISwDMDocument13::GetSheetFormatPath](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
