# GetThread Method (ISwDMDimXpertCylinderFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature~GetThread`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature~GetThread.html) on this topic. |
| GetThread Method (ISwDMDimXpertCylinderFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.md) : GetThread Method (ISwDMDimXpertCylinderFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*IsThreaded*
:   True if the cylinder is threaded; false otherwise

*ThreadDesignation*
:   Description of the thread

*ThreadDepth*
:   Depth of the thread for a threaded cylindrical hole

Gets thread information for this DimXpert cylinder.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetThread( _    ByRef IsThreaded As System.Boolean, _    ByRef ThreadDesignation As System.String, _    ByRef ThreadDepth As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCylinderFeature Dim IsThreaded As System.Boolean Dim ThreadDesignation As System.String Dim ThreadDepth As System.Double Dim value As System.Boolean   value = instance.GetThread(IsThreaded, ThreadDesignation, ThreadDepth) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetThread(     out System.bool IsThreaded,    out System.string ThreadDesignation,    out System.double ThreadDepth ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetThread(  &   [Out] System.bool IsThreaded, &   [Out] System.String^ ThreadDesignation, &   [Out] System.double ThreadDepth ) ``` | |

#### Parameters

*IsThreaded*
:   True if the cylinder is threaded; false otherwise

*ThreadDesignation*
:   Description of the thread

*ThreadDepth*
:   Depth of the thread for a threaded cylindrical hole

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCylinderFeature::GetThread](swdocumentmgr~SwDMDimXpertCylinderFeature~GetThread.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.md)
  
[ISwDMDimXpertCylinderFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
