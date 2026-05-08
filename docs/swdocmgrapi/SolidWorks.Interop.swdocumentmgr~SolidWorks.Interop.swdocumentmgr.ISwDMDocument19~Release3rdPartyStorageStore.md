# Release3rdPartyStorageStore Method (ISwDMDocument19)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorageStore`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorageStore.html) on this topic. |
| Release3rdPartyStorageStore Method (ISwDMDocument19) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.md) : Release3rdPartyStorageStore Method (ISwDMDocument19) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*SubStorageName*
:   Name of the storage to close

Closes the specified third-party storage store.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function Release3rdPartyStorageStore( _    ByVal SubStorageName As System.String _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument19 Dim SubStorageName As System.String Dim value As System.Boolean   value = instance.Release3rdPartyStorageStore(SubStorageName) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool Release3rdPartyStorageStore(     System.string SubStorageName ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool Release3rdPartyStorageStore(  &   System.String^ SubStorageName ) ``` | |

#### Parameters

*SubStorageName*
:   Name of the storage to close

#### Return Value

True if the storage is closed, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument19::Release3rdPartyStorageStore](swdocumentmgr~SwDMDocument19~Release3rdPartyStorageStore.md).

# Example

[Read and Write to Third-party Storage (VB.NET)](Get_and_Set_3rd_Party_Storage_Example_VBNET.htm)
  
[Read and Write to Third-party Storage (C#)](Get_and_Set_3rd_Party_Storage_Example_CSharp.htm)

# Remarks

You must call this method after calling [ISwDMDocument19::Get3rdPartyStorageStore](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorageStore.md).

# See Also

#### 

[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.md)
  
[ISwDMDocument19 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19_members.md)
  
[ISwDMDocument19::Release3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorage.md)
  
[ISwDocument20::Delete3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorageStore.md)

# Availability

SOLIDWORKS Document Manager API 2015 SP0
