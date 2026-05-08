# SaveAs Method (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SaveAs`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SaveAs.html) on this topic. |
| SaveAs Method (ISwDMDocument) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : SaveAs Method (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*saveName*
:   Filename to which to save the document

Saves the document as the specified filename.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function SaveAs( _    ByVal saveName As System.String _ ) As SwDmDocumentSaveError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim saveName As System.String Dim value As SwDmDocumentSaveError   value = instance.SaveAs(saveName) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmDocumentSaveError SaveAs(     System.string saveName ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmDocumentSaveError SaveAs(  &   System.String^ saveName ) ``` | |

#### Parameters

*saveName*
:   Filename to which to save the document

#### Return Value

Success or error code as defined by [SwDMDocumentSaveError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentSaveError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::SaveAs](swdocumentmgr~SwDMDocument~SaveAs.md).

# Remarks

A read-only document saved as a different file results in the new file being read-write.

This method lets you save a file to a different filename; this method does not let you save a file to a different file type.

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)
  
[ISwDMDocument::Save Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Save.md)
  
[ISwDMDocument::LastSavedBy Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.md)
  
[ISwDMDocument::LastSavedDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
