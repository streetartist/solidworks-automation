# Get3rdPartyStorageStore Method (ISwDMDocument19)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorageStore`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorageStore.html) on this topic. |
| Get3rdPartyStorageStore Method (ISwDMDocument19) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.md) : Get3rdPartyStorageStore Method (ISwDMDocument19) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*SubStorageName*
:   Name of the storage

*IsStoring*
:   True if writing data, false if reading data

Gets the IStorage interface to the specified third-party storage store of this model document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function Get3rdPartyStorageStore( _    ByVal SubStorageName As System.String, _    ByVal IsStoring As System.Boolean _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument19 Dim SubStorageName As System.String Dim IsStoring As System.Boolean Dim value As System.Object   value = instance.Get3rdPartyStorageStore(SubStorageName, IsStoring) ``` | |

| C# |  |
| --- | --- |
| ``` System.object Get3rdPartyStorageStore(     System.string SubStorageName,    System.bool IsStoring ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ Get3rdPartyStorageStore(  &   System.String^ SubStorageName, &   System.bool IsStoring ) ``` | |

#### Parameters

*SubStorageName*
:   Name of the storage

*IsStoring*
:   True if writing data, false if reading data

#### Return Value

Pointer to Unknown (see **Remarks**)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument19::Get3rdPartyStorageStore](swdocumentmgr~SwDMDocument19~Get3rdPartyStorageStore.md).

# Example

[Read and Write to Third-party Storage (VB.NET)](Get_and_Set_3rd_Party_Storage_Example_VBNET.htm)
  
[Read and Write to Third-party Storage (C#)](Get_and_Set_3rd_Party_Storage_Example_CSharp.htm)

# Remarks

After calling this method, you must call [ISwDMDocument19::Release3rdPartyStorageStore](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorageStore.md). Otherwise, the third-party node might remain locked and prevent future access.

NOTE: The name given to the storage should be registered so that no conflicts occur. Once registered, the storage name is reserved exclusively for your application.

Passing the unique ID string and a flag to determine if data is being stored or loaded returns an IUnknown pointer. You must then use QueryInterface() to get the **Microsoft.VisualStudio.OLE.Interop.IStorage** interface. The storage object is used for serialization and then released in the third-party code.

The IStorage object used by the third party is written under an IStorage object called ThirdPtyStore in the SOLIDWORKS compound document. Each third party writes to a single IStorage whose name is assigned by SOLIDWORKS.

SwRootStorage --|

        |-- ThirdPtyStore --|

                |-- <SW Assigned IStorage name 1> --|

                                  |-- <Application 1 IStream name 1>

                                  |-- <Application 1 IStream name 2>

                |-- <SW Assigned IStorage name 2> --|

                                  |-- <Application 2 IStream name 1>

                                  |-- <Application 2 IStream name 2>

                                  |-- <Application 2 IStorage name 2> --|

                                                     |-- <Application 2 IStream name 3>

NOTE: If you are using serialization, then be careful with the standard MFC macros. Otherwise, you may get a message like Unexpected File Format after your application is unloaded. One way of using IMPLEMENT\_SERIAL:

IMPLEMENT\_SERIAL( CCustomAttr, CObject, VERSIONABLE\_SCHEMA|0 )

# See Also

#### 

[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.md)
  
[ISwDMDocument19 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19_members.md)
  
[ISwDMDocument19::Get3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorage.md)
  
[ISwDMDocument20::Delete3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorageStore.md)

# Availability

SOLIDWORKS Document Manager API 2015 SP0
