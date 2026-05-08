# SetCustomProperty2 Method (ISwDMDocument29)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29~SetCustomProperty2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29~SetCustomProperty2.html) on this topic. |
| SetCustomProperty2 Method (ISwDMDocument29) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument29 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29.md) : SetCustomProperty2 Method (ISwDMDocument29) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Name of custom property

*newValue*
:   Value for custom property

Sets a custom property for this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function SetCustomProperty2( _    ByVal FieldName As System.String, _    ByVal newValue As System.String _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument29 Dim FieldName As System.String Dim newValue As System.String Dim value As System.Boolean   value = instance.SetCustomProperty2(FieldName, newValue) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool SetCustomProperty2(     System.string FieldName,    System.string newValue ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool SetCustomProperty2(  &   System.String^ FieldName, &   System.String^ newValue ) ``` | |

#### Parameters

*FieldName*
:   Name of custom property

*newValue*
:   Value for custom property

#### Return Value

True if custom property successfully set, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument29::SetCustomProperty2](swdocumentmgr~SwDMDocument29~SetCustomProperty2.md).

# Remarks

Before calling this method, call [ISwDMDocument::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.md) to populate FieldName.

If you call this method to set a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMDocument::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.md), [ISwDMDocument17::GetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.md), [ISwDMDocument3::GetAllCustomPropertyNamesAndValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.md), or [ISwDMDocument5::GetCustomPropertyValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.md). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

# See Also

#### 

[ISwDMDocument29 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29.md)
  
[ISwDMDocument29 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29_members.md)
  
[ISwDMDocument::AddCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.md)
  
[ISwDMDocument::DeleteCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.md)
  
[ISwDMDocument::GetCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.md)
  
[ISwDMConfiguration18::SetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.md)

# Availability

SOLIDWORKS Document Manager API 2023 FCS
