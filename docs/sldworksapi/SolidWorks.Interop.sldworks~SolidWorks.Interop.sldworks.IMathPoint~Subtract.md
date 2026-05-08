# Subtract Method (IMathPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~Subtract`

Gets a math vector that describes the difference between the math point magnitude from the calling math point.
Gets a math vector that describes the difference between the math point magnitude from the calling math point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Subtract( _
   ByVal PointObjIn As System.Object _
) As System.Object
```

```

Dim instance As IMathPoint
Dim PointObjIn As System.Object
Dim value As System.Object
 
value = instance.Subtract(PointObjIn)
```

```

System.object Subtract( 
   System.object PointObjIn
)
```

```

System.Object^ Subtract( 
   System.Object^ PointObjIn
) 
```

#### Parameters

*PointObjIn*
:   [Math point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) by which to subtract this math point

#### Return Value

Newly created [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)  
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.md)  
[IMathPoint::ISubtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ISubtract.md)
