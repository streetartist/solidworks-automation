# GetPreviewBitmapBytes Method (ISwDMDocument11)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11~GetPreviewBitmapBytes`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11~GetPreviewBitmapBytes.html) on this topic. |
| GetPreviewBitmapBytes Method (ISwDMDocument11) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11.md) : GetPreviewBitmapBytes Method (ISwDMDocument11) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*result*
:   Success or error code as defined by [swDmPreviewError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmPreviewError.md)

Obsolete. Superseded by [ISwDMConfiguration9::GetPreviewBitmapBytes](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewBitmapBytes.md).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPreviewBitmapBytes( _    ByRef result As SwDmPreviewError _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument11 Dim result As SwDmPreviewError Dim value As System.Object   value = instance.GetPreviewBitmapBytes(result) ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetPreviewBitmapBytes(     out SwDmPreviewError result ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetPreviewBitmapBytes(  &   [Out] SwDmPreviewError result ) ``` | |

#### Parameters

*result*
:   Success or error code as defined by [swDmPreviewError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmPreviewError.md)

#### Return Value

Preview byte array

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument11::GetPreviewBitmapBytes](swdocumentmgr~SwDMDocument11~GetPreviewBitmapBytes.md).

 

# See Also

#### 

[ISwDMDocument11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11.md)
  
[ISwDMDocument11 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11_members.md)

# Availability

SOLIDWORKS Document Manager API 2007 SP5
