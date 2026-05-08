# AddProfileArc Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileArc`

Creates an arc profile curve and returns a pointer to that curve.
Creates an arc profile curve and returns a pointer to that curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddProfileArc( _
   ByVal Center As System.Object, _
   ByVal Axis As System.Object, _
   ByVal Radius As System.Double, _
   ByVal StartPoint As System.Object, _
   ByVal EndPoint As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim Center As System.Object
Dim Axis As System.Object
Dim Radius As System.Double
Dim StartPoint As System.Object
Dim EndPoint As System.Object
Dim value As System.Object
 
value = instance.AddProfileArc(Center, Axis, Radius, StartPoint, EndPoint)
```

```

System.object AddProfileArc( 
   System.object Center,
   System.object Axis,
   System.double Radius,
   System.object StartPoint,
   System.object EndPoint
)
```

```

System.Object^ AddProfileArc( 
   System.Object^ Center,
   System.Object^ Axis,
   System.double Radius,
   System.Object^ StartPoint,
   System.Object^ EndPoint
) 
```

#### Parameters

*Center*
:   Array of 3 doubles (x,y,z)

*Axis*
:   Array of 3 doubles (x,y,z)

*Radius*
:   Arc radius

*StartPoint*
:   Array of 3 doubles (x,y,z)

*EndPoint*
:   Array of 3 doubles (x,y,z)

#### Return Value

Object for the curve

Remarks

This method always creates a full circle.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IAddProfileArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArc.md)
