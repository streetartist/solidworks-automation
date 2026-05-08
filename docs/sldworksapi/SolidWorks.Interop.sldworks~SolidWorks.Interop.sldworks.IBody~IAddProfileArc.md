# IAddProfileArc Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileArc`

Obsolete. Superseded by IBody2::IAddProfileArc.
Obsolete. Superseded by [IBody2::IAddProfileArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArc.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileArc( _
   ByVal Center As System.Object, _
   ByVal Axis As System.Object, _
   ByVal Radius As System.Double, _
   ByVal StartPoint As System.Object, _
   ByVal EndPoint As System.Object _
) As Curve
```

```

Dim instance As IBody
Dim Center As System.Object
Dim Axis As System.Object
Dim Radius As System.Double
Dim StartPoint As System.Object
Dim EndPoint As System.Object
Dim value As Curve
 
value = instance.IAddProfileArc(Center, Axis, Radius, StartPoint, EndPoint)
```

```

Curve IAddProfileArc( 
   System.object Center,
   System.object Axis,
   System.double Radius,
   System.object StartPoint,
   System.object EndPoint
)
```

```

Curve^ IAddProfileArc( 
   System.Object^ Center,
   System.Object^ Axis,
   System.double Radius,
   System.Object^ StartPoint,
   System.Object^ EndPoint
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
