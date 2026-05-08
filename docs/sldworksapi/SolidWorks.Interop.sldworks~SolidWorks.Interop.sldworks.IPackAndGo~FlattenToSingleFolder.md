# FlattenToSingleFolder Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FlattenToSingleFolder`

Gets or sets whether to save all files to the root directory of the Pack and Go destination folder.
Gets or sets whether to save all files to the root directory of the Pack and Go destination folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlattenToSingleFolder As System.Boolean
```

```

Dim instance As IPackAndGo
Dim value As System.Boolean
 
instance.FlattenToSingleFolder = value
 
value = instance.FlattenToSingleFolder
```

```

System.bool FlattenToSingleFolder {get; set;}
```

```

property System.bool FlattenToSingleFolder {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to save all files to the root directory of the Pack and Go destination folder, false to save the files to subfolders in the destination folder that mirror the current model's folder structure

Example

[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)  
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)  
[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::SetSaveToName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName.md)  
[IPackAndGo::SetDocumentSaveToNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md)  
[IPackAndGo::ISetDocumentSaveToNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md)
