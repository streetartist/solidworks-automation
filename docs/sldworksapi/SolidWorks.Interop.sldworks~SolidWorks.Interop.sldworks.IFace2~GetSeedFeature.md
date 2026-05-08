# GetSeedFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSeedFeature`

Gets the seed feature of a patterned, mirrored, or copied body for this face.
Gets the seed feature of a patterned, mirrored, or copied body for this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSeedFeature() As Feature
```

```

Dim instance As IFace2
Dim value As Feature
 
value = instance.GetSeedFeature()
```

```

Feature GetSeedFeature()
```

```

Feature^ GetSeedFeature(); 
```

#### Return Value

Seed [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) of a patterned, mirrored, or copied body

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetPatternSeedFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetPatternSeedFeature.md)
