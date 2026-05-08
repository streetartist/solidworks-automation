# GetCustomPropertyNames Method (ISwDMCutListItem)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyNames`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyNames.html) on this topic. |
| GetCustomPropertyNames Method (ISwDMCutListItem) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.md) : GetCustomPropertyNames Method (ISwDMCutListItem) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the names of custom property names for this cut-list item.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCustomPropertyNames() As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMCutListItem Dim value As System.Object   value = instance.GetCustomPropertyNames() ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetCustomPropertyNames() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetCustomPropertyNames(); ``` | |

#### Return Value

Array of custom property names

# Visual Basic for Applications (VBA) Syntax

See [SwDMCutListItem::GetCustomPropertyNames](swdocumentmgr~SwDMCutListItem~GetCustomPropertyNames.md).

# Example

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
  
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

# See Also

#### 

[ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.md)
  
[ISwDMCutListItem Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem_members.md)
  
[ISwDMCutListItem2::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~DeleteCustomProperty.md)
  
[ISwDMCutListItem2::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~SetCustomProperty.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
