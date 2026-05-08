# CreateTransformRotateAxis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransformRotateAxis`

Creates a new math transform matrix that represents the rotation by an angle about a vector positioned at a point.
Creates a new math transform matrix that represents the rotation by an angle about a vector positioned at a point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTransformRotateAxis( _
   ByVal PointObjIn As System.Object, _
   ByVal VectorObjIn As System.Object, _
   ByVal Angle As System.Double _
) As System.Object
```

```

Dim instance As IMathUtility
Dim PointObjIn As System.Object
Dim VectorObjIn As System.Object
Dim Angle As System.Double
Dim value As System.Object
 
value = instance.CreateTransformRotateAxis(PointObjIn, VectorObjIn, Angle)
```

```

System.object CreateTransformRotateAxis( 
   System.object PointObjIn,
   System.object VectorObjIn,
   System.double Angle
)
```

```

System.Object^ CreateTransformRotateAxis( 
   System.Object^ PointObjIn,
   System.Object^ VectorObjIn,
   System.double Angle
) 
```

#### Parameters

*PointObjIn*
:   Center [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) of the axis of the transform

*VectorObjIn*
:   Axis [vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) of the transform

*Angle*
:   Angle of rotation about the X axis vector

#### Return Value

Newly created [math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) or null or nothing if the operation fails

Example

[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VBA)](Rotate_Assembly_Component_on_Axis_Example2_VB.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VB.NET)](Rotate_Assembly_Component_on_Axis_Example2_VBNET.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (C#)](Rotate_Assembly_Component_on_Axis_Example2_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.md)  
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.md)  
[IMathUtility::ComposeTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ComposeTransform.md)  
[IMathUtility::CreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransform.md)  
[IMathUtility::ICreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransform.md)  
[IMathUtility::ICreateTransformRotateAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransformRotateAxis.md)
