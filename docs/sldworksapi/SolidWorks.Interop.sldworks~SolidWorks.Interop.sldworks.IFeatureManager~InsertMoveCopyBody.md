# InsertMoveCopyBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveCopyBody`

Obsolete. Superseded by IFeatureManager::InsertMoveCopyBody2.
Obsolete. Superseded by [IFeatureManager::InsertMoveCopyBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMoveCopyBody( _
   ByVal TransX As System.Double, _
   ByVal TransY As System.Double, _
   ByVal TransZ As System.Double, _
   ByVal TransDist As System.Double, _
   ByVal RotPointX As System.Double, _
   ByVal RotPointY As System.Double, _
   ByVal RotPointZ As System.Double, _
   ByVal RotAngleX As System.Double, _
   ByVal RotAngleY As System.Double, _
   ByVal RotAngleZ As System.Double, _
   ByVal BCopy As System.Boolean, _
   ByVal NumCopies As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim TransX As System.Double
Dim TransY As System.Double
Dim TransZ As System.Double
Dim TransDist As System.Double
Dim RotPointX As System.Double
Dim RotPointY As System.Double
Dim RotPointZ As System.Double
Dim RotAngleX As System.Double
Dim RotAngleY As System.Double
Dim RotAngleZ As System.Double
Dim BCopy As System.Boolean
Dim NumCopies As System.Integer
Dim value As Feature
 
value = instance.InsertMoveCopyBody(TransX, TransY, TransZ, TransDist, RotPointX, RotPointY, RotPointZ, RotAngleX, RotAngleY, RotAngleZ, BCopy, NumCopies)
```

```

Feature InsertMoveCopyBody( 
   System.double TransX,
   System.double TransY,
   System.double TransZ,
   System.double TransDist,
   System.double RotPointX,
   System.double RotPointY,
   System.double RotPointZ,
   System.double RotAngleX,
   System.double RotAngleY,
   System.double RotAngleZ,
   System.bool BCopy,
   System.int NumCopies
)
```

```

Feature^ InsertMoveCopyBody( 
   System.double TransX,
   System.double TransY,
   System.double TransZ,
   System.double TransDist,
   System.double RotPointX,
   System.double RotPointY,
   System.double RotPointZ,
   System.double RotAngleX,
   System.double RotAngleY,
   System.double RotAngleZ,
   System.bool BCopy,
   System.int NumCopies
) 
```

#### Parameters

*TransX*

*TransY*

*TransZ*

*TransDist*

*RotPointX*

*RotPointY*

*RotPointZ*

*RotAngleX*

*RotAngleY*

*RotAngleZ*

*BCopy*

*NumCopies*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
