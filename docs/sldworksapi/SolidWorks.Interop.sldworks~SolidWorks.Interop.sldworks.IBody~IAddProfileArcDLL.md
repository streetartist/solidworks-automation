# IAddProfileArcDLL Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileArcDLL`

Obsolete. Superseded by IBody2::IAddProfileArcDLL.
Obsolete. Superseded by [IBody2::IAddProfileArcDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArcDLL.md).

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

Dim instance As IBody
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

*Axis*

*Radius*

*StartPoint*

*EndPoint*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
