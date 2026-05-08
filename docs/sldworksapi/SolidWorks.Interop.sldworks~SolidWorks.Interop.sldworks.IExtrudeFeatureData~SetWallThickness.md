# SetWallThickness Method (IExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetWallThickness`

Obsolete. Superseded by IExtrudeFeatureData2::SetWallThickness.
Obsolete. Superseded by [IExtrudeFeatureData2::SetWallThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetWallThickness.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetWallThickness( _
   ByVal Forward As System.Boolean, _
   ByVal WallThickness As System.Double _
) 
```

```

Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim WallThickness As System.Double
 
instance.SetWallThickness(Forward, WallThickness)
```

```

void SetWallThickness( 
   System.bool Forward,
   System.double WallThickness
)
```

```

void SetWallThickness( 
   System.bool Forward,
   System.double WallThickness
) 
```

#### Parameters

*Forward*

*WallThickness*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.md)  
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.md)
