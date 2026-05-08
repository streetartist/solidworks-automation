# IConvertToPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IConvertToPoint`

Converts this math vector to a point by using the three components of the math vector to be the coordinates of a new math point.
Converts this math vector to a point by using the three components of the math vector to be the coordinates of a new math point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IConvertToPoint() As MathPoint
```

```

Dim instance As IMathVector
Dim value As MathPoint
 
value = instance.IConvertToPoint()
```

```

MathPoint IConvertToPoint()
```

```

MathPoint^ IConvertToPoint(); 
```

#### Return Value

Newly created [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) object or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.md)  
[IMathVector::ConvertToPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ConvertToPoint.md)
