# NeedSuppress Property (ISwDMExternalReferenceOption)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~NeedSuppress`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~NeedSuppress.html) on this topic. |
| NeedSuppress Property (ISwDMExternalReferenceOption) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMExternalReferenceOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.md) : NeedSuppress Property (ISwDMExternalReferenceOption) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets and sets whether to retrieve information about suppressed external references in the document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property NeedSuppress As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMExternalReferenceOption Dim value As System.Boolean   instance.NeedSuppress = value   value = instance.NeedSuppress ``` | |

| C# |  |
| --- | --- |
| ``` System.bool NeedSuppress {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.bool NeedSuppress {    System.bool get();    void set ( &   System.bool value); } ``` | |

#### Property Value

True to retrieve suppressed references, false to not

# Visual Basic for Applications (VBA) Syntax

See [SwDMExternalReferenceOption::NeedSuppress](swdocumentmgr~SwDMExternalReferenceOption~NeedSuppress.md).

# Example

[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
  
[Get External References (C#)](Get_External_References_Example_CSharp.htm)
  
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
  
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
  
[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
  
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

# Remarks

To find out if a reference is suppressed:

1. Call [ISwDMComponent6::PathName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6~PathName.md) to set the component returned by [ISwDMDocument15::GetExternalFeatureReferences](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.md).
2. Call [ISwDMComponent::IsSuppressed](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~IsSuppressed.md).

The suppression states of all of the external references are also stored in the parent document. To obtain this information in XML format, call [ISwDMDocument::GetXMLStream](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetXmlStream.md).

# See Also

#### 

[ISwDMExternalReferenceOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.md)
  
[ISwDMExternalReferenceOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption_members.md)

# Availability

SOLIDWORKS Document Manager API 2011 SP0
