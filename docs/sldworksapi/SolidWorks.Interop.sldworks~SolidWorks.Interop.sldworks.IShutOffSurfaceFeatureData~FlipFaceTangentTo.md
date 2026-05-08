# FlipFaceTangentTo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~FlipFaceTangentTo`

Indicates to create the patch on the opposite tangent face.
Indicates to create the patch on the opposite tangent face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FlipFaceTangentTo( _
   ByVal Index As System.Integer _
) 
```

```

Dim instance As IShutOffSurfaceFeatureData
Dim Index As System.Integer
 
instance.FlipFaceTangentTo(Index)
```

```

void FlipFaceTangentTo( 
   System.int Index
)
```

```

void FlipFaceTangentTo( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the loop to use to create the patch

Remarks

This method is only available when the type of patch is set to swPatchTypeTangent. See [IShutOffSurfaceFeatureData::LoopPatchType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.md) and [IShutOffSurfaceFeatureData::SetAllPatchTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.md).

Example

See [IShutOffSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md)  
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.md)  
[IShutOffSurfaceFeatureData::GetFaceTangentTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetFaceTangentTo.md)
