# SetEndCondition Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndCondition`

Sets the end condition type of the extrusion feature for the forward or reverse direction.
Sets the end condition type of the extrusion feature for the forward or reverse direction.

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

Dim instance As IExtrudeFeatureData2
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
:   True for forward direction, false for reverse

*EndCondition*
:   End condition type as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::SetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.md)  
[IExtrudeFeatureData2::GetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.md)  
[IExtrudeFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.md)  
[IExtrudeFeatureData2::SetDepth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDepth.md)
