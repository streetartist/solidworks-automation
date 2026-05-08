# IAddProfileArcDLL Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArcDLL`

Adds a profile arc.
Adds a profile arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileArcDLL( _
   ByRef Center As System.Double, _
   ByRef Axis As System.Double, _
   ByVal Radius As System.Double, _
   ByRef StartPoint As System.Double, _
   ByRef EndPoint As System.Double _
) As Curve
```

```

Dim instance As IBody2
Dim Center As System.Double
Dim Axis As System.Double
Dim Radius As System.Double
Dim StartPoint As System.Double
Dim EndPoint As System.Double
Dim value As Curve
 
value = instance.IAddProfileArcDLL(Center, Axis, Radius, StartPoint, EndPoint)
```

```

Curve IAddProfileArcDLL( 
   ref System.double Center,
   ref System.double Axis,
   System.double Radius,
   ref System.double StartPoint,
   ref System.double EndPoint
)
```

```

Curve^ IAddProfileArcDLL( 
   System.double% Center,
   System.double% Axis,
   System.double Radius,
   System.double% StartPoint,
   System.double% EndPoint
) 
```

#### Parameters

*Center*
:   Pointer to an array of 3 doubles (x,y,z)

*Axis*
:   Pointer to an array of 3 doubles (x,y,z)

*Radius*
:   Radius of the arc

*StartPoint*
:   Pointer to an array of 3 doubles (x,y,z)

*EndPoint*
:   Pointer to an array of 3 doubles (x,y,z)

#### Return Value

Pointer to the arc profile [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
