# GetSearchFolders Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSearchFolders`

Gets the current folder search path as shown in Tools &gt; Options &gt; System Options &gt; File Locations &gt; Show folders for &gt; Referenced Documents.
Gets the current folder search path as shown in Tools > Options > System Options > File Locations > Show folders for > Referenced Documents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSearchFolders( _
   ByVal FolderType As System.Integer _
) As System.String
```

```

Dim instance As ISldWorks
Dim FolderType As System.Integer
Dim value As System.String
 
value = instance.GetSearchFolders(FolderType)
```

```

System.string GetSearchFolders( 
   System.int FolderType
)
```

```

System.String^ GetSearchFolders( 
   System.int FolderType
) 
```

#### Parameters

*FolderType*
:   Search folder type; the only type supported is swDocumentType; for an up-to-date listing, see [swSearchFolderTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSearchFolderTypes_e.html)

#### Return Value

String containing all of the search folders; each search folder is separated by a semicolon

Remarks

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
[ISldWorks::SetSearchFolders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSearchFolders.md)  
[ISldWorks::GetDataFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDataFolder.md)  
[ISldWorks::SetMissingReferencePathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMissingReferencePathName.md)
