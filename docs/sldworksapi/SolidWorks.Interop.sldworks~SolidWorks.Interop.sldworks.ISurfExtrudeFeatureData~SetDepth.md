# SetDepth Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetDepth`

Sets the depth of this extruded surface in the forward or reverse direction.
Sets the depth of this extruded surface in the forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDepth( _
   ByVal Forward As System.Boolean, _
   ByVal Depth As System.Double _
) 
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim Depth As System.Double
 
instance.SetDepth(Forward, Depth)
```

```

void SetDepth( 
   System.bool Forward,
   System.double Depth
)
```

```

void SetDepth( 
   System.bool Forward,
   System.double Depth
) 
```

#### Parameters

*Forward*
:   True sets the depth in the forward direction, false sets it in the reverse direction

*Depth*
:   Extrusion depth

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::GetDepth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetDepth.md)
