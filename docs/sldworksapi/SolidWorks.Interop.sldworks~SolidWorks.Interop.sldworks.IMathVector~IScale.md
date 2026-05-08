# IScale Method (IMathVector)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IScale`

Scales this math vector's magnitude by a factor and returns a new math vector.
Scales this math vector's magnitude by a factor and returns a new math vector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IScale( _
   ByVal ValueIn As System.Double _
) As MathVector
```

```

Dim instance As IMathVector
Dim ValueIn As System.Double
Dim value As MathVector
 
value = instance.IScale(ValueIn)
```

```

MathVector IScale( 
   System.double ValueIn
)
```

```

MathVector^ IScale( 
   System.double ValueIn
) 
```

#### Parameters

*ValueIn*
:   Value by which to scale the math vector

#### Return Value

Newly created [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.md)  
[IMathVector::Scale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Scale.md)
