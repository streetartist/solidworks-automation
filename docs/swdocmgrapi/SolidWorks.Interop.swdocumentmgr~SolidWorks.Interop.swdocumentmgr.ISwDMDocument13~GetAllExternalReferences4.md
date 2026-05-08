# GetAllExternalReferences4 Method (ISwDMDocument13)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetAllExternalReferences4`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetAllExternalReferences4.html) on this topic. |
| GetAllExternalReferences4 Method (ISwDMDocument13) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md) : GetAllExternalReferences4 Method (ISwDMDocument13) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*pSrcOption*
:   Pointer to the [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) object

*brokenRefVar*
:   Array of the statuses of any broken external references as defined in [swDmReferenceStatus](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmReferenceStatus.md) (see Remarks)

*IsVirtual*
:   Array of Booleans that indicate whether each reference corresponds to a virtual component

*TimeStamp*
:   Array of time stamps in time\_t format

Obsolete. Superseded by [ISwDMDocument13::GetAllExternalReferences5](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument21~GetAllExternalReferences5.md).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetAllExternalReferences4( _    ByVal pSrcOption As SwDMSearchOption, _    ByRef brokenRefVar As System.Object, _    ByRef IsVirtual As System.Object, _    ByRef TimeStamp As System.Object _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument13 Dim pSrcOption As SwDMSearchOption Dim brokenRefVar As System.Object Dim IsVirtual As System.Object Dim TimeStamp As System.Object Dim value As System.Object   value = instance.GetAllExternalReferences4(pSrcOption, brokenRefVar, IsVirtual, TimeStamp) ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetAllExternalReferences4(     SwDMSearchOption pSrcOption,    out System.object brokenRefVar,    out System.object IsVirtual,    out System.object TimeStamp ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetAllExternalReferences4(  &   SwDMSearchOption^ pSrcOption, &   [Out] System.Object^ brokenRefVar, &   [Out] System.Object^ IsVirtual, &   [Out] System.Object^ TimeStamp ) ``` | |

#### Parameters

*pSrcOption*
:   Pointer to the [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) object

*brokenRefVar*
:   Array of the statuses of any broken external references as defined in [swDmReferenceStatus](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmReferenceStatus.md) (see Remarks)

*IsVirtual*
:   Array of Booleans that indicate whether each reference corresponds to a virtual component

*TimeStamp*
:   Array of time stamps in time\_t format

#### Return Value

Array of the names of the external references used in this document

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument13::GetAllExternalReferences4](swdocumentmgr~SwDMDocument13~GetAllExternalReferences4.md).

# Remarks

Use this method for drawings; use [ISwDMDocument15::GetExternalFeatureReferences](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.md) for parts and assemblies.

This method only supports model documents saved in SOLIDWORKS 2009 and later.

Although this method returns valid data for files created in SOLIDWORKS 2005 and earlier, this method only returns valid data for the brokenRefVar argument for files created in SOLIDWORKS 2005 files and later. For files created in versions of SOLIDWORKS earlier than SOLIDWORKS 2005, it returns swDmReferenceStatusUnknown for brokenRefVar.

Call this method before calling [ISwDMDocument::ReplaceReference](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.md).

The SOLIDWORKS Document Manager API applies the same rules when searching for a reference as described in the SOLIDWORKS Help. The mix-and-match of sub-folder combinations is applied to the current document, which for the SOLIDWORKS Document Manager is the document attached using [ISwDMApplication::GetDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetDocument.md) and the reference being searched for. You can set up the list of folders to be searched using [ISwDMSearchOption::AddSearchPath](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption~AddSearchPath.md), which is equivalent to using the SOLIDWORKS user-interface commands Tools, Options > System Options > File Locations > Referenced Documents.

Two differences between SOLIDWORKS and the SOLIDWORKS Document Manager API searches are:

- the path of the last opened visible top-level document (drawing or assembly) is not tried directly.
- the last user path is not tried directly.

as these concepts have little meaning when SOLIDWORKS is not running.

SOLIDWORKS does not open suppressed components of assemblies in memory. Thus, information, such as a suppressed component's time stamp, is not updated when the assembly is rebuilt. You can call [ISwDMComponent6::PathName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6~PathName.md) to compare the path returned by ISwDMDocument13::GetAllExternalReferences4 and call [ISwDMComponent::IsSuppressed](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~IsSuppressed.md) to find out if the component is suppressed.

Because the search routine is shared between SOLIDWORKS and the SOLIDWORKS Document Manager API, most of the same changes apply going from SOLIDWORKS 2006 to SOLIDWORKS 2007 and later. However, one significant change related to caching of resolved paths for references being searched for in SOLIDWORKS does not apply to the SOLIDWORKS Document Manager API. In SOLIDWORKS 2007 and later, the next time these references are needed, a simple lookup suffices instead of a potentially lengthy search. However, because this caching mechanism was not applied to the SOLIDWORKS Document Manager API, the SOLIDWORKS Document Manager API in 2006 and 2007, and later, exhibit similar behavior.

The array of time stamps are in time\_t format, which Microsoft defines "as time as seconds elapsed since midnight, January 1, 1970 or -1 in the case of error". You must either have built-in functions to convert these values to something more accessible or write your own functions.

# See Also

#### 

[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md)
  
[ISwDMDocument13 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13_members.md)
  
[ISwDMDocument13::GetLastUpdateTimeStamp Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetLastUpdateTimeStamp.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
