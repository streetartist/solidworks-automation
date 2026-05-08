# GetComponentVisibleByDisplayStateName Method (ISwDMConfiguration12)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetComponentVisibleByDisplayStateName`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetComponentVisibleByDisplayStateName.html) on this topic. |
| GetComponentVisibleByDisplayStateName Method (ISwDMConfiguration12) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.md) : GetComponentVisibleByDisplayStateName Method (ISwDMConfiguration12) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*DisplayStateName*
:   Display state name

*ComponentVisibleList*
:   Array of booleans indicating whether the components in *ComponentFileDirectory* are visible in the given display state; true if visble, false if suppressed

*ComponentFileDirectory*
:   Array of paths and file names of the components in the given display state

Gets the visibility states and path and file names of the components in the given display state.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub GetComponentVisibleByDisplayStateName( _    ByVal DisplayStateName As System.String, _    ByRef ComponentVisibleList As System.Object, _    ByRef ComponentFileDirectory As System.Object _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration12 Dim DisplayStateName As System.String Dim ComponentVisibleList As System.Object Dim ComponentFileDirectory As System.Object   instance.GetComponentVisibleByDisplayStateName(DisplayStateName, ComponentVisibleList, ComponentFileDirectory) ``` | |

| C# |  |
| --- | --- |
| ``` void GetComponentVisibleByDisplayStateName(     System.string DisplayStateName,    out System.object ComponentVisibleList,    out System.object ComponentFileDirectory ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void GetComponentVisibleByDisplayStateName(  &   System.String^ DisplayStateName, &   [Out] System.Object^ ComponentVisibleList, &   [Out] System.Object^ ComponentFileDirectory ) ``` | |

#### Parameters

*DisplayStateName*
:   Display state name

*ComponentVisibleList*
:   Array of booleans indicating whether the components in *ComponentFileDirectory* are visible in the given display state; true if visble, false if suppressed

*ComponentFileDirectory*
:   Array of paths and file names of the components in the given display state

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration12::GetComponentVisibleByDisplayStateName](swdocumentmgr~SwDMConfiguration12~GetComponentVisibleByDisplayStateName.md).

# Example

[Get Linked Display States (VB.NET)](Get_Linked_Display_States_Example_VBNET.htm)
  
[Get Linked Display States (C#)](Get_Linked_Display_States_Example_CSharp.htm)

# See Also

#### 

[ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.md)
  
[ISwDMConfiguration12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12_members.md)
  
[ISwDMConfiguration12::GetLinkedDisplayStates Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetLinkedDisplayStates.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
