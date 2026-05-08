# InsertMoldPartingSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingSurface`

Inserts a mold parting surface feature.
Inserts a mold parting surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMoldPartingSurface( _
   ByVal Radiate As System.Integer, _
   ByVal ReverseAlignment As System.Boolean, _
   ByVal ReverseOffset As System.Boolean, _
   ByVal OffsetDistance As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Smooth As System.Integer, _
   ByVal SmoothDistance As System.Double, _
   ByVal Knit As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Radiate As System.Integer
Dim ReverseAlignment As System.Boolean
Dim ReverseOffset As System.Boolean
Dim OffsetDistance As System.Double
Dim Angle As System.Double
Dim Smooth As System.Integer
Dim SmoothDistance As System.Double
Dim Knit As System.Boolean
Dim value As Feature
 
value = instance.InsertMoldPartingSurface(Radiate, ReverseAlignment, ReverseOffset, OffsetDistance, Angle, Smooth, SmoothDistance, Knit)
```

```

Feature InsertMoldPartingSurface( 
   System.int Radiate,
   System.bool ReverseAlignment,
   System.bool ReverseOffset,
   System.double OffsetDistance,
   System.double Angle,
   System.int Smooth,
   System.double SmoothDistance,
   System.bool Knit
)
```

```

Feature^ InsertMoldPartingSurface( 
   System.int Radiate,
   System.bool ReverseAlignment,
   System.bool ReverseOffset,
   System.double OffsetDistance,
   System.double Angle,
   System.int Smooth,
   System.double SmoothDistance,
   System.bool Knit
) 
```

#### Parameters

*Radiate*
:   Radiate mold parting surface as defined by [swPartingSurfaceMoldParmType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartingSurfaceMoldParmType_e.html)

*ReverseAlignment*
:   True to reverse alignment, false to not; only available when radiate set to swPartingSurfaceMoldParmNormal and a parting line does not yet exist (see **Remarks**)

*ReverseOffset*
:   True to reverse offset direction, false to not

*OffsetDistance*
:   True to reverse offset direction, false to not

*Angle*
:   Angle of mold parting surface; only available when radiate set to either swPartingSurfaceMoldParmTangent or swPartingSurfaceMoldParmNormal

*Smooth*
:   Smooth mold parting surface as defined by [swPartingSurfaceSmoothingType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartingSurfaceSmoothingType_e.html)

*SmoothDistance*
:   Distance to smooth mold parting surface; only available when smooth set to swPartingSurfaceSmooth

*Knit*
:   True to knit all surfaces, false to not

#### Return Value

Pointer to [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

f a parting line feature does not yet exist in the model, you must first select the direction of pull and the edges for the parting line using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md). For example, a face (direction of pull) has a mark of 1 and edges (parting lines) a mark of 4.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.md)  
[IFeatureManager::InsertMoldCoreCavitySolids Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldCoreCavitySolids.md)  
[IFeatureManager::InsertMoldPartingLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingLine.md)  
[IFeatureManager::InsertMoldShutOffSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldShutOffSurface.md)
