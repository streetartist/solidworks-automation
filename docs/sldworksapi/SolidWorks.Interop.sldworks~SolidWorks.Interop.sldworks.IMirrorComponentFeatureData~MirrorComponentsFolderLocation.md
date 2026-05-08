# MirrorComponentsFolderLocation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorComponentsFolderLocation`

Gets or sets the existing folder where all opposite-hand versions are saved.
Gets or sets the existing folder where all opposite-hand versions are saved.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MirrorComponentsFolderLocation As System.String
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.String
 
instance.MirrorComponentsFolderLocation = value
 
value = instance.MirrorComponentsFolderLocation
```

```

System.string MirrorComponentsFolderLocation {get; set;}
```

```

property System.String^ MirrorComponentsFolderLocation {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Existing folder name

Remarks

This property is valid only if [IMirrorComponentFeatureData::PlaceFilesInOneFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PlaceFilesInOneFolder.md) is true.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
