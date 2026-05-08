# GetCustomPropertyValues Method (ISwDMConfiguration5)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.html) on this topic. |
| GetCustomPropertyValues Method (ISwDMConfiguration5) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5.md) : GetCustomPropertyValues Method (ISwDMConfiguration5) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Property Name

*type*
:   Type of custom property as defined in [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

*linkedTo*
:   Linked to Value/Text Expression (see Remarks)

Gets the specified custom property value for this configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCustomPropertyValues( _    ByVal FieldName As System.String, _    ByRef type As SwDmCustomInfoType, _    ByRef linkedTo As System.String _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration5 Dim FieldName As System.String Dim type As SwDmCustomInfoType Dim linkedTo As System.String Dim value As System.String   value = instance.GetCustomPropertyValues(FieldName, type, linkedTo) ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetCustomPropertyValues(     System.string FieldName,    out SwDmCustomInfoType type,    out System.string linkedTo ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetCustomPropertyValues(  &   System.String^ FieldName, &   [Out] SwDmCustomInfoType type, &   [Out] System.String^ linkedTo ) ``` | |

#### Parameters

*FieldName*
:   Property Name

*type*
:   Type of custom property as defined in [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

*linkedTo*
:   Linked to Value/Text Expression (see Remarks)

#### Return Value

See **Remarks**

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration5::GetCustomPropertyValues](swdocumentmgr~SwDMConfiguration5~GetCustomPropertyValues.md).

# Remarks

|  |  |
| --- | --- |
| **If the property is...** | **Then this method returns...** |
| Linked | The evaluated result of linkedTo |
| Not linked | An empty string.  This method returns the same value as returned by [ISwDMConfiguration::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.md) |

This property only supports documents saved in SOLIDWORKS 2005 and later. To get the version of a document, use [ISwDMDocument::GetVersion](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md).

If you called [ISwDMConfiguration::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.md) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.

# See Also

#### 

[ISwDMConfiguration5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5.md)
  
[ISwDMConfiguration5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5_members.md)

# Availability

SOLIDWORKS Document Manager API 2005 FCS
