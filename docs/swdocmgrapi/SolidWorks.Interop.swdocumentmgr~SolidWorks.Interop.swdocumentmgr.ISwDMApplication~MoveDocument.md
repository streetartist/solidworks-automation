# MoveDocument Method (ISwDMApplication)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~MoveDocument`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~MoveDocument.html) on this topic. |
| MoveDocument Method (ISwDMApplication) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.md) : MoveDocument Method (ISwDMApplication) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*fromName*
:   Full path and filename of the document to move

*toName*
:   Full path and filename of the new document to which to move the document specified for fromName

*fromChildren*
:   Array containing the full path and filenames of the child documents dependent on the document specified for fromName

*toChildren*
:   Array containing the new full path and filenames for the child documents to which to move the documents specified for fromChildren

*option*
:   Move options as defined by [SwDmCopyOptions](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCopyOptions.md)

*pSrcOption*
:   Pointer to an [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) object

Moves a single document and optionally updates references to it.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function MoveDocument( _    ByVal fromName As System.String, _    ByVal toName As System.String, _    ByVal fromChildren As System.Object, _    ByVal toChildren As System.Object, _    ByVal option As System.Integer, _    ByVal pSrcOption As SwDMSearchOption _ ) As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMApplication Dim fromName As System.String Dim toName As System.String Dim fromChildren As System.Object Dim toChildren As System.Object Dim option As System.Integer Dim pSrcOption As SwDMSearchOption Dim value As System.Integer   value = instance.MoveDocument(fromName, toName, fromChildren, toChildren, option, pSrcOption) ``` | |

| C# |  |
| --- | --- |
| ``` System.int MoveDocument(     System.string fromName,    System.string toName,    System.object fromChildren,    System.object toChildren,    System.int option,    SwDMSearchOption pSrcOption ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int MoveDocument(  &   System.String^ fromName, &   System.String^ toName, &   System.Object^ fromChildren, &   System.Object^ toChildren, &   System.int option, &   SwDMSearchOption^ pSrcOption ) ``` | |

#### Parameters

*fromName*
:   Full path and filename of the document to move

*toName*
:   Full path and filename of the new document to which to move the document specified for fromName

*fromChildren*
:   Array containing the full path and filenames of the child documents dependent on the document specified for fromName

*toChildren*
:   Array containing the new full path and filenames for the child documents to which to move the documents specified for fromChildren

*option*
:   Move options as defined by [SwDmCopyOptions](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCopyOptions.md)

*pSrcOption*
:   Pointer to an [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) object

#### Return Value

Success or error code as defined by [SwDmMoveCopyError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmMoveCopyError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMApplication::MoveDocument](swdocumentmgr~SwDMApplication~MoveDocument.md).

# Remarks

If a document is opened, you must call [ISwDMDocument::CloseDoc](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CloseDoc.md) to close it before calling this method.

# See Also

#### 

[ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.md)
  
[ISwDMApplication Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication_members.md)
  
[ISwDMApplication::CopyDocument Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~CopyDocument.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
