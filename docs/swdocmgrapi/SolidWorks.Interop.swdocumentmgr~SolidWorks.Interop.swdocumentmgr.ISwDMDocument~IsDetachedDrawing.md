# IsDetachedDrawing Method (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~IsDetachedDrawing`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~IsDetachedDrawing.html) on this topic. |
| IsDetachedDrawing Method (ISwDMDocument) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : IsDetachedDrawing Method (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets whether this file is a detached drawing.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function IsDetachedDrawing() As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim value As System.Boolean   value = instance.IsDetachedDrawing() ``` | |

| C# |  |
| --- | --- |
| ``` System.bool IsDetachedDrawing() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool IsDetachedDrawing(); ``` | |

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::IsDetachedDrawing](swdocumentmgr~SwDMDocument~IsDetachedDrawing.md).

# Example

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
  
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

# Remarks

True if the file is detached drawing, false if not

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
