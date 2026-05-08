# GetLastUpdateTimeStamp Method (ISwDMDocument13)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetLastUpdateTimeStamp`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetLastUpdateTimeStamp.html) on this topic. |
| GetLastUpdateTimeStamp Method (ISwDMDocument13) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md) : GetLastUpdateTimeStamp Method (ISwDMDocument13) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the last update stamp for this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetLastUpdateTimeStamp() As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument13 Dim value As System.Integer   value = instance.GetLastUpdateTimeStamp() ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetLastUpdateTimeStamp() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetLastUpdateTimeStamp(); ``` | |

#### Return Value

Last update stamp in time\_t format

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument13::GetLastUpdateTimeStamp](swdocumentmgr~SwDMDocument13~GetLastUpdateTimeStamp.md).

# Example

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
  
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

# Remarks

The return value is in time\_t format, which Microsoft defines "as time as seconds elapsed since midnight, January 1, 1970 or -1 in the case of error". You must either have built-in functions to convert this value to something more accessible or write your own functions.

# See Also

#### 

[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md)
  
[ISwDMDocument13 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13_members.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
