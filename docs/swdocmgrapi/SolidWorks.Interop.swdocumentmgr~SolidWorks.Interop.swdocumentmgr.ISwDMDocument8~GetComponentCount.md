# GetComponentCount Method (ISwDMDocument8)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetComponentCount`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetComponentCount.html) on this topic. |
| GetComponentCount Method (ISwDMDocument8) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8.md) : GetComponentCount Method (ISwDMDocument8) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the number of components in a SOLIDWORKS assembly document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetComponentCount() As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument8 Dim value As System.Integer   value = instance.GetComponentCount() ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetComponentCount() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetComponentCount(); ``` | |

#### Return Value

Number of components in an assembly document

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument8::GetComponentCount](swdocumentmgr~SwDMDocument8~GetComponentCount.md).

# Remarks

This method supports SOLIDWORKS assembly documents only. A -1 is returned for all other types of SOLIDWORKS documents.

# See Also

#### 

[ISwDMDocument8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8.md)
  
[ISwDMDocument8 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8_members.md)

# Availability

SOLIDWORKS Document Manager API 2007 FCS
