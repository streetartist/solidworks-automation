# IAddVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IAddVector`

Translates a math point by a math vector to create a new math point.
Translates a math point by a math vector to create a new math point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddVector( _
   ByVal VectorObjIn As MathVector _
) As MathPoint
```

```

Dim instance As IMathPoint
Dim VectorObjIn As MathVector
Dim value As MathPoint
 
value = instance.IAddVector(VectorObjIn)
```

```

MathPoint IAddVector( 
   MathVector VectorObjIn
)
```

```

MathPoint^ IAddVector( 
   MathVector^ VectorObjIn
) 
```

#### Parameters

*VectorObjIn*
:   [Math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) by which to translate this math point

#### Return Value

Newly created translated [math point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)  
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.md)  
[IMathPoint::AddVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~AddVector.md)  
[IMathPoint::SubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~SubtractVector.md)  
[IMathPoint::ISubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ISubtractVector.md)
