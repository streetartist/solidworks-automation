# Delete3rdPartyStorage Method (ISwDMDocument20)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorage`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorage.html) on this topic. |
| Delete3rdPartyStorage Method (ISwDMDocument20) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument20 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20.md) : Delete3rdPartyStorage Method (ISwDMDocument20) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*StringIn*
:   Name of the stream to delete

Deletes the specified third-party storage.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function Delete3rdPartyStorage( _    ByVal StringIn As System.String _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument20 Dim StringIn As System.String Dim value As System.Boolean   value = instance.Delete3rdPartyStorage(StringIn) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool Delete3rdPartyStorage(     System.string StringIn ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool Delete3rdPartyStorage(  &   System.String^ StringIn ) ``` | |

#### Parameters

*StringIn*
:   Name of the stream to delete

#### Return Value

True if the stream is deleted, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument20::Delete3rdPartyStorage](swdocumentmgr~SwDMDocument20~Delete3rdPartyStorage.md).

 

# See Also

#### 

[ISwDMDocument20 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20.md)
  
[ISwDMDocument20 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20_members.md)
  
[ISwDMDocument19::Get3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorage.md)
  
[ISwDMDocument19::Release3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorage.md)
  
[ISwDMDocument20::Delete3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorageStore.md)

# Availability

SOLIDWORKS Document Manager API 2016 FCS
