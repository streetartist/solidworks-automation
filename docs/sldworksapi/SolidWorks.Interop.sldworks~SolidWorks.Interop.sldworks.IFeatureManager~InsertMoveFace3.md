# InsertMoveFace3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace3`

Moves the selected faces on a solid or surface model.
Moves the selected faces on a solid or surface model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMoveFace3( _
   ByVal MoveType As System.Integer, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal Distance As System.Double, _
   ByVal TranslationParams As System.Object, _
   ByVal RotationParams As System.Object, _
   ByVal EndConditionType As System.Integer, _
   ByVal OffsetDistance As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim MoveType As System.Integer
Dim ReverseDir As System.Boolean
Dim Angle As System.Double
Dim Distance As System.Double
Dim TranslationParams As System.Object
Dim RotationParams As System.Object
Dim EndConditionType As System.Integer
Dim OffsetDistance As System.Double
Dim value As Feature
 
value = instance.InsertMoveFace3(MoveType, ReverseDir, Angle, Distance, TranslationParams, RotationParams, EndConditionType, OffsetDistance)
```

```

Feature InsertMoveFace3( 
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance,
   System.object TranslationParams,
   System.object RotationParams,
   System.int EndConditionType,
   System.double OffsetDistance
)
```

```

Feature^ InsertMoveFace3( 
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance,
   System.Object^ TranslationParams,
   System.Object^ RotationParams,
   System.int EndConditionType,
   System.double OffsetDistance
) 
```

#### Parameters

*MoveType*
:   Type of move as defined in [swMoveFaceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveFaceType_e.html)

*ReverseDir*
:   True to reverse the direction, false to not

*Angle*
:   Angle at which to draft the faces; valid only if MoveType is swMoveFaceType\_e.swMoveFaceTypeRotate (see **Remarks**)

*Distance*
:   Distance to translate or offset the faces; valid only if MoveType is one of the following:

    - swMoveFaceType\_e.swMoveFaceTypeOffset
    - swMoveFaceType\_e.swMoveFaceTypeTranslate and EndConditionType is swEndConditions\_e.swEndCondBlind (see **Remarks**)

*TranslationParams*
:   Array of three doubles for the delta x, delta y, and delta z direction translation (see **Remarks**)

*RotationParams*
:   Array of six doubles:

    - First three doubles are the x, y, and z rotation origin
    - Last three doubles are the x, y, and z rotation angle

    (see **Remarks**)

*EndConditionType*
:   End condition as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html); valid only if MoveType is swMoveFaceType\_e.swMoveFaceTypeTranslate

    Only the following end condition types are valid:

    - swEndConditions\_e.swEndCondBlind
    - swEndConditions\_e.swEndCondUpToVertex
    - swEndConditions\_e.swEndCondUpToSurface
    - swEndConditions\_e.swEndCondOffsetFromSurface
    - swEndConditions\_e.swEndCondUpToBody

*OffsetDistance*
:   Offset from surface; valid only if MoveType is swMoveFaceType\_e.swMoveFaceTypeTranslate and EndConditionType is swEndConditions\_e.swEndCondOffsetFromSurface

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, you need to select specific entities.

| If MoveFaceType is swMoveFaceType\_e... | And EndConditionType is swEndConditions\_e... | Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select... | With mark... |
| --- | --- | --- | --- |
| Any option | Any option | Face to move | 1 |
| swMoveFaceTypeTranslate | Any option | Direction reference (plane, planar face, linear edge, or reference axis) | 2 |
| swMoveFaceTypeTranslate | - swEndCondUpToVertex - swEndCondUpToSurface - swEndCondOffsetFromSurface - swEndCondUpToBody | - Up-to vertex - Up-to surface - Offset-from surface - Up-to body | 8 |
| swMoveFaceTypeRotate | N/A | Axis reference (linear edge or reference axis) | 4 |

If you specify a value for TranslationParms or RotationParams, then do not specify a value for Distance or Angle, respectively. The translation or rotation parameters are calculated internally when Distance or Angle is specified.

Example

[Create and Modify Move Face Feature (VBA)](Create_and_Modify_Move_Face_Feature_Example_VB.htm)  
[Create and Modify Move Face Feature (VB.NET)](Create_and_Modify_Move_Face_Feature_Example_VBNET.htm)  
[Create and Modify Move Face Feature (C#)](Create_and_Modify_Move_Face_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)
