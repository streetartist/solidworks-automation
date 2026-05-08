# GetCustomPropertyValue2 Method (ISwDMCutListItem2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~GetCustomPropertyValue2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~GetCustomPropertyValue2.html) on this topic. |
| GetCustomPropertyValue2 Method (ISwDMCutListItem2) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.md) : GetCustomPropertyValue2 Method (ISwDMCutListItem2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Custom property name (see **Remarks**)

*type*
:   Property type as defined by [swDMCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

*linkedTo*
:   Link-to value or text expresssion

Gets the evaluated value of this custom property for this cut-list item.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCustomPropertyValue2( _    ByVal FieldName As System.String, _    ByRef type As SwDmCustomInfoType, _    ByRef linkedTo As System.String _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMCutListItem2 Dim FieldName As System.String Dim type As SwDmCustomInfoType Dim linkedTo As System.String Dim value As System.String   value = instance.GetCustomPropertyValue2(FieldName, type, linkedTo) ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetCustomPropertyValue2(     System.string FieldName,    out SwDmCustomInfoType type,    out System.string linkedTo ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetCustomPropertyValue2(  &   System.String^ FieldName, &   [Out] SwDmCustomInfoType type, &   [Out] System.String^ linkedTo ) ``` | |

#### Parameters

*FieldName*
:   Custom property name (see **Remarks**)

*type*
:   Property type as defined by [swDMCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

*linkedTo*
:   Link-to value or text expresssion

#### Return Value

Evaluated value

# Visual Basic for Applications (VBA) Syntax

See [SwDMCutListItem2::GetCustomPropertyValue2](swdocumentmgr~SwDMCutListItem2~GetCustomPropertyValue2.md).

# Example

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
  
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

# Remarks

This method only supports model documents saved in SOLIDWORKS 2009 or later.

To populate FieldName, use [ISwDMCutListItem::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyNames.md) to get the names of all of the custom properties.

If you called [ISwDMCutListItem2::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~SetCustomProperty.md) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.

# See Also

#### 

[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.md)
  
[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.md)
  
[ISwDMCutListItem2::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~AddCustomProperty.md)
  
[ISwDMCutListItem2::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~DeleteCustomProperty.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
