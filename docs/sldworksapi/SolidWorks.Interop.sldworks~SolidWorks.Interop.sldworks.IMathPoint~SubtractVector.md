# SubtractVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~SubtractVector`

Gets a math point that describes the difference between a math vector's magnitude from the calling math point
Gets a math point that describes the difference between a math vector's magnitude from the calling math point

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SubtractVector( _
   ByVal VectorObjIn As System.Object _
) As System.Object
```

```

Dim instance As IMathPoint
Dim VectorObjIn As System.Object
Dim value As System.Object
 
value = instance.SubtractVector(VectorObjIn)
```

```

System.object SubtractVector( 
   System.object VectorObjIn
)
```

```

System.Object^ SubtractVector( 
   System.Object^ VectorObjIn
) 
```

#### Parameters

*VectorObjIn*
:   [Math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) by which to subtract this math point

#### Return Value

Newly created [math point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)  
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.md)  
[IMathPoint::ISubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ISubtractVector.md)
