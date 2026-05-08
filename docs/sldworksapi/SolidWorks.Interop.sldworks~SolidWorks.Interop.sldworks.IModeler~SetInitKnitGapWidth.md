# SetInitKnitGapWidth Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetInitKnitGapWidth`

Sets the initial gap bound width for sewing a body. Call this method before calling any calls that attempt to knit a body; for example, IBody2::CreateBodyFromSurfaces.
Sets the initial gap bound width for sewing a body. Call this method before calling any calls that attempt to knit a body; for example, [IBody2::CreateBodyFromSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromSurfaces.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetInitKnitGapWidth( _
   ByVal InitGapWidth As System.Double _
) As System.Boolean
```

```

Dim instance As IModeler
Dim InitGapWidth As System.Double
Dim value As System.Boolean
 
value = instance.SetInitKnitGapWidth(InitGapWidth)
```

```

System.bool SetInitKnitGapWidth( 
   System.double InitGapWidth
)
```

```

System.bool SetInitKnitGapWidth( 
   System.double InitGapWidth
) 
```

#### Parameters

*InitGapWidth*
:   Desired knitting gap width for body knitting; valid range is from 1e-8 to 0.1 meters

#### Return Value

True if successfully set, false if not

Remarks

This initial gap width bound is adjusted during the knitting operation in an attempt to successfully knit a body. Upon completion of the knitting operation, the value is reset to the default value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::GetInitKnitGapWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetInitKnitGapWidth.md)
