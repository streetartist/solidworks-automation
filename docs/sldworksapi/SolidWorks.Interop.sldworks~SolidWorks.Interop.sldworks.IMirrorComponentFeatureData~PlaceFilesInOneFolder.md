# PlaceFilesInOneFolder Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PlaceFilesInOneFolder`

Gets or sets whether to place the opposite-hand versions in one folder.
Gets or sets whether to place the opposite-hand versions in one folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PlaceFilesInOneFolder As System.Boolean
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean
 
instance.PlaceFilesInOneFolder = value
 
value = instance.PlaceFilesInOneFolder
```

```

System.bool PlaceFilesInOneFolder {get; set;}
```

```

property System.bool PlaceFilesInOneFolder {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to place the opposite-hand files in one folder, false to not

Remarks

This property is valid only if [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.md) is false.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
