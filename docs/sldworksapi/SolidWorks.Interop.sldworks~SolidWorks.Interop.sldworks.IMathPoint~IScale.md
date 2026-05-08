# IScale Method (IMathPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IScale`

Scales a math point's magnitude.
Scales a math point's magnitude.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IScale( _
   ByVal ValueIn As System.Double _
) As MathPoint
```

```

Dim instance As IMathPoint
Dim ValueIn As System.Double
Dim value As MathPoint
 
value = instance.IScale(ValueIn)
```

```

MathPoint IScale( 
   System.double ValueIn
)
```

```

MathPoint^ IScale( 
   System.double ValueIn
) 
```

#### Parameters

*ValueIn*
:   Scale by which to multiply the magnitude of the math point

#### Return Value

Newly created scaled [math point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)  
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.md)  
[IMathPoint::Scale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~Scale.md)
