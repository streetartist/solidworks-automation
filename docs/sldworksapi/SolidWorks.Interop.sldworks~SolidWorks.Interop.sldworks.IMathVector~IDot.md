# IDot Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IDot`

Gets the value of the dot product between two math vectors.
Gets the value of the dot product between two math vectors.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDot( _
   ByVal VectorObjIn As MathVector _
) As System.Double
```

```

Dim instance As IMathVector
Dim VectorObjIn As MathVector
Dim value As System.Double
 
value = instance.IDot(VectorObjIn)
```

```

System.double IDot( 
   MathVector VectorObjIn
)
```

```

System.double IDot( 
   MathVector^ VectorObjIn
) 
```

#### Parameters

*VectorObjIn*
:   [Math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) to use to determine the dot value

#### Return Value

Value of the dot product

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.md)  
[IMathVector::Dot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Dot.md)
