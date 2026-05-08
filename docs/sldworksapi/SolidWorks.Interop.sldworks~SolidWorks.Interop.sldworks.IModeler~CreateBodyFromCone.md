# CreateBodyFromCone Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone`

Creates a temporary body from cone dimensions.
Creates a temporary body from cone dimensions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBodyFromCone( _
   ByVal ConeDimArray As System.Object _
) As System.Object
```

```

Dim instance As IModeler
Dim ConeDimArray As System.Object
Dim value As System.Object
 
value = instance.CreateBodyFromCone(ConeDimArray)
```

```

System.object CreateBodyFromCone( 
   System.object ConeDimArray
)
```

```

System.Object^ CreateBodyFromCone( 
   System.Object^ ConeDimArray
) 
```

#### Parameters

*ConeDimArray*
:   Array containing 9 doubles (see **Remarks**)

#### Return Value

[Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

The ConeArray argument is the following array of doubles:

[ coneFaceCenter[3], coneAxis[3], coneBaseRadius, coneTopRadius, coneHeight ]

where:

|  |  |
| --- | --- |
| coneFaceCenter[3] | XYZ location that represents the center of one of the cone faces |
| coneAxis[3] | XYZ direction; the cone is extruded along this vector from the coneFaceCenter location, a distance of coneHeight |
| coneBaseRadius | Cone radius at the coneFaceCenter plane |
| coneTopRadius | Cone radius at coneHeight from the coneFaceCenter along the axis |
| coneHeight | Length to extrude along the coneAxis direction; if coneHeight is 0, then a sheet body is created of dimension coneBaseRadius and normal is defined by coneAxis |

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
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.md)  
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
