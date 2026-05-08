# InsertMoveFace2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace2`

Obsolete. Superseded by IFeatureManager::InsertMoveFace3.
Obsolete. Superseded by [IFeatureManager::InsertMoveFace3.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace3.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMoveFace2( _
   ByVal MoveType As System.Integer, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal Distance As System.Double, _
   ByVal TranslationParams As System.Object, _
   ByVal RotationParams As System.Object _
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
Dim value As Feature
 
value = instance.InsertMoveFace2(MoveType, ReverseDir, Angle, Distance, TranslationParams, RotationParams)
```

```

Feature InsertMoveFace2( 
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance,
   System.object TranslationParams,
   System.object RotationParams
)
```

```

Feature^ InsertMoveFace2( 
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance,
   System.Object^ TranslationParams,
   System.Object^ RotationParams
) 
```

#### Parameters

*MoveType*
:   Type of move:

    - 0 = Offset
    - 1 = Translate
    - 2 = Rotate

*ReverseDir*
:   True to reverse the direction, false to not

*Angle*
:   If MoveType is Rotate, then specify the angle at which to draft the faces

*Distance*
:   Distance to offset or translate the faces

*TranslationParams*
:   Array of three doubles for the delta x, delta y, and delta z direction translation

*RotationParams*
:   Array of six doubles:

    - First three doubles are the x, y, and z rotation origin
    - Last three doubles are the x, y, and z rotation angle

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Use the following marks with [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md):

- 1 = face
- 2 = direction reference (plane, planar face, linear edge, or reference axis) for translate
- 4 = axis reference (linear edge or reference axis) for rotate

If you specify a value for TranslationParms or RotationParams, then do not specify a value for Distance or Angle, respectively. The translation or rotation parameters are calculated internally when Distance or Angle is specified.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::IInsertMoveFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMoveFace2.md)  
[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)
