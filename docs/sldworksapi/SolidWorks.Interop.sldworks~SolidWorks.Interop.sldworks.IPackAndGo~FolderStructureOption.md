# FolderStructureOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FolderStructureOption`

Gets or sets the folder structure to save to with Pack and Go.
Gets or sets the folder structure to save to with Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FolderStructureOption As System.Integer
```

```

Dim instance As IPackAndGo
Dim value As System.Integer
 
instance.FolderStructureOption = value
 
value = instance.FolderStructureOption
```

```

System.int FolderStructureOption {get; set;}
```

```

property System.int FolderStructureOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Folder structure as defined by [swPackAndGoFolderOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPackAndGoFolderOptions_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::SetSaveToName2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName2.md)
