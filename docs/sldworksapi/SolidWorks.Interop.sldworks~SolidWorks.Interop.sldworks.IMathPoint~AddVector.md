# AddVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~AddVector`

Translates a math point by a math vector to create a new math point.
Translates a math point by a math vector to create a new math point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddVector( _
   ByVal VectorObjIn As System.Object _
) As System.Object
```

```

Dim instance As IMathPoint
Dim VectorObjIn As System.Object
Dim value As System.Object
 
value = instance.AddVector(VectorObjIn)
```

```

System.object AddVector( 
   System.object VectorObjIn
)
```

```

System.Object^ AddVector( 
   System.Object^ VectorObjIn
) 
```

#### Parameters

*VectorObjIn*
:   [Math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) by which to translate this math point

#### Return Value

Newly created translated [math point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) or NULL if the operation fails

Example

[Locate Apex of Conical Face (VBA)](Locate_Apex_of_Conical_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)  
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.md)  
[IMathPoint::IAddVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IAddVector.md)  
[IMathPoint::SubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~SubtractVector.md)  
[IMathPoint::ISubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ISubtractVector.md)
