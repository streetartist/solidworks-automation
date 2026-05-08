# CreateCoordinateSystem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystem`

Creates a coordinate system feature using the specified entities.
Creates a coordinate system feature using the specified entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCoordinateSystem( _
   ByVal OriginPointEntity As System.Object, _
   ByVal XAxisEntities As System.Object, _
   ByVal YAxisEntities As System.Object, _
   ByVal ZAxisEntities As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim OriginPointEntity As System.Object
Dim XAxisEntities As System.Object
Dim YAxisEntities As System.Object
Dim ZAxisEntities As System.Object
Dim value As Feature
 
value = instance.CreateCoordinateSystem(OriginPointEntity, XAxisEntities, YAxisEntities, ZAxisEntities)
```

```

Feature CreateCoordinateSystem( 
   System.object OriginPointEntity,
   System.object XAxisEntities,
   System.object YAxisEntities,
   System.object ZAxisEntities
)
```

```

Feature^ CreateCoordinateSystem( 
   System.Object^ OriginPointEntity,
   System.Object^ XAxisEntities,
   System.Object^ YAxisEntities,
   System.Object^ ZAxisEntities
) 
```

#### Parameters

*OriginPointEntity*
:   Entity (vertex, point, midpoint, or the default point of origin on a part or assembly) for the coordinate system origin

*XAxisEntities*
:   Array of entities (vertex, point, or midpoint; linear edge or sketch line; non-linear edge or sketch entity; or planar face) for the x axis

*YAxisEntities*
:   Array of entities (vertex, point, or midpoint; linear edge or sketch line; non-linear edge or sketch entity; or planar face) for the y axis

*ZAxisEntities*
:   Array of entities (vertex, point, or midpoint; linear edge or sketch line; non-linear edge or sketch entity; or planar face) for the z axis

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

[Create Coordinate System Feature (VBA)](Create_Coordinate_System_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.md)  
[IFeatureManager::InsertCoordinateSystem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCoordinateSystem.md)  
[IFeatureManager::CreateCoordinateSystemUsingNumericalValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystemUsingNumericalValues.md)
