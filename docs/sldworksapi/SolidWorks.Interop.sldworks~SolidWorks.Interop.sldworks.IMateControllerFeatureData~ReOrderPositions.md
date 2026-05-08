# ReOrderPositions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~ReOrderPositions`

Reorders the mate positions in this mate controller.
Reorders the mate positions in this mate controller.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ReOrderPositions( _
   ByVal Positions As System.Object _
) 
```

```

Dim instance As IMateControllerFeatureData
Dim Positions As System.Object
 
instance.ReOrderPositions(Positions)
```

```

void ReOrderPositions( 
   System.object Positions
)
```

```

void ReOrderPositions( 
   System.Object^ Positions
) 
```

#### Parameters

*Positions*
:   Array of re-ordered mate positions

Remarks

Before calling this method, use [IMateControllerFeatureData::GetPositions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~GetPositions.md) to get the existing mate positions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md)  
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.md)
