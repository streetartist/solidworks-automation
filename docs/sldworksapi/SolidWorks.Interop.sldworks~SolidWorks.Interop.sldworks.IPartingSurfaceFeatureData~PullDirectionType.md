# PullDirectionType Property (IPartingSurfaceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PullDirectionType`

Gets the type of entity that specifies the direction of pull for this parting surface feature.
Gets the type of entity that specifies the direction of pull for this parting surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property PullDirectionType As System.Integer
```

```

Dim instance As IPartingSurfaceFeatureData
Dim value As System.Integer
 
value = instance.PullDirectionType
```

```

System.int PullDirectionType {get;}
```

```

property System.int PullDirectionType {
   System.int get();
}
```

#### Property Value

Type of entity that represents the direction of pull as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

- swSelEDGES
- swSelDATUMAXES
- swSelDATUMPLANES
- swSelFaCES

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.md)  
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.md)  
[IPartingSurfaceFeatureData::PullDirectionBase Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PullDirectionBase.md)
