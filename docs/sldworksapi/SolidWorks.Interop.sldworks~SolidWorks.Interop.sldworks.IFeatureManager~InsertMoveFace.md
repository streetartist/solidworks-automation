# InsertMoveFace Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace`

Obsolete. Superseded by IFeatureManager::InsertMoveFace2 and IFeatureManager::IInsertMoveFace2.
Obsolete. Superseded by [IFeatureManager::InsertMoveFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace2.md) and [IFeatureManager::IInsertMoveFace2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMoveFace2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMoveFace( _
   ByVal MoveType As System.Integer, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal Distance As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim MoveType As System.Integer
Dim ReverseDir As System.Boolean
Dim Angle As System.Double
Dim Distance As System.Double
Dim value As Feature
 
value = instance.InsertMoveFace(MoveType, ReverseDir, Angle, Distance)
```

```

Feature InsertMoveFace( 
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance
)
```

```

Feature^ InsertMoveFace( 
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance
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

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Use the following marks with [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md):

- 1 = face
- 2 = direction reference (plane, planar face, linear edge, or reference axis) for translate
- 4 = axis reference (linear edge or reference axis) for rotate

Example

[Move Selected Face (VBA)](Move_Selected_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)
