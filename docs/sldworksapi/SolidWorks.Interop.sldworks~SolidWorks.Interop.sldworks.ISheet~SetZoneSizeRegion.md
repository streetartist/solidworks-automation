# SetZoneSizeRegion Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetZoneSizeRegion`

Sets the type of zone size region.
Sets the type of zone size region.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetZoneSizeRegion( _
   ByVal RegionType As System.Integer _
) As System.Boolean
```

```

Dim instance As ISheet
Dim RegionType As System.Integer
Dim value As System.Boolean
 
value = instance.SetZoneSizeRegion(RegionType)
```

```

System.bool SetZoneSizeRegion( 
   System.int RegionType
)
```

```

System.bool SetZoneSizeRegion( 
   System.int RegionType
) 
```

#### Parameters

*RegionType*
:   Type of zone size region as defined by [swRegionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRegionType_e.html)

#### Return Value

True of zone size region successfully set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
