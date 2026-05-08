# RotateOrCopy3DAboutXYZ Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~RotateOrCopy3DAboutXYZ`

Rotates, and optionally copies, the selected 3D sketch entities about the specified x, y, and z coordinates.
Rotates, and optionally copies, the selected 3D sketch entities about the specified x, y, and z coordinates.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RotateOrCopy3DAboutXYZ( _
   ByVal Copy As System.Boolean, _
   ByVal NumCopies As System.Integer, _
   ByVal KeepRelations As System.Boolean, _
   ByVal BaseX As System.Double, _
   ByVal BaseY As System.Double, _
   ByVal BaseZ As System.Double, _
   ByVal AngleAboutXDir As System.Double, _
   ByVal AngleAboutYDir As System.Double, _
   ByVal AngleAboutZDir As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim Copy As System.Boolean
Dim NumCopies As System.Integer
Dim KeepRelations As System.Boolean
Dim BaseX As System.Double
Dim BaseY As System.Double
Dim BaseZ As System.Double
Dim AngleAboutXDir As System.Double
Dim AngleAboutYDir As System.Double
Dim AngleAboutZDir As System.Double
Dim value As System.Boolean
 
value = instance.RotateOrCopy3DAboutXYZ(Copy, NumCopies, KeepRelations, BaseX, BaseY, BaseZ, AngleAboutXDir, AngleAboutYDir, AngleAboutZDir)
```

```

System.bool RotateOrCopy3DAboutXYZ( 
   System.bool Copy,
   System.int NumCopies,
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double AngleAboutXDir,
   System.double AngleAboutYDir,
   System.double AngleAboutZDir
)
```

```

System.bool RotateOrCopy3DAboutXYZ( 
   System.bool Copy,
   System.int NumCopies,
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double AngleAboutXDir,
   System.double AngleAboutYDir,
   System.double AngleAboutZDir
) 
```

#### Parameters

*Copy*
:   True to copy 3D sketch entities, false to not

*NumCopies*
:   :   Number of copies

*KeepRelations*
:   True to keep sketch relations, false to not

*BaseX*
:   X coordinate from the base point from which to rotate the 3D sketch entities

*BaseY*
:   Y coordinate from the base point from which to rotate the 3D sketch entities

*BaseZ*
:   Z coordinate from the base point from which to rotate the 3D sketch entities

*AngleAboutXDir*
:   Angle to rotate the 3D sketch entities in the x direction

*AngleAboutYDir*
:   Angle to rotate 3D sketch entities in the y direction

*AngleAboutZDir*
:   Angle to rotate 3D sketch entities in the z direction

#### Return Value

True if the 3D sketch entities are rotated, and optionally copied, in the specified x, y, and z directions, false if not

Example

[Rotate and Copy 3D Sketch About Coordinates (C#)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_CSharp.htm)  
[Rotate and Copy 3D Sketch about Coordinates (VB.NET)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VBNET.htm)  
[Rotate and Copy 3D Sketch About Coordinates (VBA)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::RotateOrCopy3DAboutVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~RotateOrCopy3DAboutVector.md)  
[IModelDocExtension::RotateOrCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RotateOrCopy.md)
