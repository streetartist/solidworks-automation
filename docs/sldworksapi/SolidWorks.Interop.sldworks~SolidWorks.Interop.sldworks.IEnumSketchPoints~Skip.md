# Skip Method (IEnumSketchPoints)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints~Skip`

Skips the specified number of sketch points in the sketch points enumeration.
Skips the specified number of sketch points in the sketch points enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Skip( _
   ByVal Celt As System.Integer _
) 
```

```

Dim instance As IEnumSketchPoints
Dim Celt As System.Integer
 
instance.Skip(Celt)
```

```

void Skip( 
   System.int Celt
)
```

```

void Skip( 
   System.int Celt
) 
```

#### Parameters

*Celt*
:   Number of sketch points to skip

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumSketchPoints Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints.md)  
[IEnumSketchPoints Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints_members.md)
