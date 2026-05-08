# GetAllCustomPropertyNamesAndValues Method (ISwDMDocument3)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html) on this topic. |
| GetAllCustomPropertyNamesAndValues Method (ISwDMDocument3) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3.md) : GetAllCustomPropertyNamesAndValues Method (ISwDMDocument3) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*names*
:   Array of Property Names

*types*
:   Array of Types

*linkedTo*
:   Array of linked to Values/Text Expressions (see Remarks)

*values*
:   Array of Evaluated Values

Gets all of the custom properties for this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub GetAllCustomPropertyNamesAndValues( _    ByRef names As System.Object, _    ByRef types As System.Object, _    ByRef linkedTo As System.Object, _    ByRef values As System.Object _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument3 Dim names As System.Object Dim types As System.Object Dim linkedTo As System.Object Dim values As System.Object   instance.GetAllCustomPropertyNamesAndValues(names, types, linkedTo, values) ``` | |

| C# |  |
| --- | --- |
| ``` void GetAllCustomPropertyNamesAndValues(     out System.object names,    out System.object types,    out System.object linkedTo,    out System.object values ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void GetAllCustomPropertyNamesAndValues(  &   [Out] System.Object^ names, &   [Out] System.Object^ types, &   [Out] System.Object^ linkedTo, &   [Out] System.Object^ values ) ``` | |

#### Parameters

*names*
:   Array of Property Names

*types*
:   Array of Types

*linkedTo*
:   Array of linked to Values/Text Expressions (see Remarks)

*values*
:   Array of Evaluated Values

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument3::GetAllCustomPropertyNamesAndValues](swdocumentmgr~SwDMDocument3~GetAllCustomPropertyNamesAndValues.md).

# Remarks

|  |  |
| --- | --- |
| **If the properties are...** | **Then this method returns...** |
| Linked | The evaluated results of linkedTo |
| Not linked | Empty strings.  This method returns the same values as returned by [ISwDMDocument::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.md) |

This method returns evaluated values from when the document was last saved in SOLIDWORKS.

If you called [ISwDMDocument::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.md) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.

# See Also

#### 

[ISwDMDocument3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3.md)
  
[ISwDMDocument3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3_members.md)
  
[ISwDMDocument::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.md)
  
[ISwDMDocument::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.md)
  
[ISwDMDocument::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.md)
  
[ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.md)
  
[ISwDMDocument5::GetCustomPropertyValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.md)
  
[ISwDMDocument17::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.md)

# Availability

SOLIDWORKS Document Manager API 2004 SP4
