# ICreatePoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreatePoint`

Creates a new math point.
Creates a new math point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePoint( _
   ByRef ArrayDataIn As System.Double _
) As MathPoint
```

```

Dim instance As IMathUtility
Dim ArrayDataIn As System.Double
Dim value As MathPoint
 
value = instance.ICreatePoint(ArrayDataIn)
```

```

MathPoint ICreatePoint( 
   ref System.double ArrayDataIn
)
```

```

MathPoint^ ICreatePoint( 
   System.double% ArrayDataIn
) 
```

#### Parameters

*ArrayDataIn*
:   Array of doubles representing the coordinates (x,y,z) of the point

#### Return Value

Newly created [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) object or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.md)  
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.md)  
[IMathUtility::CreatePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreatePoint.md)
