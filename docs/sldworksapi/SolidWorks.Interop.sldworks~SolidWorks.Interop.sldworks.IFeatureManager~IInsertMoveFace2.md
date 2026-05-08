# IInsertMoveFace2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMoveFace2`

Obsolete. Superseded by IFeatureManager::InsertMoveFace3.
Obsolete. Superseded by [IFeatureManager::InsertMoveFace3.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace3.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertMoveFace2( _
   ByVal MoveType As System.Integer, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal Distance As System.Double, _
   ByRef TranslationParams As System.Double, _
   ByRef RotationParams As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim MoveType As System.Integer
Dim ReverseDir As System.Boolean
Dim Angle As System.Double
Dim Distance As System.Double
Dim TranslationParams As System.Double
Dim RotationParams As System.Double
Dim value As Feature
 
value = instance.IInsertMoveFace2(MoveType, ReverseDir, Angle, Distance, TranslationParams, RotationParams)
```

```

Feature IInsertMoveFace2( 
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance,
   ref System.double TranslationParams,
   ref System.double RotationParams
)
```

```

Feature^ IInsertMoveFace2( 
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance,
   System.double% TranslationParams,
   System.double% RotationParams
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
:   - in-process, unmanaged C++: Pointer to an array three doubles for delta x, delta y, and delta z direction translation

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*RotationParams*
:   - in-process, unmanaged C++: Pointer to an array six doubles:
      - first three doubles are the x, y, and z rotation origin
      - last three doubles are the x, y, and z rotation angle

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)  
[IFeatureManager::InsertMoveFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace2.md)
