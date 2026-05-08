# GetID Method (ISwDMConfiguration12)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetID`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetID.html) on this topic. |
| GetID Method (ISwDMConfiguration12) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.md) : GetID Method (ISwDMConfiguration12) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the ID of the configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetID() As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration12 Dim value As System.Integer   value = instance.GetID() ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetID() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetID(); ``` | |

#### Return Value

ID of the configuration

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration12::GetID](swdocumentmgr~SwDMConfiguration12~GetID.md).

# Example

[Get Linked Display States (C#)](Get_Linked_Display_States_Example_CSharp.htm)
  
[Get Linked Display States (VB.NET)](Get_Linked_Display_States_Example_VBNET.htm)

# Remarks

Each configuration is assigned a unique and persistent ID. This ID does not change if you change the name of the configuration.

# See Also

#### 

[ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.md)
  
[ISwDMConfiguration12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
