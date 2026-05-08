# IsCustomPropertyEditable Method (ISwDMDocument22)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22~IsCustomPropertyEditable`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22~IsCustomPropertyEditable.html) on this topic. |
| IsCustomPropertyEditable Method (ISwDMDocument22) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument22 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22.md) : IsCustomPropertyEditable Method (ISwDMDocument22) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Name of the custom property in this document

*IsEditable*
:   True if editable, false if not

Gets whether the specified custom property is editable.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub IsCustomPropertyEditable( _    ByVal FieldName As System.String, _    ByRef IsEditable As System.Boolean _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument22 Dim FieldName As System.String Dim IsEditable As System.Boolean   instance.IsCustomPropertyEditable(FieldName, IsEditable) ``` | |

| C# |  |
| --- | --- |
| ``` void IsCustomPropertyEditable(     System.string FieldName,    out System.bool IsEditable ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void IsCustomPropertyEditable(  &   System.String^ FieldName, &   [Out] System.bool IsEditable ) ``` | |

#### Parameters

*FieldName*
:   Name of the custom property in this document

*IsEditable*
:   True if editable, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument22::IsCustomPropertyEditable](swdocumentmgr~SwDMDocument22~IsCustomPropertyEditable.md).

# Example

See the [ISwDMDocument22](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22.md) examples.

# Remarks

To populate FieldName, use [ISwDMDocument::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.md) to get the names of all of the custom properties in this document.

# See Also

#### 

[ISwDMDocument22 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22.md)
  
[ISwDMDocument22 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22_members.md)

# Availability

SOLIDWORKS Document Manager API 2018 SP0
