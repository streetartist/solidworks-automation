# SetZoneSizeDistribution Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetZoneSizeDistribution`

Sets the zone size distribution.
Sets the zone size distribution.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetZoneSizeDistribution( _
   ByVal Type As System.Integer, _
   ByVal Rows As System.Integer, _
   ByVal Column As System.Integer _
) As System.Boolean
```

```

Dim instance As ISheet
Dim Type As System.Integer
Dim Rows As System.Integer
Dim Column As System.Integer
Dim value As System.Boolean
 
value = instance.SetZoneSizeDistribution(Type, Rows, Column)
```

```

System.bool SetZoneSizeDistribution( 
   System.int Type,
   System.int Rows,
   System.int Column
)
```

```

System.bool SetZoneSizeDistribution( 
   System.int Type,
   System.int Rows,
   System.int Column
) 
```

#### Parameters

*Type*
:   Type of zone size distribution as defined by [swZoneSizeDistribution\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZoneSizeDistribution_e.html)

*Rows*
:   Number of zone rows; valid only if Type is swZoneSizeDistribution.swZoneSizeDistribution\_EvenlySized

*Column*
:   Number of zone columns; valid only if Type is swZoneSizeDistribution.swZoneSizeDistribution\_EvenlySized

#### Return Value

True if zone size distribution successfully set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
