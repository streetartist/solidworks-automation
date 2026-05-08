# GetCustomPropertyValue Method (ISwDMCutListItem)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyValue`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyValue.html) on this topic. |
| GetCustomPropertyValue Method (ISwDMCutListItem) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.md) : GetCustomPropertyValue Method (ISwDMCutListItem) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*

*type*

*linkedTo*

Obsolete. Superseded by [ISwDMCutListItem2::GetCustomPropertyValue2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyValue.md).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCustomPropertyValue( _    ByVal FieldName As System.String, _    ByRef type As SwDmCustomInfoType, _    ByRef linkedTo As System.String _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMCutListItem Dim FieldName As System.String Dim type As SwDmCustomInfoType Dim linkedTo As System.String Dim value As System.String   value = instance.GetCustomPropertyValue(FieldName, type, linkedTo) ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetCustomPropertyValue(     System.string FieldName,    out SwDmCustomInfoType type,    out System.string linkedTo ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetCustomPropertyValue(  &   System.String^ FieldName, &   [Out] SwDmCustomInfoType type, &   [Out] System.String^ linkedTo ) ``` | |

#### Parameters

*FieldName*

*type*

*linkedTo*

# Visual Basic for Applications (VBA) Syntax

See [SwDMCutListItem::GetCustomPropertyValue](swdocumentmgr~SwDMCutListItem~GetCustomPropertyValue.md).

 

# See Also

#### 

[ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.md)
  
[ISwDMCutListItem Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem_members.md)
