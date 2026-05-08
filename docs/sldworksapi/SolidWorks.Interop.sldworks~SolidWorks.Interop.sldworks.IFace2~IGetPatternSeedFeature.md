# IGetPatternSeedFeature Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetPatternSeedFeature`

Gets the seed feature of a pattern.
Gets the seed feature of a pattern.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPatternSeedFeature() As Feature
```

```

Dim instance As IFace2
Dim value As Feature
 
value = instance.IGetPatternSeedFeature()
```

```

Feature IGetPatternSeedFeature()
```

```

Feature^ IGetPatternSeedFeature(); 
```

#### Return Value

Seed feature of the current face; if the face does not belong to a pattern, this method returns NULL

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetPatternSeedFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetPatternSeedFeature.md)  
[IModelDoc2::EditSeedFeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSeedFeat.md)
