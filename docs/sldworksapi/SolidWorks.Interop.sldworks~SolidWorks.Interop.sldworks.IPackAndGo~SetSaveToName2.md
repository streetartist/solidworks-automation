# SetSaveToName2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName2`

Overrides the paths and filenames of the documents set by IPackAndGo::SetDocumentSaveToNames or IPackAndGo::ISetDocumentSaveToNames with the specified path or the path and name of the Zip file.
Overrides the paths and filenames of the documents set by [IPackAndGo::SetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md) or [IPackAndGo::ISetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md) with the specified path or the path and name of the Zip file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSaveToName2( _
   ByVal Override As System.Boolean, _
   ByVal SaveToName As System.String _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim Override As System.Boolean
Dim SaveToName As System.String
Dim value As System.Boolean
 
value = instance.SetSaveToName2(Override, SaveToName)
```

```

System.bool SetSaveToName2( 
   System.bool Override,
   System.string SaveToName
)
```

```

System.bool SetSaveToName2( 
   System.bool Override,
   System.String^ SaveToName
) 
```

#### Parameters

*Override*
:   True to override the paths and filenames of the documents set by [IPackAndGo::SetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md) or [IPackAndGo::ISetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md), false to not

*SaveToName*
:   Path or the path and filename of the Zip file to use to override the paths and filenames of the documents set by IPackAndGo::SetDocumentSaveToNames or IPackAndGo::ISetDocumentSaveToNames

#### Return Value

True if the paths and filenames of the documents set by IPackAndGo::SetDocumentSaveToNames or IPackAndGo::ISetDocumentSaveToNames are overridden, false if not

Remarks

The difference between this method and the now obsolete IPackAndGo::SetSaveToName is that this method supports saving to minimal folders. It saves to any folder structure as defined by [IPackAndGo::FolderStructureOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FolderStructureOption.md).

Example

[Add and Remove Files from Pack and Go (VBA)](Add_and_Remove_Files_from_Pack_and_Go_Example_VB.htm)  
[Add and Remove Files from Pack and Go (VB.NET)](Add_and_Remove_Files_from_Pack_and_Go_Example_VBNET.htm)  
[Add and Remove Files from Pack and Go (C#)](Add_and_Remove_Files_from_Pack_and_Go_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::GetSaveToName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetSaveToName.md)  
[IPackAndGo::FlattenToSingleFolder Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FlattenToSingleFolder.md)
