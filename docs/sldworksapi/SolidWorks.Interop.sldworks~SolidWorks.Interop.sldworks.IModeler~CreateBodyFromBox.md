# CreateBodyFromBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox`

Obsolete. Superseded by IModeler::CreateBodyFromBox3.
Obsolete. Superseded by [IModeler::CreateBodyFromBox3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBodyFromBox( _
   ByVal BoxDimArray As System.Object _
) As System.Object
```

```

Dim instance As IModeler
Dim BoxDimArray As System.Object
Dim value As System.Object
 
value = instance.CreateBodyFromBox(BoxDimArray)
```

```

System.object CreateBodyFromBox( 
   System.object BoxDimArray
)
```

```

System.Object^ CreateBodyFromBox( 
   System.Object^ BoxDimArray
) 
```

#### Parameters

*BoxDimArray*
:   Array of 9 doubles (see **Remarks**)

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
| boxWidth | Box width. If boxAxis is parallel to the Z axis (0,0,1), then this value represents the dimension that is parallel to the X-axis; otherwise, the orientation is not defined. |
| boxLength | Box length. If boxAxis is parallel to the Z axis (0,0,1), then this value represents the dimension that is parallel to the Y axis; otherwise, the orientation is not defined. |
| boxHeight | Height to extrude along the boxAxis direction. If boxHeight is 0, a sheet body will be created of dimension boxWidth x boxLength and whose normal is defined by boxAxis. |

Example

[Create Solid Bodies Using Geometry and Topology (C#)](Create_Solid_Bodies_using_Geometry_and_Topology_APIs_Example_CSharp.htm)  
[Create Solid Bodies Using Geometry and Topology (VB.NET)](Create_Solid_Bodies_using_Geometry_and_Topology_APIs_Example_VBNET.htm)  
[Create Solid Bodies Using Geometry and Topology (VBA)](Create_Solid_Bodies_using_Geometry_and_Topology_APIs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.md)  
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.md)  
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.md)  
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.md)  
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md)  
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.md)  
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.md)  
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.md)  
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.md)  
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.md)  
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.md)  
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.md)  
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md)  
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.md)  
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.md)
