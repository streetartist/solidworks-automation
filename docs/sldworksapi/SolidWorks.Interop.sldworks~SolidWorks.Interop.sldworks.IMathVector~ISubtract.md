# ISubtract Method (IMathVector)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ISubtract`

Subtracts the specified math vector's magnitude from this math vector and returns a new math vector.
Subtracts the specified math vector's magnitude from this math vector and returns a new math vector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISubtract( _
   ByVal VectorObjIn As MathVector _
) As MathVector
```

```

Dim instance As IMathVector
Dim VectorObjIn As MathVector
Dim value As MathVector
 
value = instance.ISubtract(VectorObjIn)
```

```

MathVector ISubtract( 
   MathVector VectorObjIn
)
```

```

MathVector^ ISubtract( 
   MathVector^ VectorObjIn
) 
```

#### Parameters

*VectorObjIn*
:   [Math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) to subtract from this math vector

#### Return Value

Newly created [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.md)  
[IMathVector::Subtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Subtract.md)  
[IMathVector::Add Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Add.md)  
[IMathVector::IAdd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IAdd.md)
