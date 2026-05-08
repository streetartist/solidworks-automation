# DeleteCustomProperty Method (ISwDMCutListItem2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~DeleteCustomProperty`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~DeleteCustomProperty.html) on this topic. |
| DeleteCustomProperty Method (ISwDMCutListItem2) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.md) : DeleteCustomProperty Method (ISwDMCutListItem2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Custom property to delete from the cut-list item

Deletes the specified custom property from this cut-list item.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function DeleteCustomProperty( _    ByVal FieldName As System.String _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMCutListItem2 Dim FieldName As System.String Dim value As System.Boolean   value = instance.DeleteCustomProperty(FieldName) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool DeleteCustomProperty(     System.string FieldName ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool DeleteCustomProperty(  &   System.String^ FieldName ) ``` | |

#### Parameters

*FieldName*
:   Custom property to delete from the cut-list item

#### Return Value

True if the custom property is deleted, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMCutListItem2::DeleteCustomProperty](swdocumentmgr~SwDMCutListItem2~DeleteCustomProperty.md).

# Example

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
  
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

# Remarks

This method only supports model documents saved in SOLIDWORKS 2009 or later.

Before calling this method, call [ISwDMCutListItem::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyNames.md).

# See Also

#### 

[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.md)
  
[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.md)
  
[ISwDMCutListItem2::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~AddCustomProperty.md)
  
[ISwDMCutListItem2::GetCustomPropertyValue2 Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~GetCustomPropertyValue2.md)
  
[ISwDMCutListItem2::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~SetCustomProperty.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
