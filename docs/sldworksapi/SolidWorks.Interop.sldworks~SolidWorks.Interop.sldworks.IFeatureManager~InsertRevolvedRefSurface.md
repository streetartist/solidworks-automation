# InsertRevolvedRefSurface Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRevolvedRefSurface`

Creates a revolved reference surface by revolving a profile around a centerline.
Creates a revolved reference surface by revolving a profile around a centerline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertRevolvedRefSurface( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim value As Feature
 
value = instance.InsertRevolvedRefSurface(Angle, ReverseDir, Angle2, RevType)
```

```

Feature InsertRevolvedRefSurface( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType
)
```

```

Feature^ InsertRevolvedRefSurface( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType
) 
```

#### Parameters

*Angle*
:   Angle of revolution in radians

*ReverseDir*
:   Angle is positive or negative (True or false)

*Angle2*
:   Angle of revolution in radians

*RevType*
:   Type of revolution (see **Remarks**)

#### Return Value

Pointer to [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Make the selections using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) before calling this method. See the SOLIDWORKS Help for information about what entities are valid for selection.

The RevType argument can be one of these values:

- 0 = One direction revolution.
- 1 = MidPlane revolution. For this type of revolve, the angle specification specifies the full revolution. The angle to revolve is (angle/2) on either side of the sketch. The ReverseDir argument has no effect.
- 2 = Two direction revolution. For a two direction revolve, Angle is the angle to revolve in Direction1 and Angle2 is the angle to revolve in Direction2.

This method does not support 3D sketches.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)
