# GetInvisibleCustomProperty Method (ISwDMSheet)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomProperty`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomProperty.html) on this topic. |
| GetInvisibleCustomProperty Method (ISwDMSheet) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMSheet Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.md) : GetInvisibleCustomProperty Method (ISwDMSheet) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Name of the custom property

*type*
:   Type of custom property as defined by [swDMCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

Gets the sheet's specified invisible sheet custom property.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetInvisibleCustomProperty( _    ByVal FieldName As System.String, _    ByRef type As SwDmCustomInfoType _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMSheet Dim FieldName As System.String Dim type As SwDmCustomInfoType Dim value As System.String   value = instance.GetInvisibleCustomProperty(FieldName, type) ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetInvisibleCustomProperty(     System.string FieldName,    out SwDmCustomInfoType type ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetInvisibleCustomProperty(  &   System.String^ FieldName, &   [Out] SwDmCustomInfoType type ) ``` | |

#### Parameters

*FieldName*
:   Name of the custom property

*type*
:   Type of custom property as defined by [swDMCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

#### Return Value

Value of the custom property

# Visual Basic for Applications (VBA) Syntax

See [SwDMSheet::GetInvisibleCustomProperty](swdocumentmgr~SwDMSheet~GetInvisibleCustomProperty.md).

# Remarks

Before calling this method, call [ISwDMSheet::GetInvisibleCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomPropertyNames.md).

# See Also

#### 

[ISwDMSheet Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.md)
  
[ISwDMSheet Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet_members.md)
  
[ISwDMSheet::GetInvisibleCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomPropertyCount.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
