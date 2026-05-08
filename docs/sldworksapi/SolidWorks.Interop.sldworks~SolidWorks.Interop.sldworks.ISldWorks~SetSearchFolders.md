# SetSearchFolders Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSearchFolders`

Sets the current folder search path as shown in Tools &gt; Options &gt; System Options &gt; File Locations &gt; Show folders for &gt; Referenced Documents.
Sets the current folder search path as shown in Tools > Options > System Options > File Locations > Show folders for  > Referenced Documents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSearchFolders( _
   ByVal FolderType As System.Integer, _
   ByVal Folders As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FolderType As System.Integer
Dim Folders As System.String
Dim value As System.Boolean
 
value = instance.SetSearchFolders(FolderType, Folders)
```

```

System.bool SetSearchFolders( 
   System.int FolderType,
   System.string Folders
)
```

```

System.bool SetSearchFolders( 
   System.int FolderType,
   System.String^ Folders
) 
```

#### Parameters

*FolderType*
:   The search folder type; the only type currently supported is swDocumentType; for an up-to-date listing, see [swSearchFolderTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSearchFolderTypes_e.html)

*Folders*
:   String containing all of the search folders; each search folder should be separated by a semicolon

#### Return Value

True if the search folders were set, false if not

Remarks

The search folders are used by SOLIDWORKS based on their order. Folders at the top of the list get searched first and folders at the bottom of the list get searched last.

This method does not allow you to incrementally add to the search folders list. Calling this method overwrites the existing search folder settings. If you want to add a folder to the existing search folder list, you must get the current search folder list using [ISldWorks::GetSearchFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSearchFolders.md) and then add your folder string at the appropriate location.

Search folder settings are ignored unless **Tools > Options > System Options > External References >** Search file locations for external references is selected. To get and set Search file locations for external references in the SOLIDWORKS API, use [swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html).swUseFolderSearchRules with [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.md) and [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md), respectively.

Example

[Get and Set Search Folders (VBA)](Get_and_Set_Search_Folders_Example_VB.htm)  
[Get and Set Search Folders (VB.NET)](Get_and_Set_Search_Folders_Example_VBNET.htm)  
[Get and Set Search Folders (C#)](Get_and_Set_Search_Folders_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetSearchFolders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSearchFolders.md)  
[ISldWorks::SetMissingReferencePathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMissingReferencePathName.md)  
[ISldWorks::GetDataFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDataFolder.md)
