# SetDepth Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDepth`

Sets the depth of the feature in the forward or reverse direction.
Sets the depth of the feature in the forward or reverse direction.

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

Dim instance As IExtrudeFeatureData2
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
:   True for forward direction, false for reverse

*Depth*
:   Depth of the extrusion

Remarks

Use this method to specify the surface offset distance when [end condition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.md) is swEndCondOffsetFromSurface.

Example

[Access Selections (VBA)](Access_Selections_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::GetDepth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDepth.md)
