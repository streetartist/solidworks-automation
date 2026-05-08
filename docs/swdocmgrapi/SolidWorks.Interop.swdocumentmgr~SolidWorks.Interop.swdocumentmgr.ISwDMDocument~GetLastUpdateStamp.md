# GetLastUpdateStamp Method (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetLastUpdateStamp`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetLastUpdateStamp.html) on this topic. |
| GetLastUpdateStamp Method (ISwDMDocument) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : GetLastUpdateStamp Method (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the date on which this document was last updated.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetLastUpdateStamp() As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim value As System.Integer   value = instance.GetLastUpdateStamp() ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetLastUpdateStamp() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetLastUpdateStamp(); ``` | |

#### Return Value

Date document last updated

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::GetLastUpdateStamp](swdocumentmgr~SwDMDocument~GetLastUpdateStamp.md).

# Example

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
  
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

# Remarks

The update stamp is an integer representing a time stamp. The update stamp in a SOLIDWORKS document is incremented when:

- the state of the model changes (for example, you suppress or unsuppress a feature in a part or an assembly)
- the geometry changes (for example, any action that requires a rebuild)

This time stamp is not incremented for such operations as color changes, feature or configuration name changes, and so on.

This method returns 0 for non-SOLIDWORKS documents.

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)
  
[ISwDMDocument::CreationDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CreationDate.md)
  
[ISwDMDocument::LastSavedBy Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.md)
  
[ISwDMDocument::LastSavedDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
