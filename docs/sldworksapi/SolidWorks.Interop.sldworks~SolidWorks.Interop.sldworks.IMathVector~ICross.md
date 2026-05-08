# ICross Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ICross`

Gets the cross product between two math vectors.
Gets the cross product between two math vectors.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICross( _
   ByVal VectorObjIn As MathVector _
) As MathVector
```

```

Dim instance As IMathVector
Dim VectorObjIn As MathVector
Dim value As MathVector
 
value = instance.ICross(VectorObjIn)
```

```

MathVector ICross( 
   MathVector VectorObjIn
)
```

```

MathVector^ ICross( 
   MathVector^ VectorObjIn
) 
```

#### Parameters

*VectorObjIn*
:   [Math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) to use to determine the cross product

#### Return Value

Newly created [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.md)  
[IMathVector::Cross Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Cross.md)
