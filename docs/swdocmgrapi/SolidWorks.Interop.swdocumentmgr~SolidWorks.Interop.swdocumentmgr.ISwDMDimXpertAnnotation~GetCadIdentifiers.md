# GetCadIdentifiers Method (ISwDMDimXpertAnnotation)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~GetCadIdentifiers`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~GetCadIdentifiers.html) on this topic. |
| GetCadIdentifiers Method (ISwDMDimXpertAnnotation) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertAnnotation Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.md) : GetCadIdentifiers Method (ISwDMDimXpertAnnotation) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets all of the CAD identifiers of this DimXpert annotation.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCadIdentifiers() As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertAnnotation Dim value As System.Object   value = instance.GetCadIdentifiers() ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetCadIdentifiers() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetCadIdentifiers(); ``` | |

#### Return Value

Array of strings; the format of each string is bodyid:faceid

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertAnnotation::GetCadIdentifiers](swdocumentmgr~SwDMDimXpertAnnotation~GetCadIdentifiers.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertAnnotation Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.md)
  
[ISwDMDimXpertAnnotation Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation_members.md)
  
[ISwDMDimXpertAnnotation::IGetCadIdentifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~IGetCadIdentifiers.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
