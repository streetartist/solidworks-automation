# GetISO2768PartType Method (ISwDMDimXpertBlockTolerances)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances~GetISO2768PartType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances~GetISO2768PartType.html) on this topic. |
| GetISO2768PartType Method (ISwDMDimXpertBlockTolerances) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertBlockTolerances Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances.md) : GetISO2768PartType Method (ISwDMDimXpertBlockTolerances) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*type*
:   Type of ISO 2768 block tolerance as defined in [swDmDimXpertISO2768PartType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertISO2768PartType_e.md)

Gets the ISO 2768 part type of this DimXpert block tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetISO2768PartType( _    ByRef type As swDmDimXpertISO2768PartType_e _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertBlockTolerances Dim type As swDmDimXpertISO2768PartType_e Dim value As System.Boolean   value = instance.GetISO2768PartType(type) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetISO2768PartType(     out swDmDimXpertISO2768PartType_e type ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetISO2768PartType(  &   [Out] swDmDimXpertISO2768PartType_e type ) ``` | |

#### Parameters

*type*
:   Type of ISO 2768 block tolerance as defined in [swDmDimXpertISO2768PartType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertISO2768PartType_e.md)

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertBlockTolerances::GetISO2768PartType](swdocumentmgr~SwDMDimXpertBlockTolerances~GetISO2768PartType.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertBlockTolerances Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances.md)
  
[ISwDMDimXpertBlockTolerances Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
