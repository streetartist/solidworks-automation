# AddCustomProperty Method (ISwDMCutListItem2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~AddCustomProperty`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~AddCustomProperty.html) on this topic. |
| AddCustomProperty Method (ISwDMCutListItem2) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.md) : AddCustomProperty Method (ISwDMCutListItem2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Property name

*FieldType*
:   Property type as defined by [swDMCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

*FieldValue*
:   Property link-to value or text expression

Adds a custom property to this cut-list item.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function AddCustomProperty( _    ByVal FieldName As System.String, _    ByVal FieldType As SwDmCustomInfoType, _    ByVal FieldValue As System.String _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMCutListItem2 Dim FieldName As System.String Dim FieldType As SwDmCustomInfoType Dim FieldValue As System.String Dim value As System.Boolean   value = instance.AddCustomProperty(FieldName, FieldType, FieldValue) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool AddCustomProperty(     System.string FieldName,    SwDmCustomInfoType FieldType,    System.string FieldValue ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool AddCustomProperty(  &   System.String^ FieldName, &   SwDmCustomInfoType FieldType, &   System.String^ FieldValue ) ``` | |

#### Parameters

*FieldName*
:   Property name

*FieldType*
:   Property type as defined by [swDMCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

*FieldValue*
:   Property link-to value or text expression

#### Return Value

True if the custom property is added to the cut-list item, false if not and false if the specified custom property name already exists

# Visual Basic for Applications (VBA) Syntax

See [SwDMCutListItem2::AddCustomProperty](swdocumentmgr~SwDMCutListItem2~AddCustomProperty.md).

# Example

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
  
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

# Remarks

This method only supports model documents saved in SOLIDWORKS 2009 or later.

If you call this method to add a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMCutListItem2::GetCustomPropertyValue2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~GetCustomPropertyValue2.md). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

# See Also

#### 

[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.md)
  
[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.md)
  
[ISwDMCutListItem2::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~DeleteCustomProperty.md)
  
[ISwDMCutListItem2::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~SetCustomProperty.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
