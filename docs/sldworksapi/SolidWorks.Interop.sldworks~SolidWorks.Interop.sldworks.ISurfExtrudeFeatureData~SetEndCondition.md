# SetEndCondition Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetEndCondition`

Sets the end condition of this extruded surface in the forward or reverse direction.
Sets the end condition of this extruded surface in the forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEndCondition( _
   ByVal Forward As System.Boolean, _
   ByVal EndCondition As System.Integer _
) 
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim EndCondition As System.Integer
 
instance.SetEndCondition(Forward, EndCondition)
```

```

void SetEndCondition( 
   System.bool Forward,
   System.int EndCondition
)
```

```

void SetEndCondition( 
   System.bool Forward,
   System.int EndCondition
) 
```

#### Parameters

*Forward*
:   True sets the end condition in the forward direction, false sets it in the reverse direction

*EndCondition*
:   End condition as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::GetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetEndCondition.md)
