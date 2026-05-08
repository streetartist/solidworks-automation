# GetExternalFeatureReferences Method (ISwDMDocument15)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.html) on this topic. |
| GetExternalFeatureReferences Method (ISwDMDocument15) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15.md) : GetExternalFeatureReferences Method (ISwDMDocument15) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*ExtRefOption*
:   An [ISwDMExternalReferenceOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.md) object (see **Remarks)**

Obsolete. Superseded by [ISwDMDocument18::GetExternalFeatureReferences2.](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument18~GetExternalFeatureReferences2.md)

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetExternalFeatureReferences( _    ByRef ExtRefOption As SwDMExternalReferenceOption _ ) As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument15 Dim ExtRefOption As SwDMExternalReferenceOption Dim value As System.Integer   value = instance.GetExternalFeatureReferences(ExtRefOption) ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetExternalFeatureReferences(     out SwDMExternalReferenceOption ExtRefOption ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetExternalFeatureReferences(  &   [Out] SwDMExternalReferenceOption^ ExtRefOption ) ``` | |

#### Parameters

*ExtRefOption*
:   An [ISwDMExternalReferenceOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.md) object (see **Remarks)**

#### Return Value

Number of external references used in this document

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument15::GetExternalFeatureReferences](swdocumentmgr~SwDMDocument15~GetExternalFeatureReferences.md).

# Remarks

Use this method with parts and assemblies; use [ISwDMDocument13::GetAllExternalReferences4](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetAllExternalReferences4.md) with drawings.

This method only works in documents saved in SOLIDWORKS 2011 SP0 or later.

Before calling this method:

1. Call [ISwDMApplication3::GetExternalReferenceOptionObject](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication3~GetExternalReferenceOptionObject.md) to obtain an [ISwDMExternalReferenceOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.md) object.
2. Set [ISwDMExternalReferenceOption::Configuration](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~Configuration.md).
3. Set [ISwDMExternalReferenceOption::NeedSuppress](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~NeedSuppress.md).
4. Set [ISwDMExternalReferenceOption::SearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~SearchOption.md).
5. Assign this method's ExtRefOption parameter to the ISwDMExternalReferenceOption object.

After calling this method, call [ISwDMExternalReferenceOption::ExternalReferences](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~ExternalReferences.md) and [ISwDMExternalReferenceOption::ReferencedConfigurations](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~ReferencedConfigurations.md) to obtain the external feature references and their configurations.

To find out if an external feature reference is suppressed:

1. Call [ISwDMComponent6::PathName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6~PathName.md) to set one of the external components returned by ISwDMDocument15::GetExternalFeatureReferences.
2. Call [ISwDMComponent::IsSuppressed](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~IsSuppressed.md).

The suppression states and other information of all of the external references are also embedded in the parent document. To obtain this information in XML format, call [ISwDMDocument::GetXMLStream](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetXmlStream.md).

Call this method before calling [ISwDMDocument::ReplaceReference](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.md).

The SOLIDWORKS Document Manager API applies the same rules when searching for a reference as described in the SOLIDWORKS Help. The mix-and-match of sub-folder combinations is applied to the current document, which for the SOLIDWORKS Document Manager API is the document attached using [ISwDMApplication::GetDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetDocument.md) and the reference being searched for. You can set up the list of folders to be searched using [ISwDMSearchOption::AddSearchPath](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption~AddSearchPath.md), which is equivalent to using the SOLIDWORKS user-interface commands Tools > Options > System Options > File Locations > Referenced Documents.

Two differences between SOLIDWORKS and the SOLIDWORKS Document Manager API searches are:

- the path of the last opened visible top-level document (drawing or assembly) is not tried directly.
- the last user path is not tried directly.

These concepts have little meaning when SOLIDWORKS is not running.

Because the search routine is shared between SOLIDWORKS and the SOLIDWORKS Document Manager API, most of the same changes apply going from SOLIDWORKS 2006 to SOLIDWORKS 2007 and later. However, one significant change related to caching of resolved paths for references being searched for in SOLIDWORKS does not apply to the SOLIDWORKS Document Manager API. In SOLIDWORKS 2007 and later, the next time these references are needed, a simple lookup suffices instead of a potentially lengthy search. However, because this caching mechanism was not applied to the SOLIDWORKS Document Manager API, the SOLIDWORKS Document Manager API in 2006 and 2007, and later, exhibit similar behavior.

# See Also

#### 

[ISwDMDocument15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15.md)
  
[ISwDMDocument15 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15_members.md)

# Availability

SOLIDWORKS Document Manager API 2011 SP0
