# GetExternalDesignTable Method (ISwDMDocument13)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetExternalDesignTable`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetExternalDesignTable.html) on this topic. |
| GetExternalDesignTable Method (ISwDMDocument13) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md) : GetExternalDesignTable Method (ISwDMDocument13) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*pSrcOption*
:   Pointer to an [ISwDMSerachOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) object

*Status*
:   Error status as defined by [SwDmDesignTableDataError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDesignTableDataError.md)

Gets the path to an external (i.e., linked) design table, if one exists.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetExternalDesignTable( _    ByVal pSrcOption As SwDMSearchOption, _    ByRef Status As SwDmDesignTableDataError _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument13 Dim pSrcOption As SwDMSearchOption Dim Status As SwDmDesignTableDataError Dim value As System.String   value = instance.GetExternalDesignTable(pSrcOption, Status) ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetExternalDesignTable(     SwDMSearchOption pSrcOption,    out SwDmDesignTableDataError Status ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetExternalDesignTable(  &   SwDMSearchOption^ pSrcOption, &   [Out] SwDmDesignTableDataError Status ) ``` | |

#### Parameters

*pSrcOption*
:   Pointer to an [ISwDMSerachOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) object

*Status*
:   Error status as defined by [SwDmDesignTableDataError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDesignTableDataError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument13::GetExternalDesignTable](swdocumentmgr~SwDMDocument13~GetExternalDesignTable.md).

 

# See Also

#### 

[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.md)
  
[ISwDMDocument13 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13_members.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
