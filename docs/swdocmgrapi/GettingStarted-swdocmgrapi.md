# Getting Started

Help ID: `GettingStarted-swdocmgrapi`
![](images/collapse.gif)
![](images/expand.gif)
![](images/copycode.gif)
![](images/copycodeHighlight.gif)
![](images/drpdown.gif)
![](images/drpdown_orange.gif)

|  |
| --- |
|  |

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help |  |
| Getting Started |
| [Send Feedback](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: GettingStarted-swdocmgrapi.html) | |

Glossary Item Box

This topic provides information to help you get started with using the SOLIDWORKS Document Manager API.

- [License Key](#LicenseKey)
- [Software Requirements](#SoftwareRequirements)
- [Installation](#Installation)
- [Application Basics](#ApplicationBasics)
- [Third-party Data in SOLIDWORKS Files](#third-party)
- Read how you might use our [Active Content Protection Framework](sldworksapiprogguide.chm::/Overview/ActiveContentProtectionFramework.htm) to guard against malicious active content.

#### License Key

The SOLIDWORKS Document Manager API requires a license key that is only available via the SOLIDWORKS customer portal to SOLIDWORKS customers who are currently under subscription. Each user of SOLIDWORKS Document Manager API must have a license key.

Existing users must request new SOLIDWORKS Document Manager API license keys beginning with SOLIDWORKS Document Manager API 2015 FCS and renew their SOLIDWORKS Document Manager API license keys when installing any new major release of SOLIDWORKS or the SOLIDWORKS Document Manager API.

SOLIDWORKS Document Manager API checks the version of the file being accessed. If the file was created using the same or an earlier version of SOLIDWORKS than the version of SOLIDWORKS Document Manager API license key, then SOLIDWORKS Document Manager API can access the file. However, if the file was created using a later version of SOLIDWORKS than the version of the SOLIDWORKS Document Manager API license key, then SOLIDWORKS Document Manager API cannot access the file and a message is displayed informing the user that the current SOLIDWORKS Document Manager API license key is expired. For example:

| Version in which SOLIDWORKS file created | Version of SOLIDWORKS Document Manager API license key | File Access Result |
| --- | --- | --- |
| 2014 or earlier | 2014 or earlier | Success |
| 2015 or later | 2014 or earlier | Failure |
| 2015 or earlier | 2015 or later | Success |

When requesting or renewing a SOLIDWORKS Document Manager API license key, you are presented with a dialog containing a list of check boxes showing the categories of functionality that a SOLIDWORKS Document Manager API license key controls. You can select more than one category.

- **Basic**: All interfaces, methods, and properties except for those listed below
- **Previews**: Preview and stream methods and properties on all ISwDMConfiguration, ISwDMDocument, and ISwDMSheet interfaces
- **DimXpert**: DimXpert methods and properties on all ISwDMConfiguration and all DimXpert-related interfaces
- **Geometry** **Streams**: Preview, stream, and imported body methods and properties on all ISwDMConfiguration interfaces
- **XML Streams**: XML stream methods on all ISwDMDocument interfaces
- **Tesselation**: Display List DLL (previously called the Display List Sample); although not a component of the SOLIDWORKS Document Manager API, its license key controls access to the Display List DLL

To request a SOLIDWORKS Document Manager API license key: <https://www.solidworks.com/support/subscription/key-request/>

A SOLIDWORKS Document Manager API license key is emailed to you upon approval of your request.  

IMPORTANT: Do not share this license key with anyone outside your company or distribute it with any software that you ship.

You must specify the license key when instantiating a SOLIDWORKS Document Manager API connection. See [Application Basics](#ApplicationBasics) for details.

[Back to top](#Top)

#### Software Requirements

The SOLIDWORKS Document Manager API requires:

- [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145), which installs the runtime components of Visual C++ libraries. These runtime components are required to successfully register the SOLIDWORKS Document Manager 2018 DLL, which was developed using Visual Studio 2015.

- Microsoft Core XML Services (MSXML) 4.0 or later; MSXML 6.0 is the first version of MSXML that supports 64-bit processors. MSXML is only needed if you want to use ISwDMComponent or ISwDMComponent2. Download MSXML from [www.microsoft.com](http://www.microsoft.com).

NOTE: A full SOLIDWORKS 2018 installation includes MSXML and the Visual C++ Redistributable for Visual Studio 2015. Clients installing SOLIDWORKS Document Manager on systems without a full SOLIDWORKS installation must also install MSXML and the Visual C++ Redistributable or ensure that they have been previously installed.

[Back to top](#Top)

#### Installation

Read the Software Requirements section before proceeding. MSXML and the Visual C++ Redistributable for Visual Studio 2015 must be installed in order to successfully register the SOLIDWORKS Document Manager DLLs.

The SOLIDWORKS Document Manager API is a COM object contained in SwDocumentMgr.dll. The SOLIDWORKS Document Manager DimXpert API is contained in **dimxpert.dll**. The zlib.dll DLL was automatically installed in the following folder if you installed the SOLIDWORKS software:

<disk>:\Program Files\Common Files\SOLIDWORKS Shared

SwDocumentMgr.dll and **dimxpert.dll** were also automatically registered if you installed the SOLIDWORKS software.

If you did not install the SOLIDWORKS software on the system where you want to use these APIs, you can manually register them.

SwDocumentMgr.dll and zlib.dll must either reside in the same folder or be accessible via the Windows search path.

To manually register **SwDocumentMgr.dll**:

1. On the task bar, click the search icon.
2. Type "C" in the Type here to search field.
3. Right-click on Command Prompt, and select Run as administrator.
4. Click **Yes** in the dialog box.
5. In the Administrator Command Prompt, type:  
     
   regsvr32  "<disk>:\Program Files\Common Files\SOLIDWORKS Shared\SwDocumentMgr.dll"
6. Click OK.

NOTE: Install programs, such as InstallShield, can automatically register the DLL for you.

To manually unregister **SwDocumentMgr.dll**:

1. Follow steps 1-4 in the manual registration instructions above.
2. In the Administrator Command Prompt, type:  
     
   regsvr32  /u "<disk>:\Program Files\Common Files\SOLIDWORKS Shared\SwDocumentMgr.dll"
3. Click OK.

You can redistribute swDocumentMgr.dll and zlib.dll.

To manually register **dimxpert.dll**:

1. On the task bar, click the search icon.
2. Type "C" in the Type here to search field.
3. Right-click on Command Prompt, and select Run as administrator.
4. Click **Yes** in the dialog box.
5. In the Administrator Command Prompt, type (*vX.X* is the name of a version directory that contains **RegAsm.exe**):  
     
   C:\WINDOWS\Microsoft.NET\Framework\*vX.X***\regasm /codebase**   "<disk>:\Program Files\Common Files\SOLIDWORKS Shared\dimxpert.dll"
6. Click OK.

[Back to top](#Top)

#### Application Basics

Writing a SOLIDWORKS Document Manager application typically involves:

1. Instantiating a SOLIDWORKS Document Manager connection ([ISwDMClassFactory::GetApplication](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory~GetApplication.md)).  
     
   NOTE: You must have a [license key](#LicenseKey) from SOLIDWORKS Corporation to instantiate the application object.
2. Opening a file ([ISwDMApplication::GetDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetDocument.md)).
3. Querying the file for data such as custom properties, configurations, references, and where the file is used ([ISwDMConfiguration::GetBodiesCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBodiesCount.md), [ISwDMConfiguration::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.md), [ISwDMDocument::GetAllExternalReferences](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetAllExternalReferences.md), [ISwDMDocument::GetHyperLinkAt](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetHyperLinkAt.md)).
4. Extracting data such as Parasolid bodies and XML data from assemblies ([ISwDMConfiguration::GetBody](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBody.md) and [ISwDMDocument::GetXMLStream](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetXmlStream.md)).
5. Extracting features and annotations from DimXpert parts ([ISwDMConfiguration12:DimXpertPart](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~DimXpertPart.md)).
6. Making changes ([ISwDMDocument::AddCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.md), [ISwDMDocument::DeleteCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.md), [ISwDMDocument::ModifyHyperLinkAt](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ModifyHyperLinkAt.md), [ISwDMDocument::ReplaceReference](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.md), [ISwDMDocument::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.md), etc.).
7. If any changes are made, saving the document ([ISwDMDocument::Save](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Save.md) or [ISwDMDocument::SaveAs](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SaveAs.md)).  
     
   **NOTE:** If recreating an application using an example and the example uses a SOLIDWORKS sample file, do not save changes.
8. Closing the document ([ISwDMDocument::CloseDoc](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CloseDoc.md)).  
     
   NOTE: You must close a document before you can copy or move it using [ISwDMApplication::CopyDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~CopyDocument.md) or [ISwDMApplication::MoveDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~MoveDocument.md).

Be sure to examine all returned error codes.

NOTE: Documents created using SOLIDWORKS 99 (Version 1137) or earlier are not supported by this API. See [ISwDMDocument::GetVersion](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md) for a detailed list of SOLIDWORKS versions supported by this API.

[Back to top](#Top)

#### Third-party Data in SOLIDWORKS Files

Starting with SOLIDWORKS 2015, third-party data stored in SOLIDWORKS files cannot be externally read or written by standard structured storage or compound file techniques.

To read or write third-party data, use the methods and events in the SOLIDWORKS API or SOLIDWORKS Document Manager API.

SOLIDWORKS API:

- [IModelDoc2::IGet3rdPartyStorage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.md)
- [IModelDoc2::IRelease3rdPartyStorage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IRelease3rdPartyStorage.md)
- [IModelDocExtension::IGet3rdPartyStorageStore](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.md)
- [IModelDocExtension::IRelease3rdPartyStorageStore](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IRelease3rdPartyStorageStore.md)
- [DAssemblyDocEvents::AutoSaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AutoSaveToStorageNotifyEventHandler.md)
- [DAssemblyDocEvents::AutoSaveToStorageStoreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AutoSaveToStorageStoreNotifyEventHandler.md)
- [DAssemblyDocEvents::LoadFromStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LoadFromStorageNotifyEventHandler.md)
- [DAssemblyDocEvents::LoadFromStorageStoreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler.md)
- [DAssemblyDocEvents::SaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SaveToStorageNotifyEventHandler.md)
- [DAssemblyDocEvents::SaveToStorageStoreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler.md)
- [DDrawingDocEvents::AutoSaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler.md)
- [DDrawingDocEvents::AutoSaveToStorageStoreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_AutoSaveToStorageStoreNotifyEventHandler.md)
- [DDrawingDocEvents::LoadFromStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_LoadFromStorageNotifyEventHandler.md)
- [DDrawingDocEvents::LoadFromStorageStoreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler.md)
- [DDrawingDocEvents::SaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_SaveToStorageNotifyEventHandler.md)
- [DDrawingDocEvents::SaveToStorageStoreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler.md)
- [DPartDocEvents::AutoSaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AutoSaveToStorageNotifyEventHandler.md)
- [DPartDocEvents::AutoSaveToStorageStoreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler.md)
- [DPartDocEvents::LoadFromStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_LoadFromStorageNotifyEventHandler.md)
- [DPartDocEvents::LoadFromStorageStoreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_LoadFromStorageStoreNotifyEventHandler.md)
- [DPartDocEvents::SaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SaveToStorageNotifyEventHandler.md)
- [DPartDocEvents::SaveToStorageStoreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SaveToStorageStoreNotifyEventHandler.md)

**SOLIDWORKS Document Manager API:**

- [ISwDMDocument20::Delete3rdPartyStorage](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorage.md)
- [ISwDMDocument20::Delete3rdPartyStorageStore](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorageStore.md)
- [ISwDMDocument19::Get3rdPartyStorage](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorage.md)
- [ISwDMDocument19::Get3rdPartyStorageStore](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorageStore.md)
- [ISwDMDocument19::Release3rdPartyStorage](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorage.md)
- [ISwDMDocument19::Release3rdPartyStorageStore](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorageStore.md)

[Back to top](#Top)
