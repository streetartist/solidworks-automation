# Delete3rdPartyStorageStore Method (ISwDMDocument20)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorageStore`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorageStore.html) on this topic. |
| Delete3rdPartyStorageStore Method (ISwDMDocument20) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument20 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20.md) : Delete3rdPartyStorageStore Method (ISwDMDocument20) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*SubStorageName*
:   Name of the storage to delete

Deletes the specified third-party storage store.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function Delete3rdPartyStorageStore( _    ByVal SubStorageName As System.String _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument20 Dim SubStorageName As System.String Dim value As System.Boolean   value = instance.Delete3rdPartyStorageStore(SubStorageName) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool Delete3rdPartyStorageStore(     System.string SubStorageName ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool Delete3rdPartyStorageStore(  &   System.String^ SubStorageName ) ``` | |

#### Parameters

*SubStorageName*
:   Name of the storage to delete

#### Return Value

True if the storage is deleted, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument20::Delete3rdPartyStorageStore](swdocumentmgr~SwDMDocument20~Delete3rdPartyStorageStore.md).

 

# See Also

#### 

[ISwDMDocument20 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20.md)
  
[ISwDMDocument20 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20_members.md)
  
[ISwDMDocument19::Get3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorageStore.md)
  
[ISwDMDocument19::Release3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorageStore.md)
  
[ISwDMDocument20::Delete3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorage.md)

# Availability

SOLIDWORKS Document Manager API 2016 FCS
