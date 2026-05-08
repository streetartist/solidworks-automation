# InsertCoordinateSystem Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCoordinateSystem`

Inserts a coordinate system feature.
Inserts a coordinate system feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCoordinateSystem( _
   ByVal XFlippedIn As System.Boolean, _
   ByVal YFlippedIn As System.Boolean, _
   ByVal ZFlippedIn As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim XFlippedIn As System.Boolean
Dim YFlippedIn As System.Boolean
Dim ZFlippedIn As System.Boolean
Dim value As Feature
 
value = instance.InsertCoordinateSystem(XFlippedIn, YFlippedIn, ZFlippedIn)
```

```

Feature InsertCoordinateSystem( 
   System.bool XFlippedIn,
   System.bool YFlippedIn,
   System.bool ZFlippedIn
)
```

```

Feature^ InsertCoordinateSystem( 
   System.bool XFlippedIn,
   System.bool YFlippedIn,
   System.bool ZFlippedIn
) 
```

#### Parameters

*XFlippedIn*
:   True to flip the x axis direction, false to not

*YFlippedIn*
:   :   True to flip the y axis direction, false to not

*ZFlippedIn*
:   True to flip the z axis direction, false to not

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Make the selections using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with a mark of:

- 1 - Origin
- 2 - X axis
- 4 - Y axis
- 8 - Z axis

This method:

- does not require all three axis to be selected. The behavior is the same as interactively creating a coordinate system. See the SOLIDWORKS Help for more information.
- works in section-view mode, but not if temporary geometry that only exists in section-view mode is selected.

Example

[Insert Coordinate System Feature at Center of Mass (VBA)](Insert_Coordinate_System_Feature_at_Center_of_Mass_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.md)  
[IFeatureManager::CreateCoordinateSystem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystem.md)
