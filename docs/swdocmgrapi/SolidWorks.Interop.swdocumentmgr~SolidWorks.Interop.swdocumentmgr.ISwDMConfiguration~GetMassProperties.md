# GetMassProperties Method (ISwDMConfiguration)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetMassProperties`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetMassProperties.html) on this topic. |
| GetMassProperties Method (ISwDMConfiguration) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md) : GetMassProperties Method (ISwDMConfiguration) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*bRet*
:   Success or error code as defined by [SwDmMassPropError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmMassPropError.md)

Gets the mass properties, if valid, for this configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetMassProperties( _    ByRef bRet As SwDmMassPropError _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration Dim bRet As SwDmMassPropError Dim value As System.Object   value = instance.GetMassProperties(bRet) ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetMassProperties(     out SwDmMassPropError bRet ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetMassProperties(  &   [Out] SwDmMassPropError bRet ) ``` | |

#### Parameters

*bRet*
:   Success or error code as defined by [SwDmMassPropError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmMassPropError.md)

#### Return Value

Array of mass properties (see Remarks)

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration::GetMassProperties](swdocumentmgr~SwDMConfiguration~GetMassProperties.md).

# Remarks

This method only returns data for documents created using SOLIDWORKS 2004 (Version 2500) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md).

The 13 elements in the array are:

|  |  |
| --- | --- |
| **Element** | **Description** |
| [0 2]: | (x, y, z) Center of mass (m) |
| [3]: | Volume (m^3) |
| [4]: | Surface area (m^2) |
| [5] : | Mass (kg) |
| [6]: | momXX (kg\*m^2) |
| [7] : | momYY (kg\*m^2) |
| [8] : | momZZ (kg\*m^2) |
| [9] : | momXY (kg\*m^2) |
| [10]: | momZX (kg\*m^2) |
| [11]: | momYZ (kg\*m^2) |
| [12]: | Include hidden |

# See Also

#### 

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md)
  
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
