# GetChangedReferences Method (ISwDMDocument8)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.html) on this topic. |
| GetChangedReferences Method (ISwDMDocument8) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8.md) : GetChangedReferences Method (ISwDMDocument8) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*originalreferences*
:   Array of the names of the original references

*newreferences*
:   Array of the names of the corresponding references

Gets a list of the names of the original references and their corresponding new references if the references were changed using the SOLIDWORKS Document Manager API or SOLIDWORKS Explorer.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub GetChangedReferences( _    ByRef originalreferences As System.Object, _    ByRef newreferences As System.Object _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument8 Dim originalreferences As System.Object Dim newreferences As System.Object   instance.GetChangedReferences(originalreferences, newreferences) ``` | |

| C# |  |
| --- | --- |
| ``` void GetChangedReferences(     out System.object originalreferences,    out System.object newreferences ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void GetChangedReferences(  &   [Out] System.Object^ originalreferences, &   [Out] System.Object^ newreferences ) ``` | |

#### Parameters

*originalreferences*
:   Array of the names of the original references

*newreferences*
:   Array of the names of the corresponding references

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument8::GetChangedReferences](swdocumentmgr~SwDMDocument8~GetChangedReferences.md).

 

# See Also

#### 

[ISwDMDocument8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8.md)
  
[ISwDMDocument8 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8_members.md)
  
[ISwDMDocument::ReplaceReference Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.md)
  
[ISwDMDocument5::GetAllExternalReferences2 Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetAllExternalReferences2.md)
  
[ISwDMConfiguration11::GetReplacedComponents Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~GetReplacedComponents.md)
  
**ISwDMDocument30::ClearChangedReferences Method ()**

# Availability

SOLIDWORKS Document Manager API 2007 FCS
