# GetZoneSizeDistribution Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetZoneSizeDistribution`

Gets the zone size distribution.
Gets the zone size distribution.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetZoneSizeDistribution( _
   ByRef Rows As System.Integer, _
   ByRef Columns As System.Integer _
) As System.Integer
```

```

Dim instance As ISheet
Dim Rows As System.Integer
Dim Columns As System.Integer
Dim value As System.Integer
 
value = instance.GetZoneSizeDistribution(Rows, Columns)
```

```

System.int GetZoneSizeDistribution( 
   out System.int Rows,
   out System.int Columns
)
```

```

System.int GetZoneSizeDistribution( 
   [Out] System.int Rows,
   [Out] System.int Columns
) 
```

#### Parameters

*Rows*
:   Zone rows; Nothing or null if the zone size distribution is swZoneSizeDistribution\_e.swZoneSizeDistribution\_50mmFromCenter

*Columns*
:   Zone columns; Nothing or null if the zone size distribution is swZoneSizeDistribution\_e.swZoneSizeDistribution\_50mmFromCenter

#### Return Value

Zone size distribution as defined by [swZoneSizeDistribution\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZoneSizeDistribution_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
