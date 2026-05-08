# GetLinkedDisplayStates Method (ISwDMConfiguration12)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetLinkedDisplayStates`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetLinkedDisplayStates.html) on this topic. |
| GetLinkedDisplayStates Method (ISwDMConfiguration12) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.md) : GetLinkedDisplayStates Method (ISwDMConfiguration12) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*DisplayStateNameList*
:   Array of strings containing the linked display state names

Gets the names and number of linked display states.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetLinkedDisplayStates( _    ByRef DisplayStateNameList As System.Object _ ) As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration12 Dim DisplayStateNameList As System.Object Dim value As System.Integer   value = instance.GetLinkedDisplayStates(DisplayStateNameList) ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetLinkedDisplayStates(     out System.object DisplayStateNameList ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetLinkedDisplayStates(  &   [Out] System.Object^ DisplayStateNameList ) ``` | |

#### Parameters

*DisplayStateNameList*
:   Array of strings containing the linked display state names

#### Return Value

Number of linked display states

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration12::GetLinkedDisplayStates](swdocumentmgr~SwDMConfiguration12~GetLinkedDisplayStates.md).

# Example

[Get Linked Display States (VB.NET)](Get_Linked_Display_States_Example_VBNET.htm)
  
[Get Linked Display States (C#)](Get_Linked_Display_States_Example_CSharp.htm)

# See Also

#### 

[ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.md)
  
[ISwDMConfiguration12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12_members.md)
  
[ISwDMConfiguration12::GetComponentVisibleByDisplayStateName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetComponentVisibleByDisplayStateName.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
