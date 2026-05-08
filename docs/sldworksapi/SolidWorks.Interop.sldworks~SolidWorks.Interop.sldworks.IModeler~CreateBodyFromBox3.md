# CreateBodyFromBox3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox3`

Creates a temporary body from the specified box dimensions.
Creates a temporary body from the specified box dimensions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBodyFromBox3( _
   ByVal BoxDimArray As System.Object _
) As Body2
```

```

Dim instance As IModeler
Dim BoxDimArray As System.Object
Dim value As Body2
 
value = instance.CreateBodyFromBox3(BoxDimArray)
```

```

Body2 CreateBodyFromBox3( 
   System.object BoxDimArray
)
```

```

Body2^ CreateBodyFromBox3( 
   System.Object^ BoxDimArray
) 
```

#### Parameters

*BoxDimArray*
:   Array of 9 doubles (see Remarks)

#### Return Value

[Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

The input parameter is the following array of doubles:

[ boxFaceCenter[3], boxAxis[3], boxWidth, boxLength, boxHeight ]

where:

|  |  |
| --- | --- |
| boxFaceCenter[3] | XYZ location that represents the center of one of the box faces. |
| boxAxis[3] | XYZ direction. The box will be extruded along this vector from the boxFaceCenter location, a distance of boxHeight. |
| boxWidth | Box width. If boxAxis is parallel to the Z axis (0,0,1), then this value represents the dimension that is parallel to the X-axis; the new body is rotated to the input boxAxis direction and translates it to the boxFaceCenter. |
| boxLength | Box length. If boxAxis is parallel to the Z axis (0,0,1), then this value represents the dimension that is parallel to the Y axis; the new body is rotated to the input boxAxis direction and translates it to the boxFaceCenter. |
| boxHeight | Height to extrude along the boxAxis direction. If boxHeight is 0, a sheet body and whose normal is defined by boxAxis. |

Example

[Create Multibody Macro Feature (VBA)](Create_Multibody_Macro_Feature_Example_VB.htm)  
[Create Multibody Macro Feature (VB.NET)](Create_Multibody_Macro_Feature_Example_VBNET.htm)  
[Create Multibody Macro Feature (C#)](Create_Multibody_Macro_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IFeature::ISetBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody3.md)  
[IFeature::SetBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBody2.md)
