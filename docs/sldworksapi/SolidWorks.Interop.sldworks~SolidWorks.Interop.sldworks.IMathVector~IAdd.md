# IAdd Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IAdd`

Adds this math vector with the specified math vector.
Adds this math vector with the specified math vector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAdd( _
   ByVal VectorObjIn As MathVector _
) As MathVector
```

```

Dim instance As IMathVector
Dim VectorObjIn As MathVector
Dim value As MathVector
 
value = instance.IAdd(VectorObjIn)
```

```

MathVector IAdd( 
   MathVector VectorObjIn
)
```

```

MathVector^ IAdd( 
   MathVector^ VectorObjIn
) 
```

#### Parameters

*VectorObjIn*
:   [Math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) object to add to this math vector

#### Return Value

Newly created [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) object or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.md)  
[MathVector::Add Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Add.md)  
[IMathVector::ISubtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ISubtract.md)  
[IMathVector::Subtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Subtract.md)
